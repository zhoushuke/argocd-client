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
from argocd_client.models.v1alpha1_gnu_pg_public_key import V1alpha1GnuPGPublicKey  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1GnuPGPublicKey(unittest.TestCase):
    """V1alpha1GnuPGPublicKey unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1GnuPGPublicKey
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_gnu_pg_public_key.V1alpha1GnuPGPublicKey()  # noqa: E501
        if include_optional :
            return V1alpha1GnuPGPublicKey(
                fingerprint = '0', 
                key_data = '0', 
                key_id = '0', 
                owner = '0', 
                sub_type = '0', 
                trust = '0'
            )
        else :
            return V1alpha1GnuPGPublicKey(
        )

    def testV1alpha1GnuPGPublicKey(self):
        """Test V1alpha1GnuPGPublicKey"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()