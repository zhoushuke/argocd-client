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


class V1alpha1OperationInitiator(object):
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
        'automated': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'automated': 'automated',
        'username': 'username'
    }

    def __init__(self, automated=None, username=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1OperationInitiator - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._automated = None
        self._username = None
        self.discriminator = None

        if automated is not None:
            self.automated = automated
        if username is not None:
            self.username = username

    @property
    def automated(self):
        """Gets the automated of this V1alpha1OperationInitiator.  # noqa: E501

        Automated is set to true if operation was initiated automatically by the application controller.  # noqa: E501

        :return: The automated of this V1alpha1OperationInitiator.  # noqa: E501
        :rtype: bool
        """
        return self._automated

    @automated.setter
    def automated(self, automated):
        """Sets the automated of this V1alpha1OperationInitiator.

        Automated is set to true if operation was initiated automatically by the application controller.  # noqa: E501

        :param automated: The automated of this V1alpha1OperationInitiator.  # noqa: E501
        :type: bool
        """

        self._automated = automated

    @property
    def username(self):
        """Gets the username of this V1alpha1OperationInitiator.  # noqa: E501

        Name of a user who started operation.  # noqa: E501

        :return: The username of this V1alpha1OperationInitiator.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1alpha1OperationInitiator.

        Name of a user who started operation.  # noqa: E501

        :param username: The username of this V1alpha1OperationInitiator.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, V1alpha1OperationInitiator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1OperationInitiator):
            return True

        return self.to_dict() != other.to_dict()
