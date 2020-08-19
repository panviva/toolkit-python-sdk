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


class GetFolderRootResponse(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'version': 'int',
        'language': 'str',
        'tags': 'list[Tag]',
        'hidden': 'bool',
        'source': 'str',
        'type': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'version': 'version',
        'language': 'language',
        'tags': 'tags',
        'hidden': 'hidden',
        'source': 'source',
        'type': 'type',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, description=None, version=None, language=None, tags=None, hidden=None, source=None, type=None, links=None):  # noqa: E501
        """GetFolderRootResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._version = None
        self._language = None
        self._tags = None
        self._hidden = None
        self._source = None
        self._type = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if language is not None:
            self.language = language
        if tags is not None:
            self.tags = tags
        if hidden is not None:
            self.hidden = hidden
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this GetFolderRootResponse.  # noqa: E501


        :return: The id of this GetFolderRootResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetFolderRootResponse.


        :param id: The id of this GetFolderRootResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetFolderRootResponse.  # noqa: E501


        :return: The name of this GetFolderRootResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetFolderRootResponse.


        :param name: The name of this GetFolderRootResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this GetFolderRootResponse.  # noqa: E501


        :return: The description of this GetFolderRootResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetFolderRootResponse.


        :param description: The description of this GetFolderRootResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this GetFolderRootResponse.  # noqa: E501


        :return: The version of this GetFolderRootResponse.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GetFolderRootResponse.


        :param version: The version of this GetFolderRootResponse.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def language(self):
        """Gets the language of this GetFolderRootResponse.  # noqa: E501


        :return: The language of this GetFolderRootResponse.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this GetFolderRootResponse.


        :param language: The language of this GetFolderRootResponse.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def tags(self):
        """Gets the tags of this GetFolderRootResponse.  # noqa: E501


        :return: The tags of this GetFolderRootResponse.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetFolderRootResponse.


        :param tags: The tags of this GetFolderRootResponse.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def hidden(self):
        """Gets the hidden of this GetFolderRootResponse.  # noqa: E501


        :return: The hidden of this GetFolderRootResponse.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this GetFolderRootResponse.


        :param hidden: The hidden of this GetFolderRootResponse.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def source(self):
        """Gets the source of this GetFolderRootResponse.  # noqa: E501


        :return: The source of this GetFolderRootResponse.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this GetFolderRootResponse.


        :param source: The source of this GetFolderRootResponse.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this GetFolderRootResponse.  # noqa: E501


        :return: The type of this GetFolderRootResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetFolderRootResponse.


        :param type: The type of this GetFolderRootResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def links(self):
        """Gets the links of this GetFolderRootResponse.  # noqa: E501


        :return: The links of this GetFolderRootResponse.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this GetFolderRootResponse.


        :param links: The links of this GetFolderRootResponse.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if issubclass(GetFolderRootResponse, dict):
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
        if not isinstance(other, GetFolderRootResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other