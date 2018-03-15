import requests
from ..models import SpamAnalysisResult 

class AnalysisOperations(object):
    """AnalysisOperations operations.
    """

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def spam(self, email):
        """Perform a spam test.

        Perform spam testing on the specified email.

        :param email: The identifier of the email to be analyzed.
        :type email: str        
        :return: SpamAnalysisResult
        :rtype: ~mailosaur.models.SpamAnalysisResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%s/api/analysis/spam/%s" % (self.base_url, email)
        response = requests.get(url, auth=(self.api_key, ''))
        response.raise_for_status()
        data = response.json()

        return SpamAnalysisResult(data)
