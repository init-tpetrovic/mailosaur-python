# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations.analysis_operations import AnalysisOperations
from .operations.files_operations import FilesOperations
from .operations.messages_operations import MessagesOperations
from .operations.servers_operations import ServersOperations
from . import models


class MailosaurBaseClientConfiguration(Configuration):
    """Configuration for MailosaurBaseClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://mailosaur.com'

        super(MailosaurBaseClientConfiguration, self).__init__(base_url)

        self.add_user_agent('mailosaur/{}'.format(VERSION))

        self.credentials = credentials


class MailosaurBaseClient(object):
    """# Introduction
    This is an overview of the Mailosaur API. This API a RESTful JSON interface
    with predictable, resource-oriented URLs. We make use of HTTP response codes to indicate
    API errors.
    We use built-in HTTP features, like HTTP authentication and HTTP verbs, which are understood
    by off-the-shelf HTTP clients.
    [Official client libraries](/docs/client-libraries/) available for most popular languages.
    # Authentication
    Authenticate your account when using the API by including your API key in the request.
    You can [manage your API keys](/app/account/api-access/) in the Mailosaur UI. Your API key carrys many privileges,
    so be sure to keep it secret! Do not share your API key in publicly-accessible areas such
    GitHub, client-side code, and so on.
    All API requests must be made over HTTPS. Calls made over plain HTTP will fail.
    API requests without authentication will also fail.
    # Errors
    ## HTTP status codes
    Mailosaur uses conventional HTTP response codes to indicate the success or failure of an
    API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range
    indicate an error that failed given the information provided (e.g., a required parameter
    was omitted), and codes in the `5xx` range indicate an error with
    Mailosaur's servers (give us a shout in the unlikely event that you see one of those).
    | Code | Description |
    |---|---|
    | 200 - OK | Request was successful. |
    | 204 - No Content | Request was successful, no response content. |
    | 400 - Bad Request | The request could be handled, often due to missing a required parameter. |
    | 401 - Unauthorized | No valid API key provided. |
    | 404 - Not Found | The requested resource doesn't exist. |
    | 5XX - Server Errors | Something went wrong at Mailosaur. (Give us a shout). |
    ## Error handling
    In of an error the server will return as much information as possible. In the case of a `401` or
    `404` error the status code gives as much information as you'd need. But for `400` errors
    Mailosaur will return a JSON object containing the structure below.
    Note that our client libraries convert responses to appropriate language-specific objects.
    | Property | Description |
    |---|---|
    | `type` | The type of error returned. Can be: api_connection_error, api_error, authentication_error, card_error, idempotency_error invalid_request_error, or rate_limit_error. |
    | `message` | A human-readable message providing more details about the error. |
    | `parameters` | A JSON object containing a key for each property name at fault, with a human-readable message per field |
    | `model` | The request model that we sent and failed to be processed |

    :ivar config: Configuration for client.
    :vartype config: MailosaurBaseClientConfiguration

    :ivar analysis: Analysis operations
    :vartype analysis: mailosaur.operations.AnalysisOperations
    :ivar files: Files operations
    :vartype files: mailosaur.operations.FilesOperations
    :ivar messages: Messages operations
    :vartype messages: mailosaur.operations.MessagesOperations
    :ivar servers: Servers operations
    :vartype servers: mailosaur.operations.ServersOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = MailosaurBaseClientConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '5.0.2'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.analysis = AnalysisOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.files = FilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.messages = MessagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.servers = ServersOperations(
            self._client, self.config, self._serialize, self._deserialize)