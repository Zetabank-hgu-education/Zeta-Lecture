import math
from time import sleep

class Movement:
    """
    Functions for robot arm movements
    
    :Arm: Robot Arm object
    :initial_position: Initial position
    :angle_range: Used to calculate angles to draw a circle
    :circle_positions: Stores the position where the robot arm moves to draw a circle
    :square_positions: Stores the position where the robot arm moves to draw a square
    :triangle_positions: Stores the position where the robot arm moves to draw a triangle
    :time: The time length for the movement
    """
    
    def __init__(self, Arm):
        self.Arm = Arm

        self.initial_position = [90, 90, 0, 90, 90, 170]
        self.angle_range = range(0, 361, 10)
        self.circle_positions = self.calculate_circle_positions
        self.square_positions = self.calculate_square_positions
        self.triangle_positions = self.calculate_triangle_positions
        
    def move_to_initial_position(self, time) :
        """
        Move the Robot Arm to its initial position. 
        
        :param time: Movement time for the Robot Arm 
        :type: int
        
        """

        self.Arm.Arm_serial_servo_write6_array(self.initial_position, time)
        sleep(2)

    def calculate_circle_positions(self, length):
        """
        Receive the radius and performs an operation to draw a concentric circle.
        
        :param length: Concentric radius
        :type: int
        
        """
        
        positions = []
        for angle in self.angle_range:
            x = self.initial_position[0] + length * math.cos(math.radians(angle))
            y = self.initial_position[1] + length * math.sin(math.radians(angle))
            positions.append([x, y, self.initial_position[2], self.initial_position[3], self.initial_position[4], self.initial_position[5]])
        return positions
    
    def calculate_square_positions(self, length):
        """
        Receive the length of the base and perform an operation to draw a square.
        
        :param length: Base of a square
        :type: int
        
        """
        
        positions = [
            [self.initial_position[0] - length/2, self.initial_position[1], self.initial_position[2] - length/2, self.initial_position[3], self.initial_position[4], self.initial_position[5]],    
            [self.initial_position[0] + length/2, self.initial_position[1], self.initial_position[2] - length/2, self.initial_position[3], self.initial_position[4], self.initial_position[5]],
            [self.initial_position[0] + length/2, self.initial_position[1], self.initial_position[2] + length/2, self.initial_position[3], self.initial_position[4], self.initial_position[5]],
            [self.initial_position[0] - length/2, self.initial_position[1], self.initial_position[2] + length/2, self.initial_position[3], self.initial_position[4], self.initial_position[5]]
        ]
        return positions
    
    def calculate_triangle_positions(self, length):
        """
        Receive the length of the base and perform an operation to draw an equilateral triangle.
        
        :param length: Base of a equilateral triangle
        :type: int
        
        """
        
        positions = [
            [self.initial_position[0], self.initial_position[1], self.initial_position[2] - length * math.sqrt(3) / 6, self.initial_position[3], self.initial_position[4], self.initial_position[5]],
            [self.initial_position[0] - length / 2, self.initial_position[1], self.initial_position[2] + length * math.sqrt(3) / 3, self.initial_position[3], self.initial_position[4], self.initial_position[5]],
            [self.initial_position[0] + length / 2, self.initial_position[1], self.initial_position[2] + length * math.sqrt(3) / 3, self.initial_position[3], self.initial_position[4], self.initial_position[5]]
        ]
        return positions
    
    """
    Move the joints of the robot arm in the order of the received positions
        
    """

    def move_to_circle_positions(self, length, time):
        for position in self.circle_positions(length):
            self.Arm.Arm_serial_servo_write6_array(position, time)
            sleep(0.1)
            
    def move_to_square_positions(self, length, time):
        for position in self.square_positions(length):
            self.Arm.Arm_serial_servo_write6_array(position, time)
            sleep(1)
                
    def move_to_triangle_positions(self, length, time):
        for position in self.triangle_positions(length):
            self.Arm.Arm_serial_servo_write6_array(position, time)
            sleep(1)