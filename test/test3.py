#複数のサーボをゆっくり動かすテスト

import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

print("start pca9685")

value = 150

for i in range(225):
	value += 2
	pwm.set_pwm(0, 0, value)
	pwm.set_pwm(1, 0, value)
	pwm.set_pwm(2, 0, value)
	pwm.set_pwm(3, 0, value)
	pwm.set_pwm(4, 0, value)
	i += 2
	time.sleep(0.002)

for i in range(225):
	value -= 2
	pwm.set_pwm(0, 0, value)
	pwm.set_pwm(1, 0, value)
	pwm.set_pwm(2, 0, value)
	pwm.set_pwm(3, 0, value)
	pwm.set_pwm(4, 0, value)
	i -= 2
	time.sleep(0.002)
for i in range(225):
	value += 2
	pwm.set_pwm(0, 0, value)
	pwm.set_pwm(1, 0, value)
	pwm.set_pwm(2, 0, value)
	pwm.set_pwm(3, 0, value)
	pwm.set_pwm(4, 0, value)
	i += 2
	time.sleep(0.002)
