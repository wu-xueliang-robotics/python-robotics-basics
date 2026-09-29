wheel_radius = 0.15
circle = 2 * 3.14 * wheel_radius
count = 0

while True:
    user_input = input(f"please input speed (m/s),input q will break")

    if user_input == "q":
        print(f"this calculate to No.{count},goodbye!")
        break
    speed = float(user_input)

    if speed > 5:
        print("your speed is too fast,warning!")
    elif speed < 0:
        print("speed is minus,error!")
        continue
    else:
        rps = speed/circle
        print(f"speed is {speed},wheel rotation speed is {rps:.2f}")
    count = count + 1