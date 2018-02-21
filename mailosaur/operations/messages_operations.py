# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class MessagesOperations(object):
    """MessagesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Retrieve a message.

        Retrieves the detail for a single email message. Simply supply the
        unique identifier for the required message.

        :param id: The identifier of the email message to be retrieved.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Message or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.Message or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/messages/{id}'
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.MailosaurException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Message', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Delete a message.

        Permanently deletes a message. This operation cannot be undone. Also
        deletes any attachments related to the message.

        :param id: The identifier of the message to be deleted.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/messages/{id}'
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.MailosaurException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def list(
            self, server, page=None, items_per_page=None, custom_headers=None, raw=False, **operation_config):
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
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MessageListResult or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.MessageListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/messages'

        # Construct parameters
        query_parameters = {}
        query_parameters['server'] = self._serialize.query("server", server, 'str')
        if page is not None:
            query_parameters['page'] = self._serialize.query("page", page, 'int')
        if items_per_page is not None:
            query_parameters['itemsPerPage'] = self._serialize.query("items_per_page", items_per_page, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.MailosaurException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('MessageListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete_all(
            self, server, custom_headers=None, raw=False, **operation_config):
        """Delete all messages.

        Permanently deletes all messages held by the specified server. This
        operation cannot be undone. Also deletes any attachments related to
        each message.

        :param server: The identifier of the server to be emptied.
        :type server: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/messages'

        # Construct parameters
        query_parameters = {}
        query_parameters['server'] = self._serialize.query("server", server, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.MailosaurException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def search(
            self, server, criteria, page=None, items_per_page=None, custom_headers=None, raw=False, **operation_config):
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
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: MessageListResult or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.MessageListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/messages/search'

        # Construct parameters
        query_parameters = {}
        query_parameters['server'] = self._serialize.query("server", server, 'str')
        if page is not None:
            query_parameters['page'] = self._serialize.query("page", page, 'int')
        if items_per_page is not None:
            query_parameters['itemsPerPage'] = self._serialize.query("items_per_page", items_per_page, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(criteria, 'SearchCriteria')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.MailosaurException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('MessageListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def wait_for(
            self, server, criteria, custom_headers=None, raw=False, **operation_config):
        """Wait for a specific message.

        Returns as soon as a message matching the specified search criteria is
        found. This is the most efficient method of looking up a message.

        :param server: The identifier of the server hosting the message.
        :type server: str
        :param criteria: The search criteria to use in order to find a match.
        :type criteria: ~mailosaur.models.SearchCriteria
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Message or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.Message or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/messages/await'

        # Construct parameters
        query_parameters = {}
        query_parameters['server'] = self._serialize.query("server", server, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(criteria, 'SearchCriteria')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.MailosaurException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Message', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized