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
from argocd_client.models.project_sync_windows_response import ProjectSyncWindowsResponse  # noqa: E501
from argocd_client.rest import ApiException

class TestProjectSyncWindowsResponse(unittest.TestCase):
    """ProjectSyncWindowsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectSyncWindowsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.project_sync_windows_response.ProjectSyncWindowsResponse()  # noqa: E501
        if include_optional :
            return ProjectSyncWindowsResponse(
                windows = [
                    argocd_client.models.sync_window_contains_the_kind,_time,_duration_and_attributes_that_are_used_to_assign_the_sync_windows_to_apps.SyncWindow contains the kind, time, duration and attributes that are used to assign the syncWindows to apps(
                        applications = [
                            '0'
                            ], 
                        clusters = [
                            '0'
                            ], 
                        duration = '0', 
                        kind = '0', 
                        manual_sync = True, 
                        namespaces = [
                            '0'
                            ], 
                        schedule = '0', )
                    ]
            )
        else :
            return ProjectSyncWindowsResponse(
        )

    def testProjectSyncWindowsResponse(self):
        """Test ProjectSyncWindowsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
