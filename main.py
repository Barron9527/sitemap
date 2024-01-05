import subprocess
import time

num = 1

def execute_curl():
    global num  # 使用 global 关键字声明全局变量

    try:
        # 执行 curl 命令
        subprocess.run(["curl", "https://www.google.com/ping?sitemap=https://raw.githubusercontent.com/Barron9527/sitemap/main/sitemap.xml"], check=True)
        subprocess.run(["curl", "https://www.google.com/ping?sitemap=https://ads.6af403a09ca3.com/sitemap.xml"], check=True)
        subprocess.run(["curl", "https://www.google.com/search?q=https://ads.6af403a09ca3.com"], check=True)
        print("\n成功推送！No." + str(num) + "\n")
    except subprocess.CalledProcessError as e:
        print(f"Error during curl execution: {e}")

def main():
    global num  # 使用 global 关键字声明全局变量

    while True:
        try:
            # 执行 curl
            execute_curl()

            # 休眠1s
            num = num + 1
            time.sleep(1)
        except KeyboardInterrupt:
            # 如果在休眠期间接收到 KeyboardInterrupt（Ctrl+C），退出脚本
            print("Script terminated by user.")
            break

if __name__ == "__main__":
    main()
