# -*- coding: utf-8 -*-

import argparse

from labzoo import (
    Database,
    SessionConfig,
)


def main():
    parser = argparse.ArgumentParser(
        description='run LabZoo checks on remote targets'
    )
    parser.add_argument('config', help='path to the YAML file describing the'
                        'check to run')
    parser.add_argument('database', help='path to the database file of the '
                        'session')
    args = parser.parse_args()

    session = SessionConfig.load_from_file(args.config)
    Database.load_db(args.database)
