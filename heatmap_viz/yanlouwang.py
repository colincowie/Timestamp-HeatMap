import json, os
from glob import glob
from HeatMapViz import HeatMapViz
from datetime import datetime as dt

uniq_users = []
username_freq = []
all_timestamps = []
# load raw json data
def load_raw_data():
    for file_path in glob('data/yanluowang/*.json'):
        print(file_path)
        with open(file_path, 'r') as json_file:
            raw_json_data = json.loads(json_file.read())
            for message in raw_json_data['messages']:
                sender = message['sender'].split(":")[0]
                timestamp = message['origin_server_ts']
                body_content = ""
                try:
                    body_content = message['content']['body']
                except Exception as e:
                    #print(message['content'])
                    pass
                if body_content != "":
                    all_timestamps.append(str(timestamp))

                    username_freq.append(sender)

                    if sender not in uniq_users:
                        uniq_users.append(sender)

def viz_sub_group(handle, output_name):
    subgroup_timestamps = []
    for file_path in glob('data/yanluowang/*.json'):
        with open(file_path, 'r') as json_file:
            raw_json_data = json.loads(json_file.read())
            for message in raw_json_data['messages']:
                sender = message['sender'].split(":")[0]
                timestamp = message['origin_server_ts']
                body_content = ""
                try:
                    body_content = message['content']['body']
                except Exception as e:
                    pass
                if body_content != "":
                    if sender == handle:
                        subgroup_timestamps.append(str(timestamp))
                        #print(str(timestamp))

    visualizer = HeatMapViz(subgroup_timestamps)
    print("[+] Starting visualization")
    heatmap = visualizer.run_timezone_heatmap() # run the main analysis function
    visualizer.write_report(heatmap, output_name) # create the report


if __name__ == '__main__':
    load_raw_data()
    #print(uniq_users)
    #print(username_freq)
    viz_sub_group("@saint", "saint.html")
    viz_sub_group("@killanas", "killanas.html")
    viz_sub_group("@guki", "guki.html")
    viz_sub_group("@felix", "felix.html")
    viz_sub_group("@stealer", "stealer.html")

    visualizer = HeatMapViz(all_timestamps)
    print("[+] Starting visualization")
    heatmap = visualizer.run_timezone_heatmap() # run the main analysis function
    visualizer.write_report(heatmap, "yanluowang_all.html") # create the report
