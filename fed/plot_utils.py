import pandas as pd
import matplotlib.pyplot as plt

def plot_gdp_trend(csv_path="gdp_clean.csv"):
    """读取 CSV 并绘制 2000–2022 各国 GDP 趋势图（单位：Trillions of USD）"""
    
    df = pd.read_csv(csv_path)
    print("📊 Loaded columns:", df.columns.tolist())

    # 自动识别列名
    if "gdp_trillion_usd" in df.columns:
        gdp_col = "gdp_trillion_usd"
    elif "gdp_usd" in df.columns:
        gdp_col = "gdp_usd"
        df[gdp_col] = df[gdp_col] / 1e12  # 转换为 trillion
    else:
        raise KeyError("❌ GDP 列未找到（应为 gdp_trillion_usd 或 gdp_usd）")

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
