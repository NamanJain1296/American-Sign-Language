from signLanguage.logger import logging
from signLanguage.exception import SignException
import sys

#logging.info("Welcome to the American Sign Language Project")

try:
    a = 7/'9'

except Exception as e:
    raise SignException(e, sys) from e