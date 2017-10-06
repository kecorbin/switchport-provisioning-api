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
db = mongo.db.discovery


class DiscoveryObject(Model):
    """
    Discovery Object w/ mongo backend
    """
    def __init__(self, id: str=None, interface: str=None, switch: str=None, mac_addresses: List[str]=None):
        """
        DiscoveryObject - a model defined in Swagger

        :param id: The id of this DiscoveryObject.
        :type id: str
        :param interface: The interface of this DiscoveryObject.
        :type interface: str
        :param switch: The switch of this DiscoveryObject.
        :type switch: str
        :param mac_addresses: The mac_addresses of this DiscoveryObject.
        :type mac_addresses: List[str]
        """
        self.swagger_types = {
            'id': str,
            'interface': str,
            'switch': str,
            'mac_addresses': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'interface': 'interface',
            'switch': 'switch',
            'mac_addresses': 'mac_addresses'
        }

        self._id = id
        self._interface = interface
        self._switch = switch
        self._mac_addresses = mac_addresses

    @classmethod
    def from_dict(cls, dikt) -> 'DiscoveryObject':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DiscoveryObject of this DiscoveryObject.
        :rtype: DiscoveryObject
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this DiscoveryObject.

        :return: The id of this DiscoveryObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this DiscoveryObject.

        :param id: The id of this DiscoveryObject.
        :type id: str
        """

        self._id = id

    @property
    def interface(self) -> str:
        """
        Gets the interface of this DiscoveryObject.

        :return: The interface of this DiscoveryObject.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface: str):
        """
        Sets the interface of this DiscoveryObject.

        :param interface: The interface of this DiscoveryObject.
        :type interface: str
        """
        if interface is None:
            raise ValueError("Invalid value for `interface`, must not be `None`")

        self._interface = interface

    @property
    def switch(self) -> str:
        """
        Gets the switch of this DiscoveryObject.
        ip/hostname of switch

        :return: The switch of this DiscoveryObject.
        :rtype: str
        """
        return self._switch

    @switch.setter
    def switch(self, switch: str):
        """
        Sets the switch of this DiscoveryObject.
        ip/hostname of switch

        :param switch: The switch of this DiscoveryObject.
        :type switch: str
        """
        if switch is None:
            raise ValueError("Invalid value for `switch`, must not be `None`")

        self._switch = switch

    @property
    def mac_addresses(self) -> List[str]:
        """
        Gets the mac_addresses of this DiscoveryObject.

        :return: The mac_addresses of this DiscoveryObject.
        :rtype: List[str]
        """
        return self._mac_addresses

    @mac_addresses.setter
    def mac_addresses(self, mac_addresses: List[str]):
        """
        Sets the mac_addresses of this DiscoveryObject.

        :param mac_addresses: The mac_addresses of this DiscoveryObject.
        :type mac_addresses: List[str]
        """
        if mac_addresses is None:
            raise ValueError("Invalid value for `mac_addresses`, must not be `None`")

        self._mac_addresses = mac_addresses

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
        data = {
            "_id": object_id,
            "switch": self.switch,
            "id": self.id,
            "interface": self.interface,
            "mac_addresses": self.mac_addresses
        }
        db.insert(data)
        doc = db.find_one({"id": self.id}, {"_id": 0})
        return doc



