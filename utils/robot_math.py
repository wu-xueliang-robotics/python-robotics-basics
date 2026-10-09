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
    
def moving_average(data,window = 5):
    result = []
    for i in range(len(data) - window + 1):
        chunk = data[i:i + window]
        result.append(sum(chunk)/window)
    return result
