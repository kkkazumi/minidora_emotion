from __future__ import division
import time
import pygame.mixer

import Adafruit_PCA9685
import DRV8830

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
drv8830 = DRV8830.DRV8830()

pygame.mixer.init()

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_center = int((600-150)/2)
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)


def move_dora(action_num):
    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

    time.sleep(3)

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    #while True:
    #pygame.mixer.music.play(1)
    speed = 25
    drv8830.drive(1,speed)
    drv8830.drive(0,speed)
    time.sleep(1.2)
    drv8830.drive(1,-speed)
    drv8830.drive(0,-speed)
    time.sleep(0.15)
    drv8830.drive(1,0)
    drv8830.drive(0,0)
        
    # Move servo on channel O between extremes.

    #pwm.set_pwm(1, 0, 300)

    if action_num==0:
        pygame.mixer.music.load("n1.wav")
        pygame.mixer.music.play(1)
        pwm.set_pwm(14, 0, servo_min)
        pwm.set_pwm(15, 0, servo_max)
        time.sleep(2)

        drv8830.drive(1,0)
        drv8830.drive(0,0)
        pwm.set_pwm(0, 0, 350)
        pwm.set_pwm(14, 0, servo_max)
        pwm.set_pwm(15, 0, servo_min)
        time.sleep(1)
    elif action_num==1:
        pygame.mixer.music.load("y2.wav")
        pygame.mixer.music.play(1)
        pwm.set_pwm(14, 0, servo_min)
        time.sleep(2)
        drv8830.drive(1,0)
        drv8830.drive(0,0)
        pwm.set_pwm(0, 0, 350)
        pwm.set_pwm(14, 0, servo_max)
        time.sleep(1)
    elif action_num==2:
        pygame.mixer.music.load("w1.wav")
        pygame.mixer.music.play(1)
        pwm.set_pwm(15, 0, servo_max)
        time.sleep(2)
        drv8830.drive(1,0)
        drv8830.drive(0,0)
        pwm.set_pwm(0, 0, 350)
        pwm.set_pwm(15, 0, servo_min)
        time.sleep(1)
    elif action_num==3:
        pygame.mixer.music.load("y4.wav")
        pygame.mixer.music.play(1)
        pwm.set_pwm(14, 0, servo_min)
        time.sleep(2)

        drv8830.drive(1,0)
        drv8830.drive(0,0)
        pwm.set_pwm(0, 0, 350)
        pwm.set_pwm(14, 0, servo_max)
        pwm.set_pwm(15, 0, servo_max)
        time.sleep(1)

        drv8830.drive(1,0)
        drv8830.drive(0,0)
        pwm.set_pwm(0, 0, 350)
        pwm.set_pwm(15, 0, servo_min)

    for nth in range(16):
        pwm.set_pwm(nth, 0, 0)

if __name__ == '__main__':
    move_dora(0)
    move_dora(1)
    move_dora(2)
    move_dora(3)

