class MailosaurError:
    """MailosaurError.

    :param type: Possible values include: 'None', 'ValidationError',
     'AuthenticationError', 'PermissionDeniedError', 'ResourceNotFoundError'
    :type type: str or ~mailosaur.models.enum
    :param messages:
    :type messages: dict[str, str]
    :param model:
    :type model: object
    """

    def __init__(self, data):
        self.type = data.get('type', None)
        self.messages = data.get('messages', None)
        self.model = data.get('model', None)


class MailosaurException:
    """Server responsed with exception of type: 'MailosaurError'.
    """

    def __init__(self, data):

        super(MailosaurException, self).__init__(deserialize, response, 'MailosaurError', *args)
