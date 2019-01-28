#!/usr/bin/env python3

#########################################################
# 母比率の差の検定／タイプ4
#########################################################

import sys
import math
import numpy as np


def error_usage():
    sys.stderr.write("usage: " + sys.argv[0] + "\n")
    sys.stderr.write("\tこのプログラムは、4つの引数が必要です。\n\n")
    sys.stderr.write(
        "\t1.全体のn数 2.全体における比率 3.ある属性のn数 4.ある属性における比率\n")
    sys.stderr.write("\t例： 150 0.3 100 0.45\n\n")
    sys.stderr.write("\tただし、それぞれn数は30以上かつ比率pは[0<=p<=1]を満たすこと\n")
    sys.stderr.write("\t「1.全体のn数」は「3.ある属性のn数」より大きいこと\n")
    sys.exit(1)


def checkFig(figures):
    # n数が30以上か？
    if (figures[0, 0] >= 30) and (figures[1, 0] >= 30):
        pass
    else:
        error_usage()

    # 比率は0から1の間か？
    if (0 <= figures[0, 1] <= 1) and (0 <= figures[1, 1] <= 1):
        pass
    else:
        error_usage()

    # nはn1より大きいか？
    if (figures[0, 0] > figures[1, 0]):
        pass
    else:
        error_usage()


class zTestType4:
    def __init__(self, figures):
        n = figures[0, 0]
        p = figures[0, 1]
        n1 = figures[1, 0]
        p1 = figures[1, 1]

        pdif = math.fabs(p - p1)

        self.z = pdif / math.sqrt((p * (1-p)) * (n - n1)/(n * n1))
        self.sig1p = 2.58
        self.sig5p = 1.96
        self.sig10p = 1.65

    def test(self):
        if self.z >= self.sig1p:
            return self.resultReturn("1%有意", self.z)
        elif self.z >= self.sig5p:
            return self.resultReturn("5%有意", self.z)
        elif self.z >= self.sig10p:
            return self.resultReturn("10%有意", self.z)
        else:
            return self.resultReturn("有意差なし", self.z)

    def resultReturn(self, rate, z):
        return "{} (検定統計量:{:.5f})".format(rate, z)


if __name__ == '__main__':
    # 引数がちょうど4つあるか？
    if len(sys.argv[1:]) == 4:
        figures = np.array(sys.argv[1:], dtype=np.float64)
    else:
        error_usage()

    # 2行2列のデータ型に変換
    figures = np.reshape(figures, (2, -1))

    # 数値が検定の前提を満たしているか確認
    checkFig(figures)

    st = zTestType4(figures)
    print(st.test())
