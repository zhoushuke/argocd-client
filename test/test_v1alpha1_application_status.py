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
from argocd_client.models.v1alpha1_application_status import V1alpha1ApplicationStatus  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1ApplicationStatus(unittest.TestCase):
    """V1alpha1ApplicationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ApplicationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_application_status.V1alpha1ApplicationStatus()  # noqa: E501
        if include_optional :
            return V1alpha1ApplicationStatus(
                conditions = [
                    argocd_client.models.application_condition_contains_details_about_current_application_condition.ApplicationCondition contains details about current application condition(
                        last_transition_time = argocd_client.models.v1_time.v1Time(
                            nanos = 56, 
                            seconds = '0', ), 
                        message = '0', 
                        type = '0', )
                    ], 
                health = argocd_client.models.v1alpha1_health_status.v1alpha1HealthStatus(
                    message = '0', 
                    status = '0', ), 
                history = [
                    argocd_client.models.revision_history_contains_information_relevant_to_an_application_deployment.RevisionHistory contains information relevant to an application deployment(
                        deploy_started_at = argocd_client.models.v1_time.v1Time(
                            nanos = 56, 
                            seconds = '0', ), 
                        deployed_at = argocd_client.models.v1_time.v1Time(
                            nanos = 56, 
                            seconds = '0', ), 
                        id = '0', 
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
                            target_revision = '0', ), )
                    ], 
                observed_at = argocd_client.models.v1_time.v1Time(
                    nanos = 56, 
                    seconds = '0', ), 
                operation_state = argocd_client.models.v1alpha1_operation_state.v1alpha1OperationState(
                    finished_at = argocd_client.models.v1_time.v1Time(
                        nanos = 56, 
                        seconds = '0', ), 
                    message = '0', 
                    operation = argocd_client.models.v1alpha1_operation.v1alpha1Operation(
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
                                        force = True, ), ), ), ), ), 
                    phase = '0', 
                    retry_count = '0', 
                    started_at = argocd_client.models.v1_time.v1Time(
                        nanos = 56, 
                        seconds = '0', ), 
                    sync_result = argocd_client.models.sync_operation_result_represent_result_of_sync_operation.SyncOperationResult represent result of sync operation(
                        resources = [
                            argocd_client.models.resource_result_holds_the_operation_result_details_of_a_specific_resource.ResourceResult holds the operation result details of a specific resource(
                                group = '0', 
                                hook_phase = '0', 
                                hook_type = '0', 
                                kind = '0', 
                                message = '0', 
                                name = '0', 
                                namespace = '0', 
                                status = '0', 
                                sync_phase = '0', 
                                version = '0', )
                            ], 
                        revision = '0', ), ), 
                reconciled_at = argocd_client.models.v1_time.v1Time(
                    nanos = 56, 
                    seconds = '0', ), 
                resources = [
                    argocd_client.models.resource_status_holds_the_current_sync_and_health_status_of_a_resource.ResourceStatus holds the current sync and health status of a resource(
                        group = '0', 
                        health = argocd_client.models.v1alpha1_health_status.v1alpha1HealthStatus(
                            message = '0', 
                            status = '0', ), 
                        hook = True, 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        requires_pruning = True, 
                        status = '0', 
                        version = '0', )
                    ], 
                source_type = '0', 
                summary = argocd_client.models.v1alpha1_application_summary.v1alpha1ApplicationSummary(
                    external_ur_ls = [
                        '0'
                        ], 
                    images = [
                        '0'
                        ], ), 
                sync = argocd_client.models.v1alpha1_sync_status.v1alpha1SyncStatus(
                    compared_to = argocd_client.models.compared_to_contains_application_source_and_target_which_was_used_for_resources_comparison.ComparedTo contains application source and target which was used for resources comparison(
                        destination = argocd_client.models.application_destination_contains_deployment_destination_information.ApplicationDestination contains deployment destination information(
                            name = '0', 
                            namespace = '0', 
                            server = '0', ), 
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
                            target_revision = '0', ), ), 
                    revision = '0', 
                    status = '0', )
            )
        else :
            return V1alpha1ApplicationStatus(
        )

    def testV1alpha1ApplicationStatus(self):
        """Test V1alpha1ApplicationStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()