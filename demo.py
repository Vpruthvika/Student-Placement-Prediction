from placement_prediction.logger import logging
from placement_prediction.exception import placementException
import sys
logging.info("Welocome to my first log")


try:
    a=2/0
except Exception as e:
    raise placementException(e,sys)