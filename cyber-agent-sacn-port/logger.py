import logging
from config import LOG_FILE

def setup_logger():
    logger = logging.getLogger("PortScanAgent")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    if not logger.hasHandlers():
        logger.addHandler(fh)
    return logger
