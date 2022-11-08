#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


from sklearn.datasets import load_digits 
digits = load_digits()
digits.keys()


# In[3]:


X=digits.data
y=digits.target


# In[4]:


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20, random_state=42)

X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[5]:


from sklearn.preprocessing import StandardScaler
clf = StandardScaler()
X_train1=clf.fit_transform(X_train)
X_test1 =clf.transform(X_test)

X_train1.shape, X_test1.shape


# In[7]:


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf1 = LinearDiscriminantAnalysis(n_components=9)
X_train2=clf1.fit_transform(X_train1,y_train)
X_test2 =clf1.transform(X_test1)
X_train2.shape,X_test2.shape


# In[9]:


explained_variance=clf1.explained_variance_ratio_
explained_variance


# In[10]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train2,y_train)


# In[11]:


y_pred=rf.predict(X_test2)


# In[15]:


y_pred.shape


# In[16]:


from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score


# In[23]:


cm=confusion_matrix(y_test, y_pred)
cm


# In[26]:


# Plotting the heatmap:

sns.heatmap(cm,annot=True, cmap='Greens')
plt.title('Correlation Matrix')
plt.show()


# In[30]:


accuracy_score(y_test,y_pred)


# In[20]:


print('Classification Report:')
classification=classification_report(y_test,y_pred)
print(classification)

