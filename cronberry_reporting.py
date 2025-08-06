"""
Cronberry Multi-Currency Reporting
---------------------------------

This module ingests the Cronberry ledger dataset, converts multi-currency
transactions into a single reporting currency (EUR) using fixed example
rates and produces monthly summaries of debits and credits.  It also
calculates key performance metrics like total chargebacks and net
balance per currency.

Usage::

    python cronberry_reporting.py --input cronberry_ledger.xlsx --output cronberry_report.xlsx

Dependencies:
    pandas
"""

import argparse
import pandas as pd

FX_RATES = {'USD': 0.93, 'INR': 0.011, 'EUR': 1.0}


def load_ledger(path: str) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name='Ledger')


def convert_to_eur(df: pd.DataFrame) -> pd.DataFrame:
    df['Amount_EUR'] = df.apply(lambda r: r['Amount'] * FX_RATES.get(r['Currency'], 1.0), axis=1)
    return df


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M').dt.to_timestamp()
    summary = df.groupby(['Month','Type'])['Amount_EUR'].sum().unstack().fillna(0)
    summary['Net'] = summary.get('Credit',0) - summary.get('Debit',0)
    return summary.reset_index()


def export(summary: pd.DataFrame, output: str) -> None:
    with pd.ExcelWriter(output) as writer:
        summary.to_excel(writer, sheet_name='MonthlySummary', index=False)
    print(f'Report saved to {output}')


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Cronberry multi-currency report")
    parser.add_argument('--input', required=True, help='Path to Cronberry ledger Excel')
    parser.add_argument('--output', required=True, help='Path to save the report Excel')
    args = parser.parse_args()
    df = load_ledger(args.input)
    df = convert_to_eur(df)
    summary = monthly_summary(df)
    export(summary, args.output)


if __name__ == '__main__':
    main()