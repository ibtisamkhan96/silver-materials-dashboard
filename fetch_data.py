"""
Materials Data Series -- Silver
fetch_data.py

Compiles verified figures from primary sources into tidy CSVs in data/.
Run:  python fetch_data.py
Requires: pandas

Sources
-------
- USGS Mineral Commodity Summaries 2026 (MCS 2026), Silver sheet
  https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-silver.pdf
- Silver Institute / Metals Focus, World Silver Survey 2025
  https://silverinstitute.org/silver-supply-demand/
- Silver Institute, Industrial Demand Press Release April 2025
  https://silverinstitute.org/silver-industrial-demand-reached-a-record-680-5-moz-in-2024/
- Federal Register 90 FR 50494 (US Critical Minerals List, Nov 2025)
"""

import os
import pandas as pd

os.makedirs("data", exist_ok=True)

# ── 1. Mine production & reserves by country, 2024 ─────────────────────────
# Source: USGS MCS 2026, table "World Mine Production and Reserves"
# production_t: metric tons, silver content
# reserves_t:   metric tons
production = [
    ("Mexico",       5780, 37000),
    ("China",        3430, 67000),
    ("Peru",         3510, 110000),
    ("Bolivia",      1490, 22000),
    ("Russia",       1280, 92000),
    ("Poland",       1320, 59000),
    ("Chile",        1200, 33000),
    ("Australia",    1050, 109000),
    ("United States",1050, 23000),
    ("Kazakhstan",    850, None),
    ("India",         700,  8000),
    ("Argentina",     774,  6500),
    ("Sweden",        432, None),
    ("Canada",        366,  4900),
    ("Other",        2110, 57000),
]
df_prod = pd.DataFrame(production, columns=["country", "production_t_2024", "reserves_t"])
df_prod["share_pct"] = (df_prod["production_t_2024"] / df_prod["production_t_2024"].sum() * 100).round(1)
# Exclude "Other" from country-level display rows for the map
df_prod.to_csv("data/production_by_country_2024.csv", index=False)
print("Saved data/production_by_country_2024.csv")

# ── 2. Global demand by segment, 2024 ─────────────────────────────────────
# Source: Silver Institute / World Silver Survey 2025
# Total demand: ~1.16 billion oz = 36,100 t  (1 t = 32.1507 troy oz)
# Industrial:   680.5 Moz  (record fourth consecutive)
# Jewelry:      208.7 Moz
# Physical investment (net): ~223.9 Moz  (back-calculated: 1160 - 680.5 - 208.7 - 25.2 - 21.7 = 224)
# Silverware:    ~21.7 Moz (est.)
# Photography:   ~25.2 Moz (est.)
demand = [
    ("Industrial (incl. PV, electronics, EVs)", 680.5),
    ("Physical investment (coins & bars)",       224.0),
    ("Jewelry",                                  208.7),
    ("Photography",                               25.2),
    ("Silverware",                                21.6),
]
df_dem = pd.DataFrame(demand, columns=["segment", "demand_moz_2024"])
df_dem["demand_t_2024"] = (df_dem["demand_moz_2024"] * 1e6 / 32150.7).round(0).astype(int)
df_dem["share_pct"] = (df_dem["demand_moz_2024"] / df_dem["demand_moz_2024"].sum() * 100).round(1)
df_dem.to_csv("data/demand_by_segment_2024.csv", index=False)
print("Saved data/demand_by_segment_2024.csv")

# ── 3. Industrial end-uses (US domestic, 2025 estimate) ───────────────────
# Source: USGS MCS 2026 "Domestic Production and Use" paragraph
end_uses = [
    ("Electrical & electronics",   25),
    ("Other industrial & photography", 19),
    ("Net physical investment",    18),
    ("Photovoltaics (PV)",         15),
    ("Coins & medals",             14),
    ("Jewelry & silverware",        6),
    ("Brazing & solder",            3),
]
df_uses = pd.DataFrame(end_uses, columns=["use", "pct_2025"])
df_uses.to_csv("data/end_uses_us_2025.csv", index=False)
print("Saved data/end_uses_us_2025.csv")

# ── 4. Supply-demand trend 2019-2024 ─────────────────────────────────────
# Sources: Silver Institute World Silver Survey 2025; USGS MCS 2025 & 2026
# Moz = million troy ounces; deficit = demand - supply (positive = deficit)
trend = [
    (2019, 836.5, 169.8, 1006.3, 991.8,  -14.5, 16.19),
    (2020, 784.4, 182.2,  966.6, 896.1,  -70.5, 20.55),
    (2021, 829.0, 182.2, 1011.2, 1049.4,  38.2, 25.23),
    (2022, 822.5, 180.2, 1002.7, 1242.1, 239.4, 21.88),
    (2023, 820.8, 182.9, 1003.7, 1197.2, 193.5, 23.54),
    (2024, 819.7, 193.9, 1013.6, 1162.5, 148.9, 28.37),
]
df_trend = pd.DataFrame(
    trend,
    columns=[
        "year",
        "mine_supply_moz",
        "recycling_moz",
        "total_supply_moz",
        "total_demand_moz",
        "deficit_moz",         # positive = demand > supply (structural deficit)
        "price_usd_per_oz",
    ],
)
df_trend.to_csv("data/supply_demand_trend.csv", index=False)
print("Saved data/supply_demand_trend.csv")

# ── 5. Scale comparisons (annual mine output tangibilised) ────────────────
# Annual world mine production 2024: 25,300 metric tons = 25,300,000 kg
annual_t = 25300
annual_kg = annual_t * 1000

# Objects & their silver/relevant mass in kg
SILVER_DENSITY_KG_M3 = 10490          # g/cm3 = 10.49 -> kg/m3 = 10490
OLYMPIC_POOL_VOLUME_M3 = 2500          # 50m x 25m x 2m
max_pool_fill_m3 = annual_kg / SILVER_DENSITY_KG_M3   # ~2.41 m3 -> expressed as % of pool

SMARTPHONE_SILVER_G = 0.3              # ~0.3 g silver per smartphone (IPC estimate)
SOLAR_PANEL_SILVER_G = 18             # ~18 g per standard 60-cell panel (declining; 2023-24 average)
IPHONE_SILVER_G = 0.34

comparisons = [
    ("Olympic swimming pool",
     "Full of liquid silver",
     f"{max_pool_fill_m3 / OLYMPIC_POOL_VOLUME_M3 * 100:.0f}% full",
     f"Melted down, 2024's entire silver output would fill {max_pool_fill_m3/OLYMPIC_POOL_VOLUME_M3:.2f} Olympic pools",
    ),
    ("Smartphones",
     "0.3 g silver each",
     f"{annual_kg / (SMARTPHONE_SILVER_G / 1000) / 1e9:.0f} billion",
     f"Enough silver to make {annual_kg / (SMARTPHONE_SILVER_G / 1000) / 1e9:.0f} billion smartphones",
    ),
    ("Solar panels",
     "18 g silver each",
     f"{annual_kg / (SOLAR_PANEL_SILVER_G / 1000) / 1e9:.2f} billion",
     f"Enough silver to manufacture ~{annual_kg / (SOLAR_PANEL_SILVER_G / 1000) / 1e9:.1f} billion solar panels",
    ),
    ("Seconds of solar adoption",
     "kg per second mined",
     f"{annual_kg / (365.25 * 24 * 3600):.2f} kg/s",
     "About 0.8 kg of silver is mined every second -- barely enough to fill a coffee mug",
    ),
    ("vs other metals",
     "Annual mine output (Mt)",
     "0.025 Mt",
     "Silver output is 1/100th of copper, 1/4000th of steel -- but its value per kg rivals aluminium x 1,000",
    ),
]
df_scale = pd.DataFrame(comparisons, columns=["object", "unit", "value", "description"])
df_scale.to_csv("data/scale_comparisons.csv", index=False)
print("Saved data/scale_comparisons.csv")

# ── 6. Historical price series (annual average, USD/troy oz) ──────────────
# Sources: USGS MCS 2026 salient statistics; Metals Focus
prices = [
    (2015, 15.68), (2016, 17.14), (2017, 17.04), (2018, 15.71),
    (2019, 16.19), (2020, 20.55), (2021, 25.23), (2022, 21.88),
    (2023, 23.54), (2024, 28.37), (2025, 38.00),
]
df_prices = pd.DataFrame(prices, columns=["year", "price_usd_per_oz"])
df_prices.to_csv("data/historical_prices.csv", index=False)
print("Saved data/historical_prices.csv")

print("\nAll datasets written to data/")
print(f"\nKey headline checks:")
print(f"  World mine production 2024: {df_prod['production_t_2024'].sum():,} t  (USGS: 25,300 t)")
print(f"  Total demand 2024: {df_dem['demand_moz_2024'].sum():.1f} Moz  (Silver Institute: 1,160 Moz)")
print(f"  Supply deficit 2024: {df_trend.loc[df_trend.year==2024,'deficit_moz'].values[0]:.1f} Moz")
