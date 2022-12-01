import logging

from pythonjsonlogger import jsonlogger

DEBUG = logging.DEBUG
ERROR = logging.ERROR
INFO = logging.INFO
WARN = logging.WARN
WARNING = logging.WARNING

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = jsonlogger.JsonFormatter(
    fmt="%(asctime)s %(levelname)s %(module)s %(message)s",
    json_ensure_ascii=False,
)
logHandler = logging.StreamHandler()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


def set_file_handler(filename, fileLogLevel, mode, filt=None):
    __fileHandler = logging.FileHandler(filename=filename, mode=mode)
    __fileHandler.setFormatter(formatter)
    __fileHandler.setLevel(fileLogLevel)
    logger.addHandler(__fileHandler)
    if filt:
        __fileHandler.addFilter(LogTextFilter(filtText=filt))


class LogTextFilter(logging.Filter):
    def __init__(self, filtText):
        self.filt_text = filtText

    def filter(self, record):
        if self.filt_text in record.getMessage():
            return True
        return False
