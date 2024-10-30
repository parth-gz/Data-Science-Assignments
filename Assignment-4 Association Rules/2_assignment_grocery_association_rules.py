# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:40:08 2024

@author: Vaishnavi
"""
"""
Problem Statement: - 
The Departmental Store, has gathered the data of the products it sells on a Daily basis.
Using Association Rules concepts, provide the insights on the rules and the plots.
2.) Groceries.csv
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder
#lets import the file 
df=pd.read_csv("C:/10-reccomendation_engine/assignments/grocery.csv",on_bad_lines='skip')
df.shape
df.dtypes


#step1:convert the dataset into a format suitable for Apriori
te=TransactionEncoder()
te_ary=te.fit(df).transform(df)
df1=pd.DataFrame(te_ary,columns=te.columns_)
frequent_itemsets=apriori(df1,min_support=0.03,use_colnames=True)
print(frequent_itemsets)
df1

rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
#try for threshold=2
#step4:Output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])


