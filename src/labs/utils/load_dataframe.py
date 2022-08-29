import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


class Loader:
    def __init__(self, sample: str, range_sample=tuple, *args, **kwargs):
        self.sample = sample,
        self.range_sample = range_sample
        
    def loader(self):
        DATASETS_DIR = "../records/usd2idr/" if self.sample == "USD" \
            else "../records/jpy2idr"
        self.datasets = all_files[
            f"{DATASETS_DIR}{x}.csv" for x in range(*(self.range_sample))]
        df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
        df_merged = pd.concat(df_from_each_file, ignore_index=True)
        df_merged.to_csv()