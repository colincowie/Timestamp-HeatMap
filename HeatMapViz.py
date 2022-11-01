import argparse
import pandas as pd
import plotly.express as px
from collections import Counter
from datetime import datetime as dt
from plotly.subplots import make_subplots

class HeatMapViz():

    def __init__(self, target_data):
        self.target_data = pd.DataFrame(target_data,columns =['index'])
        print("[!] Running HeatMap Viz...")

    def run_timezone_heatmap(self):

        # Base dict with values to populate after parsing
        DoW_hours = {'Monday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        'Tuesday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        'Wednesday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        'Thursday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        'Friday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        'Saturday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        'Sunday': {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0,
                '6':0, '7':0, '8':0, '9':0, '10':0, '11':0,
                '12':0, '13':0, '14':0, '15':0, '16':0, '17':0,
                '18':0, '19':0, '20':0, '21':0, '22':0, '23': 0},
        }

        df_times = self.target_data

        # iterate through all days of the week
        df_times = pd.to_datetime(df_times.iloc[:, 0], unit='ms', utc=True)
        df_times = pd.DataFrame(df_times,columns =['index'])
        #df_times = pd.to_datetime(df_times['index'], errors='coerce')
        for idx, gp in df_times.groupby(df_times['index'].dt.dayofweek):
            # get day name, ie 'Monday'
            DOW = gp['index'].dt.day_name().iloc[0]
            # get all hours of the day observed and count thier frequency
            hour_block = gp.groupby(gp['index'].dt.hour).size()
            for hour, count_value in hour_block.items():
                DoW_hours[DOW][str(hour)] = count_value # set the values in the predefined dict 'DoW_hours'

        heatmap_df = pd.DataFrame.from_dict(DoW_hours)

        fig = px.imshow(heatmap_df, labels=dict(x="Day of Week", y="Hour of the Day (UTC)",  color="Occurrences"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                y=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
              )
        print("[*] Finished heatmap! Starting report generation...")
        return fig

    def write_report(self, fig_data, output_name):
        # Report Generation
        template = open('templates/template.html', 'r')
        report_data = template.read()
        template.close()
        title = output_name.replace(".html","").replace("_"," ")
        # Append title
        title_header = "<div class=\"top_bar\"><h1 style=\"text-align: center;\">"+title+"</h1></div><div class=\"main_box\">"
        report_data = report_data + title_header
        # Append HeatMap to the report
        report_data += fig_data.to_html(full_html=False, include_plotlyjs='cdn')
        out_path = "reports/" + output_name

        #report_data += issues_pie.to_html(full_html=False, include_plotlyjs='cdn')
        with open(out_path, 'w') as f:
            f.write(report_data)
        print("[*] Wrote report to: \033[0;32m"+out_path+"\033[0m")
