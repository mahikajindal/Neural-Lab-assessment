import pandas as pd
import numpy as np

filePath = "stats_full_stack_dev.csv"

def random_timestamps():
    data = pd.read_csv(filePath) 
    time_frame = pd.datetime.now().replace(microsecond=0) - pd.Timedelta('3H')
    dates = pd.date_range(time_frame, periods = 30 * 60 * 60, freq='S')
    N = len(data)
    data['time_stamp'] = np.random.choice(dates, size=N)
    data.to_csv(filePath)



random_timestamps()