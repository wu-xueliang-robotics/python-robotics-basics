def calc_rps(speed,radius = 0.15):
    circle = 2 * 3.14159 * radius
    return speed / circle

def check_speed(speed):
    if speed > 5:
        return "too fast"
    elif speed < 0:
        return "minus"
    else:
        return "safety"
def count_add(count):
    count = count + 1
    return count

count = 0
while True:
    user_input = input("please input speed :   ,input q will break")

    if user_input == "q":
        print(f"this is No.{count},goodbye")
        break

    speed = float(user_input)
    status = check_speed(speed)

    if status == "too fast":
        print("you are overspeed,please reduce speed!")
    elif status == "minus":
        print("speed can not be minus,please input again!")
        continue
    else:
        rps = calc_rps(speed)
        print(f"your speed is {speed},your wheel rotation speed is {rps:.2f}!")
        count = count_add(count)