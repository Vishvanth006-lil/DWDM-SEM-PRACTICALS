#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("Market_Basket_Optimisation.csv")
# len(df)
print(df)


# In[2]:



max_row = None
max_val = 0

for idx,row in df.iterrows():
    cnt = 0
    for a in row:
        if pd.isnull(a):
            break
        cnt += 1
        
    if cnt > max_val:
        max_val = cnt
        max_row = row
        
# print(row)
print(max_val)


# In[3]:


all_transactions = []

for idx,row in df.iterrows():
    transaction_items = []
    
    for i in row:
        if pd.isnull(i):
            break
        else:
            transaction_items.append(i)
            
    all_transactions.append(transaction_items)
    


# In[6]:


from apyori import apriori


# In[7]:


def printRules(rules):
    for rule in rules:
        print(rule)


# # GIVEN CONDITIONS
# ### min_support = 0.6 
# ### confidence = 0.8
# ### min_length = 2

# In[8]:


rules = apriori(all_transactions,min_support=0.6,min_confidence=0.8,min_length=2)
printRules(rules) # NO RULES PRINTED


# # EXAMPLE RULE EXISTING CONDITION
# ### min_support = 0.1
# ### confidence = 0.1
# ### min_length = 2

# In[16]:


rules = apriori(all_transactions,min_support=0.1,min_confidence=0.2,min_length=2)
printRules(rules)

