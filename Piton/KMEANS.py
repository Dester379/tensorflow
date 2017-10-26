import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from pandas import ExcelWriter
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer as DV
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

from sklearn import linear_model
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import LogisticRegression

vec = DV(sparse=False)
scaler = MinMaxScaler()
label = LabelEncoder()
dicts = {}

location=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\Segmentation\KM_3.xlsx'
location2=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\Segmentation\KMEANS.xlsx'
df=pd.read_excel(location)

col=df.columns[:16]
for q in col:
    df[q]=df[q].fillna(0)
col2=df.columns[16:]
for q in col2:
    df[q]=df[q].fillna(1)

kmeans = KMeans(n_clusters=10, init='k-means++').fit(df[col2])
kmeans.labels_ 
   

from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(df[col2])

df["kLabels"]=pd.Series(kmeans.labels_) 

df[col2]=scaler.fit_transform(df[col2])

df['CLV']=0.087*df.R + 0.345*df.F + 0.653*df.M

writer = ExcelWriter(location2)
df.to_excel(writer)
writer.save() 
#########################################################################################################################
y=df.claster
X=df[['BD_code', 'IS_TD','IS_CREDIT', 'IS_CARD', 'IS_CC', 'IS_DC', 'Unsecured', 'mortgage',
       'A3RC', 'A3ATM', 'A3POS', 'A3Br']]
       
accuracy_score(clf.predict(X), y)
metrics.roc_curve(clf.predict(X), y)
scores = cross_val_score(clf, X, y)

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier

clf = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0).fit(X,y)
scores = cross_val_score(clf, X, y)
scores.mean()  
col=X.columns
imp=clf.feature_importances_
fet=[col, imp]
fordata=pd.DataFrame(np.array(fet).T)
fordata.sort(1, ascending=False)

#for CLV
y=df.CLV
clf=LogisticRegression(penalty='l1', multi_class='multinomial')
clf.fit(X, y)
clf = ExtraTreesRegressor()
clf.fit(X, y)
