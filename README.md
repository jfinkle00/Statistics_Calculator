# 📊 Single Mean Statistics Calculator

A user-friendly desktop GUI application (built with PySimpleGUI) for calculating statistical summaries, visualizing distributions, and analyzing confidence intervals for a single numerical dataset.

---

## 🚀 Features

- 📁 **CSV File Upload** support
- ✍️ **Manual Data Entry** option
- 🧠 **Summary Statistics**:
  - Mean, Standard Deviation, Variance, Min/Max, Range
  - Coefficient of Variation, Standard Error, Z-Score, MOE
  - Confidence Intervals (t-distribution)
- 📈 **Plotting**:
  - Line Plot
  - Histogram
- 📦 **Descriptive Statistics** for column in uploaded file

---

## 🖼️ GUI Overview

| Feature                  | Description |
|--------------------------|-------------|
| File Upload              | Enter file path to a `.csv` file |
| Column Selector          | Specify the column name to analyze |
| Manual Data Input        | Enter a comma-separated list of values |
| Manual Parameters        | Input mean, standard deviation, count, and x-value |
| Confidence Level         | Default is 0.95 |
| Buttons                  | Trigger statistical calculations or visualizations |

---

## 🛠️ Technologies Used

- Python 3.x  
- [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) – GUI interface  
- [matplotlib](https://matplotlib.org/) – Plotting  
- [pandas](https://pandas.pydata.org/) – File and data handling  
- [scipy.stats](https://docs.scipy.org/doc/scipy/) – Confidence intervals  
- [statistics](https://docs.python.org/3/library/statistics.html) – Descriptive stats

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/single-mean-statistics-calculator.git
cd single-mean-statistics-calculator
```

2. Install dependencies:
```bash
pip install PySimpleGUI matplotlib pandas scipy
```

---

## ▶️ How to Run

```bash
python statistics_calculator.py
```

---

## 📸 Example

- Analyze custom data:
  - Input: `1,2,3,4,5,6`
  - Click "Manual Stat Summary"
- Or:
  - Upload a `.csv` file
  - Enter column name
  - Click "File Stat Summary" or plot buttons

---

## 📁 File Format

CSV files should be structured with a **header row** and at least one column of numeric data:
```
col1
1
2
3
4
5
```

---

## 📈 Output Includes

- `Mean`, `StDev`, `Variance`
- `Z-Score` and `Margin of Error (MOE)`
- `Confidence Intervals`
- `Range`, `Quantiles`, `Coefficient of Variation`
- Descriptive summary for uploaded files

---

## 🧪 Future Enhancements

- Support for two-sample comparisons  
- Export results to PDF/CSV  
- Integration of normality tests  
- GUI enhancements with dark mode  

---

## 🧑‍💻 Author

**Your Name**  
Feel free to contribute or suggest improvements via pull requests or issues!

---

## 📄 License

MIT License  
See `LICENSE` for more information.