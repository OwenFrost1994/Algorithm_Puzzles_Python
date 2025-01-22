import pandas as pd
from fredapi import Fred
from datetime import datetime
import os

api_key = 'ca1dc18f39d667e31e7c344e180cdc95'
filename = "GDPPOT.xlsx"

def load_stored_data(filename):
    if os.path.exists(filename):
        return pd.read_excel(filename, index_col=0)
    else:
        return None

def fetch_gdp_pot(api_key, start_date=None, end_date=None):
    fred = Fred(api_key)
    data = fred.get_series('GDPPOT', start_date, end_date)
    return data

def update_excel(data, filename, startrow):
    with pd.ExcelWriter(filename, engine='openpyxl', mode = 'a', if_sheet_exists = "overlay") as writer:
        data.to_excel(writer, sheet_name="Sheet1", header = False, startrow = startrow)

stored_data = load_stored_data(filename)
end_date = datetime.now().date()
if stored_data is not None:
    start_date = stored_data.index[-1]
else:
    start_date = None

data = fetch_gdp_pot(api_key, start_date, end_date)
if data is not None and not data.empty:
    if not data.index[-1] == start_date:
        if stored_data is None:
            data.to_excel(filename, header = False)
            print("New excel created!:" + filename)
        else:
            update_excel(data, filename, len(stored_data))
            print("Excel updated!")
    else:
        print("No new data!")
else:
    print("Data is None!")