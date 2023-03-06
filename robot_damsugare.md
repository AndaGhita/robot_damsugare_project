# Robot Damsugare Project
~~ Roboten ska navigera genom att mäta avstånd till olika föremål i rummet  ~~

## Funktion som omvandlar från tiden vi mätt upp till avstånd: 
``` python
  # Constants. 
 SPEED_OF_lIGHT = 299792458
 
 Calculates distance to object from measured time
    s = c * t / 2 
    s: distance (sträcka)
    c: speed of light, constant 
    t: measured time 
def time_to_distance(time: float):
    s = (time * SPEED_OF_LIGHT) / 2
    return s

 #Short test. Assume 20 ns (nanoseconds) = 2.0 × 10^-8 s 
laserTimeMeasurement = 0.00000002
print(f"Measured distance: {time_to_distance(laserTimeMeasurement)} m")
```

## Omvandling från A/D värde -> nanosekunder -> sekunder

The A/D clock frequency is set to 40 MHz (40,000,000 Hz) and the A/D resolution is set to 2 bytes.Can adjust these constants to match the specifications of your A/D converter. The ad_to_time function takes an A/D value as input and returns the corresponding time in seconds.

```python
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
```

## Givet vinkel av mätningen, var befinner sig objektet? Inte bara avstånd utan x,y-koordinater
* Robotens rotation
* Mätningens vinkel

Roboten vara placerad vid (0, 0) och  roboten pekar i riktning mot 45 grader (pi/4 radianer). calculate_coordinates-funktionen tar avståndet till objektet (i meter) och vinkeln på mätningen (i radianer) och returnerar x- och y-koordinaterna för objektet relativt roboten.

```python
import math

# Constants.
SPEED_OF_LIGHT = 299792458

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

```


