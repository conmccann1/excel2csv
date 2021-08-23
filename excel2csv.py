#!/usr/bin/env python3
import sys
import os
import pandas as pd

def excel2csv(path):
    df = pd.read_excel(path, None)
    sheets = df.keys()
    out_dir = path.rsplit('/')[-1].rsplit('.')[0]
    print('OUT_DIR: ' + './' + out_dir)
    os.mkdir(out_dir)
    for sheet in sheets:
        df[sheet].to_csv('./' + out_dir + '/' + sheet + '.csv', index=False)

if __name__ == "__main__":
    path2file = sys.argv[1]
    print('PATH TO FILE: ' + path2file)
    excel2csv(path2file)
    
    
