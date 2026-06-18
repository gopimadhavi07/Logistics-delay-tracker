import pandas as pd, pathlib, json, sys
DATA_PATH = "data/logistics_features.csv" if pathlib.Path('data/logistics_features.csv').exists() else "data/enhanced_logistics.csv"
df = pd.read_csv(DATA_PATH, parse_dates=['promised_date','delivery_date'])
vc = df['vendor_performance_category'].value_counts().reset_index().rename(columns={'index':'category','vendor_performance_category':'count'})
print('Columns:', vc.columns.tolist())
print(vc.head())
