# coding: utf-8

# flake8: noqa

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from argocd_client.api.account_service_api import AccountServiceApi
from argocd_client.api.application_service_api import ApplicationServiceApi
from argocd_client.api.certificate_service_api import CertificateServiceApi
from argocd_client.api.cluster_service_api import ClusterServiceApi
from argocd_client.api.gpg_key_service_api import GPGKeyServiceApi
from argocd_client.api.project_service_api import ProjectServiceApi
from argocd_client.api.repo_creds_service_api import RepoCredsServiceApi
from argocd_client.api.repository_service_api import RepositoryServiceApi
from argocd_client.api.session_service_api import SessionServiceApi
from argocd_client.api.settings_service_api import SettingsServiceApi
from argocd_client.api.version_service_api import VersionServiceApi

# import ApiClient
from argocd_client.api_client import ApiClient
from argocd_client.configuration import Configuration
from argocd_client.exceptions import OpenApiException
from argocd_client.exceptions import ApiTypeError
from argocd_client.exceptions import ApiValueError
from argocd_client.exceptions import ApiKeyError
from argocd_client.exceptions import ApiException
# import models into sdk package
from argocd_client.models.account_account import AccountAccount
from argocd_client.models.account_accounts_list import AccountAccountsList
from argocd_client.models.account_can_i_response import AccountCanIResponse
from argocd_client.models.account_create_token_request import AccountCreateTokenRequest
from argocd_client.models.account_create_token_response import AccountCreateTokenResponse
from argocd_client.models.account_token import AccountToken
from argocd_client.models.account_update_password_request import AccountUpdatePasswordRequest
from argocd_client.models.application_application_patch_request import ApplicationApplicationPatchRequest
from argocd_client.models.application_application_resource_response import ApplicationApplicationResourceResponse
from argocd_client.models.application_application_rollback_request import ApplicationApplicationRollbackRequest
from argocd_client.models.application_application_sync_request import ApplicationApplicationSyncRequest
from argocd_client.models.application_application_sync_window import ApplicationApplicationSyncWindow
from argocd_client.models.application_application_sync_windows_response import ApplicationApplicationSyncWindowsResponse
from argocd_client.models.application_log_entry import ApplicationLogEntry
from argocd_client.models.application_managed_resources_response import ApplicationManagedResourcesResponse
from argocd_client.models.application_resource_actions_list_response import ApplicationResourceActionsListResponse
from argocd_client.models.cluster_connector import ClusterConnector
from argocd_client.models.cluster_dex_config import ClusterDexConfig
from argocd_client.models.cluster_google_analytics_config import ClusterGoogleAnalyticsConfig
from argocd_client.models.cluster_help import ClusterHelp
from argocd_client.models.cluster_oidc_config import ClusterOIDCConfig
from argocd_client.models.cluster_plugin import ClusterPlugin
from argocd_client.models.cluster_settings import ClusterSettings
from argocd_client.models.gpgkey_gnu_pg_public_key_create_response import GpgkeyGnuPGPublicKeyCreateResponse
from argocd_client.models.oidc_claim import OidcClaim
from argocd_client.models.project_project_create_request import ProjectProjectCreateRequest
from argocd_client.models.project_project_token_create_request import ProjectProjectTokenCreateRequest
from argocd_client.models.project_project_token_response import ProjectProjectTokenResponse
from argocd_client.models.project_project_update_request import ProjectProjectUpdateRequest
from argocd_client.models.project_sync_windows_response import ProjectSyncWindowsResponse
from argocd_client.models.protobuf_any import ProtobufAny
from argocd_client.models.repository_app_info import RepositoryAppInfo
from argocd_client.models.repository_helm_app_spec import RepositoryHelmAppSpec
from argocd_client.models.repository_helm_chart import RepositoryHelmChart
from argocd_client.models.repository_helm_charts_response import RepositoryHelmChartsResponse
from argocd_client.models.repository_ksonnet_app_spec import RepositoryKsonnetAppSpec
from argocd_client.models.repository_ksonnet_environment import RepositoryKsonnetEnvironment
from argocd_client.models.repository_ksonnet_environment_destination import RepositoryKsonnetEnvironmentDestination
from argocd_client.models.repository_kustomize_app_spec import RepositoryKustomizeAppSpec
from argocd_client.models.repository_manifest_response import RepositoryManifestResponse
from argocd_client.models.repository_repo_app_details_query import RepositoryRepoAppDetailsQuery
from argocd_client.models.repository_repo_app_details_response import RepositoryRepoAppDetailsResponse
from argocd_client.models.repository_repo_apps_response import RepositoryRepoAppsResponse
from argocd_client.models.runtime_stream_error import RuntimeStreamError
from argocd_client.models.session_get_user_info_response import SessionGetUserInfoResponse
from argocd_client.models.session_session_create_request import SessionSessionCreateRequest
from argocd_client.models.session_session_response import SessionSessionResponse
from argocd_client.models.v1_event import V1Event
from argocd_client.models.v1_event_list import V1EventList
from argocd_client.models.v1_event_series import V1EventSeries
from argocd_client.models.v1_event_source import V1EventSource
from argocd_client.models.v1_fields_v1 import V1FieldsV1
from argocd_client.models.v1_group_kind import V1GroupKind
from argocd_client.models.v1_list_meta import V1ListMeta
from argocd_client.models.v1_load_balancer_ingress import V1LoadBalancerIngress
from argocd_client.models.v1_managed_fields_entry import V1ManagedFieldsEntry
from argocd_client.models.v1_micro_time import V1MicroTime
from argocd_client.models.v1_object_meta import V1ObjectMeta
from argocd_client.models.v1_object_reference import V1ObjectReference
from argocd_client.models.v1_owner_reference import V1OwnerReference
from argocd_client.models.v1_time import V1Time
from argocd_client.models.v1alpha1_aws_auth_config import V1alpha1AWSAuthConfig
from argocd_client.models.v1alpha1_app_project import V1alpha1AppProject
from argocd_client.models.v1alpha1_app_project_list import V1alpha1AppProjectList
from argocd_client.models.v1alpha1_app_project_spec import V1alpha1AppProjectSpec
from argocd_client.models.v1alpha1_app_project_status import V1alpha1AppProjectStatus
from argocd_client.models.v1alpha1_application import V1alpha1Application
from argocd_client.models.v1alpha1_application_condition import V1alpha1ApplicationCondition
from argocd_client.models.v1alpha1_application_destination import V1alpha1ApplicationDestination
from argocd_client.models.v1alpha1_application_list import V1alpha1ApplicationList
from argocd_client.models.v1alpha1_application_source import V1alpha1ApplicationSource
from argocd_client.models.v1alpha1_application_source_directory import V1alpha1ApplicationSourceDirectory
from argocd_client.models.v1alpha1_application_source_helm import V1alpha1ApplicationSourceHelm
from argocd_client.models.v1alpha1_application_source_jsonnet import V1alpha1ApplicationSourceJsonnet
from argocd_client.models.v1alpha1_application_source_ksonnet import V1alpha1ApplicationSourceKsonnet
from argocd_client.models.v1alpha1_application_source_kustomize import V1alpha1ApplicationSourceKustomize
from argocd_client.models.v1alpha1_application_source_plugin import V1alpha1ApplicationSourcePlugin
from argocd_client.models.v1alpha1_application_spec import V1alpha1ApplicationSpec
from argocd_client.models.v1alpha1_application_status import V1alpha1ApplicationStatus
from argocd_client.models.v1alpha1_application_summary import V1alpha1ApplicationSummary
from argocd_client.models.v1alpha1_application_tree import V1alpha1ApplicationTree
from argocd_client.models.v1alpha1_application_watch_event import V1alpha1ApplicationWatchEvent
from argocd_client.models.v1alpha1_backoff import V1alpha1Backoff
from argocd_client.models.v1alpha1_cluster import V1alpha1Cluster
from argocd_client.models.v1alpha1_cluster_cache_info import V1alpha1ClusterCacheInfo
from argocd_client.models.v1alpha1_cluster_config import V1alpha1ClusterConfig
from argocd_client.models.v1alpha1_cluster_info import V1alpha1ClusterInfo
from argocd_client.models.v1alpha1_cluster_list import V1alpha1ClusterList
from argocd_client.models.v1alpha1_command import V1alpha1Command
from argocd_client.models.v1alpha1_compared_to import V1alpha1ComparedTo
from argocd_client.models.v1alpha1_config_management_plugin import V1alpha1ConfigManagementPlugin
from argocd_client.models.v1alpha1_connection_state import V1alpha1ConnectionState
from argocd_client.models.v1alpha1_env_entry import V1alpha1EnvEntry
from argocd_client.models.v1alpha1_gnu_pg_public_key import V1alpha1GnuPGPublicKey
from argocd_client.models.v1alpha1_gnu_pg_public_key_list import V1alpha1GnuPGPublicKeyList
from argocd_client.models.v1alpha1_health_status import V1alpha1HealthStatus
from argocd_client.models.v1alpha1_helm_file_parameter import V1alpha1HelmFileParameter
from argocd_client.models.v1alpha1_helm_parameter import V1alpha1HelmParameter
from argocd_client.models.v1alpha1_info import V1alpha1Info
from argocd_client.models.v1alpha1_info_item import V1alpha1InfoItem
from argocd_client.models.v1alpha1_jwt_token import V1alpha1JWTToken
from argocd_client.models.v1alpha1_jwt_tokens import V1alpha1JWTTokens
from argocd_client.models.v1alpha1_jsonnet_var import V1alpha1JsonnetVar
from argocd_client.models.v1alpha1_known_type_field import V1alpha1KnownTypeField
from argocd_client.models.v1alpha1_ksonnet_parameter import V1alpha1KsonnetParameter
from argocd_client.models.v1alpha1_kustomize_options import V1alpha1KustomizeOptions
from argocd_client.models.v1alpha1_operation import V1alpha1Operation
from argocd_client.models.v1alpha1_operation_initiator import V1alpha1OperationInitiator
from argocd_client.models.v1alpha1_operation_state import V1alpha1OperationState
from argocd_client.models.v1alpha1_orphaned_resource_key import V1alpha1OrphanedResourceKey
from argocd_client.models.v1alpha1_orphaned_resources_monitor_settings import V1alpha1OrphanedResourcesMonitorSettings
from argocd_client.models.v1alpha1_override_ignore_diff import V1alpha1OverrideIgnoreDiff
from argocd_client.models.v1alpha1_project_role import V1alpha1ProjectRole
from argocd_client.models.v1alpha1_repo_creds import V1alpha1RepoCreds
from argocd_client.models.v1alpha1_repo_creds_list import V1alpha1RepoCredsList
from argocd_client.models.v1alpha1_repository import V1alpha1Repository
from argocd_client.models.v1alpha1_repository_certificate import V1alpha1RepositoryCertificate
from argocd_client.models.v1alpha1_repository_certificate_list import V1alpha1RepositoryCertificateList
from argocd_client.models.v1alpha1_repository_list import V1alpha1RepositoryList
from argocd_client.models.v1alpha1_resource_action import V1alpha1ResourceAction
from argocd_client.models.v1alpha1_resource_action_param import V1alpha1ResourceActionParam
from argocd_client.models.v1alpha1_resource_diff import V1alpha1ResourceDiff
from argocd_client.models.v1alpha1_resource_ignore_differences import V1alpha1ResourceIgnoreDifferences
from argocd_client.models.v1alpha1_resource_networking_info import V1alpha1ResourceNetworkingInfo
from argocd_client.models.v1alpha1_resource_node import V1alpha1ResourceNode
from argocd_client.models.v1alpha1_resource_override import V1alpha1ResourceOverride
from argocd_client.models.v1alpha1_resource_ref import V1alpha1ResourceRef
from argocd_client.models.v1alpha1_resource_result import V1alpha1ResourceResult
from argocd_client.models.v1alpha1_resource_status import V1alpha1ResourceStatus
from argocd_client.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from argocd_client.models.v1alpha1_revision_history import V1alpha1RevisionHistory
from argocd_client.models.v1alpha1_revision_metadata import V1alpha1RevisionMetadata
from argocd_client.models.v1alpha1_signature_key import V1alpha1SignatureKey
from argocd_client.models.v1alpha1_sync_operation import V1alpha1SyncOperation
from argocd_client.models.v1alpha1_sync_operation_resource import V1alpha1SyncOperationResource
from argocd_client.models.v1alpha1_sync_operation_result import V1alpha1SyncOperationResult
from argocd_client.models.v1alpha1_sync_policy import V1alpha1SyncPolicy
from argocd_client.models.v1alpha1_sync_policy_automated import V1alpha1SyncPolicyAutomated
from argocd_client.models.v1alpha1_sync_status import V1alpha1SyncStatus
from argocd_client.models.v1alpha1_sync_strategy import V1alpha1SyncStrategy
from argocd_client.models.v1alpha1_sync_strategy_apply import V1alpha1SyncStrategyApply
from argocd_client.models.v1alpha1_sync_strategy_hook import V1alpha1SyncStrategyHook
from argocd_client.models.v1alpha1_sync_window import V1alpha1SyncWindow
from argocd_client.models.v1alpha1_tls_client_config import V1alpha1TLSClientConfig
from argocd_client.models.version_version_message import VersionVersionMessage

