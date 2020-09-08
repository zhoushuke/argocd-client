# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argocd_client.configuration import Configuration


class V1alpha1AppProjectSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cluster_resource_blacklist': 'list[V1GroupKind]',
        'cluster_resource_whitelist': 'list[V1GroupKind]',
        'description': 'str',
        'destinations': 'list[V1alpha1ApplicationDestination]',
        'namespace_resource_blacklist': 'list[V1GroupKind]',
        'namespace_resource_whitelist': 'list[V1GroupKind]',
        'orphaned_resources': 'V1alpha1OrphanedResourcesMonitorSettings',
        'roles': 'list[V1alpha1ProjectRole]',
        'signature_keys': 'list[V1alpha1SignatureKey]',
        'source_repos': 'list[str]',
        'sync_windows': 'list[V1alpha1SyncWindow]'
    }

    attribute_map = {
        'cluster_resource_blacklist': 'clusterResourceBlacklist',
        'cluster_resource_whitelist': 'clusterResourceWhitelist',
        'description': 'description',
        'destinations': 'destinations',
        'namespace_resource_blacklist': 'namespaceResourceBlacklist',
        'namespace_resource_whitelist': 'namespaceResourceWhitelist',
        'orphaned_resources': 'orphanedResources',
        'roles': 'roles',
        'signature_keys': 'signatureKeys',
        'source_repos': 'sourceRepos',
        'sync_windows': 'syncWindows'
    }

    def __init__(self, cluster_resource_blacklist=None, cluster_resource_whitelist=None, description=None, destinations=None, namespace_resource_blacklist=None, namespace_resource_whitelist=None, orphaned_resources=None, roles=None, signature_keys=None, source_repos=None, sync_windows=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1AppProjectSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_resource_blacklist = None
        self._cluster_resource_whitelist = None
        self._description = None
        self._destinations = None
        self._namespace_resource_blacklist = None
        self._namespace_resource_whitelist = None
        self._orphaned_resources = None
        self._roles = None
        self._signature_keys = None
        self._source_repos = None
        self._sync_windows = None
        self.discriminator = None

        if cluster_resource_blacklist is not None:
            self.cluster_resource_blacklist = cluster_resource_blacklist
        if cluster_resource_whitelist is not None:
            self.cluster_resource_whitelist = cluster_resource_whitelist
        if description is not None:
            self.description = description
        if destinations is not None:
            self.destinations = destinations
        if namespace_resource_blacklist is not None:
            self.namespace_resource_blacklist = namespace_resource_blacklist
        if namespace_resource_whitelist is not None:
            self.namespace_resource_whitelist = namespace_resource_whitelist
        if orphaned_resources is not None:
            self.orphaned_resources = orphaned_resources
        if roles is not None:
            self.roles = roles
        if signature_keys is not None:
            self.signature_keys = signature_keys
        if source_repos is not None:
            self.source_repos = source_repos
        if sync_windows is not None:
            self.sync_windows = sync_windows

    @property
    def cluster_resource_blacklist(self):
        """Gets the cluster_resource_blacklist of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The cluster_resource_blacklist of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._cluster_resource_blacklist

    @cluster_resource_blacklist.setter
    def cluster_resource_blacklist(self, cluster_resource_blacklist):
        """Sets the cluster_resource_blacklist of this V1alpha1AppProjectSpec.


        :param cluster_resource_blacklist: The cluster_resource_blacklist of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._cluster_resource_blacklist = cluster_resource_blacklist

    @property
    def cluster_resource_whitelist(self):
        """Gets the cluster_resource_whitelist of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The cluster_resource_whitelist of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._cluster_resource_whitelist

    @cluster_resource_whitelist.setter
    def cluster_resource_whitelist(self, cluster_resource_whitelist):
        """Sets the cluster_resource_whitelist of this V1alpha1AppProjectSpec.


        :param cluster_resource_whitelist: The cluster_resource_whitelist of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._cluster_resource_whitelist = cluster_resource_whitelist

    @property
    def description(self):
        """Gets the description of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The description of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1alpha1AppProjectSpec.


        :param description: The description of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destinations(self):
        """Gets the destinations of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The destinations of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1alpha1ApplicationDestination]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this V1alpha1AppProjectSpec.


        :param destinations: The destinations of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1alpha1ApplicationDestination]
        """

        self._destinations = destinations

    @property
    def namespace_resource_blacklist(self):
        """Gets the namespace_resource_blacklist of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The namespace_resource_blacklist of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._namespace_resource_blacklist

    @namespace_resource_blacklist.setter
    def namespace_resource_blacklist(self, namespace_resource_blacklist):
        """Sets the namespace_resource_blacklist of this V1alpha1AppProjectSpec.


        :param namespace_resource_blacklist: The namespace_resource_blacklist of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._namespace_resource_blacklist = namespace_resource_blacklist

    @property
    def namespace_resource_whitelist(self):
        """Gets the namespace_resource_whitelist of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The namespace_resource_whitelist of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1GroupKind]
        """
        return self._namespace_resource_whitelist

    @namespace_resource_whitelist.setter
    def namespace_resource_whitelist(self, namespace_resource_whitelist):
        """Sets the namespace_resource_whitelist of this V1alpha1AppProjectSpec.


        :param namespace_resource_whitelist: The namespace_resource_whitelist of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1GroupKind]
        """

        self._namespace_resource_whitelist = namespace_resource_whitelist

    @property
    def orphaned_resources(self):
        """Gets the orphaned_resources of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The orphaned_resources of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: V1alpha1OrphanedResourcesMonitorSettings
        """
        return self._orphaned_resources

    @orphaned_resources.setter
    def orphaned_resources(self, orphaned_resources):
        """Sets the orphaned_resources of this V1alpha1AppProjectSpec.


        :param orphaned_resources: The orphaned_resources of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: V1alpha1OrphanedResourcesMonitorSettings
        """

        self._orphaned_resources = orphaned_resources

    @property
    def roles(self):
        """Gets the roles of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The roles of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1alpha1ProjectRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this V1alpha1AppProjectSpec.


        :param roles: The roles of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1alpha1ProjectRole]
        """

        self._roles = roles

    @property
    def signature_keys(self):
        """Gets the signature_keys of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The signature_keys of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1alpha1SignatureKey]
        """
        return self._signature_keys

    @signature_keys.setter
    def signature_keys(self, signature_keys):
        """Sets the signature_keys of this V1alpha1AppProjectSpec.


        :param signature_keys: The signature_keys of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1alpha1SignatureKey]
        """

        self._signature_keys = signature_keys

    @property
    def source_repos(self):
        """Gets the source_repos of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The source_repos of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_repos

    @source_repos.setter
    def source_repos(self, source_repos):
        """Sets the source_repos of this V1alpha1AppProjectSpec.


        :param source_repos: The source_repos of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[str]
        """

        self._source_repos = source_repos

    @property
    def sync_windows(self):
        """Gets the sync_windows of this V1alpha1AppProjectSpec.  # noqa: E501


        :return: The sync_windows of this V1alpha1AppProjectSpec.  # noqa: E501
        :rtype: list[V1alpha1SyncWindow]
        """
        return self._sync_windows

    @sync_windows.setter
    def sync_windows(self, sync_windows):
        """Sets the sync_windows of this V1alpha1AppProjectSpec.


        :param sync_windows: The sync_windows of this V1alpha1AppProjectSpec.  # noqa: E501
        :type: list[V1alpha1SyncWindow]
        """

        self._sync_windows = sync_windows

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1AppProjectSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1AppProjectSpec):
            return True

        return self.to_dict() != other.to_dict()
