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


class SearchResult(object):
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
        'content': 'list[ResponseSection]',
        'category': 'Category',
        'meta_data': 'dict(str, MetaDataValueDetails)',
        'search_score': 'float',
        'links': 'list[Link]',
        'query_variations': 'list[QueryVariation]',
        'primary_query': 'str',
        'panviva_document_id': 'int',
        'panviva_document_version': 'int',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'content': 'content',
        'category': 'category',
        'meta_data': 'metaData',
        'search_score': 'searchScore',
        'links': 'links',
        'query_variations': 'queryVariations',
        'primary_query': 'primaryQuery',
        'panviva_document_id': 'panvivaDocumentId',
        'panviva_document_version': 'panvivaDocumentVersion',
        'title': 'title'
    }

    def __init__(self, id=None, content=None, category=None, meta_data=None, search_score=None, links=None, query_variations=None, primary_query=None, panviva_document_id=None, panviva_document_version=None, title=None):  # noqa: E501
        """SearchResult - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._content = None
        self._category = None
        self._meta_data = None
        self._search_score = None
        self._links = None
        self._query_variations = None
        self._primary_query = None
        self._panviva_document_id = None
        self._panviva_document_version = None
        self._title = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if content is not None:
            self.content = content
        if category is not None:
            self.category = category
        if meta_data is not None:
            self.meta_data = meta_data
        if search_score is not None:
            self.search_score = search_score
        if links is not None:
            self.links = links
        if query_variations is not None:
            self.query_variations = query_variations
        if primary_query is not None:
            self.primary_query = primary_query
        if panviva_document_id is not None:
            self.panviva_document_id = panviva_document_id
        if panviva_document_version is not None:
            self.panviva_document_version = panviva_document_version
        if title is not None:
            self.title = title

    @property
    def id(self):
        """Gets the id of this SearchResult.  # noqa: E501


        :return: The id of this SearchResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchResult.


        :param id: The id of this SearchResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def content(self):
        """Gets the content of this SearchResult.  # noqa: E501


        :return: The content of this SearchResult.  # noqa: E501
        :rtype: list[ResponseSection]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SearchResult.


        :param content: The content of this SearchResult.  # noqa: E501
        :type: list[ResponseSection]
        """

        self._content = content

    @property
    def category(self):
        """Gets the category of this SearchResult.  # noqa: E501


        :return: The category of this SearchResult.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SearchResult.


        :param category: The category of this SearchResult.  # noqa: E501
        :type: Category
        """

        self._category = category

    @property
    def meta_data(self):
        """Gets the meta_data of this SearchResult.  # noqa: E501


        :return: The meta_data of this SearchResult.  # noqa: E501
        :rtype: dict(str, MetaDataValueDetails)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this SearchResult.


        :param meta_data: The meta_data of this SearchResult.  # noqa: E501
        :type: dict(str, MetaDataValueDetails)
        """

        self._meta_data = meta_data

    @property
    def search_score(self):
        """Gets the search_score of this SearchResult.  # noqa: E501


        :return: The search_score of this SearchResult.  # noqa: E501
        :rtype: float
        """
        return self._search_score

    @search_score.setter
    def search_score(self, search_score):
        """Sets the search_score of this SearchResult.


        :param search_score: The search_score of this SearchResult.  # noqa: E501
        :type: float
        """

        self._search_score = search_score

    @property
    def links(self):
        """Gets the links of this SearchResult.  # noqa: E501


        :return: The links of this SearchResult.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SearchResult.


        :param links: The links of this SearchResult.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def query_variations(self):
        """Gets the query_variations of this SearchResult.  # noqa: E501


        :return: The query_variations of this SearchResult.  # noqa: E501
        :rtype: list[QueryVariation]
        """
        return self._query_variations

    @query_variations.setter
    def query_variations(self, query_variations):
        """Sets the query_variations of this SearchResult.


        :param query_variations: The query_variations of this SearchResult.  # noqa: E501
        :type: list[QueryVariation]
        """

        self._query_variations = query_variations

    @property
    def primary_query(self):
        """Gets the primary_query of this SearchResult.  # noqa: E501


        :return: The primary_query of this SearchResult.  # noqa: E501
        :rtype: str
        """
        return self._primary_query

    @primary_query.setter
    def primary_query(self, primary_query):
        """Sets the primary_query of this SearchResult.


        :param primary_query: The primary_query of this SearchResult.  # noqa: E501
        :type: str
        """

        self._primary_query = primary_query

    @property
    def panviva_document_id(self):
        """Gets the panviva_document_id of this SearchResult.  # noqa: E501


        :return: The panviva_document_id of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._panviva_document_id

    @panviva_document_id.setter
    def panviva_document_id(self, panviva_document_id):
        """Sets the panviva_document_id of this SearchResult.


        :param panviva_document_id: The panviva_document_id of this SearchResult.  # noqa: E501
        :type: int
        """

        self._panviva_document_id = panviva_document_id

    @property
    def panviva_document_version(self):
        """Gets the panviva_document_version of this SearchResult.  # noqa: E501


        :return: The panviva_document_version of this SearchResult.  # noqa: E501
        :rtype: int
        """
        return self._panviva_document_version

    @panviva_document_version.setter
    def panviva_document_version(self, panviva_document_version):
        """Sets the panviva_document_version of this SearchResult.


        :param panviva_document_version: The panviva_document_version of this SearchResult.  # noqa: E501
        :type: int
        """

        self._panviva_document_version = panviva_document_version

    @property
    def title(self):
        """Gets the title of this SearchResult.  # noqa: E501


        :return: The title of this SearchResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SearchResult.


        :param title: The title of this SearchResult.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(SearchResult, dict):
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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
