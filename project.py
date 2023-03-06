import math

# Constants. (Python har inte konstanter, konvention att använda versaler för konstanter)
SPEED_OF_LIGHT = 299792458

""" Calculates distance to object from measured time
    s = c * t / 2
    s: distance (sträcka)
    c: speed of light, constant
    t: measured time
"""
def time_to_distance(time: float):
    s = (time * SPEED_OF_LIGHT) / 2
    return s

# Short test. Assume 20 ns (nanoseconds) = 2.0 × 10^-8 s
laserTimeMeasurement = 0.00000002
print(f"Measured distance: {time_to_distance(laserTimeMeasurement)} m")

# Constants
A_D_CLOCK_FREQUENCY = 40000000  # Hz
A_D_RESOLUTION = 2  # Bytes

""" Converts A/D value to seconds
    t = (value * resolution) / clockFrequency
    t: time in seconds
    value: A/D value
"""
def ad_to_time(value: int):
    t = (value * A_D_RESOLUTION) / A_D_CLOCK_FREQUENCY
    return t

# Short test. Assume A/D value is 500
adValue = 500
print(f"Time in seconds: {ad_to_time(adValue)} s")

# Robot position and orientation.
robot_x = 0.0
robot_y = 0.0
robot_theta = math.pi/4  # 45 degrees in radians

# Convert time to distance.
def time_to_distance(time: float):
    return (time * SPEED_OF_LIGHT) / 2

# Calculate x and y coordinates of object.
def calculate_coordinates(distance: float, angle: float):
    x = robot_x + distance * math.cos(robot_theta + angle)
    y = robot_y + distance * math.sin(robot_theta + angle)
    return (x, y)

# Example usage.
laserTimeMeasurement = 0.00000002  # 20 ns
distance = time_to_distance(laserTimeMeasurement)
angle = math.pi/6  # 30 degrees in radians
x, y = calculate_coordinates(distance, angle)
print(f"Object coordinates: ({x}, {y})")