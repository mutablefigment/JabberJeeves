import slixmpp
import logging


class JabberJeeves(slixmpp.ClientXMPP):

    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        # The session_start event will be triggered when
        # the bot establishes its connection with the server
        # and the XML streams are ready for use. We want to
        # listen for this event so that we we can initialize
        # our roster.
        self.add_event_handler("session_start", self.start)

        # The message event is triggered whenever a message
        # stanza is received. Be aware that that includes
        # MUC messages and error messages.
        self.add_event_handler("message", self.message)

    async def start(self, event):
        """ """
        self.send_presence()
        await self.get_roster()

    def message(self, msg):
        """ """
        if msg["type"] in ("chat", "normal"):

            logging.debug(msg)
            msg.reply("Thanks for sending\n%(body)s" % msg).send()
