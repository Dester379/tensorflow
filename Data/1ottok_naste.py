import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
from sklearn.metrics import roc_auc_score, roc_curve, log_loss, confusion_matrix, precision_score, recall_score, classification_report, accuracy_score
from sklearn.feature_extraction import DictVectorizer as DV
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier


scaler = StandardScaler()
label = LabelEncoder()

#считываем
location=u'Z:\RBA\MSK\Krasnogorsk\Workgroups\Products Development\Remote Channels\R-CONNECT\Иван Серов\Отток\DATASET.xlsx'
df=pd.read_excel(location)


#заменяем пропуски на нули
torep=['Customer', 'Age', 'COUNT_of_AccountN', 'SUM_BALANCE', 'IS_CARD',
       'COUNT_CARD', 'IS_CC', 'COUNT_CC_Main', 'COUNT_CC_Suppl', 'IS_DC',
       'COUNT_DC_Main', 'COUNT_DC_Suppl', 'Count_UNSECURED', 'Count_MORTGAGE',
       'Count_CARLOAN','Sum_UNSECURED', 'Sum_MORTGAGE', 'Sum_CARLOAN', 'COUNT_TD', 'SUM_TD',
       'SESS_1M_COUNT', 'SESS_3M_COUNT', 'SESS_12M_COUNT',
       'A12', 'A6', 'A3', 'A1', 'Active_months', 'COUNT_12', 'SumR_12',
       'COUNT_6', 'SumR_6', 'COUNT_3', 'SumR_3', 'COUNT_1', 'SumR_1', 
       'Active_months_RC', 'COUNT_12RC',
       'SumR_12RC', 'COUNT_3RC', 'SumR_3RC', 'COUNT_1RC', 'SumR_1RC', 'A12ATM', 'A3ATM',
       'A1ATM', 'Active_months_ATM', 'COUNT_12ATM', 'SumR_12ATM', 'COUNT_3ATM',
       'SumR_3ATM', 'COUNT_1ATM', 'SumR_1ATM', 'A12POS', 'A3POS', 'A1POS',
       'Active_months_POS', 'COUNT_12POS', 'SumR_12POS', 'COUNT_3POS',
       'SumR_3POS', 'COUNT_1POS', 'SumR_1POS', 'A12Br', 'A3Br', 'A1Br',
       'Active_months_Br', 'COUNT_12Br', 'SumR_12Br', 'COUNT_3Br','SumR_3Br', 'COUNT_1Br', 'SumR_1Br', 'CountTr', 'SumTr',
       'CountTr_Vyvod_', 'SumTrVyvod', 'Part_CountTrVyvod', 'Part_SumTrVyvod',
       'IS_RCAS','IS_CA', 'IS_B1000', 'IS_TD', 'IS_CREDIT', 'IS_SMS_ALERT', 'IS_PIN',
       '#_MWS_Оплата услуг', '#_RC_Оплата услуг',
       '#_RC_перевод на карту другого ба', '#_MWS_перевод на чужую карту Рай',
       '#_RC_Рублевые переводы', '#_MWS_перевод на карту другого б',
       '#_MWS_Пополнение депозита', '#_MWS_Частичное снятие депозита',
       '#_MWS_Внутренние Переводы/Конвер', '#_RC_перевод на чужую карту Райф','#_RC_перевод средств между своим', '#_MWS_Перевод с карты на карту',
       '#_MWS_Рублевые переводы', '#_RC_Перевод с карты на карту',
       '#_RC_Внутренние Переводы/Конверт', '#_MWS_Добавление Push ID',
       '#_RC_Перевод с карты другого бан', '#_MWS_Открытие депозита',
       '#_RC_Платежи в бюджет (РФ)', '#_RC_перевод с зп карты на карту',
       '#_MWS_Перевод с карты другого ба', '#_RC_Заявление на ЧДП кредита Ум',
       '#_RC_Пополнение депозита', '#_MWS_перевод средств между свои',
       '#_RC_Создание нового счета', '#_MWS_Заявление на ЧДП кредита У',
       '#_MWS_Заявление на полное досроч', '#_MWS_Изменение телефона для SMS',
       '#_RC_Частичное снятие депозита', '#_RC_Открытие депозита',
       '#_RC_Валютные переводы за рубеж', '#_MWS_Создание нового счета',
       '#_RC_Изменение телефона для SMS', '#_RC_Заявление на полное досрочн',
       '#_MBG_Оплата услуг', '#_RC_Изменение телефона для СМС-',
       '#_RC_Изменение контактного телеф', '#_MWS_Платежи в бюджет (РФ)',
       '#_RC_Валютные переводы РФ', '#_RCP_Перевод с карты на карту',
       '#_MWS_Оплата паев', '#_RC_Подтверждение входа однораз',
       '#_RC_Оплата паев', '#_RC_Изменение параметров автопл',
       '#_RCP_Рублевые переводы', '#_RC_Отключение автоплатежа',
       '#_RCP_Открытие депозита', '#_RCP_Оплата услуг',
       '#_RCP_Внутренние Переводы/Конвер', '#_RCP_Частичное снятие депозита','#_RCP_Платежи в бюджет (РФ)', '#_RCP_Валютные переводы за рубеж',
       '#_RCP_Пополнение депозита', '#_RC_Подключение автоплатежа',
       '#_RC_Добавление Push ID', 'S_MWS_Оплата услуг', 'S_RC_Оплата услуг',
       'S_RC_перевод на карту другого ба', 'S_MWS_перевод на чужую карту Рай',
       'S_RC_Рублевые переводы', 'S_MWS_перевод на карту другого б',
       'S_MWS_Пополнение депозита', 'S_MWS_Частичное снятие депозита',
       'S_MWS_Внутренние Переводы/Конвер', 'S_RC_перевод на чужую карту Райф',
       'S_RC_перевод средств между своим', 'S_MWS_Перевод с карты на карту',
       'S_MWS_Рублевые переводы', 'S_RC_Перевод с карты на карту',
       'S_RC_Внутренние Переводы/Конверт', 'S_MWS_Добавление Push ID',
       'S_RC_Перевод с карты другого бан', 'S_MWS_Открытие депозита',
       'S_RC_Платежи в бюджет (РФ)', 'S_RC_перевод с зп карты на карту',
       'S_MWS_Перевод с карты другого ба', 'S_RC_Заявление на ЧДП кредита Ум',
       'S_RC_Пополнение депозита', 'S_MWS_перевод средств между свои',
       'S_RC_Создание нового счета', 'S_MWS_Заявление на ЧДП кредита У',
       'S_MWS_Заявление на полное досроч', 'S_MWS_Изменение телефона для SMS',
       'S_RC_Частичное снятие депозита', 'S_RC_Открытие депозита',
       'S_RC_Валютные переводы за рубеж', 'S_MWS_Создание нового счета',
       'S_RC_Изменение телефона для SMS', 'S_RC_Заявление на полное досрочн',
       'S_MBG_Оплата услуг','S_RC_Изменение телефона для СМС-', 'S_RC_Изменение контактного телеф',
       'S_MWS_Платежи в бюджет (РФ)', 'S_RC_Валютные переводы РФ',
       'S_RCP_Перевод с карты на карту', 'S_MWS_Оплата паев',
       'S_RC_Подтверждение входа однораз', 'S_RC_Оплата паев',
       'S_RC_Изменение параметров автопл', 'S_RCP_Рублевые переводы',
       'S_RC_Отключение автоплатежа', 'S_RCP_Открытие депозита',
       'S_RCP_Оплата услуг', 'S_RCP_Внутренние Переводы/Конвер',
       'S_RCP_Частичное снятие депозита', 'S_RCP_Платежи в бюджет (РФ)',
       'S_RCP_Валютные переводы за рубеж', 'S_RCP_Пополнение депозита',
       'S_RC_Подключение автоплатежа', 'S_RC_Добавление Push ID', 'SUM_ALL',
       '/_MWS_Оплата услуг', '/_RC_Оплата услуг',
       '/_RC_перевод на карту другого ба', '/_MWS_перевод на чужую карту Рай',
       '/_RC_Рублевые переводы', '/_MWS_перевод на карту другого б',
       '/_MWS_Пополнение депозита', '/_MWS_Частичное снятие депозита',
       '/_MWS_Внутренние Переводы/Конвер', '/_RC_перевод на чужую карту Райф',
       '/_RC_перевод средств между своим', '/_MWS_Перевод с карты на карту',
       '/_MWS_Рублевые переводы', '/_RC_Перевод с карты на карту',
       '/_RC_Внутренние Переводы/Конверт', '/_MWS_Добавление Push ID',
       '/_RC_Перевод с карты другого бан', '/_MWS_Открытие депозита',
       '/_RC_Платежи в бюджет (РФ)', '/_RC_перевод с зп карты на карту',
       '/_MWS_Перевод с карты другого ба', '/_RC_Заявление на ЧДП кредита Ум',
       '/_RC_Пополнение депозита', '/_MWS_перевод средств между свои',
       '/_RC_Создание нового счета', '/_MWS_Заявление на ЧДП кредита У',
       '/_MWS_Заявление на полное досроч', '/_MWS_Изменение телефона для SMS',
       '/_RC_Частичное снятие депозита', '/_RC_Открытие депозита',
       '/_RC_Валютные переводы за рубеж', '/_MWS_Создание нового счета',
       '/_RC_Изменение телефона для SMS', '/_RC_Заявление на полное досрочн',
       '/_MBG_Оплата услуг', '/_RC_Изменение телефона для СМС-',
       '/_RC_Изменение контактного телеф', '/_MWS_Платежи в бюджет (РФ)',
       '/_RC_Валютные переводы РФ', '/_RCP_Перевод с карты на карту',
       '/_MWS_Оплата паев', '/_RC_Подтверждение входа однораз',
       '/_RC_Оплата паев', '/_RC_Изменение параметров автопл',
       '/_RCP_Рублевые переводы', '/_RC_Отключение автоплатежа',
       '/_RCP_Открытие депозита', '/_RCP_Оплата услуг',
       '/_RCP_Внутренние Переводы/Конвер', '/_RCP_Частичное снятие депозита',
       '/_RCP_Платежи в бюджет (РФ)', '/_RCP_Валютные переводы за рубеж',
       '/_RCP_Пополнение депозита', '/_RC_Подключение автоплатежа',
       '/_RC_Добавление Push ID', 'TMP_cnt_this_month',
       'TMP_count_creation_dates', 'TMP_count', 'TMP_count_type',
       'TMP_delta_MinMax_days',
       'TMP_delta_MaxAv_days', 'COUNT_Comp_Mob', 'COUNT_of_Browser',
       'CNT_send_cards', 'CNT_recieve_banks', 'CNT_distinct_sums',
       'MAX_of_OP_IS_MTC', 'MAX_of_OP_IS_Beeline', 'MAX_of_OP_IS_Megafon',
       'MAX_of_OP_IS_Tele2', 'MAX_of_OP_IS_other']
for q in torep:
    df[q]=df[q].fillna(0) 
'''    
rep=['Category', 'Client_Category', 'segment', 'Client_Type',
'AgeGroup', 'Gender', 'Married', 'HomeBranch',
'Branch_HB', 'Hub_HB', 'ClientBranch', 'Branch_C', 'Hub_C','Вывод', 'SMS_ALERTING',  'Branch_BR', 'HUB_BR']  
for q in torep:
    df[q]=df[q].fillna('NaN')
  ''' 
cltype=pd.get_dummies(df.Client_Type) 
df = pd.concat([df, cltype], axis=1)
#создаем новые фичи по датам
df['DIF_1-2Trans']=df['Second_TrRC']-df['First_TrRC']
df['DIF_1-2Trans']=df['DIF_1-2Trans'].fillna(df['DIF_1-2Trans'].mean())
df['dif_A']=df['DATE_LAST_SESSION'] - df['Last_A_RC']
df['dif_A']=df['dif_A'].fillna(df['dif_A'].mean())
df['years_acc']=df['DATE_LAST_SESSION'] - df['First_Account']
df['years_acc']=df['years_acc'].fillna(df['years_acc'].mean())
df['SESS_2M_COUNT']=df['SESS_3M_COUNT'] - df['SESS_1M_COUNT']

df['DIF_1-2Trans']=df['DIF_1-2Trans'].apply(lambda x: x.days)
df['dif_A']=df['dif_A'].apply(lambda x: x.days)
df['years_acc']=df['years_acc'].apply(lambda x: x.days)
     
Y=df.Y
to_drop=['Client_Type','IS_CARD', 'IS_DC', 'IS_CC', 'Customer', 'Y', 'Last_A', 'Last_A_RC','First_Account','DATE_LAST_SESSION','First_TrRC','Second_TrRC','min_creation_date','max_creation_date']
df=df.drop(to_drop,axis=1)  
 
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
#df.Client_Type=df.Client_Type.fillna('nan')
df.Client_Category=label.fit_transform(df.Client_Category)
#df.Client_Type=label.fit_transform(df.Client_Type)
df.Category=df.Category.fillna('nan')   
df.Category=label.fit_transform(df.Category)
df.HomeBranch=df.HomeBranch.fillna('nan')   
df.HomeBranch=label.fit_transform(df.HomeBranch)
df.Branch_HB=df.Branch_HB.fillna('nan')   
df.Branch_HB=label.fit_transform(df.Branch_HB)
df.ClientBranch=df.ClientBranch.fillna('nan')   
df.ClientBranch=label.fit_transform(df.ClientBranch)
df.Branch_C=df.Branch_C.fillna('nan')   
df.Branch_C=label.fit_transform(df.Branch_C)
df.Hub_C=df.Hub_C.fillna('nan')   
df.Hub_C=label.fit_transform(df.Hub_C)
df.Вывод=df.Вывод.fillna('nan')   
df.Вывод=label.fit_transform(df.Вывод)
df.Branch_BR=df.Branch_BR.fillna('nan')   
df.Branch_BR=label.fit_transform(df.Branch_BR)
df.HUB_BR=df.HUB_BR.fillna('nan')   
df.HUB_BR=label.fit_transform(df.HUB_BR)

X=scaler.fit_transform(df)
X=pd.DataFrame(X)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=0)                





#смотрим важность фич и их влияние на целевую переменную
clf = LogisticRegression(random_state = 0).fit(X_train, y_train)
preds_lr = clf.predict_proba(X_test)

imp = pd.DataFrame(list(zip(df.columns, clf.coef_[0])))
imp=imp[:30]
imp = imp.reindex(imp[1].abs().sort_values().index).set_index(0)
from matplotlib.pyplot import savefig
#график_фич
ax = imp.plot.barh(width = .6, legend = "", figsize = (12, 9))
ax.set_title("Logistic Regression coefs", y = 1.03, fontsize = 16.)
_ = ax.set(frame_on = False, xlabel = "", xticklabels = "", ylabel = "")
for i, label in enumerate(list(imp.index)):
    score = imp.loc[label][1]
    ax.annotate('%.2f' % score, (score + (-.12 if score < 0 else .02), i - .2), fontsize = 10.5)
savefig('fol.png', bbox_inches='tight')
#фичи списком для импорта
col=df.columns
imp=clf.feature_importances_
fet=[col, imp]
fordata=pd.DataFrame(np.array(fet).T)
fordata.sort(1, ascending=False)    


#############################################################################
#МОДЕЛЬ    
clf = GradientBoostingClassifier(random_state=0).fit(X_train, y_train)
tuned_parameters = [{'learning_rate':np.arange(0.2, 1, 0.1)},
                     {'n_estimators':np.arange(60, 200, 20)},
                      {'max_depth':np.arange(2, 6, 1)}]
gs = GridSearchCV(clf, tuned_parameters, cv=5, verbose=True)
gs.fit(X_train, y_train)
roc_auc_score(gs.predict(X_test), y_test)       
preds_gb=gs.predict_proba(X_test)
##############################################################################    
imp = pd.DataFrame(list(zip(df.columns, clf.feature_importances_)))
imp=imp[:30]
imp = imp.reindex(imp[1].abs().sort_values().index).set_index(0)
#график_фич
ax = imp.plot.barh(width = .6, legend = "", figsize = (12, 9))
ax.set_title("Gradient Boosting coefs", y = 1.03, fontsize = 16.)
_ = ax.set(frame_on = False, xlabel = "", xticklabels = "", ylabel = "")
for i, label in enumerate(list(imp.index)):
    score = imp.loc[label][1]
    ax.annotate('%.2f' % score, (score + (-.12 if score < 0 else .02), i - .2), fontsize = 10.5)
############################################################################## 
clf = RandomForestClassifier(random_state=0).fit(X,Y)
tuned_parameters = [{'min_samples_split':np.arange(2, 4, 1)},
                     {'n_estimators':np.arange(10, 30, 5)},
                      {'max_depth':np.arange(2, 6, 1)}]
gs = GridSearchCV(clf, tuned_parameters, cv=5, verbose=True)
gs.fit(X_train, y_train)
roc_auc_score(gs.predict(X_test), y_test)       
preds_rf=gs.predict_proba(X_test)


#ROC_Curve of 3 models
plt.figure(figsize = (8, 8))
plt.plot(*roc_curve(y_test, preds_gb[:, 1])[:2])
plt.plot(*roc_curve(y_test, preds_lr[:, 1])[:2])
plt.plot(*roc_curve(y_test, preds_rf[:, 1])[:2])
plt.legend(["GB Classifier", "Logistic Regression", "Random Forest"], loc = "upper left")
plt.plot((0., 1.), (0., 1.), "--k", alpha = .7)
plt.xlabel("False Positive Rate"), plt.ylabel("True Positive Rate")
plt.title("ROC Curves", fontsize = 16.)













