import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/content/icg_recruitment_dataset.csv")
df_sorted = df.sort_values(by=['Annual_Revenue', 'Revenue_Growth_Pct'], ascending=[False, False])
top_5_companies = df_sorted.head(5)
print("Top 5 companies for potential market insight (based on Revenue and Growth):")
print(top_5_companies[['Company', 'Annual_Revenue', 'Revenue_Growth_Pct', 'EBITDA_Actual', 'P/E_Ratio']])


selected = df[df['Company'].isin(['Coca-cola', 'Mastercard', 'Meta', 'Tesla', 'JP Morgan'])]
plt.figure(figsize=(7, 5))
sns.scatterplot(data=selected, x="Q4_Revenue", y="EBITDA_Actual", hue="Company")
plt.title("Q4 Revenue vs EBITDA Actual")
plt.savefig("1_q4rev_vs_ebitda.png")
plt.close()

plt.figure(figsize=(7, 5))
sns.regplot(data=selected, x="R&D_Intensity_Pct", y="Revenue_Growth_Pct")
plt.title("R&D Intensity vs Revenue Growth")
plt.savefig("2_rdintensity_vs_growth.png")
plt.close()

melted = pd.melt(selected, id_vars=["Company"], value_vars=["Annual_Revenue", "EBITDA_Actual"])
plt.figure(figsize=(8, 5))
sns.barplot(data=melted, x="Company", y="value", hue="variable")
plt.title("Annual Revenue and EBITDA Comparison")
plt.ylabel("Amount in USD")
plt.savefig("3_revenue_ebitda_comparison.png")
plt.close()

plt.figure(figsize=(7, 5))
sns.barplot(data=selected, x="Company", y="P/E_Ratio", palette="crest")
plt.title("P/E Ratio per Company")
plt.savefig("4_pe_ratios.png")
plt.close()

