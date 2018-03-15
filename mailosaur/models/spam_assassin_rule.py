class SpamAssassinRule(object):
    """SpamAssassinRule.

    :param score:
    :type score: float
    :param rule:
    :type rule: str
    :param description:
    :type description: str
    """

    def __init__(self, data=dict):
        self.score = data.get('score', 0)
        self.rule = data.get('rule', None)
        self.description = get.get('description', None)
