# Import necessary modules
import os
import json
from analyzer.repo_scanner import get_python_files  # Function to retrieve Python files from a repository
from analyzer.linter_runner import run_flake8  # Function to run Flake8 linter on a file
from analyzer.complexity_checker import get_file_complexity  # Function to calculate code complexity
from analyzer.suggester import get_suggestions  # Function to generate suggestions based on linter issues
from analyzer.scorer import calculate_file_score  # Function to calculate a score for a file based on issues and complexity

# Function to analyze a Python repository for code quality
def analyze_repo(repo_path, output_path="report"):
    """
    Analyzes a Python repository for code quality and generates a JSON report.

    Args:
        repo_path (str): Path to the repository to analyze.
        output_path (str): Directory to save the analysis report. Defaults to "report".

    Returns:
        None
    """
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)
    results = []  # List to store analysis results for each file

    # Retrieve all Python files in the repository
    py_files = get_python_files(repo_path)
    for file_path in py_files:
        # Read the content of the Python file
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()

        # Run Flake8 linter on the file and get issues
        linter_issues = run_flake8(file_path)
        # Calculate complexity metrics for the file
        complexity_metrics = get_file_complexity(code)
        # Generate suggestions based on linter issues
        suggestions = get_suggestions(linter_issues)
        # Calculate the overall score for the file
        score = calculate_file_score(linter_issues, complexity_metrics)

        # Append the analysis result for the file
        results.append({
            "filename": file_path,
            "linter_issues": len(linter_issues),
            "complexity_score": score["complexity_score"],
            "total_score": score["total_score"],
            "suggestions": suggestions
        })

    # Calculate the overall score for the repository
    overall_score = sum([r["total_score"] for r in results]) / len(results) if results else 0

    # Create a report dictionary
    report = {
        "summary": {
            "files_analyzed": len(results),
            "overall_score": round(overall_score, 2)
        },
        "details": results
    }

    # Save the report as a JSON file
    with open(os.path.join(output_path, "report.json"), "w") as f:
        json.dump(report, f, indent=4)

    # Print a success message
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
    # Define the path for the Markdown report
    md_path = os.path.join(output_path, "report.md")
    with open(md_path, "w") as md:
        # Write the report header
        md.write(f"# 🧪 Code Quality Report\n\n")
        md.write(f"**Files Analyzed**: {report['summary']['files_analyzed']}\n\n")
        md.write(f"**Overall Score**: {report['summary']['overall_score']} / 100\n\n")
        md.write("---\n\n")

        # Write details for each analyzed file
        for detail in report["details"]:
            md.write(f"### 📄 {detail['filename']}\n")
            md.write(f"- **Linter Issues**: {detail['linter_issues']}\n")
            md.write(f"- **Complexity Score**: {detail['complexity_score']:.2f}\n")
            md.write(f"- **Total Score**: {detail['total_score']:.2f}\n")
            if detail['suggestions']:
                md.write(f"- **Suggestions:**\n")
                for s in detail['suggestions']:
                    md.write(f"  - {s}\n")
            md.write("\n")
    # Print a success message
    print(f"📄 Markdown report saved to {md_path}")

# Main entry point for the script
if __name__ == "__main__":
    import argparse  # Module to handle command-line arguments

    # Set up argument parser
    parser = argparse.ArgumentParser(description="🔍 Analyze a Python codebase for code quality and standards.")
    parser.add_argument("repo_path", help="Path to the Python repository")  # Path to the repository
    parser.add_argument("--output", default="report", help="Directory to save the report")  # Output directory

    # Parse the command-line arguments
    args = parser.parse_args()
    # Run the analysis
    analyze_repo(args.repo_path, args.output)

    # Optional: Generate a Markdown report
    with open(os.path.join(args.output, "report.json")) as f:
        report_data = json.load(f)
    write_markdown_report(report_data, args.output)