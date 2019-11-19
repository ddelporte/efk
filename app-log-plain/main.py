#!/usr/bin/env python

import logging

import time

logger_simple = logging.getLogger()

while True:
    logger_simple.info("info level - simple message to display")
    logger_simple.warning("warning level - simple message to display")
    logger_simple.error("error level - simple message to display")
    logger_simple.fatal("fatal level - simple message to display")
    time.sleep(60)
