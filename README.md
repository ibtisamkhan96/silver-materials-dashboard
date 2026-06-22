# Silver (Ag) | Materials Data Series #11

Interactive data dashboard and LinkedIn carousel on silver: where it comes from, what it goes into, and why the gap between supply and demand has been widening for four years straight.

**Live dashboard:** open `index.html` in a browser  
**Carousel:** open `carousel/index.html` and print to PDF

---

## What this covers

- Global mine production by country (2024, USGS MCS 2026)
- Demand breakdown: industrial vs. jewelry vs. investment
- Supply deficit timeline 2019-2024 (four consecutive years of demand outpacing supply)
- Price history 2015-2025, including the 2025 run to $53.60/oz
- Scale comparisons: what 25,300 tonnes actually looks like
- Silver's addition to the US Critical Minerals List in November 2025

---

## Files

```
materials-silver/
├── fetch_data.py                    # data pipeline, compiles figures to CSVs
├── data/
│   ├── production_by_country_2024.csv
│   ├── demand_by_segment_2024.csv
│   ├── end_uses_us_2025.csv
│   ├── supply_demand_trend.csv
│   ├── historical_prices.csv
│   └── scale_comparisons.csv
├── index.html                       # interactive Chart.js dashboard
├── carousel/
│   └── index.html                   # 9-slide LinkedIn carousel, 1080x1080
├── Silver_Materials_Carousel.pdf    # exported PDF
└── linkedin-post.txt                # caption + hashtags
```

---

## Run the data pipeline

```bash
pip install pandas
python fetch_data.py
```

All figures come from the sources cited in comments inside the script. Nothing is scraped; the data is manually compiled from primary sources and is intentionally static so the pipeline is reproducible without API keys.

---

## Key numbers (2024)

| Metric | Value | Source |
|--------|-------|--------|
| World mine production | 25,300 t (813 Moz) | USGS MCS 2026 |
| Top producer | Mexico, 5,780 t (22.8%) | USGS MCS 2026 |
| Total demand | 1,162.5 Moz | Silver Institute WSS 2025 |
| Industrial demand | 680.5 Moz (record) | Silver Institute |
| Supply deficit | 148.9 Moz | Silver Institute WSS 2025 |
| 4-yr cumulative deficit | 678 Moz | Silver Institute WSS 2025 |
| Avg price 2024 | $28.37/oz | USGS MCS 2026 |
| Avg price 2025 | $38.00/oz (+34%) | USGS MCS 2026 |
| Recycling 2024 | 193.9 Moz (12-yr high) | Silver Institute WSS 2025 |

---

## Sources

- **USGS MCS 2026** (primary): https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-silver.pdf
- **Silver Institute / Metals Focus, World Silver Survey 2025**: https://silverinstitute.org/silver-supply-demand/
- **Silver Institute industrial demand release (April 2025)**: https://silverinstitute.org/silver-industrial-demand-reached-a-record-680-5-moz-in-2024/
- **Federal Register, US Critical Minerals List 2025** (90 FR 50494): November 7, 2025

---

## Export the carousel PDF

```bash
"C:/Program Files/Google/Chrome/Application/chrome.exe" ^
  --headless --disable-gpu --no-pdf-header-footer ^
  --print-to-pdf="F:\job applications claude\materials-silver\Silver_Materials_Carousel.pdf" ^
  "file:///F:/job applications claude/materials-silver/carousel/index.html"
```

Verify page count:
```bash
grep -a -o "/Count [0-9]*" Silver_Materials_Carousel.pdf | head -1
```

Expected output: `/Count 9`

---

## Part of the Materials Data Series

Each project in this series takes one material and turns it into a data story: a reproducible pipeline, an interactive dashboard, and a LinkedIn carousel.

Completed (10): steel, aluminium, copper, rare earths, lithium, nickel, cobalt, titanium, graphite, silicon  
This one (#11): **silver**  
Next: tin

---

## About

**Ibtisam Ahmed Khan** | BS Materials Engineering (GIKI) | MSc Engineering Management (Tsinghua)  
[linkedin.com/in/ibtisam-ahmed-khan](https://linkedin.com/in/ibtisam-ahmed-khan)  
[github.com/ibtisamkhan96](https://github.com/ibtisamkhan96)
