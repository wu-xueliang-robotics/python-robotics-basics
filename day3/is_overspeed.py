def is_overspeed(speed):
    if speed > 5:
        return True
    else:
        return False
b = int(input("please input speed :"))
a = is_overspeed(b)
if a == True:
    print("overspeed")
else:
    print("safety speed")
