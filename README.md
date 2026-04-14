# retail-demand-intelligence-engine

Predicting next-month SKU demand for large retail networks in a FMCG setup.

Retail Demand Intelligence Engine is a machine learning system designed to recommend the most probable SKUs a retail shop will purchase in the upcoming month. The project focuses on modelling shop behaviour at scale and generating interpretable recommendations rather than building a conventional product recommender.

---

## Problem

Retail distributors and FMCG companies often struggle to anticipate what each shop will order next. Traditional forecasting methods operate at aggregate levels (region, product category, etc.), but inventory decisions are made at the **shop level**.

The objective of this system is:

> For each shop, predict the top SKUs most likely to be purchased next month.

This transforms historical transactional data into actionable demand signals.

---

## Dataset

The system is built on a large-scale FMCG transaction dataset.

| Metric | Scale |
|------|------|
| Total records | ~13 million |
| Unique shops | ~110,000 |
| Unique SKUs | ~1,400 |
| Time granularity | Monthly |

The dataset captures purchasing behaviour across thousands of independent retailers.

---
