

class Car:
    def __init__(self, owner="", cur_speed=0, dist=0, trip_time=0, max_speed=0):
        self.speeds = []
        self.MAX = 100
        self.acceleration = 5
        self.deceleration = 5
        self.set_owner(owner)
        self.set_current_speed(cur_speed)
        self.set_distance_traveled(dist)
        self.set_trip_time(trip_time)
        self.set_max_speed(max_speed)

    def move(self):
        self.set_distance_traveled(self.get_distance_traveled() + 1)
        self.set_trip_time((self.trip_time + 60) / self.get_current_speed())

    def accelerate(self, iteration):
        self.set_current_speed(iteration * self.get_acceleration())
        if self.get_current_speed() >= self.get_MAX():
            self.set_current_speed(self.get_MAX())

    def brake(self):
        self.set_current_speed(self.get_current_speed() - self.get_deceleration())

    def get_avg_speed(self):
        return sum(self.get_speeds()) / len(self.get_speeds())

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    def set_deceleration(self, deceleration):
        self.deceleration = deceleration

    def set_owner(self, owner):
        self.owner = owner

    def set_current_speed(self, speed):
        self.current_speed = speed
        self.speeds.append(speed)

    def set_distance_traveled(self, distance):
        self.distance_traveled = distance

    def set_trip_time(self, time):
        self.trip_time = time

    def set_max_speed(self, speed):
        self.max_speed = speed

    def get_MAX(self):
        return self.MAX

    def get_acceleration(self):
        return self.acceleration

    def get_deceleration(self):
        return self.deceleration

    def get_owner(self):
        return self.owner

    def get_current_speed(self):
        return self.current_speed

    def get_distance_traveled(self):
        return self.distance_traveled

    def get_trip_time(self):
        return self.trip_time

    def get_max_speed(self):
        return self.max_speed

    def get_speeds(self):
        return self.speeds

    def __str__(self):
        return f"""Car Description:
                 Owner:          {self.get_owner()}
                 Current Speed:  {self.get_current_speed()}
                 Distance:       {self.get_distance_traveled()}
                 Time:           {self.get_trip_time()}
                 Max Speed:      {self.get_max_speed()}
                 Avg Speed:      {self.get_avg_speed()}"""
