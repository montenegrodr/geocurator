import argparse

from geo_curator.curator import CuratorJob
from geo_curator.parser import Location
from geo_curator.distance import GreatCircle
from geo_curator.io import TextFileReader, TextFileWriter


def main(args):
    CuratorJob(
        radius=args.radius,
        calculator=GreatCircle(),
        writer=TextFileWriter(args.output_file),
        reader=TextFileReader(args.customers_file),
        reference=Location(args.reference_lat,
                           args.reference_long)
    ).run()


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

    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
