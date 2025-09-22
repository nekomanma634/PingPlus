import ping3
import datetime
import pytz
import time
from pathlib import Path

def ping_with_ping3(host):
    try:
        delay = ping3.ping(host, timeout=2) # timeoutを秒単位で指定
        count = delay*1000

        if delay is not False:
            print(f"✅ {host} との疎通が確認できました。応答時間: {count:.1f}ms")
            return count
        else:
            print(f"❌ {host} との疎通が確認できませんでした。")
            return False
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False

def GetPingData(count, filepath, ip):
    with open(filepath, "w", encoding="utf-8") as file: # fileをクリア
        file.write("")

    for i in range(count):
        time.sleep(1)
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(f"{datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%Y%m%d%H%M%S")}-")   # 日付(年 月 日 時 分 秒)
            file.write(f"{ping_with_ping3(ip):.1f}\n")                                                      # ping[ms]

if __name__ == "__main__":
    current_dir = Path('../data') # pathの指定
    for item in current_dir.iterdir():
        print(item)

    print("どのファイルにデータを保存しますか.(ファイルが存在しない場合は作成されます.) 例_result1.txt")
    filepath = "../data/"
    filepath += input()
    print("アドレスを指定してください.")
    ip = input()
    print("何回データを取得しますか.\n(約n*1[s]秒の時間がかかります)")
    GetPingData(int(input()), str(filepath), str(ip))