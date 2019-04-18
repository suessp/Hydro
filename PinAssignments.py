import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#pins for all system peripherals

#Water Control
mainpump = 13
solnd1 = 16
solnd2 = 17

#Nutrient Autodoser
doser1 = 19
doser2 = 20
doser3 = 21
doser4 = 22
doser5 = 23
airpump = 24

#EC/PH switch
ch1 = 25
ch2 = 26

#ADC
adcCLK = 11
adcDout = 9
adcDin = 10
adcCS = 8

#Flow Sensors
flow1 = 12
flow2 = 6

#Level Sensor
trig = 4
echo = 5

#LCD i2c pins
sda1 = 2
scl1 = 3
