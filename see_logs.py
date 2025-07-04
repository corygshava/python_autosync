import pandas as pd

df = pd.read_json('history.json');

print(df.to_string(index=False));