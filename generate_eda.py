import csv
import os
import datetime
from collections import defaultdict, Counter
import plotly.express as px
import plotly.graph_objects as go

# Ensure charts directory exists
charts_dir = os.path.join('charts')
os.makedirs(charts_dir, exist_ok=True)

# Load data from CSV
csv_path = os.path.join('data', 'logistics_features.csv')
rows = []
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        # Parse dates
        r['promised_date'] = datetime.datetime.strptime(r['promised_date'], '%Y-%m-%d')
        r['delivery_date'] = datetime.datetime.strptime(r['delivery_date'], '%Y-%m-%d')
        # Compute derived fields
        r['delay_duration'] = (r['delivery_date'] - r['promised_date']).days
        r['is_delayed'] = 1 if r['delay_duration'] > 0 else 0
        # Extract month for trend analysis
        r['month'] = r['promised_date'].strftime('%Y-%m')
        rows.append(r)

# Helper to save figure using kaleido
def save_fig(fig, name):
    path = os.path.join(charts_dir, name)
    fig.write_image(path, engine='kaleido')

# 1. Delay Duration Histogram
fig1 = px.histogram([r['delay_duration'] for r in rows], nbins=30, title='Delay Duration Distribution')
fig1.update_xaxes(title_text='Days')
fig1.update_yaxes(title_text='Frequency')
save_fig(fig1, 'delay_duration_hist.png')

# 2. Delay % by Courier
courier_stats = defaultdict(lambda: {'delayed':0, 'total':0})
for r in rows:
    c = r['courier']
    courier_stats[c]['delayed'] += r['is_delayed']
    courier_stats[c]['total'] += 1
courier_perf = []
for c, stats in courier_stats.items():
    delay_pct = (stats['delayed'] / stats['total']) * 100 if stats['total'] else 0
    courier_perf.append({'courier': c, 'delay_pct': delay_pct})
fig2 = px.bar(courier_perf, x='courier', y='delay_pct', title='Delay % by Courier')
fig2.update_yaxes(title_text='Delay %')
save_fig(fig2, 'delay_by_courier.png')

# 3. Vendor Performance Category Bar
vendor_counts = Counter(r['vendor_performance_category'] for r in rows)
vendor_data = [{'category': k, 'count': v} for k, v in vendor_counts.items()]
fig3 = px.bar(vendor_data, x='category', y='count', title='Vendor Performance Categories')
fig3.update_yaxes(title_text='Count')
save_fig(fig3, 'vendor_performance.png')

# 4. Courier Performance Category Bar
courier_counts = Counter(r['courier_performance_category'] for r in rows)
courier_perf_data = [{'category': k, 'count': v} for k, v in courier_counts.items()]
fig4 = px.bar(courier_perf_data, x='category', y='count', title='Courier Performance Categories')
fig4.update_yaxes(title_text='Count')
save_fig(fig4, 'courier_performance.png')

# 5. Monthly Delay Trend
month_stats = defaultdict(lambda: {'delayed':0, 'total':0})
for r in rows:
    m = r['month']
    month_stats[m]['delayed'] += r['is_delayed']
    month_stats[m]['total'] += 1
monthly_data = []
for m, stats in sorted(month_stats.items()):
    delay_pct = (stats['delayed'] / stats['total']) * 100 if stats['total'] else 0
    monthly_data.append({'month': m, 'delay_pct': delay_pct})
fig5 = px.line(monthly_data, x='month', y='delay_pct', markers=True, title='Monthly Delay % Trend')
fig5.update_yaxes(title_text='Delay %')
save_fig(fig5, 'monthly_trend.png')

print('Charts generated and saved to ./charts')
# Legacy pandas/matplotlib code removed – script ends here
