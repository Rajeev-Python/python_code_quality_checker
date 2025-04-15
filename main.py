# Import necessary modules
import os
import json
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from analyzer.repo_scanner import get_python_files  # Function to retrieve Python files from a repository
from analyzer.linter_runner import run_flake8, run_pylint  # Updated: Import run_pylint
from analyzer.complexity_checker import get_file_complexity  # Function to calculate code complexity
from analyzer.suggester import generate_suggestions  # Function to generate suggestions based on linter issues
from analyzer.scorer import calculate_score  # Function to calculate a score for a file based on issues and complexity

def analyze_file(file_path):
    """
    Analyzes a single Python file and returns the result.
    """
    start_time = time.time()  # Start timing the analysis

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        code = f.read()

    # Run flake8 and pylint in parallel
    with ThreadPoolExecutor() as executor:
        flake8_future = executor.submit(run_flake8, file_path)
        pylint_future = executor.submit(run_pylint, file_path)

        flake8_issues = flake8_future.result()
        pylint_output = pylint_future.result()

    # Calculate complexity metrics for the file
    complexity_metrics = get_file_complexity(code)

    # Ensure complexity_metrics is a list of objects with a 'complexity' attribute
    complexity_metrics = [block for block in complexity_metrics if hasattr(block, 'complexity')]

    # Combine flake8 issues and raw pylint output for suggestion engine
    suggestion_input = flake8_issues + pylint_output
    suggestions = generate_suggestions(suggestion_input)

    # Calculate the overall score for the file
    score = calculate_score(flake8_issues, pylint_output, complexity_metrics)

    # Calculate the complexity score (e.g., sum or average of complexities)
    complexity_score = sum(block.complexity for block in complexity_metrics) / len(complexity_metrics) if complexity_metrics else 0

    # Log the time taken for this file
    elapsed_time = time.time() - start_time
    print(f"⏱️ {file_path} analyzed in {elapsed_time:.2f} seconds")

    return {
        "filename": file_path,
        "linter_issues": len(flake8_issues),
        "complexity_score": round(complexity_score, 2),
        "total_score": score["total_score"],
        "suggestions": suggestions
    }

# Function to analyze a Python repository for code quality
def analyze_repo(repo_path, output_path="report"):
    """
    Analyzes a Python repository for code quality and generates a JSON report.
    """
    os.makedirs(output_path, exist_ok=True)
    py_files = get_python_files(repo_path)

    results = []
    with ThreadPoolExecutor() as executor:
        # Use tqdm to display a progress bar
        futures = {executor.submit(analyze_file, file): file for file in py_files}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Analyzing files"):
            try:
                results.append(future.result())
            except Exception as e:
                print(f"❌ Error analyzing file {futures[future]}: {e}")

    overall_score = sum([r["total_score"] for r in results]) / len(results) if results else 0

    report = {
        "summary": {
            "files_analyzed": len(results),
            "overall_score": round(overall_score, 2)
        },
        "details": results
    }

    with open(os.path.join(output_path, "report.json"), "w") as f:
        json.dump(report, f, indent=4)

    print(f"✅ Analysis complete. Report saved to {os.path.join(output_path, 'report.json')}")

# Function to write a Markdown report from the analysis results
def write_markdown_report(report, output_path):
    """
    Generates a Markdown report from the analysis results.

    Args:
        report (dict): The analysis report data.
        output_path (str): Directory to save the Markdown report.

    Returns:
        None
    """
    md_path = os.path.join(output_path, "report.md")
    with open(md_path, "w", encoding="utf-8") as md:
        md.write(f"# 🧪 Code Quality Report\n\n")
        md.write(f"**Files Analyzed**: {report['summary']['files_analyzed']}\n\n")
        md.write(f"**Overall Score**: {report['summary']['overall_score']} / 100\n\n")
        md.write("---\n\n")

        for detail in report["details"]:
            md.write(f"### 📄 {detail['filename']}\n")
            md.write(f"- **Linter Issues (Flake8)**: {detail['linter_issues']}\n")
            md.write(f"- **Complexity Score**: {detail['complexity_score']:.2f}\n")
            md.write(f"- **Total Score**: {detail['total_score']:.2f}\n")
            if detail['suggestions']:
                md.write(f"- **Suggestions:**\n")
                for s in detail['suggestions']:
                    md.write(f"  - {s}\n")
            md.write("\n")
    print(f"📄 Markdown report saved to {md_path}")

# Main entry point for the script
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="🔍 Analyze a Python codebase for code quality and standards.")
    parser.add_argument("repo_path", help="Path to the Python repository")
    parser.add_argument("--output", default="report", help="Directory to save the report")

    args = parser.parse_args()
    analyze_repo(args.repo_path, args.output)

    with open(os.path.join(args.output, "report.json")) as f:
        report_data = json.load(f)
    write_markdown_report(report_data, args.output)
