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

import botcore as bot

if __name__ == "__main__":
    # Register and parse arguments
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
        "-q",
        "--quiet",
        help="set logging to ERROR",
        action="store_const",
        dest="loglevel",
        const=logging.ERROR,
        default=logging.INFO,
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="set logging to DEBUG",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument("-j", "--jid", dest="jid", help="JID to use")
    parser.add_argument("-p", "--password", dest="password", help="password to use")
    args = parser.parse_args()

    # Setup logger
    logging.basicConfig(level=args.loglevel, format="%(levelname)-8s %(message)s")
    logging.info("Starting jeeves bot ...")
    logging.debug(args)

    # Setup the xmpp bot
    xmpp = bot.JabberJeeves(args.jid, args.password)
    xmpp.register_plugin("xep_0030")  # Service Discovery
    xmpp.register_plugin("xep_0004")  # Data Forms
    xmpp.register_plugin("xep_0060")  # PubSub
    xmpp.register_plugin("xep_0199")  # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    xmpp.connect()
    xmpp.process()
