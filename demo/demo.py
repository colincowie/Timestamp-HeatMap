# HeatMap Pattern of Life Demo
from heatmap_pattern_of_life import heatmap_from_excel, heatmap_from_plaintext, heatmap_from_csv

# Custom theme options for plotly
def show_with_custom_theme(fig):
    fig.update_layout(
        template='plotly_dark',
        font=dict(family='Arial', size=18),
        paper_bgcolor="#2c2c2c"
    )
    fig.show() 

# Example graphing excel
excel_fig = heatmap_from_excel('example_data/isoon.xlsx', 'Sheet1', 'Timestamps', 'Excel Data', user_utc_offset=+8)
excel_fig.show()

# Example graphing plaintext data
figure2 = heatmap_from_plaintext('example_data/isoon.txt', 'Plaintext Data', user_utc_offset=-5)
#figure2.write_html("demo_figure2.html")
figure2.show()

# Example graphing csv data
heatmap_fig = heatmap_from_csv('example_data/isoon.csv', 'Timestamps', 'CSV Data', timestamp_format="%m/%d/%y %H:%M", user_utc_offset=+3)
show_with_custom_theme(heatmap_fig)


