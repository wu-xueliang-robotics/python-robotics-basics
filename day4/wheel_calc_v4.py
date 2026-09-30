from robot_math import calc_rps,check_speed

count = 0
while True:
    user_input = input("please input speed :   ,input q will break")

    if user_input == "q":
        print(f"this is No.{count},goodbye")
        break

    try:
        speed = float(user_input)
    except ValueError:
        print("your input is error,please input again!")
        continue

    status = check_speed(speed)

    if status == "too fast":
        print("you are overspeed,please reduce speed!")
    elif status == "minus":
        print("speed can not be minus,please input again!")
        continue
    else:
        rps = calc_rps(speed)
        print(f"your speed is {speed},your wheel rotation speed is {rps:.2f}!")
        count = count + 1
        with open("calc_log.txt","a")as f:
            f.write(f"{speed}m/s -> {rps:.2f}rps/s\n")