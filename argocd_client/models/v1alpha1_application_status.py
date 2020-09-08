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


class V1alpha1ApplicationStatus(object):
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
        'conditions': 'list[V1alpha1ApplicationCondition]',
        'health': 'V1alpha1HealthStatus',
        'history': 'list[V1alpha1RevisionHistory]',
        'observed_at': 'V1Time',
        'operation_state': 'V1alpha1OperationState',
        'reconciled_at': 'V1Time',
        'resources': 'list[V1alpha1ResourceStatus]',
        'source_type': 'str',
        'summary': 'V1alpha1ApplicationSummary',
        'sync': 'V1alpha1SyncStatus'
    }

    attribute_map = {
        'conditions': 'conditions',
        'health': 'health',
        'history': 'history',
        'observed_at': 'observedAt',
        'operation_state': 'operationState',
        'reconciled_at': 'reconciledAt',
        'resources': 'resources',
        'source_type': 'sourceType',
        'summary': 'summary',
        'sync': 'sync'
    }

    def __init__(self, conditions=None, health=None, history=None, observed_at=None, operation_state=None, reconciled_at=None, resources=None, source_type=None, summary=None, sync=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ApplicationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._health = None
        self._history = None
        self._observed_at = None
        self._operation_state = None
        self._reconciled_at = None
        self._resources = None
        self._source_type = None
        self._summary = None
        self._sync = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if health is not None:
            self.health = health
        if history is not None:
            self.history = history
        if observed_at is not None:
            self.observed_at = observed_at
        if operation_state is not None:
            self.operation_state = operation_state
        if reconciled_at is not None:
            self.reconciled_at = reconciled_at
        if resources is not None:
            self.resources = resources
        if source_type is not None:
            self.source_type = source_type
        if summary is not None:
            self.summary = summary
        if sync is not None:
            self.sync = sync

    @property
    def conditions(self):
        """Gets the conditions of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The conditions of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: list[V1alpha1ApplicationCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1alpha1ApplicationStatus.


        :param conditions: The conditions of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: list[V1alpha1ApplicationCondition]
        """

        self._conditions = conditions

    @property
    def health(self):
        """Gets the health of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The health of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: V1alpha1HealthStatus
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this V1alpha1ApplicationStatus.


        :param health: The health of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: V1alpha1HealthStatus
        """

        self._health = health

    @property
    def history(self):
        """Gets the history of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The history of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: list[V1alpha1RevisionHistory]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this V1alpha1ApplicationStatus.


        :param history: The history of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: list[V1alpha1RevisionHistory]
        """

        self._history = history

    @property
    def observed_at(self):
        """Gets the observed_at of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The observed_at of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._observed_at

    @observed_at.setter
    def observed_at(self, observed_at):
        """Sets the observed_at of this V1alpha1ApplicationStatus.


        :param observed_at: The observed_at of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: V1Time
        """

        self._observed_at = observed_at

    @property
    def operation_state(self):
        """Gets the operation_state of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The operation_state of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: V1alpha1OperationState
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        """Sets the operation_state of this V1alpha1ApplicationStatus.


        :param operation_state: The operation_state of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: V1alpha1OperationState
        """

        self._operation_state = operation_state

    @property
    def reconciled_at(self):
        """Gets the reconciled_at of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The reconciled_at of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._reconciled_at

    @reconciled_at.setter
    def reconciled_at(self, reconciled_at):
        """Sets the reconciled_at of this V1alpha1ApplicationStatus.


        :param reconciled_at: The reconciled_at of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: V1Time
        """

        self._reconciled_at = reconciled_at

    @property
    def resources(self):
        """Gets the resources of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The resources of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: list[V1alpha1ResourceStatus]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1alpha1ApplicationStatus.


        :param resources: The resources of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: list[V1alpha1ResourceStatus]
        """

        self._resources = resources

    @property
    def source_type(self):
        """Gets the source_type of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The source_type of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this V1alpha1ApplicationStatus.


        :param source_type: The source_type of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: str
        """

        self._source_type = source_type

    @property
    def summary(self):
        """Gets the summary of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The summary of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: V1alpha1ApplicationSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this V1alpha1ApplicationStatus.


        :param summary: The summary of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: V1alpha1ApplicationSummary
        """

        self._summary = summary

    @property
    def sync(self):
        """Gets the sync of this V1alpha1ApplicationStatus.  # noqa: E501


        :return: The sync of this V1alpha1ApplicationStatus.  # noqa: E501
        :rtype: V1alpha1SyncStatus
        """
        return self._sync

    @sync.setter
    def sync(self, sync):
        """Sets the sync of this V1alpha1ApplicationStatus.


        :param sync: The sync of this V1alpha1ApplicationStatus.  # noqa: E501
        :type: V1alpha1SyncStatus
        """

        self._sync = sync

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
        if not isinstance(other, V1alpha1ApplicationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ApplicationStatus):
            return True

        return self.to_dict() != other.to_dict()
