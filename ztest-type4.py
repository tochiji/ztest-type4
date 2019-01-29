#########################################################
# 母比率の差の検定／タイプ4
#########################################################

import sys
import math

def error_usage():
    sys.stderr.write("usage: " + sys.argv[0] + "\n")
    sys.stderr.write("\tこのプログラムは、4つの引数が必要です。\n\n")
    sys.stderr.write(
        "\t1.全体のn数 2.全体における比率 3.ある属性のn数 4.ある属性における比率\n")
    sys.stderr.write("\t例： 150 0.3 100 0.45\n\n")
    sys.stderr.write("\tただし、それぞれn数は30以上かつ比率pは[0<=p<=1]を満たすこと\n")
    sys.stderr.write("\t「1.全体のn数」は「3.ある属性のn数」より大きいこと\n")
    sys.exit(1)

# 引数がちょうど4つあるか？
if len(sys.argv[1:]) != 4:
    error_usage()

n,p,n1,p1 = map(float, sys.argv[1:])

# n数が30以上か？
if (n < 30) or (n1 < 30):
    error_usage()

# nはn1より大きいか？
if n < n1 :
    error_usage()

# 比率は0から1の間か？
if not (0 <= p <= 1) or not (0 <= p1 <= 1):
    error_usage()

T = math.fabs(p - p1) / math.sqrt((p * (1-p)) * (n - n1)/(n * n1))

if T >= 2.58:
    print("1%有意 (検定統計量:" + str(T) + "）")
elif T >= 1.96:
    print("5%有意 (検定統計量:" + str(T) + "）")
elif T >= 1.65:
    print("10%有意 (検定統計量:" + str(T) + "）")
else:
    print("有意差なし")
