import pandas as pd
import os
class FileProcess:
    def __init__(self,encoding='euc-kr'):
        self.path = None
        self.encoding = encoding
        self.file = None
        self.man = []
        self.score = []
        self.woman = []
        self.subject = None
        self.year = 0

    def process(self):
        current_directory = os.getcwd()
        file_list = os.listdir(current_directory)
        csv_list = [f for f in file_list if f.endswith('.csv')]
        year = [csv[:4] for csv in csv_list]
        print("\n".join(year))
        while True:
            self.year = input('연도를 입력하세요 >')
            if self.year in year:
                break
            else:
                print('존재하지 않는 연도입니다')
        for file in csv_list:
            if file.startswith(self.year):
                self.path = file
        self.file = pd.read_csv(self.path, encoding=self.encoding)
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