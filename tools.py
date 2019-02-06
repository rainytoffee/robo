

# 如意キャピ。いい具合のキャピ。
# ex. 'get wiLd anD toUGh' -> 'Get Wild And Tough'
def gp_capitalize(word):
    result = []
    if " " in word:
        word = word.split(" ")
        for w in word:
            w = w.capitalize()
            result.append(w)
        return (" ".join(result))  # pycharm先生が冗長であると怒るが僕にはわからない
    else:
        return word.capitalize()


# print(ask)してからY/N入力を求めてループ
# いるようないらないようなfunctionですが生命を感じる
# Yy/Nn以外の入力に対してはalertを表示し、ループを継続する
def yes_or_no(ask, alert):
    while True:
        print(ask)
        answer = input().capitalize()
        if answer == 'Y':
            return 'Y'
        elif answer == 'N':
            return 'N'
        else:
            print(alert)
            continue
