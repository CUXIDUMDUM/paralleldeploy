
from multiprocessing.dummy import Pool as ThreadPool
from time import sleep
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from ConfigParser import SafeConfigParser

from logger import logger
from .package_a import packagea
from .package_b import packageb

class Result(object):
    def __init__(self, msg):
        self.msg = msg

def worker(*args, **kwargs):            
    logger.info("worker")
    return Result(str(args) + str(kwargs))

def callback(result):
    logger.info("callback %s" % result.msg)
    result.msg = "ok"
    sleep(3)


def parser():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "-u", "--username",
        default='admin',
        help="pulp username")
    parser.add_argument(
        "-p", "--password",
        help="pulp password",
        required=False)
    parser.add_argument(
        "-n", "--num",
        type=int,
        default=10,
        help="number of processes to use")
    parser.add_argument(
        "-c", "--config",
        default="config.ini",
        help="path to configuration file")

    args = parser.parse_args()

    return args
        
def run():
    args = parser()
    config = SafeConfigParser()
    config.read(args.config)
    packages = config.get("install", "packages")
    consumers = config.get("install", "consumers")
    args= str(packages) + "\n" + str(consumers)
    print args
    # pa = packagea.A()
    # pa.hello()
    # pb = packageb.B()
    # pb.hello()
    # logger.info("hello")
    # pool = ThreadPool(2)
    # results = [pool.apply_async(worker, (1,2,3), {"foo": "bar"}, callback=callback)
    #            for i in range(3)]
    # pool.close()
    # pool.join()
    # for r in results:
    #     print r.get().msg
        
