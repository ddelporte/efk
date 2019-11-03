#!/usr/bin/env python

import logging
from pythonjsonlogger import jsonlogger

from sys import stdout as sys_stdout
import time

formatter = jsonlogger.JsonFormatter()

logHandler_stderr = logging.StreamHandler()
logHandler_stderr.setFormatter(formatter)
logger_stderr = logging.getLogger()
logger_stderr.setLevel(logging.DEBUG)
logger_stderr.addHandler(logHandler_stderr)

# logHandler_stdout = logging.StreamHandler(sys_stdout)
# logHandler_stdout.setFormatter(formatter)
# logger_stdout = logging.getLogger()
# logger_stdout.setLevel(logging.DEBUG)
# logger_stdout.addHandler(logHandler_stdout)


logHandler_stdout = logging.StreamHandler(sys_stdout)
logHandler_stdout.setFormatter(formatter)
# logger_stdout = logging.getLogger()
# logger_stdout.setLevel(logging.DEBUG)
logger_stderr.addHandler(logHandler_stdout)


while True:
    logger_stderr.debug("debug level - message to display", extra={"log_info_level": "debug level", "ts": time.time()})
    logger_stderr.info("info level - message to display", extra={"log_info_level": "info level", "ts": time.time()})
    logger_stderr.warning("warning level - message to display", extra={"log_info_level": "warning level", "ts": time.time()})
    logger_stderr.error("error level - message to display", extra={"log_info_level": "error level", "ts": time.time()})
    logger_stderr.fatal("fatal level - message to display", extra={"log_info_level": "fatal level", "ts": time.time()})
    time.sleep(30)