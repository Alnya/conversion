import time


def full_half(x):
    # ターミナルから入力した文字列のうち、
    # 全角のハイフンと全角のシングルクォーテーションを
    # それぞれ半角に直して出力
    n = list(input())
    if x == 0:
        print()
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
    print()
    for i in range(len(n)):
        if n[i] == "‐":
            n[i] = "-"
        if n[i] == "’" or n[i] == "‘":
            n[i] = "'"
        print(n[i], end="")
    return 1


def main():
    x = 0
    print("Paste your sentences and then, click \"Enter\" within 3 minutes")
    while True:
        x = full_half(x)


if __name__ == "__main__":
    main()
