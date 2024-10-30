# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:36:00 2024

@author: Vaishnavi
"""
"""Problem Statement: 
Kitabi Duniya, a famous book store in India, 
which was established before Independence, 
the growth of the company was incremental 
year by year, but due to online selling of
books and wide spread Internet access its
annual growth started to collapse, seeing 
sharp downfalls, you as a Data Scientist help
this heritage book store gain its popularity 
back and increase footfall of customers and 
provide ways the business can improve exponentially,
apply Association RuleAlgorithm, explain the rules,
 and visualize the graphs for clear understanding 
 of solution.
1.) Books.csv
"""
#pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder
#Sample dataset
#load the CSV file
df=pd.read_csv("C:/10-reccomendation_engine/assignments/book.csv")

#here the step 1 is not needed...directly we can go for step 2
#step1:convert the dataset into a format suitable for Apriori
#te=TransactionEncoder()
#te_ary=te.fit(df).transform(df)
#df=pd.DataFrame(te_ary,columns=te.columns_)

#step2:Apply the apriori algorithm to find frequent itemsets
frequent_itemsets=apriori(df,min_support=0.05,use_colnames=True)
print(frequent_itemsets)
#min_support =0.6/0.7 try for it

df.shape
df.dtypes
#step3:Generate association rules from the frequent itemsets
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
#try for threshold=2
#step4:Output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])









