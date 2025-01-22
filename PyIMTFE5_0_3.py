import pandas as pd
import numpy as np

df_panel = pd.DataFrame(data = {'date': ['2021-2-20']*2 + ['2021-2-21']*2 + ['2021-2-22']*2 + ['2021-2-23']*2,
                               'ticker': ['SPY','AAPL']*4, 'return': np.random.random(size=8)})
print(df_panel)
# make a pivot table of adjusted close prices out of the panel data
df_pivot = df_panel.pivot (index ='date', columns ='ticker', values ='return')
print(df_pivot)
# transform the pivot table back to the panel data layout
df_panel_new = df_pivot.reset_index().melt(id_vars =['date'], value_vars =['SPY','AAPL'], value_name = 'return').sort_values('date', ignore_index = True )
print(df_panel_new)