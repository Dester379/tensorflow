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
from sklearn.cross_validation import cross_val_score
from sklearn import tree

vec = DV(sparse=False)
scaler = StandardScaler()
label = LabelEncoder()
dicts = {}
# считываем
location=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\sample3.xlsx'
location2=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\sampleee.xlsx'
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
 'SumR_3',
  '2017_03_Рублевые переводы', '2017_03_перевод на чужую карту Р', '2017_03_Внутренние Переводы/Конв', '2017_03_Перевод с карты другого',
 '2017_03_Оплата услуг', '2017_03_Добавление Push ID', '2017_03_Перевод с карты на карту', '2017_03_перевод на карту другого',
 '2017_03_Частичное снятие депозит', '2017_03_Пополнение депозита', '2017_03_перевод средств между св', '2017_03_Создание нового счета',
 '2017_03_перевод с зп карты на ка', '2017_03_Платежи в бюджет (РФ)', '2017_03_Изменение контактного те', '2017_03_Заявление на полное доср',
 '2017_03_Валютные переводы за руб', '2017_03_Открытие депозита', '2017_03_Подтверждение входа одно', '2017_03_Изменение телефона для S',
 '2017_03_Оплата паев', '2017_03_Изменение телефона для С', '2017_03_Рублевый перевод по e-ma', '2017_03_Рублевый перевод по номе','COUNT_Tr_A1',
 'SumR_Tr_A1', 'COUNT_Tr_A2', 'SumR_Tr_A2', 'COUNT_Tr_A3', 'SumR_Tr_A3', 'COUNT_Tr_A4', 'SumR_Tr_A4', 'COUNT_Tr_A5', 'SumR_Tr_A5',
 'COUNT_Tr_A6', 'SumR_Tr_A6', 'SUM_BALANCE_now', 'SUM_BALANCE_1m', 'SUM_BALANCE_2m', 'SUM_BALANCE_3m', 'SUM_BALANCE_4m', 'SUM_BALANCE_5m',
 'SUM_BALANCE_6m', 'Source', '2017_03_Изменение лимитов по кар', '2017_03_Создание/изменение поезд', '2017_03_Валютные переводы РФ',
 '2017_03_Подключение СМС-ОТР', '2017_03_Отключение автоплатежа', '2017_02_Добавление Push ID', '2017_02_Оплата услуг', '2017_02_Рублевые переводы',
 '2017_02_Внутренние Переводы/Конв', '2017_02_Перевод с карты на карту', '2017_02_перевод на чужую карту Р', '2017_02_перевод средств между св',
 '2017_02_Валютные переводы за руб', '2017_02_Изменение телефона для S', '2017_02_перевод на карту другого', '2017_02_Пополнение депозита',
 '2017_02_Создание нового счета', '2017_02_Перевод с карты другого', '2017_02_Заявление на полное доср', '2017_02_Валютные переводы РФ',
 '2017_02_перевод с зп карты на ка', '2017_02_Частичное снятие депозит', '2017_02_Платежи в бюджет (РФ)', '2017_02_Оплата паев',
 '2017_02_Открытие депозита', '2017_02_Изменение контактного те', '2017_02_Подтверждение входа одно', '2017_02_Изменение телефона для С',
 '2017_02_Отключение автоплатежа', '2017_02_Подключение автоплатежа', '2017_02_Изменение лимитов по кар', '2017_02_Создание/изменение поезд',
 '2017_02_Изменение параметров авт', '2017_02_Подключение СМС-ОТР', '2017_01_Рублевые переводы', '2017_01_перевод на чужую карту Р',
 '2017_01_Подключение СМС-ОТР', '2017_01_Оплата услуг', '2017_01_Внутренние Переводы/Конв', '2017_01_Перевод с карты на карту', '2017_01_перевод средств между св',
 '2017_01_перевод на карту другого',
 '2017_01_Добавление Push ID',
 '2017_01_Изменение телефона для S',
 '2017_01_Перевод с карты другого',
 '2017_01_перевод с зп карты на ка',
 '2017_01_Заявление на полное доср',
 '2017_01_Создание нового счета',
 '2017_01_Платежи в бюджет (РФ)',
 '2017_01_Валютные переводы за руб',
 '2017_01_Частичное снятие депозит',
 '2017_01_Пополнение депозита',
 '2017_01_Изменение контактного те',
 '2017_01_Изменение телефона для С',
 '2017_01_Валютные переводы РФ',
 '2017_01_Оплата паев',
 '2017_01_Отключение автоплатежа',
 '2017_01_Открытие депозита',
 '2017_01_Подтверждение входа одно',
 '2017_01_Подключение автоплатежа',
 '2017_01_Изменение параметров авт',
 '2016_12_перевод на карту другого',
 '2016_12_перевод на чужую карту Р',
 '2016_12_Оплата услуг',
 '2016_12_Рублевые переводы',
 '2016_12_Внутренние Переводы/Конв',
 '2016_12_Перевод с карты на карту',
 '2016_12_Открытие депозита',
 '2016_12_Создание нового счета',
 '2016_12_Частичное снятие депозит',
 '2016_12_Добавление Push ID',
 '2016_12_перевод средств между св',
 '2016_12_Перевод с карты другого',
 '2016_12_Пополнение депозита',
 '2016_12_Платежи в бюджет (РФ)',
 '2016_12_перевод с зп карты на ка',
 '2016_12_Заявление на полное доср',
 '2016_12_Валютные переводы за руб',
 '2016_12_Изменение телефона для S',
 '2016_12_Изменение контактного те',
 '2016_12_Оплата паев',
 '2016_12_Изменение параметров авт',
 '2016_12_Изменение телефона для С',
 '2016_12_Подтверждение входа одно',
 '2016_12_Валютные переводы РФ',
 '2016_12_Отключение автоплатежа',
 '2016_12_Подключение автоплатежа',
 '2016_11_Рублевые переводы',
 '2016_11_перевод на чужую карту Р',
 '2016_11_Оплата услуг',
 '2016_11_Валютные переводы за руб',
 '2016_11_Внутренние Переводы/Конв',
 '2016_11_Перевод с карты на карту',
 '2016_11_Добавление Push ID',
 '2016_11_перевод на карту другого',
 '2016_11_Перевод с карты другого',
 '2016_11_Частичное снятие депозит',
 '2016_11_Открытие депозита',
 '2016_11_Создание нового счета',
 '2016_11_перевод средств между св',
 '2016_11_Платежи в бюджет (РФ)',
 '2016_11_Заявление на полное доср',
 '2016_11_перевод с зп карты на ка',
 '2016_11_Изменение телефона для S',
 '2016_11_Пополнение депозита',
 '2016_11_Изменение контактного те',
 '2016_11_Оплата паев',
 '2016_11_Валютные переводы РФ',
 '2016_11_Изменение телефона для С',
 '2016_11_Подключение автоплатежа',
 '2016_11_Отключение автоплатежа',
 '2016_11_Изменение параметров авт',
 '2016_10_перевод на карту другого',
 '2016_10_перевод на чужую карту Р',
 '2016_10_Внутренние Переводы/Конв',
 '2016_10_Добавление Push ID',
 '2016_10_Создание нового счета',
 '2016_10_Оплата услуг',
 '2016_10_Платежи в бюджет (РФ)',
 '2016_10_Рублевые переводы',
 '2016_10_Перевод с карты на карту',
 '2016_10_перевод средств между св',
 '2016_10_Пополнение депозита',
 '2016_10_Перевод с карты другого',
 '2016_10_Частичное снятие депозит',
 '2016_10_Заявление на полное доср',
 '2016_10_Валютные переводы за руб',
 '2016_10_перевод с зп карты на ка',
 '2016_10_Открытие депозита',
 '2016_10_Изменение телефона для S',
 '2016_10_Валютные переводы РФ',
 '2016_10_Изменение телефона для С',
 '2016_10_Изменение контактного те',
 '2016_10_Оплата паев',
 '2016_10_Отключение автоплатежа',
 '2016_10_Изменение параметров авт',
 '2016_10_Подключение автоплатежа',
 '2016_10_Подключение СМС-ОТР']
for q in torep:
    df[q]=df[q].fillna(0)
    
to_drop=['Month', 'SDate','EDate','Customer', '_TEMA001', 'PINk_Last_Channel','SMSOTPАктивно',	'PUSHOTPАктивно',	'EMVCAPАктивно',
        'SMSOTPЗаблокировано',	'EMVCAPЗаблокировано',
         'HomeBranch', 'Branch_HB', 'ClientBranch', 'CLIENT_ID','REGISTER_ID',  'Branch_C', 'Hub_C',
        'BranchResult', 'IS_RCAS',	'AUTH_FIRST_D',	'Branch_BR',	
        'HUB_BR', 'Count_CARLOAN', 'Sum_CARLOAN', 'DATE_LAST_SESSION','Source','SUM_BALANCE']
df=df.drop(to_drop,axis=1)   
df.drop(['PIN1_D','First_Account', 'Last_A', 'First_TrRC', 'Second_TrRC', 'Last_A_RC', 'PINk1_D', 'PINk_Last_D', 'LOG1_D', 'SESS_D_First','SESS_D_Last'],axis=1, inplace=True)

#создаем новые графы
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
df.Client_Category=df.Client_Category.fillna('nan')
df.Client_Type=df.Client_Type.fillna('nan')
df.Client_Category=label.fit_transform(df.Client_Category)
df.Client_Type=label.fit_transform(df.Client_Type)
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

df1=df
df['y']=[0]*len(df)
for i in range(len(df)):
    if df['A1'][i]==0 and df['SESS_1M_COUNT'][i]==0 and df['COUNT_1RC'][i]==0:
        df['y'][i]=0
    elif df['A1'][i]==1 and df['SESS_1M_COUNT'][i]==0 and df['COUNT_1RC'][i]==0:        
        df['y'][i]=1
    elif df['A1'][i]==1 and df['SESS_1M_COUNT'][i]!=0 and df['COUNT_1RC'][i]==0:
        df['y'][i]=2
    elif df['A1'][i]==1 and df['SESS_1M_COUNT'][i]!=0 and df['COUNT_1RC'][i]!=0:
        df['y'][i]=3

df['y'] = np.where(df['A1']==0, 0, np.where(df['SESS_1M_COUNT']==0, 1, np.where(df['COUNT_1RC']==0, 2, 3) ))

y=df.y[:20000]
df.drop('y', axis=1, inplace=True)

#scale
dftest=scaler.fit_transform(df[:20000])
dftest=pd.DataFrame(dftest)

'''#train
clf=LogisticRegression(penalty='l1')
clf.fit(dftest, y)
from sklearn import linear_model
clf = linear_model.SGDRegressor()
clf.fit(dftest, y)'''

from sklearn.ensemble import ExtraTreesRegressor
clf = ExtraTreesRegressor()
clf.fit(dftest, y)

clf.predict(dftest)
col=df.columns
imp=clf.feature_importances_
fet=[col, imp]
fordata=pd.DataFrame(np.array(fet).T)
score = cross_val_score(clf, dftest, y).mean()

fordata.sort(1, ascending=False)

df.drop(['A1', 'A1RC', 'SESS_3M_COUNT'], axis=1, inplace=True)

#saving
writer = ExcelWriter(location2)
dftest.to_excel(writer,'uhod')
writer.save() 




