import datetime

# 関数を引数に取る
def print_datetime(f):
    # 関数内に関数を定義
    # デコレートする関数calcと同じ引数を指定する。
    # 引数の数を任意の数に対応する為には、可変長引数を使用する
    # (*args)は普通の引数をタプルで受け取る
    # (**kwargs)はname="namae"のような、変数名を指定するキーワード引数に対応する。（辞書）
    # 上記の二つでどのような形の引数にも対応する
    def wrapper(*args, **kwargs):
        print(f"開始: {datetime.datetime.now()}")
        # デコレートする関数calcと同じ引数を指定
        f(*args, **kwargs)
        print(f"終了: {datetime.datetime.now()}")
    # wrapper関数を返す
    return wrapper


@print_datetime
def calc(a, b):
    print(a*b)

@print_datetime
def calc1(a, b, c):
    print(a*b*c)

@print_datetime
def calc2(a, b, c, d):
    print(a*b*c*d)


# 関数のオブジェクトIDが表示
# print(calc)

# func1の引数にfunc2を渡す
# wrapper関数（オブジェクト）を返す
# func = print_datetime(calc)
# 実行すると返ってきた関数を起動する
# func(3, 10)

# まとめるとこの形で出来る
# print_datetime(calc)(3, 10)


# @装飾する関数名 でデコレートする事で以下で同じ事が出来る
# デコレーター:print_datetime でデコレートされたcalc()を呼び出す
calc(3, 10)
calc1(3, 10, 2)
calc2(3, 10, 2, 4)
