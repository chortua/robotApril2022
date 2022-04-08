#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
import time

class ultrasonic_sensor_readings(Node):
    def __init__(self):
        # this is the name of the node ( Program )
        super().__init__("ultrasonic_sensor") 
        # This is the name of the Topic ( Information being transmitted (type, name, sequence)
        self.pub = self.create_publisher(Float32, "distance_to_objects", 10 ) 
        self.timer = self.create_timer(1, self.publish_distance_to_object)
        self.counter = 0

    def publish_distance_to_object(self):
        try:
            GPIO.setmode(GPIO.BCM)

            PIN_TRIGGER = 21
            PIN_ECHO = 20

            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            GPIO.output(PIN_TRIGGER, GPIO.HIGH)

            time.sleep(0.00001)

            GPIO.output(PIN_TRIGGER, GPIO.LOW)

            while GPIO.input(PIN_ECHO)==0:
                    pulse_start_time = time.time()
            while GPIO.input(PIN_ECHO)==1:
                    pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time
            distance = round(pulse_duration * 17150, 2)
            
            
    
        finally:
            GPIO.cleanup()
        
        msg = Float32()
        # import distance from another program (hc_sr04.py)
        msg.data = float(distance)
        self.pub.publish(msg)
        

def main():
    rclpy.init()
    my_pub = ultrasonic_sensor_readings()
    print("Publisher Node Running...")
    
    try:
        rclpy.spin(my_pub)
    except KeyboardInterrupt:
        my_pub.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()