#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
from goto import move_to

class positioning:
    def __init__(self):
        rospy.Subscriber('/heard', Int16, self.robotcall)
        rospy.Subscriber('/current_pos', Int16, self.position)
        rospy.Subscriber('/tables', Int16MultiArray, self.gettable)
        move_to(0)                              # While starting, robot is taken to Home position
        self.pos = 0

    def position(self,pos):
        self.pos = pos
        while not rospy.is_shutdown():
            if self.pos == 0:                   # Home (value musr be taken by localization)
                listen_to.publish(1)            # Listening for the call from Home
                if self.heard == 0:             # Heard robot call
                    move_to(4)                  # Moving towards the kitchen
            elif self.pos == 4:                 # Kitchen (value must be taken by localization)
                listen_to.publish(2)            # Listening for the table num from the Kitchen
                if self.heard == 1:             # Heard table numbers
                    for i in self.tablenum:
                        move_to(i)              # moving to every table
                    move_to(4)                  # once completed, moving back to kitchen
                    move_to(0)                  # finally, to the home position
                elif self.heard == 2:           # Heard Nothing
                    move_to(0)                  # Timeout, going back to Home


    def robotcall(self,value):
        self.heard = value

    def gettable(self,num):
        self.tablenum = num.data

if __name__ == '__main__':
    try:
        rospy.init_node('control_node', anonymous=True)
        print("Started the Controller Node")
        listen_to = rospy.Publisher('/listento', Int16, queue_size=10)
        positioning()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass