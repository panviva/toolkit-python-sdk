# coding: utf-8

"""
    Panviva API Suite v3

    Wouldn't it be great if you could share information seamlessly? This connector allows you to push your knowledge further and consume a complete list of Panviva's API offerings.  **Content APIs** perform resource related operations , e.g. `document`, `folder`, `file`, `container`, `image`.  **Live APIs** enable real-time communications with online users on our client application.  **Artefact APIs** interact with curated Panviva content, created by the Digital Orchestrator.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@panviva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Link(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'rel': 'str',
        'type': 'str'
    }

    attribute_map = {
        'href': 'href',
        'rel': 'rel',
        'type': 'type'
    }

    def __init__(self, href=None, rel=None, type=None):  # noqa: E501
        """Link - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._rel = None
        self._type = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel
        if type is not None:
            self.type = type

    @property
    def href(self):
        """Gets the href of this Link.  # noqa: E501


        :return: The href of this Link.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.


        :param href: The href of this Link.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def rel(self):
        """Gets the rel of this Link.  # noqa: E501


        :return: The rel of this Link.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this Link.


        :param rel: The rel of this Link.  # noqa: E501
        :type: str
        """

        self._rel = rel

    @property
    def type(self):
        """Gets the type of this Link.  # noqa: E501


        :return: The type of this Link.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Link.


        :param type: The type of this Link.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Link, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
