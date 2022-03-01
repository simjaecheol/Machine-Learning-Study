# %%
import numpy as np
import pandas as pd
# %%
import os
import inspect
from sys import platform
PROJ_DIR = os.path.dirname(inspect.getabsfile(inspect.currentframe()))
WORKING_DIR = os.path.dirname(PROJ_DIR)
KAGGLE_DIR = os.path.dirname(WORKING_DIR)
# %%
PROJ_NAME = PROJ_DIR.split('\\')[-1]
INPUT_DIR = os.path.join(KAGGLE_DIR, 'input')
PROJ_INPUT_DIR = os.path.join(INPUT_DIR, PROJ_NAME)

os.sys.path.insert(0, PROJ_INPUT_DIR)
print(PROJ_INPUT_DIR)
# %%
train = pd.read_csv(os.path.join(PROJ_INPUT_DIR, 'train.csv'))
test = pd.read_csv(os.path.join(PROJ_INPUT_DIR, 'test.csv'))
gender_submission = pd.read_csv(os.path.join(PROJ_INPUT_DIR, 'gender_submission.csv'))
# %%
data = pd.concat([train, test], sort=False)
data.keys()
# %%
data['Sex'].replace(['male', 'female'], [0, 1], inplace=True)
# %%
data['Fare'].fillna(np.mean(data['Fare']), inplace=True)
# %%
data
# %%
data['Embarked'].fillna(('S'), inplace=True)
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q':2}).astype(int)
data
# %%
age_avg = data['Age'].mean()
age_std = data['Age'].std()

data['Age'].fillna(np.random.randint(age_avg - age_std, age_avg + age_std), inplace=True)
# %%
delete_columns = ['Name', 'PassengerId', 'SibSp', 'Parch', 'Ticket', 'Cabin']
data.drop(delete_columns, axis=1, inplace=True)
# %%
train = data[:len(train)]
test = data[len(train):]
# %%
y_train = train['Survived']
X_train = train.drop('Survived', axis=1)
X_test = test.drop('Survived', axis=1)
# %%
print(X_train)
print('------------------------------------------')
print(y_train)
# %%

# %%
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty='l2', solver='sag', random_state=0)
clf.fit(X_train, y_train)
# %%
y_pred = clf.predict(X_test)
sub = pd.read_csv(os.path.join(PROJ_INPUT_DIR, 'gender_submission.csv'))
sub['Survived'] = list(map(int, y_pred))
sub.to_csv('submission.csv', index=False)
# %%
