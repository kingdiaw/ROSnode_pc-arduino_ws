# ROSnode Running on PC Host
#### Step 1: create and build a catkin workspace:
```
$ mkdir -p ~/rosnode_pc-arduino_ws/src
$ cd ~/rosnode_pc-arduino_ws
$ catkin_make
$ catkin_make install
```
#### Step 2: Clone catkin package
```
$ cd ~/rosnode_pc-arduino_ws/src
$ git clone https://github.com/kingdiaw/rospkg_pc-arduino.git
```
#### Step 3: Open a new terminal and run roscore
```$ roscore```

#### Step 4: Building a catkin workspace and sourcing the setup file
Open a new terminal and run following commands:
```
$ cd ~/rosnode_pc-arduino_ws
$ catkin_make
$ source devel/setup.bash
$ rosrun  rospkg_pc-arduino publisher_node.py
```
#### Step 5:Building a catkin workspace and sourcing the setup file
Open a new terminal and run following commands:
```
$ cd ~/rosnode_pc-arduino_ws
$ catkin_make
$ source devel/setup.bash
$ rosrun  rospkg_pc-arduino subscriber_node.py
```


