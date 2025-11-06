from __future__ import annotations

from typing import Any, Dict, List
import requests
import pandas as pd


def load_gdp_data(start_year: int = 2000, end_year: int = 2022) -> pd.DataFrame:
    """
    Fetch GDP (current US$) for selected countries from World Bank API,
    keep rows within [start_year, end_year], convert to trillions, and return a clean DataFrame.
    """
    url = (
        "https://api.worldbank.org/v2/country/GBR;JPN;CHN;DEU;CHE/"
        f"indicator/NY.GDP.MKTP.CD?date={start_year}:{end_year}"
        "&format=json&per_page=1000"
    )
    r: requests.Response = requests.get(url, timeout=30)
    r.raise_for_status()
    payload: List[Any] = r.json()  # [metadata, data]
    data: List[Dict[str, Any]] = payload[1]

    df = pd.DataFrame(data)

    def _country_name(x: Any) -> str:
        if isinstance(x, dict):
            val = x.get("value")
            return str(val) if val is not None else ""
        return str(x)

    df["country"] = df["country"].apply(_country_name)
    df = df.rename(
        columns={"country": "country_name", "date": "year", "value": "gdp_trillion_usd"}
    )
    df = df[["country_name", "year", "gdp_trillion_usd"]]
    df["year"] = df["year"].astype(int)
    df["gdp_trillion_usd"] = pd.to_numeric(df["gdp_trillion_usd"], errors="coerce")
    df = df.dropna()
    df = df[df["year"].between(start_year, end_year)]
    df["gdp_trillion_usd"] = df["gdp_trillion_usd"] / 1_000_000_000_000

    print(f"Loaded {len(df)} rows of GDP data (in trillions of USD).")
    return df


def save_clean_data(df: pd.DataFrame, filename: str = "gdp_clean.csv") -> None:
    """Save the cleaned GDP DataFrame to CSV."""
    df.to_csv(filename, index=False)
    print(f"Clean data saved to {filename}")
