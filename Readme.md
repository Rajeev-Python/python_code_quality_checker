# 🔍 Python Code Quality Checker

A tool to analyze a Python codebase and generate a report based on:
- Code linting issues (via flake8 and pylint)
- Code complexity (via radon)
- Suggestions for improvement
- An overall quality score

## 🌐 Features
- Automatically analyzes all Python files in a given directory
- Generates a JSON and Markdown report with detailed insights
- Streamlit app available for visual report exploration
- **Parallel Execution**: Uses `ThreadPoolExecutor` to analyze files in parallel for faster performance.
- **Linter Integration**: Runs `flake8` and `pylint` in parallel for each file.
- **Complexity Analysis**: Uses Radon to calculate cyclomatic complexity.
- **Suggestions Engine**: Provides actionable suggestions for improving code quality.
- **Progress Bar**: Displays a progress bar during analysis for better user experience.
- **Per-File Timing**: Logs the time taken to analyze each file for performance insights.


---

## 📁 Project Structure
```
project/
├── analyzer/
│   ├── repo_scanner.py         # Finds Python files in a repo
│   ├── linter_runner.py        # Runs flake8 and pylint on each file
│   ├── complexity_checker.py  # Calculates code complexity using radon
│   ├── suggester.py           # Suggests improvements based on linter output
│   └── scorer.py              # Computes code quality scores
├── main.py                    # Main script to run the analyzer
├── streamlit_app.py           # Streamlit UI for visualizing report.json
├── report/                    # Output folder for reports
│   └── report.json / report.md
└── README.md                  # This file
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/python-code-quality-checker.git
cd python-code-quality-checker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Analyzer
Analyze a Repository
Run the script to analyze a Python repository:

`python main.py <path_to_repository> --output <output_directory>`

Replace <path_to_repository> with the path to the Python repository you want to analyze.
Replace <output_directory> with the directory where the reports will be saved (default is report).
Example:

`python main.py ./example_repo --output ./output`

Output
JSON Report: A detailed JSON report is saved in the specified output directory as report.json.
Markdown Report: A human-readable Markdown report is saved in the specified output directory as report.md.

### 4. View the Report
- Check `report/report.json` for raw data
- Open `report/report.md` for a readable summary
- Launch the Streamlit app:
```bash
streamlit run streamlit_app.py
```
### 5. Running Test

- The tests folder contains unit tests for all modules in the analyzer folder. Each test file corresponds to a module and includes test cases for its functions.

Run All Tests
To run all tests, use the following command:

`python -m unittest discover -s tests`

Run a Specific Test File
To run a specific test file, use:
`python -m unittest tests.<test_file_name>`

For example:

`python -m unittest tests.test_complexity_checker`

---

## 📚 Requirements
- Python 3.8+
- `flake8`
- `pylint`
- `radon`
- `streamlit`
- `tqdm`

```bash
pip install flake8 pylint radon streamlit
```

---

## 📊 Example Output
- Linter Issues Count (from flake8 and pylint)
- Cyclomatic Complexity Score
- Suggestions for Better Code Practices
- Total Quality Score per file & repository

JSON Report
The JSON report is saved in the specified output directory as report.json. Example:

{
    "summary": {
        "files_analyzed": 157,
        "overall_score": 85.69
    },
    "details": [
        {
            "filename": "D:\\Git\\python-mini-projects\\projects\\AudioBook\\Audio-book.py",
            "linter_issues": 17,
            "complexity_score": 0.00,
            "total_score": 86.50,
            "suggestions": [
                "🟡 Style - Remove whitespace at the end of lines.",
                "🟡 Style - Fix indentation to match Python's recommended 4-space standard.",
                "🔴 Error - Always catch specific exceptions instead of using bare `except:`."
            ]
        }
    ]
}


Markdown Report
The Markdown report is saved in the specified output directory as report.md. Example:

# 🧪 Code Quality Report

**Files Analyzed**: 157

**Overall Score**: 85.69 / 100

---

### 📄 D:\Git\python-mini-projects\projects\AudioBook\Audio-book.py
- **Linter Issues (Flake8)**: 17
- **Complexity Score**: 0.00
- **Total Score**: 86.50
- **Suggestions:**
  - 🟡 Style - Remove whitespace at the end of lines.
  - 🟡 Style - Fix indentation to match Python's recommended 4-space standard.
  - 🔴 Error - Always catch specific exceptions instead of using bare `except:`.
---

## Performance Improvements
Parallel Execution: Files are analyzed in parallel using ThreadPoolExecutor.
Batch Linting: flake8 and pylint are run in parallel for each file.
Progress Bar: A progress bar is displayed during analysis using tqdm.
Per-File Timing: Logs the time taken to analyze each file for performance insight

---
## 🚧 Future Enhancements
- GitHub Actions integration for CI
- Export report to HTML/PDF
- Auto PR comments for suggestions

---
