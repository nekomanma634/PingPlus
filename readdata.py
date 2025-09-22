from pathlib import Path
import matplotlib.pyplot as plt

def GetFileData(filepath):
    data_ping = []
    data_time = []
    idx = 0

    file = open(filepath, "r", encoding="utf-8")
    for line in file:
        idx += 1
        cleaned_line = line.strip() # いらない空白などの削除

        parts = cleaned_line.split('-')
        # data_time.append(parts[0]) 本当は時間で作成した方が良い
        data_time.append(idx)
        data_ping.append(float(parts[1]))

    file.close()

    SmpGra(data_time, data_ping)

def SmpGra(x, y):

    # グラフの作成
    plt.plot(x, y)

    # グラフのタイトルと軸ラベル
    plt.title("Time Ping")
    plt.xlabel("X-time[s]")
    plt.ylabel("Y-ping[ms]")

    # グラフを表示
    plt.show()

if __name__ == "__main__":
    current_dir = Path('./data') # pathの指定
    for item in current_dir.iterdir():
        print(item)

    print("どのファイルを読み込みますか. 例_result1.txt")
    filepath = "./data/"
    filepath += input()

    GetFileData(filepath)