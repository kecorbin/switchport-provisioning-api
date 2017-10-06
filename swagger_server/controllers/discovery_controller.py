import connexion
import os
from swagger_server.models.discovery_object import DiscoveryObject
from swagger_server.models.port_provision_request import PortProvisionRequest


def add_discovery():
    """
    Add a discovery object
    This endpoint is used to submit a new provisioing request
    :param body: discovery object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        discovery = DiscoveryObject.from_dict(connexion.request.get_json())
        return discovery.save()


def delete_discovery_by_id(discoveryId):
    """
    Deletes a discovery object
    
    :param discoveryId: discovery id to delete
    :type discoveryId: str

    :rtype: None
    """
    doc = DiscoveryObject.get(id=discoveryId)

    if doc:
        print(doc)
        doc.delete()
        return {"status": "deleted"}
    else:
        return 'Not Found', 404

def get_all_discoveries():
    """
    List discovery objects
    Retrieve a list of ports requesting configuration changes

    :rtype: object
    """
    return DiscoveryObject.get()


def get_discovery_by_id(discoveryId):
    """
    get a discovery object by ID
    Returns a single discovery request
    :param discoveryId: ID of request to return
    :type discoveryId: str

    :rtype: PortProvisionRequest
    """
    doc = DiscoveryObject.get(id=discoveryId)
    if doc:
        return doc
    else:
        return 'Not Found', 404
