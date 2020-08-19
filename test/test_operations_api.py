# coding: utf-8

"""
    Panviva API Suite v3

    Wouldn't it be great if you could share information seamlessly? This connector allows you to push your knowledge further and consume a complete list of Panviva's API offerings.  **Content APIs** perform resource related operations , e.g. `document`, `folder`, `file`, `container`, `image`.  **Live APIs** enable real-time communications with online users on our client application.  **Artefact APIs** interact with curated Panviva content, created by the Digital Orchestrator.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@panviva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import panviva
from panviva.api.operations_api import OperationsApi  # noqa: E501
from panviva.rest import ApiException


class TestOperationsApi(unittest.TestCase):
    """OperationsApi unit test stubs"""

    def setUp(self):
        self.api = panviva.api.operations_api.OperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_operations_artefact_nls(self):
        """Test case for operations_artefact_nls

        Search Artefacts  # noqa: E501
        """
        pass

    def test_operations_live_csh(self):
        """Test case for operations_live_csh

        Live CSH  # noqa: E501
        """
        pass

    def test_operations_live_document(self):
        """Test case for operations_live_document

        Live Document  # noqa: E501
        """
        pass

    def test_operations_live_search(self):
        """Test case for operations_live_search

        Live Search  # noqa: E501
        """
        pass

    def test_operations_search(self):
        """Test case for operations_search

        Search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
