import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../data/halfHeusler.csv")
df = df[[ 'ZX', 'ZAB', 'ZAB.1', 'mX', 'mAB', '∆mAB', 'rowX', 'rowAB', '∆rowAB',
       'colX', 'colAB', '∆colAB', 'eX', 'eAB', '∆eAB', 'rX', 'rAB', '∆rAB',
       'χX', 'χAB', '∆χAB', 'alatt', 'cv', 'cs', 'κ˜grain',
       'κtransf', 'κforest', 'κanh','gap']]
df = df.dropna()
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
X = df_scaled.drop(columns=['cs', 'cv'])
y = df_scaled[['cv']]
