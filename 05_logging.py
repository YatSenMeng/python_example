import logging
from logging.handlers import RotatingFileHandler


# define logger use method
log_file = f"log_test.log"  # logfile path
logger = logging.getLogger("test logging")  # create logger
logger.setLevel(logging.DEBUG)  # set log level, filter low level log
handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)  # set maxBytes and backunCount
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")  # set output formatter
handler.setFormatter(formatter)  # handler load formatter
logger.addHandler(handler)  # logger load handler
logger.debug("run1")




