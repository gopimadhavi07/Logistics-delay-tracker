# Data Quality Report – Feature Engineering

**Rows:** 500  
**Columns:** 21  

## Column Types
- `order_id`: int64
- `promised_date`: datetime64[us]
- `delivery_date`: datetime64[us]
- `courier`: str
- `vendor`: str
- `delay_reason`: str
- `is_delayed`: bool
- `delay_duration`: float64
- `delay_flag`: bool
- `delivery_status`: str
- `month`: str
- `quarter`: int32
- `year`: int32
- `delay_category`: str
- `revenue_impact_flag`: bool
- `vendor_mean_delay`: float64
- `vendor_performance_category`: str
- `courier_mean_delay`: float64
- `courier_performance_category`: str
- `delay_days`: int64
- `revenue_impacted`: bool

## Missing Values

## Sample Statistics for New Features
- `delay_days` mean: {df['delay_days'].mean():.2f}
- `delay_flag` proportion delayed: {df['delay_flag'].mean():.2%}
- `revenue_impacted` proportion true: {df['revenue_impacted'].mean():.2%}
