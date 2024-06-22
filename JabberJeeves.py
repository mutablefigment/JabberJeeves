#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	JabberJeeves
	Copyright (C) 2024 Mutable Figment

	See the file LICENSE for copying permission.
"""
import logging
import configparser
from argparse import ArgumentParser


if __name__ == "__main__":

    parser = ArgumentParser(description="JabberJeeves")
    parser.add_argument(
        "-c",
        "--config",
        dest="configPath",
        default="config.json",
        help="Path to the config file",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_const",
        dest="interactive",
        const=True,
        default=False,
        help="Run in interactive mode. This will ask for a username and password",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        dest="verbose",
        const=logging.DEBUG,
        default=logging.INFO,
        help="Log debug output",
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.verbose, format="%(levelname)-8s %(message)s")
    logging.info("Starting alfred bot ...")
    logging.debug(args)
