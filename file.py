import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
data = {
    "Performance_Score": [45, 50, 55, 80, 85, 90, 95]
}

df = pd.DataFrame(data)
model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Group"] = model.fit_predict(df[["Performance_Score"]])
print(df)
plt.scatter(df.index, df["Performance_Score"], c=df["Group"], cmap='viridis', s=100)
plt.title("CM Candidate Segmentation")
plt.xlabel("Candidate Index")
plt.ylabel("Performance Score")
plt.show()