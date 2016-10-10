import pandas as pd
import json
import os
import requests

def get_tock_timecards_data(start_date, project_id):
    """
    Get timecards data from Tock API
    """
    headers = {'Authorization': 'Token ' + os.environ.get('TOCK_API_KEY')}
    url = 'https://tock.18f.gov/api/timecards.json?date=' + str(start_date) + '&project=' + str(project_id)
    tock_data = requests.get(url, headers=headers).json()
    timecards = pd.read_json(json.dumps(tock_data))
    return timecards

def get_rates():
    return pd.read_csv('fixtures/rates.csv')

def get_employees():
    return pd.read_csv('fixtures/employees.csv')
