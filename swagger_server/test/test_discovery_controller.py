# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.discovery_object import DiscoveryObject
from swagger_server.models.port_provision_request import PortProvisionRequest
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDiscoveryController(BaseTestCase):
    """ DiscoveryController integration test stubs """

    def test_add_discovery(self):
        """
        Test case for add_discovery

        Add a discovery object
        """
        body = DiscoveryObject()
        response = self.client.open('/api/discovery/link',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_discovery_by_id(self):
        """
        Test case for delete_discovery_by_id

        Deletes a discovery object
        """
        response = self.client.open('/api/discovery/link/{discoveryId}'.format(discoveryId='discoveryId_example'),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_all_discoveries(self):
        """
        Test case for get_all_discoveries

        List discovery objects
        """
        response = self.client.open('/api/discovery/link',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_discovery_by_id(self):
        """
        Test case for get_discovery_by_id

        get a discovery object by ID
        """
        response = self.client.open('/api/discovery/link/{discoveryId}'.format(discoveryId='discoveryId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
