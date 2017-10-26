import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.patches as mpatches

p = df.groupby('Y').value_count()["IS_CARD"].plot.bar(rot = 0)
p = df.groupby('AgeGroup').sum()["Y"].plot.bar(rot = 20)
p = df.Y.value_counts().sort_index().plot.bar(rot = 0)

plt.figure(figsize=(8,6))
plt.scatter(range(df.shape[0]), np.sort(df.Age.values))



plt.figure(figsize=(12,8))
sns.distplot(df.Age.values, bins=50, kde=True)
plt.xlabel('Age', fontsize=12)
plt.show()
#количество пропусков
missing_df = df.isnull().sum(axis=0).reset_index()
missing_df.columns = ['column_name', 'missing_count']
missing_df = missing_df.ix[missing_df['missing_count']>0]
missing_df = missing_df.sort_values(by='missing_count')
ind = np.arange(missing_df.shape[0])

fig, ax = plt.subplots()
rects = ax.barh(ind, missing_df.missing_count.values, color='y')
ax.set_yticks(ind)
ax.set_yticklabels(missing_df.column_name.values, rotation='horizontal')
ax.set_xlabel("Count of missing values")
ax.set_title("Number of missing values in each column")
plt.show()