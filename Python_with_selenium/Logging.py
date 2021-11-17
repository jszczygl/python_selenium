import logging

logging.basicConfig(filename="test.log", format='%(asctime)s: %(levelname)s: %(message)s')


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("message")
logging.info("message")
logging.warning("message")
logging.error("message")
logging.critical("message")


logger.debug("message")
logger.info("message")
logger.warning("message")
logger.error("message")
logger.critical("message")