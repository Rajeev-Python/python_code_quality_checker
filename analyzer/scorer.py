def calculate_score(flake8_issues, pylint_output, complexity):
    """
    Calculates the overall quality score for a Python file based on linter issues,
    pylint output, and code complexity.

    Args:
        flake8_issues (list): A list of issues reported by Flake8.
        pylint_output (str): The raw output from pylint analysis.
        complexity (list): A list of code blocks with their complexity metrics.

    Returns:
        dict: A dictionary containing:
            - 'complexity_score': The complexity score.
            - 'total_score': The overall quality score.
    """
    # Start with a perfect score of 100
    score = 100.0

    # Deduct points for each Flake8 issue (0.5 points per issue)
    score -= 0.5 * len(flake8_issues)

    # Deduct points based on pylint rating
    try:
        # Parse the pylint output to find the rating line
        for line in pylint_output.splitlines():
            if "Your code has been rated at" in line:
                # Extract the pylint rating (e.g., "8.00/10")
                rating_str = line.split(" ")[6]
                pylint_rating = float(rating_str.split("/")[0])
                # Deduct points based on the difference from the maximum rating (10)
                score -= (10 - pylint_rating)
                break
    except:
        # If no rating is found or an error occurs, apply a fallback penalty
        score -= 5

    # Deduct points for code complexity
    complexity_score = 100  # Start with a perfect complexity score
    for block in complexity:
        if isinstance(block, dict) and 'complexity' in block:
            complexity_score -= 0.2 * block['complexity']
        elif hasattr(block, 'complexity'):
            complexity_score -= 0.2 * block.complexity
        else:
            complexity_score -= 1

    # Ensure scores are not negative and round them
    complexity_score = max(0, round(complexity_score, 2))
    total_score = max(0, round(score, 2))

    return {
        "complexity_score": complexity_score,
        "total_score": total_score
    }