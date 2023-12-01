#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port

# Initialize the EV3 brick
ev3 = EV3Brick()

# Connect the NXT Light Sensor to Port 3
light_sensorRE = LightSensor(Port.S2)
light_sensorLE = LightSensor(Port.S1)
# Activate the sensor
# light_sensorRE.activate(True)
# light_sensorLE.activate(True)
while True:
    # Read ambient light intensity
    ambient_intensityRE = light_sensorRE.ambient()
    ambient_intensityLE = light_sensorLE.ambient()
    # print(ambient_intensityLE, ambient_intensityRE)

    # Read reflection intensity
    reflection_intensityRE = light_sensorRE.reflection()
    reflection_intensityLE = light_sensorLE.reflection()
    print(
        reflection_intensityLE,
        reflection_intensityRE,
        ambient_intensityLE,
        ambient_intensityRE,
    )
