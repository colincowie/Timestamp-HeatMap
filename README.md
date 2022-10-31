# Timestamp-HeatMap
A python utility for creating timestamp heatmaps in ploty

### Features
- Uses Pandas and Plotly to create a heatmap when given timestamp data
- Generates HTML reports using a template

#### Python3 Dependencies
- Pandas
- Plotly

### Usage & Implementation

[yanlouwang.py](https://github.com/colincowie/Timestamp-HeatMap/blob/master/heatmap_viz/yanlouwang.py) is an example of implementing [HeatMapViz.py](https://github.com/colincowie/Timestamp-HeatMap/blob/master/heatmap_viz/HeatMapViz.py) to visualize data

Example usage:

```
from HeatMapViz import HeatMapViz

visualizer = HeatMapViz(timestamp_data) # timestamp_data is a list with timestamps

heatmap = visualizer.run_timezone_heatmap()

visualizer.write_report(heatmap, "example_report.html")
```

<img src = "https://github.com/colincowie/Timestamp-HeatMap/raw/master/heatmap_viz/example_data/images/example.PNG">
