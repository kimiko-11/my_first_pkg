#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller')
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)  # 10Hz
        self.twist = Twist()

    def move_forward(self):
        self.twist.linear.x = 1.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

    def turn_left(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 1.0
        self.pub.publish(self.twist)

    def run(self):
        while not rospy.is_shutdown():
            print("1: Move Forward")
            print("2: Turn Left")
            print("3: Exit")
            choice = input("Select an option: ")
            
            if choice == '1':
                self.move_forward()
            elif choice == '2':
                self.turn_left()
            elif choice == '3':
                break
                
            self.rate.sleep()

if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.run()
    except rospy.ROSInterruptException:
        pass
