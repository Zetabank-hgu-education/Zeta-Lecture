class EventName:
    """
    Event name handler
    
    :action: what action setting is the robot arm in
    
    """
    
    def __init__(self):
        self.action = 'stand_by'
        
    def start_button_Callback(self, value):
        self.action = 'Start'
        
    def reset_button_Callback(self, value):
        self.action = 'Reset'

    def exit_button_Callback(self, value):
        self.action = 'Exit'
    
    def reset(self):
        self.action = 'stand_by'
        