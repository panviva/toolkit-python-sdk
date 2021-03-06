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


class PostLiveDocumentRequest(object):
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
        'username': 'str',
        'user_id': 'str',
        'id': 'str',
        'location': 'str',
        'maximize_client': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'user_id': 'userId',
        'id': 'id',
        'location': 'location',
        'maximize_client': 'maximizeClient'
    }

    def __init__(self, username=None, user_id=None, id=None, location=None, maximize_client=None):  # noqa: E501
        """PostLiveDocumentRequest - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._user_id = None
        self._id = None
        self._location = None
        self._maximize_client = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if user_id is not None:
            self.user_id = user_id
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if maximize_client is not None:
            self.maximize_client = maximize_client

    @property
    def username(self):
        """Gets the username of this PostLiveDocumentRequest.  # noqa: E501

        The Panviva user to whom you wish to send the result. (Note: Use username OR userId, not both.)  # noqa: E501

        :return: The username of this PostLiveDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PostLiveDocumentRequest.

        The Panviva user to whom you wish to send the result. (Note: Use username OR userId, not both.)  # noqa: E501

        :param username: The username of this PostLiveDocumentRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_id(self):
        """Gets the user_id of this PostLiveDocumentRequest.  # noqa: E501

        The numeric ID of the user to whom you wish to send the result. (Note: Use username OR userId, not both.)  # noqa: E501

        :return: The user_id of this PostLiveDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PostLiveDocumentRequest.

        The numeric ID of the user to whom you wish to send the result. (Note: Use username OR userId, not both.)  # noqa: E501

        :param user_id: The user_id of this PostLiveDocumentRequest.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def id(self):
        """Gets the id of this PostLiveDocumentRequest.  # noqa: E501

        The Document ID of the Panviva Document you wish to send.  # noqa: E501

        :return: The id of this PostLiveDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PostLiveDocumentRequest.

        The Document ID of the Panviva Document you wish to send.  # noqa: E501

        :param id: The id of this PostLiveDocumentRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this PostLiveDocumentRequest.  # noqa: E501

        The Section ID you would like the user to see, when the specified document is opened.  # noqa: E501

        :return: The location of this PostLiveDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PostLiveDocumentRequest.

        The Section ID you would like the user to see, when the specified document is opened.  # noqa: E501

        :param location: The location of this PostLiveDocumentRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def maximize_client(self):
        """Gets the maximize_client of this PostLiveDocumentRequest.  # noqa: E501

        True/False depending on whether you want the Panviva client to maximize on the user's desktop, when the document is delivered.  # noqa: E501

        :return: The maximize_client of this PostLiveDocumentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._maximize_client

    @maximize_client.setter
    def maximize_client(self, maximize_client):
        """Sets the maximize_client of this PostLiveDocumentRequest.

        True/False depending on whether you want the Panviva client to maximize on the user's desktop, when the document is delivered.  # noqa: E501

        :param maximize_client: The maximize_client of this PostLiveDocumentRequest.  # noqa: E501
        :type: bool
        """

        self._maximize_client = maximize_client

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
        if issubclass(PostLiveDocumentRequest, dict):
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
        if not isinstance(other, PostLiveDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
