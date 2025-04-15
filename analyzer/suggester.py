def generate_suggestions(lint_results):
    suggestions = []
    suggestion_map = {
        "line too long": ("Break long lines into shorter segments for better readability.", "🟡 Style"),
        "unused import": ("Remove unused imports to clean up the code.", "🟡 Style"),
        "imported but unused": ("Clean up imports that are never used.", "🟡 Style"),
        "undefined name": ("Make sure all variables and functions are defined before use.", "🔴 Error"),
        "missing whitespace": ("Add proper whitespace around operators or punctuation.", "🟡 Style"),
        "missing whitespace after": ("Ensure there's a space after commas, colons, or semicolons.", "🟡 Style"),
        "multiple statements": ("Avoid writing multiple statements on one line.", "🟡 Style"),
        "comparison with None": ("Use `is None` or `is not None` instead of `==` or `!=`.", "🟡 Style"),
        "comparison with True": ("Use `if var:` instead of `if var == True`.", "🟡 Style"),
        "comparison with False": ("Use `if not var:` instead of `if var == False`.", "🟡 Style"),
        "indentation": ("Fix indentation to match Python's recommended 4-space standard.", "🟡 Style"),
        "expected 2 blank lines": ("Add two blank lines before top-level definitions.", "🟡 Style"),
        "unexpected spaces": ("Remove unnecessary spaces around brackets or braces.", "🟡 Style"),
        "trailing whitespace": ("Remove whitespace at the end of lines.", "🟡 Style"),
        "redefined function": ("Avoid redefining functions or variables with the same name.", "🟠 Code Smell"),
        "too many local variables": ("Refactor functions with too many variables.", "🟠 Complexity"),
        "too many arguments": ("Simplify functions with many arguments or use `*args`/`**kwargs`.", "🟠 Complexity"),
        "too many branches": ("Consider simplifying functions with many branches.", "🟠 Complexity"),
        "too many return statements": ("Avoid excessive return statements in one function.", "🟠 Complexity"),
        "too complex": ("Simplify complex functions or split them into smaller ones.", "🔴 Complexity"),
        "missing function docstring": ("Add docstrings to explain what each function does.", "🟡 Style"),
        "missing module docstring": ("Add a docstring at the top of your module.", "🟡 Style"),
        "missing class docstring": ("Include docstrings to describe your class purpose.", "🟡 Style"),
        "attribute-defined-outside-init": ("Define instance attributes inside `__init__()`.", "🔴 Error"),
        "broad-except": ("Avoid catching all exceptions; be specific.", "🔴 Error"),
        "bare-except": ("Always catch specific exceptions instead of using bare `except:`.", "🔴 Error"),
        "no-self-use": ("Convert methods that don't use `self` to static methods.", "🟡 Style"),
    }

    seen = set()
    for issue in lint_results:
        for keyword, (message, level) in suggestion_map.items():
            if keyword in issue.lower() and keyword not in seen:
                suggestions.append(f"{level} - {message}")
                seen.add(keyword)

    if not suggestions:
        suggestions.append("✅ Code looks clean. Great job!")

    return suggestions