import sys
import argparse
import logging

from geo_curator.monitor import Monitor
from geo_curator.curator import CuratorJob
from geo_curator.distance import GreatCircle
from geo_curator.parser import Location, Parser, Parsers
from geo_curator.io import TextFileReader, TextFileWriter


def main(args, logger):
    logger.info(f'Starting curating customer with. Arguments: {args}')
    logger.info('Starting prometheus monitoring')
    monitor = Monitor(args.monitor)
    monitor.start()
    try:
        CuratorJob(
            radius=args.radius,
            calculator=GreatCircle(),
            parser=Parser.factory(Parsers.JSON),
            writer=TextFileWriter(args.output_file),
            reader=TextFileReader(args.customers_file),
            reference=Location(args.reference_lat,
                               args.reference_long)
        ).run()
    except Exception as e:
        monitor.fatal_errors()
        logger.exception(e)


def setup_logger():
    logger = logging.getLogger('geo_curator')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--customers-file',
                        type=str,
                        help='Customers file path',
                        required=True)
    parser.add_argument('--output-file',
                        type=str,
                        help='Customers file path',
                        required=True)
    parser.add_argument('--reference-lat',
                        type=float,
                        help='Reference latitude',
                        required=True)
    parser.add_argument('--reference-long',
                        type=float,
                        help='Reference longitude',
                        required=True)
    parser.add_argument('--radius',
                        type=float,
                        help='Radius threshold',
                        required=True)
    parser.add_argument('--monitor',
                        type=int,
                        help='Monitor port',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args(), setup_logger())
