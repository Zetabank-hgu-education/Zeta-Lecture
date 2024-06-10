class EventName:
    """
    Event name handler
    
    :action: what action setting is the robot arm in
    
    """
    
    def __init__(self):
        self.action = 'stand_by'
        
    def play_button_Callback(self, value):
        self.action = 'Play Music'
    def stop_button_Callback(self, value):
        self.action = 'No Music'
    def up_button_Callback(self, value):
        self.action = 'Up'
    def down_button_Callback(self, value):
        self.action = 'Down'
    def left_button_Callback(self, value):
        self.action = 'Left'
    def right_button_Callback(self, value):
        self.action = 'Right'
    def pinch_button_Callback(self, value):
        self.action = 'Pinch'
    def release_button_Callback(self, value):
        self.action = 'Release'
    def exit_button_Callback(self, value):
        self.action = 'Exit'
    
    def reset(self):
        self.action = 'stand_by'
        