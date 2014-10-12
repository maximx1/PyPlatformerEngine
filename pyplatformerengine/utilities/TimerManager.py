import pygame
import string
import random

"""
    Stop watch utlitity
"""
timerSub = {}
class TimerManager:
    
    """ 
        Initializes the object.
    """
    def __init__(self):
        self.startTime = 0 
        self.elapsedTime = 0 
        self.pauseTime = 0 
        self.stopTime = 0 
    """ 
        Starts the unique timer by storing current time since pygame.init() was called (milliseconds)
    """
    def startTimer(self):
        self.startTime = pygame.time.get_ticks()
        timerId = self.idCreator(6)
        self.updateTimer(timerId)

    """ 
        Update the timer structure using timerId
    """
    def updateTimer(self, timerId):
        timerSub[timerId] = {'start' : self.startTime,'elapsed' : self.elapsedTime,
                             'pause' : self.pauseTime,'stop' : self.stopTime}
    
    """ 
        Stop should be used when you are done.  If you want to rerun the timer, you'll need to reset it. 
    """
    def stopTimer(self, timerId):
        self.stopTime = pygame.time.get_ticks()
        self.updateTimer(timerId)

    """ 
        Resets the timer back to zero.
    """
    def resetTimer(self, timerId):
        self.startTime = 0 
        self.elapsedTime = 0
        self.pauseTime = 0
        self.stopTime = 0
        self.updateTimer(timerId)

    """
       Pauses the timer
    """
    def pauseTimer(self, timerId):
        self.pauseTime = pygame.time.get_ticks()
        self.updateTimer(timerId)

    """
        Resumes the timer.  On resume, calculates the elapsed time and stores it (for processing later)
    """
    def resumeTimer(self, timerId):
        self.elapsedTime += pygame.time.get_ticks() - self.pauseTime
        self.pauseTime = 0
        self.updateTimer(timerId)

    """
        Returns the timer dictionary with all the timers and their structures. 
    """
    def timerList(self):
        return timerSub

    """
        Creates a unique id used for keeping track of timers. 
    """
    def idCreator(self, size):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(size))

    """
        Reads the current timer. 
    """
    def readTimer(self, timerId):
        if timerSub[timerId]['stop'] == 0:
            return (pygame.time.get_ticks() - timerSub[timerId]['start']) - timerSub[timerId]['elapsed']
        else:
            return (timerSub[timerId]['stop'] - timerSub[timerId]['start']) - timerSub[timerId]['elapsed']
