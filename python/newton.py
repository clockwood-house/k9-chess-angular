# -*- coding: utf-8 -*-
#
# Tune the dog's movement
#
# authored by Richard Hopkins March 2019
#
# Licensed under The Unlicense, so free for public domain use
#
# This program moves K9 in a straight line and measures the result

import math
import time
from roboclaw import Roboclaw
rc = Roboclaw("/dev/roboclaw", 115200)
rc.Open()
rc_address = 0x80
m1_qpps = 1570
m2_qpps = 1138
acceleration = 25
speed = 50
distance = 152
# Get roboclaw version to test if is attached
version = rc.ReadVersion(rc_address)
# Set PID variables to those required by K9
rc.SetM1VelocityPID(rc_address, 6.04, 1.55, 0, m1_qpps)
rc.SetM2VelocityPID(rc_address, 6.63, 2.11, 0, m2_qpps)
# Zero the motor encoders
rc.ResetEncoders(rc_address)


def displayspeed():
    enc1 = rc.ReadEncM1(rc_address)
    enc2 = rc.ReadEncM2(rc_address)
    speed1 = rc.ReadSpeedM1(rc_address)
    speed2 = rc.ReadSpeedM2(rc_address)
    print str(time.time() - base_time) + ",",
    if(enc1[0] == 1):
        print str(enc1[1]) + ",",
    else:
        print "failed",
    if(enc2[0] == 1):
        print str(enc2[1]) + ",",
    else:
        print "failed ",
    if(speed1[0]):
        print str(speed1[1]) + ",",
    else:
        print "failed",
    if(speed2[0]):
        print str(speed2[1])
    else:
        print "failed "


base_time = time.time()
rc.SpeedAccelDistanceM1M2(address=rc_address,
                          accel=int(acceleration),
                          speed1=int(speed),
                          distance1=int(distance),
                          speed2=int(speed),
                          distance2=int(distance),
                          buffer=int(1))
print "=== accelerate command issued ==="
rc.SpeedAccelDistanceM1M2(address=rc_address,
                          accel=int(655360),
                          speed1=int(0),
                          distance1=int(0),
                          speed2=int(0),
                          distance2=int(0),
                          buffer=int(0))
print "=== decelarate command issued ==="
buffers = (0, 0, 0)
while(buffers[1] != 0x80 and buffers[2] != 0x80):
    displayspeed()
    buffers = rc.ReadBuffers(rc_address)
    # time.sleep(0.01)
print "=== all commands complete =="

rc.ForwardBackwardM1(rc_address, 64)  # Stopped
rc.ForwardBackwardM2(rc_address, 64)  # Stopped

count = 0
while (count < 50):
    displayspeed()
    time.sleep(0.01)
    count += 1

print '=== experiment finished ==='
