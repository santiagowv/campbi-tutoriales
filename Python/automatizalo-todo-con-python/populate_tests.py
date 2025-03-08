import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")

for x in range(10):
    sample = df.sample(100)
    df.to_csv(f"directorio_pruebas/sample_file_{x + 1}.csv", index = False)