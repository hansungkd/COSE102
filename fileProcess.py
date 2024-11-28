import pandas as pd
class FileProcess:
    def __init__(self,path,encoding='euc-kr'):
        self.path = path
        self.encoding = encoding
        self.file = pd.read_csv(self.path, encoding=self.encoding)
        self.man = []
        self.score = []
        self.woman = []
        self.subject = None

    def process(self):
        while True:
            self.subject = input('유형을 입력하세요 >')
            if self.subject in self.file['유형'].unique():
                break
            else:
                print('선택한 유형이 존재하지 않습니다')
        data = self.file[self.file['유형'] == self.subject]
        for i, row in data.iterrows():
            self.score.append(row['표준점수'])
            self.man.append(row['남자'])
            self.woman.append(row['여자'])