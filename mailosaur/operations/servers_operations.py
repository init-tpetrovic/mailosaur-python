# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from .. import models


class ServersOperations(object):
    """ServersOperations operations.

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

    def list(
            self, custom_headers=None, raw=False, **operation_config):
        """List all servers.

        Returns a list of your virtual SMTP servers. Servers are returned
        sorted in alphabetical order.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ServerListResult or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.ServerListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/servers'

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
            deserialized = self._deserialize('ServerListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create(
            self, server_create_options, custom_headers=None, raw=False, **operation_config):
        """Create a server.

        Creates a new virtual SMTP server and returns it.

        :param server_create_options:
        :type server_create_options: ~mailosaur.models.ServerCreateOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Server or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.Server or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/servers'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(server_create_options, 'ServerCreateOptions')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.MailosaurException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Server', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Retrieve a server.

        Retrieves the detail for a single server. Simply supply the unique
        identifier for the required server.

        :param id: The identifier of the server to be retrieved.
        :type id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Server or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.Server or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/servers/{id}'
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
            deserialized = self._deserialize('Server', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def update(
            self, id, server, custom_headers=None, raw=False, **operation_config):
        """Update a server.

        Updats a single server and returns it.

        :param id: The identifier of the server to be updated.
        :type id: str
        :param server:
        :type server: ~mailosaur.models.Server
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Server or ClientRawResponse if raw=true
        :rtype: ~mailosaur.models.Server or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        # Construct URL
        url = '/api/servers/{id}'
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

        # Construct body
        body_content = self._serialize.body(server, 'Server')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.MailosaurException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Server', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete(
            self, id, custom_headers=None, raw=False, **operation_config):
        """Delete a server.

        Permanently deletes a server. This operation cannot be undone. Also
        deletes all messages and associated attachments within the server.

        :param id: The identifier of the server to be deleted.
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
        url = '/api/servers/{id}'
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