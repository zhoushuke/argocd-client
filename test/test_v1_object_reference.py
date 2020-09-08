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
from argocd_client.models.v1_object_reference import V1ObjectReference  # noqa: E501
from argocd_client.rest import ApiException

class TestV1ObjectReference(unittest.TestCase):
    """V1ObjectReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ObjectReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1_object_reference.V1ObjectReference()  # noqa: E501
        if include_optional :
            return V1ObjectReference(
                api_version = '0', 
                field_path = '0', 
                kind = '0', 
                name = '0', 
                namespace = '0', 
                resource_version = '0', 
                uid = '0'
            )
        else :
            return V1ObjectReference(
        )

    def testV1ObjectReference(self):
        """Test V1ObjectReference"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
