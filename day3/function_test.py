def calc_rps(speed,radius = 0.15):
    circle = 2 *3.14159 * radius
    return speed / circle

result = calc_rps(4)
print(f"wheel speed is {result:.2f}")