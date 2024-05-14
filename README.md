# HeatMap Pattern of Life Analysis Library

This Python library provides tools to generate heatmaps from various data sources (Excel, CSV, and plaintext files). These heatmaps visualize the frequency of events at different times across days of the week, adjusted for specified UTC offsets.

## Installation

### From Source

To install the library from source, follow these steps:

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/yourusername/HeatMapPatternOfLife.git
   cd HeatMapPatternOfLife
   ```

2. Install the package:
   ```bash
   pip install .
   ```

This will install the library along with its dependencies.

## Usage

### Importing the Library

You can import the necessary functions from the library like this:

\```python
from heatmap_pattern_of_life import heatmap_from_excel, heatmap_from_plaintext, heatmap_from_csv
\```

### Functions

#### `heatmap_from_excel(file_path, sheet_name, timestamp_column, title, user_utc_offset=0)`

- **Purpose**: Generate a heatmap from an Excel sheet.
- **Parameters**:
  - `file_path`: Path to the Excel file.
  - `sheet_name`: Name of the sheet within the Excel file.
  - `timestamp_column`: Column name containing timestamps.
  - `title`: Title for the heatmap.
  - `user_utc_offset`: UTC offset for time adjustment (default is 0).

#### `heatmap_from_plaintext(file_path, title, timestamp_format='%Y-%m-%d %H:%M:%S', user_utc_offset=0)`

- **Purpose**: Generate a heatmap from a plaintext file where each line contains a timestamp.
- **Parameters**:
  - `file_path`: Path to the plaintext file.
  - `title`: Title for the heatmap.
  - `timestamp_format`: Format of the timestamps (default is '%Y-%m-%d %H:%M:%S').
  - `user_utc_offset`: UTC offset for time adjustment (default is 0).

#### `heatmap_from_csv(file_path, timestamp_column, title, timestamp_format='%Y-%m-%d %H:%M:%S', user_utc_offset=0)`

- **Purpose**: Generate a heatmap from a CSV file.
- **Parameters**:
  - `file_path`: Path to the CSV file.
  - `timestamp_column`: Column name containing timestamps.
  - `title`: Title for the heatmap.
  - `timestamp_format`: Format of the timestamps (default is '%Y-%m-%d %H:%M:%S').
  - `user_utc_offset`: UTC offset for time adjustment (default is 0).
