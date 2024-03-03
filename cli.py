import typer
import os
from datetime import datetime

app = typer.Typer()

@app.command("migration:create")
def create_migration(name: str):
    splitted_name = name.split(" ")
    file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_{'_'.join(splitted_name)}"
    class_name = "".join(word.capitalize() for word in splitted_name)
    
    file_content = f"""from hudorem.core import Migration
    
class {class_name}:
    def up(self):
        pass
    
    def down(self):
        pass
    """
    with open(f"migrations/{file_name}.py", "w") as file:
        file.write(file_content)
    typer.echo("Creating a new migration.")
    

@app.command("migration:rollback")
def edit_migration():
    typer.echo("Rollback a migration.")
    
@app.command("migrate")
def run_migration():
    from main import run_migrations
    run_migrations()

if __name__ == "__main__":
    app()
