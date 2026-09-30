def calc_rps(speed,radius = 0.15):
    circle = 2 * 2.14159 * radius
    return speed / circle

def check_speed(speed):
    if speed > 5:
        return "too fast"
    elif speed < 0:
        return "minus"
    else:
        return "safety"