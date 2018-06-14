# GPSR 2018 in Canada
## Overview
ロボカップ@homeのGPSRタスクのためのpythonスクリプト。  
人から口頭で指示され、物を運んだり、人に情報を伝えたりするなど、  
とても複雑な動作が求められるタスクです。

## Writter
1. Okano
2. Enomoto

--------------------------------------
# :triangular_flag_on_post::triangular_flag_on_post::triangular_flag_on_post:大会チェックリスト:triangular_flag_on_post::triangular_flag_on_post::triangular_flag_on_post:
## ハードウェア
- [ ] USE+イヤホンジャックが刺さっているかを確認
- [ ] 緊急停止スイッチOFF
- [ ] PC起動後にスピーカーの電源ON(**青く光っているか**)
- [ ] スピーカーはしっかりと接触しているか
- [ ] 設定->サウンド->入力装置->内部オーディオを消音にし、MobilePreをONにする
- [ ] MobilePreマイクに触れて、動作していることを確認する
- [ ] 音声の出力をunavailableにする
- [ ] $ sh mic_check.sh(一度エラーが起こる)
- [ ] $ 機体のスイッチをONにする
- [ ] 充電器を抜く
## ソフトウェア
- [ ] Command controler起動
```
$ cd ~/catkin_ws/src/CommandControler/scripts/
$ python CommandControler.py
```
- [ ] ブラウザを開いて、インターネットに繋がっているか確認
- [ ] Speech recognition起動(Google Speech API)
```
$ python ~/catkin_ws/src/speech_recog/scripts/speech_recog_normal.py
```
- [ ] gpsrのマスターを起動
```
$ python ~/catkin_ws/src/tm_speech_person_recognition/scripts/gpsr.py
```

---------------------------------------------------------------------------
## HotReference:fire:
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
