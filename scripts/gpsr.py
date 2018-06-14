#!/usr/bin/env python
# -*- coding: utf-8 -*

import rospy
import time
from std_msgs.msg import String, Float64,Bool
import subprocess
from geometry_msgs.msg import Twist

class GeneralPurposeServiceRobot:
    def __init__(self):
        # Subuscriver----->
        self.speech_word_sub = rospy.Subscriber('/voice_recog',String,self.recogVoiceWordCB)
        self.riddle_req_sub = rospy.Subscriber('/riddle_res/is_action_result',Bool,self.setIsActionSuccessCB)

        # Publisher------->
        self.speech_req_pub = rospy.Publisher('/speech/is_active',Bool,queue_size=1)
        self.task_pub = rospy.Publisher('/riddle_req/question_word',String,queue_size=1)
        self.head_angle_pub = rospy.Publisher('/m6_controller/command',Float64,queue_size=1)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel_mux/input/teleop',Twist,queue_size=1)

        self.recog_word = ''
        self.is_action_result = None # Success -> True, Failure -> False, No input -> None
        self.is_do_not_send_command = False

    # CallBack Functions ---------------->

    def recogVoiceWordCB(self,sentence):
        ''' receive result word in speech_recog/scripts/speech_recog_normal.py '''
        if main_state == 1: # do not speak when robot move
            if self.is_do_not_send_command == False:
                print "Q : " + sentence.data
                #self.recog_word = sentence
                self.task_pub.publish(sentence.data)
                print "send riddle request."
    

    def setIsActionSuccessCB(self,is_complete):
        ''' receive message CommandControl/scripts/CommandControl.py '''
        import types
        print "success : " + str(is_complete.data)
        self.is_action_result = is_complete.data


    # Move Function ------------------->

    def rotateBase(self,angle):
        rotate_cmd = Twist()
        for i in range(angle):
            c = float(angle)
            rotate_cmd.angular.z = (c/2-abs(c/2-i))/c*4.0+0.3
            print rotate_cmd.angular.z
            self.cmd_vel_pub.publish(rotate_cmd)
            rospy.sleep(0.035)


    def speak(self,sentence):
        try:
            voice_cmd = '/usr/bin/picospeaker %s' %sentence
            subprocess.call(voice_cmd.strip().split(' '))
            print "[PICO] " + sentence
        except OSError:
            print "[PICO] Speacker is not activate. Or not installed picospeaker."


    def sound(self):
        try:
            sound_cmd = 'aplay se_maoudamashii_system27.wav'
            subprocess.call(sound_cmd.strip().split(' '))
            print "[SOUND] Playback system sound."
            rospy.sleep(2.0)
        except OSError:
            print "[SOUND] Playback Failed."


    def startGPSR(self):#-----------------state 0
        '''
            Writter: enomoto
            Move from the entrance to the decided place.
        '''
        print 'state : 0'
        '''
        navigation_req = String()
        navigation_req.data = 'hoge' # <--- Please fix it.
        self.navigation_req_pub.publish
        '''
        return 1 #next state


    def doGivenTask(self):#----------state 1
        ''' 
            Writter: okano
        '''
        print 'state : 1'
        self.speak("I'm ready")
        rospy.sleep(3.0)
        self.speak("Let give me a task")
        rospy.sleep(3.0)
        self.speak("Please speak after the signal")
        time.sleep(3.0)
        self.sound()
        #self.speech_req_pub.Publish(True) # start GoogleSpeechAPI

        # loop 3 times
        TASK_LIMIT = 3
        reply = 0
        failure = 0
        while reply < TASK_LIMIT:
            if self.is_action_result != None:
                self.is_do_not_send_command = True
                print "count : " + str(reply)
                rospy.sleep(1.0) # wait rotate

                if self.is_action_result is True: # Action success.
                    failure = 0
                    reply += 1
                else: # Action failure.
                    failure += 1
                    if failure == 2:
                        failure = 0
                        reply += 1

                if reply != TASK_LIMIT: # sound
                    rospy.sleep(2.0)
                    self.sound()
                self.is_action_result = None
                self.is_do_not_send_command = False
        return 2 # next state


    def leaveArena(self):#---------------state 2
        ''' 
            Writter: enomoto
        '''
        print 'state : 2'
        self.speak("I did all tasks")
        time.sleep(1.5)
        self.speak("I will go to the entrance")
        time.sleep(1.5)
        '''
        navigation_req = String()
        navigation_req.data = 'entrance'
        self.navigation_req_pub.publish
        '''

        return -1 # end


if __name__ == '__main__':
    rospy.init_node('o_gpsr_2018')
    time.sleep(3.0)
    gpsr = GeneralPurposeServiceRobot()
    main_state = 0
    while not rospy.is_shutdown():
        if main_state == 0:
            main_state = gpsr.startGPSR()
        elif main_state == 1:
            main_state = gpsr.doGivenTask()
        elif main_state == 2:
            main_state = gpsr.leaveArena()
        rospy.sleep(0.1)
            
