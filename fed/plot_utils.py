import pandas as pd
import matplotlib.pyplot as plt

def plot_gdp_trend(csv_path="gdp_clean.csv")
    
    df = pd.read_csv(csv_path)
    print("📊 Loaded columns:", df.columns.tolist())
    
    if "gdp_trillion_usd" in df.columns:
        gdp_col = "gdp_trillion_usd"
    elif "gdp_usd" in df.columns:
        gdp_col = "gdp_usd"
        df[gdp_col] = df[gdp_col] / 1e12  # 转换为 trillion
    else:
        raise KeyError("❌")

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
