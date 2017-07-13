#!/usr/bin/env python
# -*- coding: utf-8 -*-

# できるだけプログラムっぽくないプログラミング.py
## コンセプト
# - できる限り、日本人に優しい「日本語」を利用する。
# - 更に「絵文字」を利用してカラフルに味付け
#   （…したいけど、今回は厳しい感じ）。

普通に表示する = lambda 文字列: print(文字列)
繋げて表示する = lambda 配列: 普通に表示する(" ".join(配列))

class 名言:

    def __init__(self, 発言, 発言者の名前):
        self.配列 = 発言
        self.発言者 = 発言者の名前
    def 吐く(self):
        繋げて表示する(["「"] + self.配列 + ["」"])
    def 詠み人(self):
        繋げて表示する(["　　　〜", self.発言者])

# 以降、できる限りプログラムっぽくなくなるよう意識する。

def main():

    名言その1 = 名言(
        ["本日は", "晴天なり。😆"],
         "坂本龍馬")
    名言その2 = 名言(
        ["ああああ", "いいいい"],
         "豊臣秀吉")

    名言その1.吐く ()
    名言その1.詠み人()

    名言その2.吐く()
    名言その2.詠み人()

# このソースがモジュールとして
# 利用されることがあるとは到底思えないが、
# 世の中何があるかわからないので。

if __name__ == "__main__":
    main()

