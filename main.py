from fileProcess import FileProcess
import matplotlib.pyplot as plt

def plot_graph(subject, score, man, woman):
    plt.rcParams['font.family'] = 'NanumGothic'

    plt.plot(score, man, label='남', linestyle='-', linewidth=2, alpha=0.7)
    plt.scatter(score, man, alpha=0.7, s=15)

    plt.plot(score, woman, label='여', linestyle='-', linewidth=2, alpha=0.7)
    plt.scatter(score, woman, alpha=0.7, s=15)

    plt.title(f"2024학년도 수능 {subject} 과목 성적 분포")
    plt.xlabel("점수")
    plt.ylabel("인원수")
    plt.legend()

    plt.show()

if __name__ == '__main__':
    path = '20231231.csv'
    file = FileProcess(path)
    file.process()
    plot_graph(file.subject, file.score, file.man, file.woman)


