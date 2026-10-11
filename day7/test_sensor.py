class Sensor:
    def __init__ (self, name):
        self.name = name

    def read(self):
        return "reading..."

class CameraSensor(Sensor):
    def __init__(self, name, resolution):
        super().__init__(name)
        self.resolution = resolution

    def read(self):
        return f"彩色图像{self.resolution}"

class LidarSensor(Sensor):
    def __init__(self, name, channels):
        super().__init__(name)
        self.channels = channels

    def read(self):
        return f"点云{self.channels}"
        
sensor = [Sensor("Sony"), CameraSensor("Leica","photo"), LidarSensor("ray",78)]
for k in sensor:
    print(k.name,"->",k.read())
