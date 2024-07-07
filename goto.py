#!/usr/bin/env python3

import rospy

positions = {"0" : "12,56",     # 0 for Home position
            "1" : "53,87",      # 1 for Table 1's position
            "2" : "123,98",     # 2 for Table 2's position
            "3" : "466,234",    # 3 for Table 3's position
            "4" : "765,459"}    # 4 for the Kitchen's position

def move_to(num):
    pos = positions[str(num)]
    # Navigation stack and path planning package can be called here with goal as "pos".
    # Ros actions can be implemented for closed Feedback.

    if "Cancel is Triggered":
        exit()


if __name__ == '__main__':
    try:

        rospy.init_node('navigation_node', anonymous=True)
        print("Started the Navigation Node")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
