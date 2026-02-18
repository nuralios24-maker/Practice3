def Myfun(a):
    return a+a

print(Myfun(30))

def temp1(b):
    if(b > 1):
        return b+b
    return b-b
print(temp1(19))

def temp2(cb):
    if(cb == "name"):
        return print("Name")
    return print("No name")

temp2("name"); temp2("None")

def temp3(dp):
    for i in range(4):
        dp += i
        if(dp > 2): return print("Hello")
        else: return print("car")

temp3(5)
temp3(0)

def temp4(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            return i
    return -1


list1 = [1, 2, 3, 4, 5]
print(temp4(list1))

list1 = [-1, -2, -3, -4, -5]
print(temp4(list1))