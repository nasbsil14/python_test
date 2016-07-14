#変数
value = "test"
print(value)

#if
if len(value) == 4:
    print("4文字")
elif len(value) == 3:
    print("ありえない")

#三項演算
num = 3
num2 = num if num == 3 else 0

#for
lists = [1, 2, 3]
for item in lists:
    print(item)

#while
count = 3
while count >= 0:
    print(count)
    count -= 1

#List
lists = [1, 2, 3]

#Tuple
tup = (1, 2, 3)

#Dectionaly
maps = {"key1": "val1", "key2": "val2", "key3": "val3"}

#lambda
lam = lambda x: print(x)
lam("test")

#class
class Customer:
    def __init__(self, number, name, height=0):
        self.number = number
        self.name = name
        self.height = height

taro = Customer(101, "太郎", 180)
print("{}: {} {}cm".format(taro.number, taro.name, taro.height))

