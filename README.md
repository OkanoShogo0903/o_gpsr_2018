# Speech Person Recognition 2018 in Canada
## Writter
1. Okano
2. Enomoto

## Use
~~~
1. Connect Realsence
$ roslaunch realsense realsense_r200_launch.launch

2. Human detector activate
$ cd ~/catkin_ws/src/e_human_detector/darknet
$ rosrun e_human_detector e_human_detector.py

3. 3D Rider activate
$ roslaunch turtlebot_bringup 3dsensor.launch

4. Base activate
$ roslaunch turtlebot_bringup minimal.launch

5. Command controler activate
$ cd ~/catkin_ws/src/CommandControler/scripts/
$ python CommandControler.py

6. Speech Recognition (Google Speech API)
$ python ~/catkin_ws/src/speech_recog/scripts/speech_recog_normal.py

7. Finally,execute GPSR
$ python ~/catkin_ws/src/tm_speech_person_recognition/scripts/gpsr.py
~~~
## Memo
~~~
Human detecter topic:  
$ rostopic pub /human_detect_req std_msgs/Bool "data: false"
~~~
