from queue import Queue
import random
from decimal import Decimal
from copy import copy

def hongbao(totalmoney, persons):
    print("红包总金额为："+str(totalmoney)+"元，红包个数为："+str(persons)+"个")
    q = Queue()
    hongbao = Queue()

    if totalmoney / persons <= 0.011:
        print("红包太小，人太多了，不够抢！")
    else:
        overplusMoney = totalmoney;
        for i in range(persons, 1, -1):
            money = random.uniform(0.01, (2 * overplusMoney) / i)

            overplusMoney = overplusMoney - money

            money = Decimal(money).quantize(Decimal('0.00'))
            q.put(money)
            hongbao.put(money)

        lasthongbao = 0
        while q.qsize():
            lasthongbao = lasthongbao + q.get()

        hongbao.put(totalmoney - lasthongbao)

        k = 1
        while not hongbao.empty():
            print("第" + str(k) + "人抢到的红包金额为：" + str(hongbao.get()) + "元")
            k = k + 1


if __name__ == "__main__":
    i = 0
    while i < 1000:
        hongbao(180, 20)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        i = i + 1