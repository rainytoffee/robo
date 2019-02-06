# coding:utf-8
import csv
# ======================================================================
# CSV処理 謎の技術。遠い未来のパワーで動いているのでいじってはならない。
# funcごとにファイル開いてるのでうなされる。
# ======================================================================


def search_in_recommends(restaurant):
    dic = {}
    f = open('recommends.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        dic[row[0]] = row[1]  # csvから辞書型生成
        if restaurant in dic:  # 辞書内に見つかればカウントアップ
            count_up(restaurant, dic[restaurant])
            break
    else:
        if restaurant not in dic:
            add_row(restaurant)  # 既存のデータになければ追記


def add_row(restaurant):  # 追記ファンク
    with open('recommends.csv', 'a') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow([restaurant, '1'])
        print("追記しました。")


def count_up(restaurant, vote):  # 店の投票数に1加算
    vote = int(vote)+1
    with open('recommends.csv', 'r') as f:
        list_for_write = []
        reader = csv.reader(f)
        for row in reader:
            if restaurant in row:
                list_for_write.append([restaurant, str(vote)])
            else:
                list_for_write.append(row)
    f = open('recommends.csv', 'w')
    writer = csv.writer(f, lineterminator="\n")
    for values in list_for_write:
        writer.writerow(values)
    f.close()

    f = open('recommends.csv', 'r')
    dic = {}
    reader = csv.reader(f)
    for row in reader:
        dic[row[0]] = row[1]
    sort_dict_downvalues(dic)  # 加算後、得票数でCSVをsort
    print("情報を更新しました。")


# sort func. key->店名：value->票数のdict。CSVに書き込みまで行う。
# 特にわからない。sorted()のkeyにlambdaを与えるあたりにもっともっとスリルに犯された体があってわからない。
def sort_dict_downvalues(dic):
    with open('recommends.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        sorted_dict = sorted(dic.items(), key=lambda x: -int(x[1]))  # 降順でソート
        for key_and_value in sorted_dict:
            writer.writerow(key_and_value)  # 書込


# キャトル・ミューティレーション
def is_empty(file):
    with open(file, 'r') as f:
        if f.readline() == "":
            return True


# CSVの中身がまろび出るのみ。debug用
def show_up():
    with open('recommends.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)
