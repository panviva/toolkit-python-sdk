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


class Facet(object):
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
        'field': 'str',
        'groups': 'list[StringInt64NullableKeyValuePair]'
    }

    attribute_map = {
        'field': 'field',
        'groups': 'groups'
    }

    def __init__(self, field=None, groups=None):  # noqa: E501
        """Facet - a model defined in Swagger"""  # noqa: E501

        self._field = None
        self._groups = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if groups is not None:
            self.groups = groups

    @property
    def field(self):
        """Gets the field of this Facet.  # noqa: E501


        :return: The field of this Facet.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Facet.


        :param field: The field of this Facet.  # noqa: E501
        :type: str
        """

        self._field = field

    @property
    def groups(self):
        """Gets the groups of this Facet.  # noqa: E501


        :return: The groups of this Facet.  # noqa: E501
        :rtype: list[StringInt64NullableKeyValuePair]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Facet.


        :param groups: The groups of this Facet.  # noqa: E501
        :type: list[StringInt64NullableKeyValuePair]
        """

        self._groups = groups

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
        if issubclass(Facet, dict):
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
        if not isinstance(other, Facet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other