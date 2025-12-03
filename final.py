import subprocess
import os

# Fill in the actual filenames for each branch below!
branch_configs = [
    {"branch": "Natasha", "file": "code.ipynb"},          # Example: Python script
    {"branch": "Miguel", "file": "code.ipynb"},        # Example: Jupyter notebook
    {"branch": "axel", "file": "main.py"},
    {"branch": "alessiagentile97-ui-patch-1", "file": "assignment2vip.ipynb"},
    # Add more as needed
]

def run_python(filepath):
    print(f"--- Running {filepath} with Python ---")
    result = subprocess.run(["python", filepath], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error output:", result.stderr)

def run_notebook(filepath):
    print(f"--- Executing notebook {filepath} ---")
    result = subprocess.run([
        "jupyter", "nbconvert", "--to", "notebook", "--execute", "--stdout", filepath
    ], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error output:", result.stderr)

def run_in_branch(branch, codefile):
    print(f"\n=== Checking out {branch} ===")
    subprocess.run(["git", "checkout", branch], check=True)
    if os.path.isfile(codefile):
        if codefile.endswith('.py'):
            run_python(codefile)
        elif codefile.endswith('.ipynb'):
            run_notebook(codefile)
        else:
            print(f"Unknown file type: {codefile}")
    else:
        print(f"{codefile} not found in {branch}")

def main():
    completed = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
    current_branch = completed.stdout.strip()
    print(f"Current branch: {current_branch}")

    for config in branch_configs:
        run_in_branch(config["branch"], config["file"])

    print(f"\n=== Returning to {current_branch} ===")
    subprocess.run(["git", "checkout", current_branch], check=True)

if __name__ == "__main__":
    main()
