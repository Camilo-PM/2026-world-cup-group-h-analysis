# FIFA World Cup 2026 - Group H Analysis

## Project Overview

This project analyzes the recent form of the national teams in Group H of the FIFA World Cup 2026.

The analysis is based on each team's most recent available matches, using data collected from local FBref HTML files.

Teams analyzed:

Spain, Cape Verde, Uruguay, Saudi Arabia

---

## Key Findings

- Highest Power Score: Spain with 23.81.
- Best attacking record: Spain with 31.0 goals scored.
- Best defensive record: Spain with 8.0 goals conceded.
- Best recent form: Spain with 24 points.

---

## Team Summary

| Team | Matches | Wins | Draws | Losses | GF | GA | GD | Points Form | Form Index | Power Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Spain | 10 | 7 | 3 | 0 | 31.0 | 8.0 | 23.0 | 24 | 80.0 | 23.81 |
| Cape Verde | 10 | 5 | 4 | 1 | 15.0 | 8.0 | 7.0 | 19 | 63.33 | 13.81 |
| Uruguay | 10 | 4 | 4 | 2 | 10.0 | 9.0 | 1.0 | 16 | 53.33 | 9.7 |
| Saudi Arabia | 10 | 3 | 3 | 4 | 9.0 | 15.0 | -6.0 | 12 | 40.0 | 5.43 |


---

## Visualizations

The project generates the following visualizations:

- ranking_form.png
- goal_difference.png
- attack_vs_defense.png

These charts are saved in:

reports/figures/

---

## Notes

New Zealand has 9 matches available in the collected dataset, while the other teams have 10. This should be considered when comparing form and performance indicators.

---

## Methodology

1. Local HTML files are collected from FBref.
2. Match data is extracted and cleaned with Python.
3. Team-level metrics are calculated.
4. Visualizations are generated with Matplotlib.
5. A Markdown report is created automatically.
