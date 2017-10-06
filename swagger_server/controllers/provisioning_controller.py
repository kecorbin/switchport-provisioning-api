import connexion
from swagger_server.models.port_provision_request import PortProvisionRequest


def add_provisioning_request():
    """
    Add a provisioning request
    This endpoint is used to submit a new provisioing request
    :param body: Provision request object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        discovery = PortProvisionRequest.from_dict(connexion.request.get_json())
        return discovery.save()


def delete_provisioning_request(requestId):
    """
    Deletes a port provisioning request
    
    :param requestId: provisioning request id to delete
    :type requestId: str

    :rtype: None
    """
    doc = PortProvisionRequest.get(id=requestId)

    if doc:
        print(doc)
        doc.delete()
        return {"status": "deleted"}
    else:
        return 'Not Found', 404


def get_provisioning_request_by_id(requestId):
    """
    get provisioning request by ID
    Returns a single provisioning request
    :param requestId: ID of request to return
    :type requestId: str

    :rtype: None
    """
    doc = PortProvisionRequest.get(id=requestId)
    if doc:
        return doc
    else:
        return 'Not Found', 404


def get_requests():
    """
    List server connectivity requests
    Retrieve a list of ports requesting configuration changes

    :rtype: None
    """
    return PortProvisionRequest.get()
