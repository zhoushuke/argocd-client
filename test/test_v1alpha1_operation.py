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
from argocd_client.models.v1alpha1_operation import V1alpha1Operation  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1Operation(unittest.TestCase):
    """V1alpha1Operation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1Operation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_operation.V1alpha1Operation()  # noqa: E501
        if include_optional :
            return V1alpha1Operation(
                info = [
                    argocd_client.models.v1alpha1_info.v1alpha1Info(
                        name = '0', 
                        value = '0', )
                    ], 
                initiated_by = argocd_client.models.operation_initiator_holds_information_about_the_operation_initiator.OperationInitiator holds information about the operation initiator(
                    automated = True, 
                    username = '0', ), 
                retry = argocd_client.models.v1alpha1_retry_strategy.v1alpha1RetryStrategy(
                    backoff = argocd_client.models.backoff_is_a_backoff_strategy_to_use_within_retry_strategy.Backoff is a backoff strategy to use within retryStrategy(
                        duration = '0', 
                        factor = '0', 
                        max_duration = '0', ), 
                    limit = '0', ), 
                sync = argocd_client.models.v1alpha1_sync_operation.v1alpha1SyncOperation(
                    dry_run = True, 
                    manifests = [
                        '0'
                        ], 
                    prune = True, 
                    resources = [
                        argocd_client.models.v1alpha1_sync_operation_resource.v1alpha1SyncOperationResource(
                            group = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', )
                        ], 
                    revision = '0', 
                    source = argocd_client.models.v1alpha1_application_source.v1alpha1ApplicationSource(
                        chart = '0', 
                        directory = argocd_client.models.v1alpha1_application_source_directory.v1alpha1ApplicationSourceDirectory(
                            jsonnet = argocd_client.models.application_source_jsonnet_holds_jsonnet_specific_options.ApplicationSourceJsonnet holds jsonnet specific options(
                                ext_vars = [
                                    argocd_client.models.jsonnet_var_is_a_jsonnet_variable.JsonnetVar is a jsonnet variable(
                                        code = True, 
                                        name = '0', 
                                        value = '0', )
                                    ], 
                                libs = [
                                    '0'
                                    ], 
                                tlas = [
                                    argocd_client.models.jsonnet_var_is_a_jsonnet_variable.JsonnetVar is a jsonnet variable(
                                        code = True, 
                                        name = '0', 
                                        value = '0', )
                                    ], ), 
                            recurse = True, ), 
                        helm = argocd_client.models.application_source_helm_holds_helm_specific_options.ApplicationSourceHelm holds helm specific options(
                            file_parameters = [
                                argocd_client.models.helm_file_parameter_is_a_file_parameter_to_a_helm_template.HelmFileParameter is a file parameter to a helm template(
                                    name = '0', 
                                    path = '0', )
                                ], 
                            parameters = [
                                argocd_client.models.helm_parameter_is_a_parameter_to_a_helm_template.HelmParameter is a parameter to a helm template(
                                    force_string = True, 
                                    name = '0', 
                                    value = '0', )
                                ], 
                            release_name = '0', 
                            value_files = [
                                '0'
                                ], 
                            values = '0', ), 
                        ksonnet = argocd_client.models.application_source_ksonnet_holds_ksonnet_specific_options.ApplicationSourceKsonnet holds ksonnet specific options(
                            environment = '0', 
                            parameters = [
                                argocd_client.models.ksonnet_parameter_is_a_ksonnet_component_parameter.KsonnetParameter is a ksonnet component parameter(
                                    component = '0', 
                                    name = '0', 
                                    value = '0', )
                                ], ), 
                        kustomize = argocd_client.models.application_source_kustomize_holds_kustomize_specific_options.ApplicationSourceKustomize holds kustomize specific options(
                            common_labels = {
                                'key' : '0'
                                }, 
                            images = [
                                '0'
                                ], 
                            name_prefix = '0', 
                            name_suffix = '0', 
                            version = '0', ), 
                        path = '0', 
                        plugin = argocd_client.models.application_source_plugin_holds_config_management_plugin_specific_options.ApplicationSourcePlugin holds config management plugin specific options(
                            env = [
                                argocd_client.models.v1alpha1_env_entry.v1alpha1EnvEntry(
                                    name = '0', 
                                    value = '0', )
                                ], 
                            name = '0', ), 
                        repo_url = '0', 
                        target_revision = '0', ), 
                    sync_options = [
                        '0'
                        ], 
                    sync_strategy = argocd_client.models.sync_strategy_controls_the_manner_in_which_a_sync_is_performed.SyncStrategy controls the manner in which a sync is performed(
                        apply = argocd_client.models.sync_strategy_apply_uses_`kubectl_apply`_to_perform_the_apply.SyncStrategyApply uses `kubectl apply` to perform the apply(
                            force = True, ), 
                        hook = argocd_client.models.v1alpha1_sync_strategy_hook.v1alpha1SyncStrategyHook(
                            sync_strategy_apply = argocd_client.models.sync_strategy_apply_uses_`kubectl_apply`_to_perform_the_apply.SyncStrategyApply uses `kubectl apply` to perform the apply(
                                force = True, ), ), ), )
            )
        else :
            return V1alpha1Operation(
        )

    def testV1alpha1Operation(self):
        """Test V1alpha1Operation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
