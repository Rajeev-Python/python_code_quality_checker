def calculate_file_score(linter_issues, complexity_metrics):
    lint_penalty = min(len(linter_issues) * 2, 50)
    complexity_score = complexity_metrics.get('complexity_score', 100)
    total_score = max(0, complexity_score - lint_penalty)
    return {
        'complexity_score': complexity_score,
        'total_score': total_score
    }
