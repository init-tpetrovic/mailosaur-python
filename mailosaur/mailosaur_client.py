"""
    mailosaur.com API library. Basic usage:

    >>> from mailosaur import Mailosaur
    >>> mailbox = Mailosaur("BOX_ID", "YOUR_API_KEY")
    >>> emails = mailbox.get_emails()

    More options at https://mailosaur.com/docs/email/
"""

import uuid
import requests

from .operations.servers_operations import ServersOperations
from .operations.messages_operations import MessagesOperations
from .operations.analysis_operations import AnalysisOperations

class MailosaurClient(object):
    """ Main class to access Mailosaur.com api. """

    def __init__(self, api_key, base_url="https://mailosaur.com"):
        """ Pass in your mailbox id and api key to authenticate """
        self.api_key = api_key
        self.base_url = base_url

        self.servers = ServersOperations(self.api_key, self.base_url)
        self.messages = MessagesOperations(self.api_key, self.base_url)
        self.analysis = AnalysisOperations(self.api_key, self.base_url)
