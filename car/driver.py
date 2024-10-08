from main import Car


def main():
    take_a_trip()


def get_to_speed(car, speed):
    # Delete pass and add your code
    loop = int(car.get_current_speed() / car.get_acceleration()) + 1
    for i in range(loop):
        car.accelerate(i)


def go_x_miles(car, distance):
    # Delete pass and add your code
    for i in range(distance):
        car.move()


def brake_to_speed(car, speed):
    # Delete pass and add your code
    loopNum = int((car.current_speed - speed) / car.deceleration)
    for i in range(loopNum):
        car.brake(i)


def take_a_trip():
    # Start the simulation
    print("\n***** Starting Simulation *****\n")
    owner = input("\tWhat is your name? ")
    max = float(input("\tWhat is the max speed of your car (in MPH)? "))
    print("\n***** Creating Car for " + owner + " *****\n")
    c1 = Car(owner=owner, max_speed=max)

    # Accelerate to speed
    speed = float(input("\tWhat speed do you want to accelerate to (in MPH)? "))
    print("\n***** Accelerating To " + str(speed) + " MPH *****\n")
    get_to_speed(c1, speed)

    # Drive a distance
    d1 = int(input("\tHow far do you want to go (in Miles)? "))
    print("\n***** Driving " + str(d1) + " Miles *****\n")
    go_x_miles(c1, d1)

    # Slow down
    brake_speed = float(input("\tWhat speed would you like to brake to (in MPH)? "))
    print("\n***** Decelerating To " + str(brake_speed) + " MPH *****\n")
    brake_to_speed(c1, brake_speed)

    # Drive a bit further
    d2 = int(input("\tHow far would you like to go at this speed (in Miles)? "))
    print("\n***** Driving " + str(d2) + " Miles *****\n")
    go_x_miles(c1, d2)

    # End trip
    print("***** Trip Over! Braking to Zero MPH *****")
    brake_to_speed(c1, 0)

    # Print Trip Summary
    print("\nTRIP SUMMARY:\n")
    print(c1)


if __name__ == "__main__":
    main()
