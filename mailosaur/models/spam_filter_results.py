class SpamFilterResults(object):
    """SpamFilterResults.

    :param spam_assassin:
    :type spam_assassin: list[~mailosaur.models.SpamAssassinRule]
    """

    def __init__(self, data=dict):
        self.spam_assassin = data.get('spamAssassin', None)
