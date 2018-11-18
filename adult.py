#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as  pd


# In[10]:


adult=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data")


# In[11]:


adult.columns=['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','label']


# In[13]:


adult.head()


# 1. Select 10 records from the adult sqladb

# In[4]:


from pandasql import sqldf


# In[32]:


pysqldf = lambda q: sqldf(q, globals())


# In[33]:


q='''SELECT * FROM adult LIMIT 10;'''


# In[34]:


a = pysqldf(q)
print(a)


# 2. Show me the average hours per week of all men who are working in private sector

# In[35]:


pysqldf = lambda r: sqldf(r, globals())  
r='''SELECT AVG(hours_per_week) FROM adult WHERE workclass =' Private' and sex=' Male';'''
a=pysqldf(r)
a


# 3. Show me the frequency table for education, occupation and relationship, separately

# In[42]:


pysqldf = lambda s: sqldf(s, globals())  
s='''select distinct education,count(education) from adult group by education  ;'''
a=pysqldf(s)
a


# same can be done for occupation and  relationship separately

# 4. Are there any people who are married, working in private sector and having a masters
# degree

# In[65]:


pysqldf = lambda w: sqldf(w, globals())  
w='''SELECT count(*) FROM adult WHERE  marital_status=' Married-civ-spouse' and  workclass =' Private' and education=' Masters';'''
a=pysqldf(w)
a


# 5. What is the average, minimum and maximum age group for people working in
# different sectors

# In[49]:


pysqldf = lambda t: sqldf(t, globals())  
t='''SELECT workclass,AVG(age) Average ,MIN(age) Minimum ,MAX(age) Maximum

FROM adult GROUP BY workclass;'''
a=pysqldf(t)
a


# 6. Calculate age distribution by country

# In[51]:


pysqldf = lambda u: sqldf(u, globals())  
u='''SELECT native_country,AVG(age) Average ,MIN(age) Minimum ,MAX(age) Maximum FROM adult GROUP BY native_country;'''
a=pysqldf(u)
a


# 7. Compute a new column as 'Net-Capital-Gain' from the two columns 'capital-gain' and
# 'capital-loss'

# In[56]:


pysqldf = lambda v: sqldf(v, globals())  
v='''SELECT (capital_gain - capital_loss) 'Net-Capital-Gain',*  FROM adult order by (capital_gain - capital_loss) desc limit 10;'''
a=pysqldf(v)
a


# In[ ]:




