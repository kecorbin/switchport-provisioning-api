# coding: utf-8

from __future__ import absolute_import
import os
from .base_model_ import Model
from typing import List
from ..util import deserialize_model
from bson.objectid import ObjectId
from flask_pymongo import MongoClient

mongo_host = os.getenv("MONGO_HOST", "mongo")
mongo = MongoClient(mongo_host)
db = mongo.db.provision


class PortProvisionRequest(Model):
    """
    A port provisioning request w/ mongo backend
    """
    def __init__(self, id: str=None, interface: str=None, requestor: str=None, switch: str=None, vlans: List[int]=None):
        """
        PortProvisionRequest - a model defined in Swagger

        :param id: The id of this PortProvisionRequest.
        :type id: str
        :param interface: The interface of this PortProvisionRequest.
        :type interface: str
        :param requestor: The requestor of this PortProvisionRequest.
        :type requestor: str
        :param switch: The switch of this PortProvisionRequest.
        :type switch: str
        :param vlans: The vlans of this PortProvisionRequest.
        :type vlans: List[int]
        """
        self.swagger_types = {
            'id': str,
            'interface': str,
            'requestor': str,
            'switch': str,
            'vlans': List[int]
        }

        self.attribute_map = {
            'id': 'id',
            'interface': 'interface',
            'requestor': 'requestor',
            'switch': 'switch',
            'vlans': 'vlans'
        }

        self._id = id
        self._interface = interface
        self._requestor = requestor
        self._switch = switch
        self._vlans = vlans

    @classmethod
    def from_dict(cls, dikt) -> 'PortProvisionRequest':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PortProvisionRequest of this PortProvisionRequest.
        :rtype: PortProvisionRequest
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this PortProvisionRequest.

        :return: The id of this PortProvisionRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this PortProvisionRequest.

        :param id: The id of this PortProvisionRequest.
        :type id: str
        """

        self._id = id

    @property
    def interface(self) -> str:
        """
        Gets the interface of this PortProvisionRequest.

        :return: The interface of this PortProvisionRequest.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface: str):
        """
        Sets the interface of this PortProvisionRequest.

        :param interface: The interface of this PortProvisionRequest.
        :type interface: str
        """
        if interface is None:
            raise ValueError("Invalid value for `interface`, must not be `None`")

        self._interface = interface

    @property
    def requestor(self) -> str:
        """
        Gets the requestor of this PortProvisionRequest.

        :return: The requestor of this PortProvisionRequest.
        :rtype: str
        """
        return self._requestor

    @requestor.setter
    def requestor(self, requestor: str):
        """
        Sets the requestor of this PortProvisionRequest.

        :param requestor: The requestor of this PortProvisionRequest.
        :type requestor: str
        """
        if requestor is None:
            raise ValueError("Invalid value for `requestor`, must not be `None`")

        self._requestor = requestor

    @property
    def switch(self) -> str:
        """
        Gets the switch of this PortProvisionRequest.
        ip/hostname of switch

        :return: The switch of this PortProvisionRequest.
        :rtype: str
        """
        return self._switch

    @switch.setter
    def switch(self, switch: str):
        """
        Sets the switch of this PortProvisionRequest.
        ip/hostname of switch

        :param switch: The switch of this PortProvisionRequest.
        :type switch: str
        """
        if switch is None:
            raise ValueError("Invalid value for `switch`, must not be `None`")

        self._switch = switch

    @property
    def vlans(self) -> List[int]:
        """
        Gets the vlans of this PortProvisionRequest.

        :return: The vlans of this PortProvisionRequest.
        :rtype: List[int]
        """
        return self._vlans

    @vlans.setter
    def vlans(self, vlans: List[int]):
        """
        Sets the vlans of this PortProvisionRequest.

        :param vlans: The vlans of this PortProvisionRequest.
        :type vlans: List[int]
        """
        if vlans is None:
            raise ValueError("Invalid value for `vlans`, must not be `None`")

        self._vlans = vlans

    # mongo hooks

    @classmethod
    def get(cls, id=None):
        if id:
            doc = db.find_one({"id": id}, {"_id": 0})
            if doc:
                return cls.from_dict(doc)
        else:
            cursor = db.find({}, {"_id": 0})
            objs = [cls.from_dict(i) for i in cursor]
            return objs

    def delete(self):
        db.delete_one({"id": self.id})

    def save(self):
        object_id = ObjectId()
        self.id = str(object_id)
        data ={
              "id": self.id,
              "interface": self.interface,
              "requestor": self.requestor,
              "switch": self.switch,
              "vlans": self.vlans
            }
        db.insert(data)
        doc = db.find_one({"id": self.id}, {"_id": 0})
        return doc

