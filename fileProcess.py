import pandas as pd
file = pd.read_csv("20231231.csv",encoding='euc-kr')
while True:
    subject = input()
    if subject in file['유형'].unique():
        break
data = file[file['유형'] == subject]
man = []
score = []
woman = []
for i, row in data.iterrows():
    score.append(row['표준점수'])
    man.append(row['남자'])
    woman.append(row['여자'])
