# encoding=utf-8
#!/env/bin python3
import os
import time
import math

import RPi.GPIO as GPIO

import control_utils
if __name__ == '__main__':
    conf_filename = 'l298_pin.txt'
    assert os.path.exists(conf_filename)

    l298_pins = open(conf_filename, encoding='utf-8').read().splitlines()

    print(type(l298_pins), l298_pins)

    l298_pins = list(map(lambda x: int(x), l298_pins))

    print(type(l298_pins), l298_pins)

    in1, in2, in3, in4 = l298_pins[:4]

    GPIO.setmode(GPIO.BCM)

    l298_driver = control_utils.L298N(in1, in2, in3, in4)

    l298_driver.forward()

    time.sleep(5)

    l298_driver.left()

    time.sleep(5)

    GPIO.cleanup()
