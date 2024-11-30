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
        subjects = self.file['유형'].unique()
        subjects_dict = {i: value for i, value in enumerate(subjects, start=1)}
        for i, value in enumerate(subjects, start=1):
            print(f"{i}. {value}")
        while True:
            subject_number = int(input('번호를 입력하세요 >'))
            if subject_number in subjects_dict:
                self.subject = subjects_dict[subject_number]
                break
            else:
                print('번호가 존재하지 않습니다')
        data = self.file[self.file['유형'] == self.subject]
        for i, row in data.iterrows():
            self.score.append(row['표준점수'])
            self.man.append(row['남자'])
            self.woman.append(row['여자'])