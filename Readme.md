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
```bash
python main.py /path/to/your/python/project
```

### 4. View the Report
- Check `report/report.json` for raw data
- Open `report/report.md` for a readable summary
- Launch the Streamlit app:
```bash
streamlit run streamlit_app.py
```

---

## 📚 Requirements
- Python 3.8+
- `flake8`
- `pylint`
- `radon`
- `streamlit`

```bash
pip install flake8 pylint radon streamlit
```

---

## 📊 Example Output
- Linter Issues Count (from flake8 and pylint)
- Cyclomatic Complexity Score
- Suggestions for Better Code Practices
- Total Quality Score per file & repository

---

## 🚧 Future Enhancements
- GitHub Actions integration for CI
- Export report to HTML/PDF
- Auto PR comments for suggestions

---

## ✅ License
MIT License. Use freely and contribute improvements!
