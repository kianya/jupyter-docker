import requests
import pandas as pd
import datetime
import time

from sqlalchemy import create_engine

import sys
import os
from tqdm import tqdm
from tqdm import tnrange

DATABASE_CONNECTION = 'postgresql://scott:tiger@localhost:5432/polonix'

POLONIEX_API = 'https://poloniex.com/public?command=returnChartData'
POLONIEX_PERIOD = 1800
POLONIEX_END = 9999999999
POLONIEX_START = 1464739200

CURRENT_DIR = os.path.dirname(os.path.realpath('__file__'))
OUTPUT_DIR = '../data/output/'

def load_table_to_database(dataframe, tablename):
    try:
        engine = create_engine(DATABASE_CONNECTION)
        dataframe.to_sql(tablename, engine)
        return "Table succesfully loaded"
    except :
        print("Error: Can't load data to Database")
    

def load_table_to_file(dataframe, filename):
    try:
        filename = os.path.normpath(os.path.join(CURRENT_DIR, (OUTPUT_DIR + filename + '.csv' )))
        dataframe.to_csv(filename, ';')
        return "Table succesfully loaded"
    except :
        print("Error: Can't load data to File")
    

        
def load_data_from_poloniex_api(currencyPair, start):
    try:
        payload = {'currencyPair': currencyPair, 'start': POLONIEX_START, 'end': POLONIEX_END, 'period': POLONIEX_PERIOD}
        var = requests.get(POLONIEX_API, params=payload)
        data = pd.read_json(var.text)
        data['currencyPair'] = currencyPair
        data['dateFrom'] = datetime.datetime.now()
        return data 
    except :
        print("Error: Can't load data from Poloniex API: " + currencyPair)
        
def main():
    filename = os.path.normpath(os.path.join(CURRENT_DIR, '../data/input/monets_tokens.csv'))
    input_data = pd.read_csv(filename, header=0, sep=';')
    input_data['Ticker']
    for ticker in tqdm(input_data[['Ticker', 'Start']].values, desc="Загрузка данных из POLONIEX API : "):
        time_start = time.mktime(datetime.datetime.strptime(ticker[1], "%d.%m.%Y").timetuple())
        data = load_data_from_poloniex_api('USDT_' + ticker[0], time_start)
        load_table_to_file(data, ticker[0])

main()