import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.dummy import DummyClassifier
from pandas import ExcelWriter
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer as DV
from os import system
from sklearn import tree

vec = DV(sparse=False)
scaler = StandardScaler()
label = LabelEncoder()
dicts = {}
#считываем
location=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\Segmentation\RANDRANDOMSAMPLERUASVII_PORTF.xlsx'
location2=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\Segmentation\sas1.xlsx'
df=pd.read_excel(location)

#заменяем пропуски на нули
torep=['SUM_BALANCE_now','SUM_BALANCE_2m','SUM_BALANCE_1m','COUNT_CARD', 'COUNT_of_AccountN', 'IS_CARD','IS_CC', 'COUNT_CC_Main', 'COUNT_CC_Suppl', 'COUNT_DC_Main',
'COUNT_DC_Suppl','Count_UNSECURED','Count_MORTGAGE','COUNT_TD','Sum_UNSECURED',
'SUM_TD','COUNT_of_AccountN','IS_DC','Sum_UNSECURED','Sum_MORTGAGE','COUNT_TD','SUM_TD',
'SESS_1M_COUNT','SESS_3M_COUNT','SESS_6M_COUNT','SESS_12M_COUNT','COUNT_YM_12m',
'A12', 'A6', 'A3',	'A1',	'Active_months',	'COUNT_12','COUNT_6',		'SumR_12',	'SumR_6', 'COUNT_3',	'SumR_3',	'COUNT_1',	'SumR_1',
'A12RC', 'A6RC',	'A3RC',	'A1RC',	'Active_months_RC',	'COUNT_12RC',	'SumR_12RC',	'COUNT_3RC',	'SumR_3RC',
	'COUNT_1RC',	'SumR_1RC', 'A12ATM',	'A3ATM',	'A1ATM',	'Active_months_ATM',	'COUNT_12ATM',	'SumR_12ATM',	
 'COUNT_3ATM',	'SumR_3ATM',	'COUNT_1ATM',	'SumR_1ATM',	'A12POS',	'A3POS',	'A1POS',	'Active_months_POS',
	'COUNT_12POS',	'SumR_12POS',	'COUNT_3POS',	'SumR_3POS',	'COUNT_1POS',	'SumR_1POS',	'A12Br',	'A3Br',
	'A1Br','Active_months_Br', 'COUNT_12Br',	'SumR_12Br'	, 'COUNT_3Br', 'SumR_3Br',	'COUNT_1Br',	'SumR_1Br',
	'CountTr',	'SumTr',	'CountTr_Vyvod_', 'SumTrVyvod','Part_CountTrVyvod','Part_SumTrVyvod', 'IS_CA', 'IS_B1000', 
 'IS_TD',	'IS_CREDIT',	'IS_SMS_ALERT',	'IS_PIN','Sum_UNSECURED','SumTr','SumTrVyvod', 'sum_PINk', 'COUNT_6RC', 'SumR_6RC', 
 'SumR_3','balance_diff_now_1m', 'balance_diff_now_2m']
for q in torep:
    df[q]=df[q].fillna(0)
    


y=df.SUM_BALANCE_now
to_drop=['Month', 'SDate','EDate','Customer', '_TEMA001', 'PINk_Last_Channel','SMSOTPАктивно',	'PUSHOTPАктивно',	'EMVCAPАктивно',
        'SMSOTPЗаблокировано',	'EMVCAPЗаблокировано',
         'HomeBranch', 'Branch_HB', 'ClientBranch', 'CLIENT_ID','REGISTER_ID',  'Branch_C', 'Hub_C',
        'BranchResult', 'IS_RCAS',	'AUTH_FIRST_D',	'Branch_BR',	
        'HUB_BR', 'Count_CARLOAN', 'Sum_CARLOAN', 'DATE_LAST_SESSION' ]
df=df.drop(to_drop,axis=1)   

#создаем новые графы
df['DIF_1-2Trans']=df['Second_TrRC']-df['First_TrRC']
df['DIF_1-2Trans']=df['DIF_1-2Trans'].fillna(df['DIF_1-2Trans'].mean())
df['dif_A']=df['Last_A'] - df['Last_A_RC']
df['dif_A']=df['dif_A'].fillna(df['dif_A'].mean())
df['sess_diff']=df['SESS_D_Last'] - df['Last_A_RC']
df['sess_diff']=df['sess_diff'].fillna(df['sess_diff'].mean())

df.BUNDLECODE=df.BUNDLECODE.fillna('NONE')  
df.BUNDLECODE=label.fit_transform(df.BUNDLECODE)
df.Married=df.Married.fillna('nan')
df.Married=label.fit_transform(df.Married)
df.Gender=df.Gender.fillna('nan')
df.Gender = label.fit_transform(df.Gender)
df.segment=df.segment.fillna('NONE')
df.segment=label.fit_transform(df.segment)
df.Вывод=df.Вывод.fillna('no info')
df.Вывод=label.fit_transform(df.Вывод)
df.Hub_HB=df.Hub_HB.fillna('nan')
df.Hub_HB=label.fit_transform(df.Hub_HB)
df.AgeGroup=df.AgeGroup.fillna('nan')
df.AgeGroup=label.fit_transform(df.AgeGroup)
df.SMS_ALERTING=df.SMS_ALERTING.fillna('nan')
df.SMS_ALERTING = label.fit_transform(df.SMS_ALERTING)
df['balance_diff_now_1m']=label.fit_transform(df['balance_diff_now_1m'])
df['balance_diff_now_2m']=label.fit_transform(df['balance_diff_now_2m'])


df.Client_Category=df.Client_Category.fillna('nan')
df.Client_Type=df.Client_Type.fillna('nan')
df.Client_Category=label.fit_transform(df.Client_Category)
df.Client_Type=label.fit_transform(df.Client_Type)

df.drop(['PIN1_D','First_Account', 'Last_A', 'First_TrRC', 'Second_TrRC', 'Last_A_RC', 'PINk1_D', 'PINk_Last_D', 'LOG1_D', 'SESS_D_First','SESS_D_Last'],axis=1, inplace=True)
df['DIF_1-2Trans']=df['DIF_1-2Trans'].apply(lambda x: x.days)
df['dif_A']=df['dif_A'].apply(lambda x: x.days)
df['sess_diff']=df['sess_diff'].apply(lambda x: x.days)

df['SumTr']=df['SumTr'].str.replace('.', '')
df['SumTrVyvod']=df['SumTrVyvod'].str.replace('.', '')
df['Sum_UNSECURED']=df['Sum_UNSECURED'].str.replace('.', '')
df['Sum_MORTGAGE']=df['Sum_MORTGAGE'].str.replace('.', '')

df['SumTr']=df['SumTr'].str.replace(',', '.')
df['SumTrVyvod']=df['SumTrVyvod'].str.replace(',', '.')
df['Sum_UNSECURED']=df['Sum_UNSECURED'].str.replace(',', '.')
df['Sum_MORTGAGE']=df['Sum_MORTGAGE'].str.replace(',', '.')
df['Sum_MORTGAGE']=df['Sum_MORTGAGE'].fillna(0)
df['Sum_UNSECURED']=df['Sum_UNSECURED'].fillna(0)
df['SumTrVyvod']=df['SumTrVyvod'].fillna(0)
df['SumTr']=df['SumTr'].fillna(0)

cat_per=['Client_Category','Client_Type','AgeGroup','segment',	'Gender',	'Married',
         'BUNDLECODE','Hub_HB', 'Вывод','SMS_ALERTING','balance_diff_now_1m', 'balance_diff_now_2m']
X_cat=df[cat_per]
oh_cat=label.fit_transform(X_cat.T.to_dict().values())
df2 = pd.concat([df, pd.DataFrame(oh_cat)], axis=1)
df2.drop(cat_per, axis=1, inplace=True)
#scale

dftest=scaler.fit_transform(df)
dftest=pd.DataFrame(dftest)
#train
clf=LogisticRegression(penalty='l1')
clf.fit(dftest, y)

from sklearn import linear_model
clf = linear_model.SGDRegressor()
clf.fit(dftest, y)

from sklearn.ensemble import ExtraTreesRegressor
clf = ExtraTreesRegressor()
clf.fit(dftest, y)
col=df.columns
imp=clf.feature_importances_
fet=[col, imp]
fordata=pd.DataFrame(np.array(fet).T)
#saving
writer = ExcelWriter(location2)
dftest.to_excel(writer,'uhod')
writer.save() 