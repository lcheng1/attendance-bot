import time
from adafruit_motorkit import MotorKit

# Inherited by robot to control over tracks
class Robot_Control:
	# MotorKit initializations
	straight_val = 0.4
	kit = MotorKit()
	left_wheel = kit.motor2
	right_wheel = kit.motor1
	left_throttle = 0
	right_throttle = 0

	# Movement functions
	def goStraight(self):
		self._setLeft(self.straight_val)
		self._setRight(-1 * self.straight_val)

	def goBack(self):
		self._setLeft(-1 * self.straight_val)
		self._setRight(self.straight_val)

	def stop(self):
		self._setLeft(0)
		self._setRight(0)
	
	# Helper function to change the speed
	def changeSpeed(self, speed = 0.4):
		if speed >= 0 and speed <=0.8:
			Robot_Control.straight_val = speed

	# Helper function to change the left motor
	def _setLeft(self, val):
		try:
			if val != self.left_wheel.throttle:
				self.left_wheel.throttle = val
				Robot_Control.left_throttle = self.left_wheel.throttle
		except:
			pass

	# Helper function to change the right motor
	def _setRight(self, val):
		try:
			if val != self.right_wheel.throttle:
				self.right_wheel.throttle = val
				Robot_Control.right_throttle = self.right_wheel.throttle
		except:
			pass

