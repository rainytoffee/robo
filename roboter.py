from robo import conversation
from robo import ctrl_csv
import os.path

# 課題をアレしました
# 各所のinput()に'junk dealer'と打ち込むとsys.exit()で落ちるようにしたかったのですが
# 個人には分際というものがあり、アレしました


def start_up():
    if not os.path.exists('recommends.csv'):
        f = open('recommends.csv', 'w')
        f.close()
    with open('recommends.csv', 'r') as f:
        # recommends.csvが空ならすぐあなたの推しを聞いてきます
        if ctrl_csv.is_empty('recommends.csv'):
            conversation.your_recommend()
        # 中身があればvotesが一番高い店を推してきます
        else:
            conversation.teach_you()
            conversation.your_recommend()
    # あなたのレコメンドを聞いたら.csvにアレしてソートしてアレします
    conversation.bye()


if __name__ == '__main__':
    start_up()
# conversation.ctrl_csv.show_up()
