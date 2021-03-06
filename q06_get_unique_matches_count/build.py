# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
path = 'data/ipl_matches_small.csv'

# Enter Code Here

def get_unique_matches_count():
    
    arr = read_ipl_data_csv(path, '|S100')
    arr = arr[:,0:1]
    return np.unique(arr).size

get_unique_matches_count()


