import os
import glob
from hudorem.core import Migration
import importlib.util

def run_migrations():
    migration = Migration("localhost", "hudya", "secret", "hudorem_test")

    migration_files = sorted(glob.glob("migrations/*.py"))
    
    for migration_file in migration_files:
        if "init" in migration_file:
            continue
        
        print("Running migration:", migration_file)
        splitted_filename = os.path.basename(migration_file)[:-3].split("_")
        splitted_filename = splitted_filename[6:]
        print(splitted_filename)
        
        class_name = "".join(word.capitalize() for word in splitted_filename[0:])
        function_name = "up"
        
        print(class_name)
        
        full_path = os.path.abspath(migration_file)
        spec = importlib.util.spec_from_file_location("module_name", full_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        obj = getattr(module, class_name)
        instance = obj()
        getattr(instance, function_name)()

    migration.close_connection()