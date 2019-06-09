import pyautogui as auto


class ActiveSkype():

    def __init__(self):
        auto.FAILSAFE = True
        self.x = 1145
        self.y = 138
        self.duration = 0.3

    def move_mouse(self):
        while(1):
            try:
                auto.moveTo(self.x,self.y,self.duration)
                auto.moveRel(10,0,self.duration)
            except auto.FailSafeException:
                exit(0) # Handles the exception raised when cursor is moved to the top left of screen


if __name__ == '__main__':
    skypeactive = ActiveSkype()
    skypeactive.move_mouse()