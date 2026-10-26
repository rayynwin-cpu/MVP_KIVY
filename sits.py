# write module to count squats
from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.current = 0 
        self.total = total
        words = "Moves that is mandatory to carry out" + str(self.total)
        super().__init__(text=words, **kwargs)

    def next(self, *args):
        self.current += 1
        time_remain = max(0, self.total - self.current)
        words = "remaining squats" + str(self.remain)
        self.text=words
