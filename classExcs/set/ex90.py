import random
import time


def get_item_list(index, list, type):
    retVAl = None
    print("start...")
    t0 = time.perf_counter()
    if type == "set":
        retVal = index in list
    else:
        retVal = list[index]
    time.sleep(2.5)
    timeItTakes = time.perf_counter() - t0
    print("done!", timeItTakes)
    return retVal, timeItTakes


mylist = random.sample(range(1, 1000001), 10000)
myset = set(mylist)
print("=================set=======================")
randNum = random.randint(1, 10000)

itemList, timeOfList = get_item_list(randNum, mylist, "list")
print("=================list=======================")
itemSet, timeOfSet = get_item_list(randNum, myset, "set")

if timeOfList > timeOfSet:
    print("list > set takes longer for item ", randNum)
    print("list takes ", timeOfList)
    print("list takes ", timeOfSet)
    print("bigger by", timeOfList - timeOfSet)

else:
    print(" set  > list takes longer for item ", randNum)
    print("list takes ", timeOfList)
    print("list takes ", timeOfSet)
    print("more by", timeOfSet - timeOfList)
