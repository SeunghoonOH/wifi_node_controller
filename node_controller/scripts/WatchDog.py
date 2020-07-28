
import threading
import time
import roslaunch
import rospy
#from std_msgs.msg import string

class watch_dog:
    def __init__(self, path, file, watch_time = 5):
        self.launch_node_launched = False
        self.launch_node = None
        self.launch_file = path + file
        self.watch_time = watch_time
        self.timer = None 
        self.uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        print(self.launch_file )
        self.a_launch_node()

    def a_launch_node(self):
        if self.launch_node_launched == False:
         #   roslaunch.configure_logging(self.uuid)
            self.launch_node = roslaunch.scriptapi.ROSLaunch()
            self.launch_node = roslaunch.parent.ROSLaunchParent(self.uuid, [self.launch_file])
            self.launch_node_launched = True
            self.launch_node.start()
        rospy.loginfo("node_start")

    def kill_node(self):
        if self.launch_node_launched == True:
            self.launch_node_launched = False
            self.launch_node.shutdown()

    def terminate_node(self):
        rospy.loginfo("close_node")
        self.launch_node.shutdown()


    def callback(self, data):
        print("watch_dog_callback")
        self.watch_node()


    def watch_node(self):
        if (self.timer is None) == False:
            self.timer.cancel()

        self.timer = threading.Timer(self.watch_time, self.timeout)
        self.timer.start()      


    def timeout(self):
        self.kill_node()
        time.sleep(0.5)
        rospy.loginfo("node_restart")
        self.a_launch_node()
