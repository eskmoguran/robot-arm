#ロボットアームの実験機Mark001です

import time
import Adafruit_PCA9685
import configparser
import sys

class Mark001:

	def __init__(self):
		#設定ファイルより各関節の現在位置を取得する
		self.config = configparser.ConfigParser()
		self.config.read("./config/position.conf","UTF-8")
		self.channel00 = self.config.get("channel0","now")
		self.channel01 = self.config.get("channel1","now")
		self.channel02 = self.config.get("channel2","now")

		#PCA9685ドライブを準備する
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(60)

	def readConfigFile(self,channel):
		#現在位置の読み込み
		return int(self.config.get(channel,"now"))

	def writeConfigFile(self,value,channel):
		#現在位置の書き込み
		self.config.set(channel,"now",str(value))
		with open("./config/position.conf","w") as configfile:
			self.config.write(configfile)

	def angleDecomposition(self,angle):
		#90度=375 0度=150 180度=600
		#1度あたり2.5
		#例: angle=60 150+60x2.5=300
		value = 150+int(angle)*2.5
		return value

	def selectChannel(self,channel):
		#チャンネルの実際の番号(整数)を返します
		if channel == "channel0":
			result = 0
		elif channel == "channel1":
			result = 1
		else:
			result = 2
		return result


	def moveServo(self,angle,channel):
		#実際にサーボモータを動かします
		print("サーボモータを動かします")
		servo = self.selectChannel(channel)
		value = self.readConfigFile(channel)
		if self.readConfigFile(channel) < self.angleDecomposition(angle):
			for i in range(int((self.angleDecomposition(angle)-self.readConfigFile(channel))/2)):
				value += 2
				self.pwm.set_pwm(servo,0,value)
				i += 1
				time.sleep(0.002)
		else:
			for i in range(int((self.readConfigFile(channel)-self.angleDecomposition(angle))/2)):
				value -= 2
				self.pwm.set_pwm(servo,0,value)
				i += 1
				time.sleep(0.002)
		print("現在位置を記録しています:"+str(self.angleDecomposition(angle)))
		self.writeConfigFile(int(self.angleDecomposition(angle)),channel)

if __name__ == "__main__":
	mark = Mark001()
	while True:
		print("動かしたいサーボモータのチャンネルを選択してください")
		print("channel0,channel1,channel2")
		print("channel: ")
		channel = input()
		print("channel0の角度を入力してください")
		print("0-180度で入力してください")
		print("angle: ")
		angle = input()
		if angle == "stop":
			break
		elif 0<=int(angle) and int(angle)<=180:
			mark.moveServo(int(angle),str(channel))
			print(type(angle))
		else:
			print("角度を入力するか、stopで終了してください")
