import os
import importlib

dps = []

commands_path = os.path.dirname(__file__)

for filename in os.listdir(commands_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module_full_name = f"src.middlewares.{module_name}"
        module = importlib.import_module(module_full_name)
        if hasattr(module, "dp"):
            dps.append(module.dp)
