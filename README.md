# Logistics Delay Tracker

A lightweight, interactive dashboard built with **Python**, **pandas**, **Dash**, and **Plotly** that visualises logistics order data and highlights key performance indicators (KPIs) such as delayed deliveries, revenue impact, and partner performance.

---

## ✨ Features

- **KPI cards** showing total orders, delay % , average delay (days) and revenue impact.
- **Bar charts** for delay % by vendor & courier.
- **Category breakdown** charts for vendor and courier performance (Excellent / Good / Average).
- **Pie chart** of delay reasons.
- **Line chart** of daily delayed orders over time.
- Fully responsive layout with a modern, pastel‑gradient aesthetic.

---

## 📁 Project Structure

```
Logistics delay tracker/
├─ data/                     # CSV files (not version‑controlled)
├─ dashboard/
│   └─ app.py                # Main Dash app – entry point
├─ generate_eda.py            # Optional exploratory‑data‑analysis helper
├─ inspect_counts.py          # Debug script that prints DataFrame columns
├─ .gitignore                # Excludes .venv, __pycache__, data files, etc.
├─ README.md                 # You are reading it!
└─ requirements.txt          # Python dependencies (pandas, dash, plotly)
```

---

## 🛠️ Installation & Setup (Windows)

1. **Clone the repo**
   ```cmd
   git clone https://github.com/<your‑username>/logistics-delay-tracker.git
   cd logistics-delay-tracker
   ```
2. **Create & activate a virtual environment**
   ```cmd
   python -m venv .venv
   .\.venv\Scripts\activate   # (prompt changes to (.venv))
   ```
3. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```
4. **Place your data**
   - Put `logistics_features.csv` (or `enhanced_logistics.csv`) inside the `data/` folder.  The file must contain the columns used by the app (`vendor`, `courier`, `delivery_date`, `promised_date`, `is_delayed`, `delay_reason`, `vendor_performance_category`, `courier_performance_category`, `revenue_impact_flag`).

---

## ▶️ Running the Dashboard

```cmd
python dashboard\app.py
```
The server starts on **http://127.0.0.1:8050**. Open that URL in any browser to explore the interactive visualisations.

---

## 🧪 Quick Validation Scripts (optional)

- `inspect_counts.py` – prints the column names of the vendor performance DataFrame, useful for debugging.
- `generate_eda.py` – runs a simple exploratory analysis and outputs summary statistics.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of the changes.
4. Ensure the app still runs with `python dashboard\app.py` before submitting.

---

## 📜 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## 📬 Contact

Feel free to open an issue on GitHub or contact the author at 'gopimadhavi07@gmail.com'
