class Movement:
    """
    Functions for robot arm movements
    
    !! Change the angles of all the servo writes to suit your task
    
    :Arm: Robot Arm object
    :first_angle: Angle for first servo
    :third_angle: Angle for third servo
    :time: The time length for the movement 
    """
    
    def __init__(self, Arm):
        self.Arm = Arm
        self.first_angle = 90
        self.third_angle = 45
        self.pincher_angle = 90
        
    def move_up(self, time):
        """
        Move the Robot Arm Up. If the limit is reached, stop the update. 
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """
        
        self.Arm.Arm_serial_servo_write(2, 90, time)
        self.Arm.Arm_serial_servo_write(4, 45, time)
        if self.third_angle >= 90:
            self.Arm.Arm_serial_servo_write(3, self.third_angle, time)
        else:
            self.third_angle += 15
            self.Arm.Arm_serial_servo_write(3, self.third_angle, time)


    def move_down(self, time):
        """
        Move the Robot Arm Down. If the limit is reached, stop the update. 
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """
        
        self.Arm.Arm_serial_servo_write(2, 45, time) 
        self.Arm.Arm_serial_servo_write(4, 35, time)

        if self.third_angle <= 15:
            self.third_angle = 10
            self.Arm.Arm_serial_servo_write(3, self.third_angle, time)
        else:
            self.third_angle -= 15
            self.Arm.Arm_serial_servo_write(3, self.third_angle, time)
            
            
    def move_left(self, time):
        """
        Turn the Robot Arm to the left. If the limit is reached, stop the update. 
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """
        
        if self.first_angle >= 150:
            self.first_angle = 180
            self.Arm.Arm_serial_servo_write(1, self.first_angle, time)
        else:
            self.first_angle += 30
            self.Arm.Arm_serial_servo_write(1, self.first_angle, time)

    def move_right(self, time):
        """
        Turn the Robot Arm to the right. If the limit is reached, stop the update. 
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """
        
        if self.first_angle <= 30:
            self.first_angle = 0
            self.Arm.Arm_serial_servo_write(1, self.first_angle, time)
        else:
            self.first_angle -= 30
            self.Arm.Arm_serial_servo_write(1, self.first_angle, time)
        
        
    def move_pincher(self, time):
        """
        Pinch the pincher
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """
        
        if self.pincher_angle >= 165:
            self.pincher_angle = 165
            self.Arm.Arm_serial_servo_write(6, self.pincher_angle, time)
        else:
            self.pincher_angle += 5
            self.Arm.Arm_serial_servo_write(6, self.pincher_angle, time)
            

        
    def release_pincher(self, time):
        """
        Pinch the pincher
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """
        self.pincher_angle = 90
        self.Arm.Arm_serial_servo_write(6, self.pincher_angle, time)
            