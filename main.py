# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Frame:
    def __init__(self, rolls=[], bonus=0):
        self.rolls = rolls
        self.bonus = bonus

class Game:
    def __init__(self):
        self.score = 0
        self.frames = []
        self.rolls = 0
        self.bonus = 0

    def roll(self, pins):
        if pins==10: #strike
            frame = Frame()
            frame.roll1 = 10
            self.frames.append(frame)
        else:
            frame = Frame()
            frame
        pass

    def calculate_score(self):
        pass