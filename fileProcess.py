import pandas as pd
class FileProcess:
    def __init__(self,path,encoding='euc-kr'):
        self.path = path
        self.encoding = encoding
        self.file = None
    def loading(self):
        self.file = pd.read_csv(self.path, encoding=self.encoding)
    def processing(self):
        while True:
            subject = input('유형을 입력하세요 >')
            if subject in self.file['유형'].unique():
                break
            else:
                print('선택한 유형이 존재하지 않습니다')
        data = self.file[self.file['유형'] == subject]
        man = []
        score = []
        woman = []
        for i, row in data.iterrows():
            score.append(row['표준점수'])
            man.append(row['남자'])
            woman.append(row['여자'])
        return man, woman, score


'''import pandas as pd
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
    woman.append(row['여자'])'''
