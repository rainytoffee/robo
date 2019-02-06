# coding:utf-8
from robo import ctrl_csv
from robo import tools

# 意図しない回答に対して朴訥かつ愛くるしい態度をみせる
alert = 'なんて？'


def is_your_name():
    while True:
        print("私はロボター。あなたの名前は？")
        name = tools.gp_capitalize(input())
        if name:
            return name
        else:
            print(alert)
            continue


your_name = is_your_name()


def your_recommend():
    while True:
        print("{}さん、あなたのおすすめのレストランは？".format(your_name))
        restaurant = tools.gp_capitalize(input())
        if "," in restaurant:
            print(", は使わんでね")
        elif restaurant:
            break
        else:
            print(alert)
    # CSV処理。オーパーツ。CSV内にrestaurantが見つからなければ追記。
    # すでに存在していれば票数を+1し、票数で降順ソート。
    # よくわからないがとにかくrestaurant名を渡すとrecommends.csvが光を放つ。
    ctrl_csv.search_in_recommends(restaurant)


def detect_you(is_first=True):
    with open("recommends.csv", "r") as f:
        for line in f:
            if is_first:
                is_first = False
                continue  # teach_youで使った店をスキップ
            ask = ("それじゃあ、"+line.split(",")[0]+"は好きですか？ (Y/N)")
            ans = tools.yes_or_no(ask, alert)
            if ans == "Y":
                return
            elif ans == "N":
                continue


def teach_you():
    with open("recommends.csv", "r") as f:
        top = f.readline().split(",")[0]
        ask = ("私のおすすめのレストランは{}です。{}さんはどうですか？(y/n)".format(top, your_name))
        ans = tools.yes_or_no(ask, alert)
        if ans == 'Y':
            return
        # nならcsv内の投票の多いものから順に店を並べ立てる。
        # yが出るか店リストがなくなるまでしつこく聞く。無邪気なロボットは体温を持たないのだ。
        elif ans == 'N':
            detect_you()


def bye():
    print("ありがとうございました。{}さん、よい一日を！".format(your_name))
