import schedule
import time
import datetime
import numpy as np
from pathlib import Path
import pandas as pd
import requests
url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

global tot_num_entries
tot_num_entries = 0

global API_update_dates
API_update_dates = []

def init_csv():
    global API_update_dates
    global tot_num_entries
    r = requests.get(url)
    dataset = pd.DataFrame.from_dict(r.json())
    dataset = dataset.drop(columns=['sna','ar','lat','lng','sareaen','sarea','aren', 'infoTime', 'infoDate', 'srcUpdateTime', 'updateTime'])
    API_update_dates = list(dataset['mday'])
    dataset.to_csv('Ubike_data.csv',index=False)
    tot_num_entries += len(dataset)
    print("---Initial csv created at---", datetime.datetime.now(),"-- Number of entries:",tot_num_entries)

def update_csv():
    global tot_num_entries
    global API_update_dates
    update_dates_copy = API_update_dates.copy()
    r = requests.get(url)
    time.sleep(1)
    dataset = pd.DataFrame.from_dict(r.json()) 
    dataset = dataset.drop(columns=['sna','ar','lat','lng','sareaen','sarea','aren', 'infoTime', 'infoDate', 'srcUpdateTime', 'updateTime'])
    indexes_to_delete = []

    for i, date in enumerate(update_dates_copy):
        new_date = dataset.at[i, 'mday']
        if(date == new_date):
            indexes_to_delete.append(i)
        else:
            API_update_dates[i] = new_date
        
    newly_added_entries = len(dataset) - len(indexes_to_delete)
    tot_num_entries += newly_added_entries
    dataset = dataset.drop(indexes_to_delete)
    dataset.to_csv('Ubike_data.csv',mode='a',header=False,index=False)
    print("---Update csv at---", datetime.datetime.now(),"-- Newly Added entries:", newly_added_entries, "-- Total no. of entries:", tot_num_entries)
    
init_csv()
schedule.every(1).minute.do(update_csv)
while True:
  schedule.run_pending()
