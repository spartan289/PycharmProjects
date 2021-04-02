#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self,speed,type):
        self.speed = speed
        self.type = type
    def __str__(self):
        string="Car with the maximum speed of {} {}"
        return string.format(self.speed,self.type)
class Boat:
    def __init__(self,speed):
        self.speed=speed
    def __str__(self):
        string="Boot with the maximum speed of {} knots"
        return string.format(self.speed)


if __name__ == '__main__':
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
