# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import argocd_client
from argocd_client.models.account_token import AccountToken  # noqa: E501
from argocd_client.rest import ApiException

class TestAccountToken(unittest.TestCase):
    """AccountToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.account_token.AccountToken()  # noqa: E501
        if include_optional :
            return AccountToken(
                expires_at = '0', 
                id = '0', 
                issued_at = '0'
            )
        else :
            return AccountToken(
        )

    def testAccountToken(self):
        """Test AccountToken"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
