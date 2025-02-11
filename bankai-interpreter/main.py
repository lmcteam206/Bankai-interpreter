import pandas as pd
import builtins
import keyword
import os
import colorama
import pyreadline3 as readline
from colorama import Fore, Style

colorama.init(autoreset=True)

EXCEL_FILE = "customs.xlsx"
HISTORY_FILE = "history.log"
CUSTOM_EXTENSION = ".bankai"  # Default extension for scripts

def create_excel():
    """Create an Excel file with Python keywords and built-in functions."""
    python_keywords = keyword.kwlist + dir(builtins)
    df = pd.DataFrame({"Original": python_keywords, "Custom": python_keywords})
    df.to_excel(EXCEL_FILE, index=False)
    print(f"{Fore.GREEN}✅ {EXCEL_FILE} has been created successfully!")

def load_custom_names():
    """Load custom names from the Excel file."""
    try:
        df = pd.read_excel(EXCEL_FILE)
        if "Original" not in df.columns or "Custom" not in df.columns:
            raise ValueError(f"{Fore.RED}❌ The Excel file does not contain the required columns!")
        return dict(zip(df["Original"].dropna(), df["Custom"].dropna()))
    except FileNotFoundError:
        print(f"{Fore.YELLOW}⚠️ Excel file not found! Creating a new one...")
        create_excel()
        return load_custom_names()

def clone_and_rename_builtin_functions(custom_names):
    """Map custom names to built-in Python functions."""
    for original, custom in custom_names.items():
        if hasattr(builtins, original):  
            setattr(builtins, custom, getattr(builtins, original))  

def convert_code(bankai_code, custom_names):
    """Convert bankai script to Python using custom names."""
    for original, custom in custom_names.items():
        bankai_code = bankai_code.replace(custom, original)
    return bankai_code

def show_excel_contents():
    """Display the contents of the Excel file."""
    try:
        df = pd.read_excel(EXCEL_FILE)
        print(f"\n{Fore.CYAN}📜 **Custom Word Mapping:** 📜\n")
        print(df.to_string(index=False))
    except FileNotFoundError:
        print(f"{Fore.YELLOW}⚠️ Excel file not found! Please create it first.")

def save_history(command):
    """Save executed commands to history file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(command + "\n")

def view_history():
    """View command history."""
    if os.path.exists(HISTORY_FILE):
        print(f"\n{Fore.MAGENTA}📜 Command History:\n")
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            print(file.read())
    else:
        print(f"{Fore.YELLOW}⚠️ No command history found.")

def run_script(script_file, custom_names):
    """Run a .bankai script file."""
    if not script_file.endswith(CUSTOM_EXTENSION):
        print(f"{Fore.RED}❌ Error: Only '{CUSTOM_EXTENSION}' files can be executed!")
        return
    
    try:
        with open(script_file, "r", encoding="utf-8") as f:
            original_code = f.read()
    except FileNotFoundError:
        print(f"{Fore.RED}❌ Script file '{script_file}' not found!")
        return
    
    converted_code = convert_code(original_code, custom_names)
    print(f"\n{Fore.YELLOW}🚀 Running Script...\n")
    try:
        exec(converted_code)
    except Exception as e:
        print(f"\n{Fore.RED}❌ Execution Error: {e}")

def change_extension():
    """Allow user to change the allowed script extension."""
    global CUSTOM_EXTENSION
    new_ext = input(f"{Fore.YELLOW}Enter new script extension (with dot, e.g., .custom): {Style.RESET_ALL}").strip()
    if not new_ext.startswith("."):
        print(f"{Fore.RED}❌ Invalid extension format. Must start with '.'")
    else:
        CUSTOM_EXTENSION = new_ext
        print(f"{Fore.GREEN}✅ Script extension changed to '{CUSTOM_EXTENSION}'")

def bankai_interpreter():
    """Interactive interpreter for .bankai language with multiline input support."""
    print(f"\n{Fore.MAGENTA}🔥 **Welcome to the Bankai Interpreter!** 🔥")
    print(f"{Fore.YELLOW}Type commands or enter a {CUSTOM_EXTENSION} script to execute.")
    print(f"{Fore.GREEN}Type `.exit` to quit, `.help` for options.\n")
    
    custom_names = load_custom_names()
    clone_and_rename_builtin_functions(custom_names)

    multiline_code = []

    while True:
        command = input(f"{Fore.BLUE}bankai> {Style.RESET_ALL}").strip()

        if command == ".exit":
            print(f"{Fore.RED}👋 Exiting Bankai Interpreter. Goodbye!")
            break
        elif command == ".help":
            print(f"\n{Fore.CYAN}📜 **Bankai Commands:**")
            print(f"  {Fore.YELLOW}.exit      {Fore.RESET}→ Exit the interpreter")
            print(f"  {Fore.YELLOW}.help      {Fore.RESET}→ Show this help menu")
            print(f"  {Fore.YELLOW}.view      {Fore.RESET}→ View custom words in Excel")
            print(f"  {Fore.YELLOW}.script    {Fore.RESET}→ Run a {CUSTOM_EXTENSION} script file")
            print(f"  {Fore.YELLOW}.reload    {Fore.RESET}→ Reload the custom words from Excel")
            print(f"  {Fore.YELLOW}.create    {Fore.RESET}→ Create a new Excel file with default mappings")
            print(f"  {Fore.YELLOW}.history   {Fore.RESET}→ View command history")
            print(f"  {Fore.YELLOW}.ext       {Fore.RESET}→ Change script extension\n")
        elif command == ".view":
            show_excel_contents()
        elif command == ".script":
            script_file = input(f"{Fore.YELLOW}Enter the script filename: {Style.RESET_ALL}").strip()
            run_script(script_file, custom_names)
        elif command == ".reload":
            custom_names = load_custom_names()
            clone_and_rename_builtin_functions(custom_names)
            print(f"{Fore.GREEN}🔄 Custom word mappings reloaded!")
        elif command == ".create":
            create_excel()
        elif command == ".history":
            view_history()
        elif command == ".ext":
            change_extension()
        else:
            save_history(command)
            try:
                converted_command = convert_code(command, custom_names)
                exec(converted_command)
            except Exception as e:
                print(f"{Fore.RED}❌ Error: {e}")

if __name__ == "__main__":
    bankai_interpreter()
