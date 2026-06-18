import pandas as pd, pathlib, sys
DATA_PATH = "data/logistics_features.csv" if pathlib.Path('data/logistics_features.csv').exists() else "data/enhanced_logistics.csv"
df = pd.read_csv(DATA_PATH, parse_dates=['promised_date','delivery_date'])
vendor_perf_counts = df['vendor_performance_category'].value_counts().reset_index(name='count').rename(columns={'index':'category'})
print('vendor_perf_counts columns:', vendor_perf_counts.columns.tolist())
print(vendor_perf_counts.head())
