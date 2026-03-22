import os
import sys
import platform
import subprocess

# ANSI Colors for better UX
class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Constants
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROMPTS_DIR = os.path.join(BASE_DIR, "commands", "prompts")

def copy_to_clipboard(text):
    """Zero-dependency clipboard copy using native OS commands."""
    try:
        os_name = platform.system()
        if os_name == "Darwin": # macOS
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            process.communicate(input=text.encode('utf-8'))
        elif os_name == "Linux":
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
            except FileNotFoundError:
                process = subprocess.Popen(['xsel', '--clipboard', '--input'], stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
        elif os_name == "Windows":
            process = subprocess.Popen(['clip.exe'], stdin=subprocess.PIPE)
            process.communicate(input=text.encode('utf-8'))
        return True
    except Exception:
        return False

import glob

def resolve_file_injection(val):
    """
    Resolves file injection. Supports:
    - @path/to/file (Single file)
    - @path/to/*.py (Glob pattern)
    Concatenates multiple files with headers.
    """
    if not val.startswith("@"):
        return val
    
    pattern = val[1:]
    matches = glob.glob(pattern, recursive=True)
    
    if not matches:
        if any(char in pattern for char in "*?[]"):
            print(f"{Colors.YELLOW}Warning: No files matched glob '{pattern}'. Using raw string.{Colors.RESET}", file=sys.stderr)
        elif not os.path.exists(pattern):
            print(f"{Colors.YELLOW}Warning: File {pattern} not found. Using raw string.{Colors.RESET}", file=sys.stderr)
        return val

    contents = []
    files = sorted([m for m in matches if os.path.isfile(m)])
    
    if not files:
        return val

    for f_path in files:
        try:
            with open(f_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if len(files) > 1:
                    contents.append(f"--- File: {f_path} ---\n{content}")
                else:
                    contents.append(content)
        except Exception as e:
            print(f"{Colors.YELLOW}Warning: Could not read file {f_path} ({e}).{Colors.RESET}", file=sys.stderr)
    
    return "\n\n".join(contents).strip()
