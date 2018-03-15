import requests
from ..models import MessageListResult
from ..models import Message

class MessagesOperations(object):
    """MessagesOperations operations.
    """

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def get(self, id):
        """Retrieve a message.

        Retrieves the detail for a single email message. Simply supply the
        unique identifier for the required message.

        :param id: The identifier of the email message to be retrieved.
        :type id: str        
        :return: Message
        :rtype: ~mailosaur.models.Message
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/messages/%s" % (self.base_url, id)
        response = requests.get(url, auth=(self.api_key, ''))
        response.raise_for_status()
        data = response.json()

        # if response.status_code not in [204]:
        #     raise models.MailosaurException(self._deserialize, response)

        return Message(data)

    def delete(self, id):
        """Delete a message.

        Permanently deletes a message. This operation cannot be undone. Also
        deletes any attachments related to the message.

        :param id: The identifier of the message to be deleted.
        :type id: str        
        :return: None
        :rtype: None
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/messages/%s" % (self.base_url, id)
        response = requests.delete(url, auth=(self.api_key, ''))
        response.raise_for_status()

    def list(self, server, page=None, items_per_page=None):
        """List all messages.

        Returns a list of your messages in summary form. The summaries are
        returned sorted by received date, with the most recently-received
        messages appearing first.

        :param server: The identifier of the server hosting the messages.
        :type server: str
        :param page: Used in conjunction with `itemsPerPage` to support
         pagination.
        :type page: int
        :param items_per_page: A limit on the number of results to be returned
         per page. Can be set between 1 and 1000 items, the default is 50.
        :type items_per_page: int        
        :return: MessageListResult
        :rtype: ~mailosaur.models.MessageListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/messages" % (self.base_url)
        params = {'server': server, 'page': page, 'itemsPerPage': items_per_page}
        response = requests.get(url, params=params, auth=(self.api_key, ''))
        response.raise_for_status()
        data = response.json()

        return MessageListResult(data)

    def delete_all(self, server):
        """Delete all messages.

        Permanently deletes all messages held by the specified server. This
        operation cannot be undone. Also deletes any attachments related to
        each message.

        :param server: The identifier of the server to be emptied.
        :type server: str        
        :return: None
        :rtype: None
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/messages" % (self.base_url)
        params = {'server': server}
        response = requests.delete(url, params=params, auth=(self.api_key, ''))
        response.raise_for_status()

    def search(self, server, criteria, page=None, items_per_page=None):
        """Search for messages.

        Returns a list of messages matching the specified search criteria, in
        summary form. The messages are returned sorted by received date, with
        the most recently-received messages appearing first.

        :param server: The identifier of the server hosting the messages.
        :type server: str
        :param criteria: The search criteria to match results against.
        :type criteria: ~mailosaur.models.SearchCriteria
        :param page: Used in conjunction with `itemsPerPage` to support
         pagination.
        :type page: int
        :param items_per_page: A limit on the number of results to be returned
         per page. Can be set between 1 and 1000 items, the default is 50.
        :type items_per_page: int        
        :return: MessageListResult
        :rtype: ~mailosaur.models.MessageListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/messages/search" % (self.base_url)
        params = {'server': server, 'page': page, 'itemsPerPage': items_per_page}
        response = requests.post(url, params=params, json=criteria.toJSON(), auth=(self.api_key, ''))
        response.raise_for_status()
        data = response.json()

        return MessageListResult(data)

    def wait_for(self, server, criteria):
        """Wait for a specific message.

        Returns as soon as a message matching the specified search criteria is
        found. This is the most efficient method of looking up a message.

        :param server: The identifier of the server hosting the message.
        :type server: str
        :param criteria: The search criteria to use in order to find a match.
        :type criteria: ~mailosaur.models.SearchCriteria        
        :return: Message
        :rtype: ~mailosaur.models.Message
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/messages/await" % (self.base_url)
        params = {'server': server}
        response = requests.post(url, params=params, json=criteria.__dict__, auth=(self.api_key, ''))
        response.raise_for_status()
        data = response.json()

        return Message(data)