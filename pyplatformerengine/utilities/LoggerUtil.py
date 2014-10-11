import logging
import os
import errno

"""
    Logger on off switch 
"""
class LoggerUtil:
    loggingEnabled = False
    _instance  = None
    
    """
        Turns new into a singleton retriever.
    """
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerUtil, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    """
        Sets up the logger
    """
    def setLogger(self, settings):
        self.loggingEnabled = settings["enableLogging"]
        self.createLoggingDirectory(os.path.dirname(settings["logFile"]))
        logging.basicConfig(filename=settings["logFile"], level=logging.DEBUG)
        self.info("********Logger Initialized*********")
    
    """
        logs a debug message
    """
    def debug(self, message):
        if self.loggingEnabled:
            logging.debug(message)
        
    """
        logs an info message
    """
    def info(self, message):
        if self.loggingEnabled:
            logging.info(message)
    
    """
        logs a warn message
    """ 
    def warn(self, message):
        if self.loggingEnabled:
            logging.warning(message)
       
    """
        logs an error message
    """ 
    def error(self, message):
        if self.loggingEnabled:
            logging.error(message)
       
    """
        logs a critical message
    """ 
    def crit(self, message):
        if self.loggingEnabled:
            logging.critical(message)
    
    """
        Ensures that the logging directory works.
    """
    def createLoggingDirectory(self, path):
        try:
            os.makedirs(path, exist_ok=True)
        except TypeError:
            try:
                os.makedirs(path)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else: raise
