import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt=("%(name)s : "
                                   "%(threadName)s :"
                                   "%(pathname)s :"
                                   "%(module)s : "
                                   "%(funcName)s : "
                                   "%(lineno)s : "
                                   "%(message)s "))
handler.setFormatter(formatter)
logger.addHandler(handler)


__all__ = ('logger',)
