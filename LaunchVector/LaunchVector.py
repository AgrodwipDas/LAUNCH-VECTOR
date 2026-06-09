"""
This program calculates the maximum height, time of flight, and horizontal range of a rocket launched from a planet.
The user is prompted to enter the planet number (1 for Earth, 2 for Mars, 3 for Moon),
the initial velocity of the rocket in meters per second, and the angle of launch in degrees.
The program then uses the appropriate gravitational acceleration based on the selected planet to perform the calculations and outputs the results.
"""
print("===== LaunchVector =====")

import math

print("\nSelect Planet:")
print("1. Earth")
print("2. Mars")
print("3. Moon")

planet_choice = int(input("Choice: "))

initial_velocity = float(input("Enter the initial velocity of the rocket (in m/s): "))

angle_of_launch = float(input("Enter the angle of launch (in degrees): "))

# Convert angle from degrees to radians
angle_of_launch_rad = math.radians(angle_of_launch)
if planet_choice == 1:
    gravity = 9.81  # Gravity on Earth in m/s^2
    planet="Earth"
elif planet_choice == 2:
    gravity = 3.71  # Gravity on Mars in m/s^2
    planet="Mars"
elif planet_choice == 3:
    gravity = 1.62  # Gravity on Moon in m/s^2
    planet="Moon"
else:
    print("Invalid planet number. Please enter a number between 1 and 3.")
    exit()

if initial_velocity <= 0:
    print("Velocity must be positive.")
    exit()

if angle_of_launch <= 0 or angle_of_launch >= 90:
    print("Angle must be between 0 and 90 degrees.")
    exit()

# Calculate the maximum height of the rocket
max_height = (initial_velocity * math.sin(angle_of_launch_rad))**2 / (2 * gravity)

# Calculate the time of flight
time_of_flight = (2 * initial_velocity * math.sin(angle_of_launch_rad)) / gravity

# Calculate the horizontal range of the rocket
horizontal_range = (initial_velocity * math.cos(angle_of_launch_rad)) * time_of_flight

print(f"Planet: {planet}")
print(f"Maximum Height: {max_height:.2f} meters")
print(f"Time of Flight: {time_of_flight:.2f} seconds")
print(f"Horizontal Range: {horizontal_range:.2f} meters")