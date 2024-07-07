#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16MultiArray, Int16
import speech_recognition as sr
import pyttsx3

def listen_and_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
    
    try:
        WhatUSpoke = r.recognize_google(audio, language="EN")
        print("I heard : ", WhatUSpoke)
        return WhatUSpoke
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return None

def callback(data):
    spoken_text = listen_and_recognize()
    if data==0 and spoken_text == "Butler":
        while not rospy.is_shutdown():
            engine = pyttsx3.init()
            engine.say("Coming to the kitchen")
            pub1.publish(0)
            engine.runAndWait()

    elif data==4:
        if spoken_text.startswith("table "):
            while not rospy.is_shutdown():
                numbers = [int(s) for s in spoken_text.split() if s.isdigit()]
                if numbers:
                    table_numbers = numbers
                    rospy.loginfo("Publishing table numbers: %s", table_numbers)
                    pub1.publish(1)
                    pub.publish(table_numbers)
                    engine = pyttsx3.init()
                    engine.say(f"Got the Table numbers {table_numbers}")
                    engine.runAndWait()
                    break
                else:
                    engine = pyttsx3.init()
                    engine.say("Please specify the table numbers correctly")
                    engine.runAndWait()
        else:
            pub1.publish(2)
    else:
        engine = pyttsx3.init()
        engine.say("I didn't hear anything. Please try again.")
        engine.runAndWait()


if __name__ == '__main__':
    try:
        rospy.init_node('audioin_node', anonymous=True)
        print("Started the Audio Input Node")
        pub = rospy.Publisher('tables', Int16MultiArray, queue_size=10)
        pub1 = rospy.Publisher('heard', Int16, queue_size=10)
        rospy.Subscriber('listen_to', Int16, callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")