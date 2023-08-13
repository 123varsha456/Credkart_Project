import logging
import inspect

class LogGenerator:
    @staticmethod
    def loggen():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        logfile=logging.FileHandler("D:\\Cred_Kart_Project_Copy\\Log\\CredKart.log")  ##jo aapn log directory create krto tyacha path ahe ha
        log_format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s ")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger



##inspect.stack()--he file ,folder,class,method la path detat

##setLevel ahet he khalche--shortcut-DIWEC
# Debug
# Info
# Warning
# Error
# Critical





