import pandas as pd
df = pd.read_csv("./Downloads/Book1.csv")
df.to_json('./Downloads/output-json-data.json', orient='records', force_ascii=False)
# force_ascii=False は日本語をUnicodeエスケープしない方法