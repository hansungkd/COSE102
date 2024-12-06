from fileProcess import FileProcess
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(year, subject, score, man, woman):
    plt.rcParams['font.family'] = 'NanumGothic'

    man_cumulative = np.cumsum(man[::-1])[::-1]
    woman_cumulative = np.cumsum(woman[::-1])[::-1]

    plt.fill_between(score, 0, man_cumulative, label='남', alpha=0.5)
    plt.fill_between(score, 0, woman_cumulative, label='여', alpha=0.5)

    plt.title(f"{int(year) + 1}학년도 수능 {subject} 과목 성적 분포")
    plt.xlabel("점수")
    plt.ylabel("누적 인원수")
    plt.legend()

    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    file = FileProcess()
    file.process()
    plot_graph(file.year, file.subject, file.score, file.man, file.woman)


