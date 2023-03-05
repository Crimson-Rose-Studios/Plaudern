import os
from pathlib import Path

# import modules in src/commands directory
for filename in os.listdir(Path.cwd() / "src" / "commands"):
    if filename.endswith(".py"):
        module_name = filename[:-3]
        exec(f"from src.commands import {commands}")