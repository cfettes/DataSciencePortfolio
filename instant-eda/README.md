# Instant EDA

Generates profile reports from a pandas `DataFrame`. 
The pandas `df.describe()` function is great but a little basic for serious exploratory data analysis. 
`pandas_profiling` extends the pandas DataFrame with `df.profile_report()` for quick data analysis.

For each column the following statistics - if relevant for the column type - are presented in an interactive HTML report:

* **Type inference**: detect the [types](#types) of columns in a dataframe.
* **Essentials**: type, unique values, missing values
* **Quantile statistics** like minimum value, Q1, median, Q3, maximum, range, interquartile range
* **Descriptive statistics** like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
* **Most frequent values**
* **Histogram**
* **Correlations** highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
* **Missing values** matrix, count, heatmap and dendrogram of missing values
* **Text analysis** learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data.
* **File and Image analysis** extract file sizes, creation dates and dimensions and scan for truncated images or those containing EXIF information.


## Installation

Install by navigating to the proper directory and running

    python setup.py install

### Getting started

Start by loading in your pandas DataFrame, e.g. by using
```python
import numpy as np
import pandas as pd
from instant_eda import InstantEDA

df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=["a", "b", "c", "d", "e"]
)
```
To generate the report, run:
```python
report = InstantEDA(df, title="EDA Report")
```

### Explore deeper

You can configure the profile report in any way you like. The example code below loads the explorative configuration file, that includes many features for text (length distribution, unicode information), files (file size, creation time) and images (dimensions, exif information). If you are interested what exact settings were used, you can compare with the [default configuration file](https://github.com/pandas-profiling/pandas-profiling/blob/master/src/pandas_profiling/config_default.yaml).

```python
profile = InstantEDA(df, title='EDA Report', explorative=True)
```

#### Jupyter Notebook

We recommend generating reports interactively by using the Jupyter notebook. 
There are two interfaces when generating reports interactively using Jupyter notebook: through widgets and through a HTML report.

The widgets version is achieved by simply displaying the report. In the Jupyter Notebook, run:
```python
profile.to_widgets()
```

The HTML report can be included in a Jupyter notebook by running the following code:

```python
profile.to_notebook_iframe()
```

#### Saving the report

To generate a HTML report file, save the `InstantEDA` to an object and use the `to_file()` function:
```python
profile.to_file("your_report.html")
```
Alternatively, you can obtain the data as json:
```python
# As a string
json_data = profile.to_json()

# As a file
profile.to_file("your_report.json")
```

### Large datasets

Minimal mode is a default configuration that disables expensive computations (such as correlations and dynamic binning).
Use the following syntax:

```python
profile = InstantEDA(large_dataset, minimal=True)
profile.to_file("output.html")
```

### Command line usage

For standard formatted CSV files that can be read immediately by pandas, you can use the `instant_eda` executable. Run

	instant_eda -h

for information about options and arguments.

### Advanced usage

A set of options is available in order to adapt the report generated.

* `title` (`str`): Title for the report ('EDA Report' by default).
* `pool_size` (`int`): Number of workers in thread pool. When set to zero, it is set to the number of CPUs available (0 by default).
* `progress_bar` (`bool`): If True, `instant-eda` will display a progress bar.

More settings can be found in the default configuration file, and minimal configuration file.

__Example__
```python
profile = df.profile_report(title='Pandas Profiling Report', plot={'histogram': {'bins': 8}})
profile.to_file("output.html")
```

## Types

Types are a powerful abstraction for effective data analysis, that goes beyond the logical data types (integer, float etc.).
`instant-eda` currently recognises the following types: _Boolean, Numerical, Date, Categorical, URL, Path, File_ and _Image_.

There is currently limited functionality for data type recognition and conversion, including date (in UK format) and numeric.

## Dependencies

The profile report is written in HTML and CSS, which means instant-eda requires a modern browser. 

You need [Python 3](https://python3statement.org/) to run this package. Other dependencies can be found in the requirements file.
