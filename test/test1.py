#フレームワーク(土台)と第一関節のテスト

import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

print("start pca9685")

pwm.set_pwm(0, 0, 150)
time.sleep(1)
pwm.set_pwm(0, 0, 600)
time.sleep(1)
pwm.set_pwm(0, 0, 150)
time.sleep(1)
