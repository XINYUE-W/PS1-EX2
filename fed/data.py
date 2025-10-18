import requests
import pandas as pd

def load_gdp_data(start_year=2000, end_year=2022):
    
    url = (
        f"https://api.worldbank.org/v2/country/GBR;JPN;CHN;DEU;CHE/"
        f"indicator/NY.GDP.MKTP.CD?date={start_year}:{end_year}&format=json&per_page=1000"
    )
    r = requests.get(url)
    data = r.json()[1]
    df = pd.DataFrame(data)

    df["country"] = df["country"].apply(lambda x: x.get("value") if isinstance(x, dict) else x)
    df = df.rename(columns={"country": "country_name", "date": "year", "value": "gdp_trillion_usd"})
    df = df[["country_name", "year", "gdp_trillion_usd"]]
    df["year"] = df["year"].astype(int)
    df["gdp_trillion_usd"] = pd.to_numeric(df["gdp_trillion_usd"], errors="coerce")
    df = df.dropna()
    df = df[df["year"].between(start_year, end_year)]
    df["gdp_trillion_usd"] = df["gdp_trillion_usd"] / 1e12

    print(f"Loaded {len(df)} rows of GDP data (in Trillions of USD).")
    return df


def save_clean_data(df, filename="gdp_clean.csv"):
    df.to_csv(filename, index=False)
    print(f" Clean data saved to {filename}")

