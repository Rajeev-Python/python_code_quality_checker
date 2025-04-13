# Import the `cc_visit` function from the Radon library to analyze cyclomatic complexity
from radon.complexity import cc_visit

# Function to calculate the complexity of a Python file
def get_file_complexity(code):
    """
    Analyzes the cyclomatic complexity of the given Python code.

    Args:
        code (str): The source code of the Python file as a string.

    Returns:
        dict: A dictionary containing:
            - 'average_complexity': The average cyclomatic complexity of the code blocks.
            - 'complexity_score': A score (0-100) based on the complexity, where lower complexity results in a higher score.
    """
    # Analyze the code blocks for cyclomatic complexity
    blocks = cc_visit(code)
    
    # Calculate the total complexity of all blocks
    total = sum([b.complexity for b in blocks])
    
    # Calculate the average complexity (avoid division by zero)
    avg = total / len(blocks) if blocks else 0
    
    # Return the average complexity and a normalized complexity score
    return {
        'average_complexity': avg,
        'complexity_score': max(0, 100 - avg * 5)  # Deduct points based on average complexity
    }