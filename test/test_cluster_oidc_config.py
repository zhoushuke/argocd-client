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
from argocd_client.models.cluster_oidc_config import ClusterOIDCConfig  # noqa: E501
from argocd_client.rest import ApiException

class TestClusterOIDCConfig(unittest.TestCase):
    """ClusterOIDCConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClusterOIDCConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.cluster_oidc_config.ClusterOIDCConfig()  # noqa: E501
        if include_optional :
            return ClusterOIDCConfig(
                cli_client_id = '0', 
                client_id = '0', 
                id_token_claims = {
                    'key' : argocd_client.models.oidc_claim.oidcClaim(
                        essential = True, 
                        value = '0', 
                        values = [
                            '0'
                            ], )
                    }, 
                issuer = '0', 
                name = '0', 
                scopes = [
                    '0'
                    ]
            )
        else :
            return ClusterOIDCConfig(
        )

    def testClusterOIDCConfig(self):
        """Test ClusterOIDCConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
