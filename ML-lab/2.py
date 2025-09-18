import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df1 = pd.read_csv('./basket_analysis.csv', index_col=0)
df1.head()

df1.info()

df1 = df1.fillna(False)

frequent_itemsets = apriori(df1, min_support=0.2, use_colnames=True)
frequent_itemsets

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules = rules.sort_values(['confidence', 'lift'], ascending=[False, False])
rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head()

