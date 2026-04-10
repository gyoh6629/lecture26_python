def getIndex(num_list, target):
    count = 0
    index = 0
    for _ in num_list:
        count += 1
    for i in range(count):
        if target == num_list[i]:
            index = i
    return index

def getMax(num_list):
    count = 0
    num = num_list[0]
    for _ in num_list:
        count += 1
    for i in range(count):
        if num < num_list[i]:
            num = num_list[i]
    return num

def getMin(num_list):
    count = 0
    num = num_list[0]
    for _ in num_list:
        count += 1
    for i in range(count):
        if num > num_list[i]:
            num = num_list[i]
    return num

def countGT(num_list, target):
    count = 0
    countgt = 0
    for _ in num_list:
        count += 1
    for i in range(count):
        if target == num_list[i]:
            countgt += 1
    return countgt

def sumList(num_list):
    s = 0
    for i in num_list:
        s += i
    return s

def swapList(num_list):
    count = 0
    for _ in num_list:
        count += 1
    for i in range(count):
        if i >= count-1-i:
            break
        temp = num_list[i]
        num_list[i] = num_list[count-1-i]
        num_list[count-1-i] = temp
    return num_list

number_list = [23, 45, 27, 11, 25, 65, 78]

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
swapList(number_list)
print(number_list)