#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
msg=0
def pub_func():
    global msg
    pub=rospy.Publisher('toggle_led',UInt16,queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(5)
    rospy.loginfo("Publisher node started, now publishing messages")
    while not rospy.is_shutdown():
        if msg == 0:
            msg = 1
        else:
            msg = 0
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_func()
    except rospy.ROSInterruptException:
        pass