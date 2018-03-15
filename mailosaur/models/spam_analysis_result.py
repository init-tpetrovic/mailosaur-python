class SpamAnalysisResult(object):
    """SpamAnalysisResult.

    :param spam_filter_results:
    :type spam_filter_results: ~mailosaur.models.SpamFilterResults
    :param score:
    :type score: float
    """

    def __init__(self, data):
        self.spam_filter_results = data.get('spamFilterResults', None)
        self.score = data.get('score', None)
