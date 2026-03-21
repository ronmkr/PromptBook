import curses
import os
import sys

# Try importing promptops_core
try:
    import promptops_core
except ImportError:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    sys.path.append(os.path.join(BASE_DIR, "scripts"))
    import promptops_core

class PromptOpsTUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.prompts = promptops_core.get_prompts()
        self.filtered_prompts = self.prompts
        self.current_row = 0
        self.search_term = ""
        self.mode = "normal"  # normal, search
        
        # Setup colors
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # Selected row
        curses.init_pair(2, curses.COLOR_CYAN, -1)                  # Header
        curses.init_pair(3, curses.COLOR_YELLOW, -1)                # Tags
        curses.init_pair(4, curses.COLOR_GREEN, -1)                 # Instructions

    def safe_addstr(self, y, x, text, attr=0):
        """Safely print to the screen, truncating to prevent wrapping/crashing."""
        try:
            height, width = self.stdscr.getmaxyx()
            if y >= height or y < 0 or x >= width or x < 0:
                return
            
            # Account for double-width characters (emojis) crudely by reducing the allowed width
            # A safer generic approach is to slice based on available space minus a small buffer
            max_len = width - x - 2 
            if max_len <= 0:
                return
                
            safe_text = text[:max_len]
            self.stdscr.addstr(y, x, safe_text, attr)
        except curses.error:
            pass

    def draw(self):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()

        # Handle terminal too small
        if height < 10 or width < 40:
            self.safe_addstr(0, 0, "Terminal too small")
            self.stdscr.refresh()
            return

        # Calculate panes
        left_width = min(40, width // 3)
        right_width = width - left_width - 1

        # Draw Header
        header = f" PromptOps | Prompts: {len(self.filtered_prompts)} "
        self.safe_addstr(0, 0, header.ljust(width - 2), curses.color_pair(2) | curses.A_BOLD)

        # Draw left pane (List)
        max_rows = height - 4
        
        # Ensure current_row is bounded
        if self.filtered_prompts:
            self.current_row = max(0, min(self.current_row, len(self.filtered_prompts) - 1))
        
        start_idx = max(0, self.current_row - (max_rows // 2))
        end_idx = min(len(self.filtered_prompts), start_idx + max_rows)
        
        # Adjust start if we hit the bottom
        if end_idx - start_idx < max_rows and len(self.filtered_prompts) > max_rows:
            start_idx = len(self.filtered_prompts) - max_rows

        for i, idx in enumerate(range(start_idx, end_idx)):
            y = i + 2
            p = self.filtered_prompts[idx]
            name = p['name']
            
            # Truncate name if too long
            if len(name) > left_width - 4:
                name = name[:left_width-7] + "..."

            display_str = f"  {name}".ljust(left_width - 1)
            if idx == self.current_row:
                display_str = f"> {name}".ljust(left_width - 1)
                self.safe_addstr(y, 1, display_str, curses.color_pair(1))
            else:
                self.safe_addstr(y, 1, display_str)

        # Vertical separator
        for y in range(2, height - 2):
            self.safe_addstr(y, left_width, "│")

        # Draw right pane (Details)
        if self.filtered_prompts:
            p = self.filtered_prompts[self.current_row]
            
            # Title
            self.safe_addstr(2, left_width + 2, p['name'], curses.A_BOLD)
            
            # Description
            self.safe_addstr(4, left_width + 2, p['description'])
            
            # Tags
            tags_str = ", ".join(p['tags'])
            self.safe_addstr(6, left_width + 2, f"Tags: {tags_str}", curses.color_pair(3))

            # Preview Header
            self.safe_addstr(8, left_width + 2, "--- Template Preview ---")
            
            # Preview Content
            preview_lines = p['prompt'].split('\n')
            for i, line in enumerate(preview_lines):
                # Stop if we hit the footer area
                y_pos = 10 + i
                if y_pos >= height - 2:
                    break
                    
                safe_line = line.replace('\t', '    ')
                self.safe_addstr(y_pos, left_width + 2, safe_line)

        # Draw Footer
        if self.mode == "normal":
            footer = " [Up/Dn] Navigate | [/] Search | [Enter] Use | [Q]uit "
            self.safe_addstr(height - 1, 0, footer.ljust(width - 2), curses.color_pair(4))
        elif self.mode == "search":
            footer = f" Search: {self.search_term}█"
            self.safe_addstr(height - 1, 0, footer.ljust(width - 2), curses.color_pair(4))

        self.stdscr.refresh()

    def run(self):
        curses.curs_set(0) # Hide cursor
        self.stdscr.nodelay(False)

        while True:
            self.draw()
            
            try:
                char = self.stdscr.get_wch()
            except curses.error:
                continue

            if self.mode == "normal":
                if char == 'q' or char == 'Q':
                    return None
                elif char == '\n' or char == '\r':  # Enter
                    if self.filtered_prompts:
                        return self.filtered_prompts[self.current_row]['name']
                elif char == curses.KEY_UP or char == 'k':
                    self.current_row = max(0, self.current_row - 1)
                elif char == curses.KEY_DOWN or char == 'j':
                    self.current_row = min(len(self.filtered_prompts) - 1, self.current_row + 1)
                elif char == '/':
                    self.mode = "search"
                    
            elif self.mode == "search":
                if char == '\n' or char == '\r':  # Enter finishes search
                    self.mode = "normal"
                elif char == '\x1b':  # Escape cancels search
                    self.mode = "normal"
                    self.search_term = ""
                    self.filtered_prompts = self.prompts
                    self.current_row = 0
                elif char == curses.KEY_BACKSPACE or char == '\x08' or char == '\x7f':
                    self.search_term = self.search_term[:-1]
                    self.update_search()
                elif isinstance(char, str) and char.isprintable():
                    self.search_term += char
                    self.update_search()

    def update_search(self):
        if not self.search_term:
            self.filtered_prompts = self.prompts
        else:
            term = self.search_term.lower()
            results = []
            for p in self.prompts:
                name = p["name"].lower()
                desc = p["description"].lower()
                
                # Simple substring for fast TUI response
                if term in name or term in desc:
                    results.append(p)
                    
            self.filtered_prompts = results
        self.current_row = 0

def main():
    try:
        # Run the curses application and get the selected prompt
        selected_prompt = curses.wrapper(lambda stdscr: PromptOpsTUI(stdscr).run())
        
        # If user pressed enter on a prompt
        if selected_prompt:
            # We exit curses mode fully before asking for input
            print(f"\n🚀 Preparing to use: {selected_prompt}\n")
            promptops_core.use_prompt(selected_prompt)
            
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error in TUI: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
