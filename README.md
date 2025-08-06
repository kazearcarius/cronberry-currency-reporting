# Cronberry Multi‑Currency Reporting Dashboard

This project reflects the work undertaken as an Accountant & Financial Reporting Associate at Cronberry Technologies. It automates the consolidation of a multi‑currency ledger, calculates monthly balances and produces key performance indicators for management dashboards.

## Scenario

Cronberry operates across Europe, the US and India, resulting in transactions denominated in EUR, USD and INR. Month‑end close required manual currency conversion and reconciliation to produce accurate financial statements. Fraud losses from chargebacks also needed monitoring.

## Key Features

* **Ledger ingestion** – Read a large ledger export with daily transactions, currency codes, categories and debit/credit indicators.
* **Currency conversion** – Apply static exchange rates to convert all amounts into EUR for reporting consistency.
* **Monthly summaries** – Aggregate debits and credits by month and calculate net balances.
* **KPIs** – Lay the groundwork for computing chargeback ratios and other operational metrics.
* **Excel output** – Export a monthly summary sheet with formatted headers.

## Files

* `cronberry_ledger.xlsx` – A mock ledger file spanning June–December 2024 with coloured headers and a summary sheet.
* `cronberry_reporting.py` – Python script that loads the ledger, converts currencies and produces a monthly summary.

## Usage

Generate a report by running:

```bash
python cronberry_reporting.py --input cronberry_ledger.xlsx --output cronberry_report.xlsx
```

The `cronberry_report.xlsx` file will have a `MonthlySummary` sheet showing total debits, credits and net balances per month in EUR.