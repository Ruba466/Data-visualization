# Data Visualization

A beginner-friendly Python program demonstrating how to create basic plots using the `matplotlib` library.
This repository is part of my Python tutorials collection for learning data visualization.


### 1. Line Plot Program
A simple line chart created using Matplotlib to visualize data trends over time.  
Includes markers, custom line styles, axis labels, title, and a grid.
### 🔧 Code File:
- `Line_plot.py`
### 📈 Line Plot Output
![Line Plot](Images/line_plot.png)


### 2. Bar Chart Program
A basic bar chart showing student scores across different subjects using Matplotlib.  
Demonstrates labeled axes, colored bars, and a descriptive chart title.
### 🔧 Code File:
- `Bar_chart.py`
### 📊 Bar Chart Output
![Bar Chart](Images/bar_chart.png)


### 3. Subplot Program
This Python program visualizes a dataset using a line plot, bar chart, and pie chart in a single figure with subplots. It uses Matplotlib to display and save the combined chart as an image.
### 🔧 Code File:
- `subplot.py`
### 📊 Bar Chart Output
![Subpot](Images/subplots_combined.png)


### 4. Iris Data Visualization (Histogram & Boxplot)

A Python program using Seaborn and Matplotlib to explore the `sepal_width` feature of the Iris dataset.  
It displays two subplots side-by-side: a histogram with a KDE curve and a boxplot for detailed distribution analysis.

#### 🔍 Inference from the Histogram:
- The **sepal width** values show a **roughly normal distribution** with a slight **left skew**.
- Most values lie between **2.8 cm and 3.4 cm**, with a peak around **3.0 cm**.
- Few samples have **extremely low or high sepal widths**, indicating limited outliers.
- The **KDE curve** suggests the data is smoothly spread without sharp deviations.

### 🔧 Code File:
- `IrisData.ipynb`


### 5. Tips Data Visualization (Histogram, Boxplot, Piechart, Barchart)
This notebook visualizes the 'tips' dataset using histogram, boxplot, pie chart, and bar chart.
It demonstrates multi-plot creation with Seaborn and Matplotlib in a 2x2 grid layout.

## 📊 Dataset

This project uses the popular `tips` dataset for visualization.

You can load it in two ways:

 1. **Using Seaborn directly** (no need to download anything):
   ```python
   import seaborn as sns
   tips = sns.load_dataset("tips")
2. **Using a CSV file dowloaded** (if you have tips.csv):
    ```python
   import pandas as pd
   tips = pd.read_csv("tips.csv")


### 🔧 Code File:
- `hist_box_plot.ipynb`


# ->>> 📊 Interactive Data Visualization App

A simple Streamlit web app that allows users to upload a CSV file and explore key data insights using a histogram, boxplot, pie chart, and bar chart interactively.

# Features
- Upload your own CSV file
- View:
  - Histogram of `total_bill`
  - Boxplot of `tip` values
  - Pie chart showing gender distribution
  - Bar chart of average total bill by day

### 🔧 Code File:
- `app.py`

## 🚀 Getting Started

Make sure you have Python and matplotlib installed:

```bash
pip install matplotlib
