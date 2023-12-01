#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.robotics import DriveBase
from pybricks.nxtdevices import LightSensor
from pybricks.tools import wait

ev3 = EV3Brick()

sensorR = LightSensor(Port.S2)
sensorL = LightSensor(Port.S1)
sensorRE = LightSensor(Port.S4)
sensorLE = LightSensor(Port.S3)
# sensorB = LightSensor(Port.D)

left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
robot = DriveBase(
    left_motor, right_motor, wheel_diameter=55.5, axle_track=93
)  # mit übersetzung WD 277.5, ohne 55.5

# ambientS = 25
reflectionS = 5


while True:
    while (  # 0110
        sensorL.reflection() < reflectionS
        and sensorR.reflection() < reflectionS
        and sensorLE.reflection() > reflectionS  # white
        and sensorRE.reflection() > reflectionS  # white
    ):
        print("0110")
        robot.drive(-600, 0)  # Wenn auf Linie: Beide mittelsensoren schwarz

    while (  # 0010
        sensorL.reflection() > reflectionS
        and sensorR.reflection() < reflectionS
        # and sensorLE.reflection() > reflectionS
        # and sensorRE.reflection() > reflectionS
    ):  # r schwarz, l weiss, aussen weiss, kleine Kurve r
        print("0010")
        robot.drive(-500, -45)

    while (  # 0100
        sensorL.reflection() < reflectionS
        and sensorR.reflection() > reflectionS
        # and sensorLE.reflection() > reflectionS
        # and sensorRE.reflection() > reflectionS
    ):  # r weiss, l schwarz, aussen weiss, kleine Kurve l
        print("0100")
        robot.drive(-500, 45)

    if (  # 1000
        sensorL.reflection() > reflectionS
        and sensorR.reflection() > reflectionS
        and sensorLE.reflection() < reflectionS
        and sensorRE.reflection() > reflectionS
    ):  # mitte weiss, le schwarz, re weiss, aus der Bahn, Kurve links erfasst
        print("1000")
        while (  # 1000
            sensorL.reflection() > reflectionS
            and sensorR.reflection() > reflectionS
            and sensorLE.reflection() < reflectionS
            and sensorRE.reflection() > reflectionS
        ):  # mitte weiss, le schwarz, re weiss, aus der Bahn, Kurve links erfasst
            robot.drive(-200, 135)

    if (  # 0001
        sensorL.reflection() > reflectionS
        and sensorR.reflection() > reflectionS
        and sensorLE.reflection() > reflectionS
        and sensorRE.reflection() < reflectionS
    ):  # mitte weiss, re schwarz, le weiss, aus der Bahn, Kurve rechts erfasst
        print("0001")
        while (  # 0001
            sensorL.reflection() > reflectionS
            and sensorR.reflection() > reflectionS
            and sensorLE.reflection() > reflectionS
            and sensorRE.reflection() < reflectionS
        ):
            robot.drive(-200, -135)

    if (  # 0011
        sensorL.reflection() > reflectionS
        and sensorR.reflection() < reflectionS
        and sensorLE.reflection() > reflectionS
        and sensorRE.reflection() < reflectionS
    ):  # r / re schwarz, l / le weiss, scharfe Kurve r, keine Kreuzung
        print("0011")
        while (  # 0011
            sensorL.reflection() > reflectionS
            and sensorR.reflection() < reflectionS
            and sensorLE.reflection() > reflectionS
            and sensorRE.reflection() < reflectionS
        ):  # r / re schwarz, l / le weiss, scharfe Kurve r, keine Kreuzung
            robot.drive(0, -90)

    if (  # 1100
        sensorL.reflection() < reflectionS
        and sensorR.reflection() > reflectionS
        and sensorLE.reflection() < reflectionS
        and sensorRE.reflection() > reflectionS
    ):  # l / le schwarz, r / re weiss, scharfe Kurve r, keine Kreuzung
        print("1100")
        while (  # 1100
            sensorL.reflection() < reflectionS
            and sensorR.reflection() > reflectionS
            and sensorLE.reflection() < reflectionS
            and sensorRE.reflection() > reflectionS
        ):
            robot.drive(0, 90)

    if (  # 1111
        sensorL.reflection() < reflectionS
        and sensorR.reflection() < reflectionS
        and sensorLE.reflection() < reflectionS
        and sensorRE.reflection() < reflectionS
    ):
        robot.stop()
        robot.drive(-50, -180)
        wait(525)
