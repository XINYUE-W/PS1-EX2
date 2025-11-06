from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def plot_gdp_trend(csv_path: str = "gdp_clean.csv") -> None:
    """Plot GDP trend per country using the cleaned CSV."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"{csv_path} does not exist. Please run save_clean_data first.")

    df = pd.read_csv(csv_path)
    print("Loaded columns:", df.columns.tolist())

    if "gdp_trillion_usd" in df.columns:
        gdp_col = "gdp_trillion_usd"
    elif "gdp_usd" in df.columns:
        gdp_col = "gdp_usd"
        df[gdp_col] = df[gdp_col] / 1_000_000_000_000  # convert to trillions
    else:
        raise KeyError("No GDP column found (expected 'gdp_trillion_usd' or 'gdp_usd').")

    plt.figure(figsize=(10, 6))
    for country in df["country_name"].unique():
        subset = df[df["country_name"] == country]
        plt.plot(subset["year"], subset[gdp_col], marker="o", label=country)

    plt.title("GDP (Trillions of US$) 2000–2022", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("GDP (Trillions of US$)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()
