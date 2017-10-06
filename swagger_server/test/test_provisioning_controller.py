# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.port_provision_request import PortProvisionRequest
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProvisioningController(BaseTestCase):
    """ ProvisioningController integration test stubs """

    def test_add_provisioning_request(self):
        """
        Test case for add_provisioning_request

        Add a provisioning request
        """
        body = PortProvisionRequest()
        response = self.client.open('/api/provisioning/port',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_provisioning_request(self):
        """
        Test case for delete_provisioning_request

        Deletes a port provisioning request
        """
        response = self.client.open('/api/provisioning/port/{requestId}'.format(requestId='requestId_example'),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_provisioning_request_by_id(self):
        """
        Test case for get_provisioning_request_by_id

        get provisioning request by ID
        """
        response = self.client.open('/api/provisioning/port/{requestId}'.format(requestId='requestId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_requests(self):
        """
        Test case for get_requests

        List server connectivity requests
        """
        response = self.client.open('/api/provisioning/port',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
