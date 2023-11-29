from serviceable import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return True if self.warning_light_on == 'on' else False
    


        

