#掴む所のテスト

import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

print("start pca9685")

#pwm.set_pwm(0, 0, 375)=90度
#pwm.set_pwm(0, 0, 150)=0度

pwm.set_pwm(0, 0, 375)
time.sleep(1)
pwm.set_pwm(0, 0, 150)
time.sleep(1)
pwm.set_pwm(0, 0, 375)
time.sleep(1)
pwm.set_pwm(0, 0, 150)
time.sleep(1)
