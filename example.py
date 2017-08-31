#!/usr/bin/env python2
import rospy
from std_msgs.msg import Int16

class Simple_s_p:
	def __init__(self):
		self.pub_steering = rospy.Publisher("/manual_control/steering", Int16, queue_size=100, latch = True)
		self.vel = rospy.Subscriber("/manual_control/speed", Int16, self.callback_speed, queue_size = 100, buff_size=2 ** 24)
		self.speed = 0

	def callback_speed(self, lectura):
		self.speed = lectura.data

	def publish(self):
		direccion = Int16()
		#Calculo
		if self.speed>0:
			direccion.data = 180
		else:
			direccion.data = 0
		self.pub_steering.publish(direccion)   #Cuando vaya a una velocidad positiva vaya a 180, negativa este en 0


def main():
	rospy.init_node('ws_2017')
	Autonomo = Simple_s_p()
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		Autonomo.publish()
		rate.sleep()
		print (Autonomo.speed)


if __name__ == '__main__' :
	main()
