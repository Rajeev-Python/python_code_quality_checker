# Import the subprocess module to run external commands
import subprocess

# Function to run Flake8 linter on a given file
def run_flake8(file_path):
    """
    Runs the Flake8 linter on the specified Python file.

    Args:
        file_path (str): The path to the Python file to lint.

    Returns:
        list: A list of linting issues reported by Flake8, or an error message if the command fails.
    """
    try:
        # Run the Flake8 command and capture its output
        result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
        # Return the list of issues if any, otherwise return an empty list
        return result.stdout.strip().split('\n') if result.stdout else []
    except Exception as e:
        # Return an error message if Flake8 fails to run
        return [f"Error running flake8: {e}"]

# Function to run Pylint on a given file
def run_pylint(file_path):
    """
    Runs the Pylint linter on the specified Python file with certain checks disabled.

    Args:
        file_path (str): The path to the Python file to lint.

    Returns:
        list: A list of linting issues reported by Pylint, or an error message if the command fails.
    """
    try:
        # Run the Pylint command with specific options and capture its output
        result = subprocess.run(['pylint', file_path, '--disable=R,C'], capture_output=True, text=True)
        # Return the list of issues if any, otherwise return an empty list
        return result.stdout.strip().split('\n') if result.stdout else []
    except Exception as e:
        # Return an error message if Pylint fails to run
        return [f"Error running pylint: {e}"]