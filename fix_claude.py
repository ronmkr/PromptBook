import json
import re
from pathlib import Path

def fix_settings():
    # Dynamically locate the .claude directory in your home folder
    settings_path = Path.home() / '.claude' / 'settings.json'
    backup_path = Path.home() / '.claude' / 'settings.json.backup'

    if not settings_path.exists():
        print(f"❌ Could not find settings file at: {settings_path}")
        return

    try:
        # Read the broken file
        content = settings_path.read_text(encoding='utf-8')

        # Create a backup
        backup_path.write_text(content, encoding='utf-8')
        print(f"\n📦 Created a backup at: {backup_path}")

        # Step 1: Strip block comments (/* ... */)
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)

        # Step 2: Strip line comments (// ...), ignoring URLs like http://
        content = re.sub(r'(?<!:)//.*', '', content)

        # Step 3: Remove trailing commas before closing braces/brackets
        content = re.sub(r',\s*([\]}])', r'\1', content)

        # Step 4: Validate and format
        parsed_json = json.loads(content)
        clean_json = json.dumps(parsed_json, indent=2)

        # Write the newly fixed JSON back to the file
        settings_path.write_text(clean_json, encoding='utf-8')
        print("✅ Successfully fixed, formatted, and saved your settings.json!\n")

    except json.JSONDecodeError as e:
        print("\n❌ Could not automatically fix the JSON.")
        print("The syntax error is too severe (e.g., missing a closing brace, bracket, or quote).")
        print(f"Details: {e}\n")
        print("To completely reset the file, run:")
        print("echo '{}' > ~/.claude/settings.json\n")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    fix_settings()
