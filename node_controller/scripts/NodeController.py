#!/usr/bin/env python
# license removed for brevity


import rospy
#import rssi
#from rssi import RSSI_Scan #Imports the RSSI_scan class from the sibling rssi file
#from rssi import RSSI_Localizer



from WatchDog import watch_dog

from wifi_scan_py.msg import AddressRSSI
from wifi_scan_py.msg import Fingerprint


def watcher():

    
    rospy.init_node('Node_Controller_node', anonymous=True)

    camera_watch_dog = watch_dog('/home/pi/catkin_ws/src/wifi_scan_pub/launch/', 'wifi_fp.launch', 10)
    rospy.Subscriber("wifi_fp", Fingerprint, camera_watch_dog.callback)
    rospy.on_shutdown(camera_watch_dog.terminate_node)
    rospy.spin()


if __name__ == '__main__':
    try:
        watcher()
    except rospy.ROSInterruptException:
        pass

