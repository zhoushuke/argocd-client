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
from argocd_client.models.v1_managed_fields_entry import V1ManagedFieldsEntry  # noqa: E501
from argocd_client.rest import ApiException

class TestV1ManagedFieldsEntry(unittest.TestCase):
    """V1ManagedFieldsEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ManagedFieldsEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1_managed_fields_entry.V1ManagedFieldsEntry()  # noqa: E501
        if include_optional :
            return V1ManagedFieldsEntry(
                api_version = '0', 
                fields_type = '0', 
                fields_v1 = argocd_client.models.v1_fields_v1.v1FieldsV1(
                    raw = 'YQ==', ), 
                manager = '0', 
                operation = '0', 
                time = argocd_client.models.v1_time.v1Time(
                    nanos = 56, 
                    seconds = '0', )
            )
        else :
            return V1ManagedFieldsEntry(
        )

    def testV1ManagedFieldsEntry(self):
        """Test V1ManagedFieldsEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
