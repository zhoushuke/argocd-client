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


class RepositoryRepoAppDetailsResponse(object):
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
        'directory': 'object',
        'helm': 'RepositoryHelmAppSpec',
        'ksonnet': 'RepositoryKsonnetAppSpec',
        'kustomize': 'RepositoryKustomizeAppSpec',
        'type': 'str'
    }

    attribute_map = {
        'directory': 'directory',
        'helm': 'helm',
        'ksonnet': 'ksonnet',
        'kustomize': 'kustomize',
        'type': 'type'
    }

    def __init__(self, directory=None, helm=None, ksonnet=None, kustomize=None, type=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryRepoAppDetailsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._directory = None
        self._helm = None
        self._ksonnet = None
        self._kustomize = None
        self._type = None
        self.discriminator = None

        if directory is not None:
            self.directory = directory
        if helm is not None:
            self.helm = helm
        if ksonnet is not None:
            self.ksonnet = ksonnet
        if kustomize is not None:
            self.kustomize = kustomize
        if type is not None:
            self.type = type

    @property
    def directory(self):
        """Gets the directory of this RepositoryRepoAppDetailsResponse.  # noqa: E501


        :return: The directory of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :rtype: object
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this RepositoryRepoAppDetailsResponse.


        :param directory: The directory of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :type: object
        """

        self._directory = directory

    @property
    def helm(self):
        """Gets the helm of this RepositoryRepoAppDetailsResponse.  # noqa: E501


        :return: The helm of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :rtype: RepositoryHelmAppSpec
        """
        return self._helm

    @helm.setter
    def helm(self, helm):
        """Sets the helm of this RepositoryRepoAppDetailsResponse.


        :param helm: The helm of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :type: RepositoryHelmAppSpec
        """

        self._helm = helm

    @property
    def ksonnet(self):
        """Gets the ksonnet of this RepositoryRepoAppDetailsResponse.  # noqa: E501


        :return: The ksonnet of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :rtype: RepositoryKsonnetAppSpec
        """
        return self._ksonnet

    @ksonnet.setter
    def ksonnet(self, ksonnet):
        """Sets the ksonnet of this RepositoryRepoAppDetailsResponse.


        :param ksonnet: The ksonnet of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :type: RepositoryKsonnetAppSpec
        """

        self._ksonnet = ksonnet

    @property
    def kustomize(self):
        """Gets the kustomize of this RepositoryRepoAppDetailsResponse.  # noqa: E501


        :return: The kustomize of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :rtype: RepositoryKustomizeAppSpec
        """
        return self._kustomize

    @kustomize.setter
    def kustomize(self, kustomize):
        """Sets the kustomize of this RepositoryRepoAppDetailsResponse.


        :param kustomize: The kustomize of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :type: RepositoryKustomizeAppSpec
        """

        self._kustomize = kustomize

    @property
    def type(self):
        """Gets the type of this RepositoryRepoAppDetailsResponse.  # noqa: E501


        :return: The type of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RepositoryRepoAppDetailsResponse.


        :param type: The type of this RepositoryRepoAppDetailsResponse.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, RepositoryRepoAppDetailsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryRepoAppDetailsResponse):
            return True

        return self.to_dict() != other.to_dict()
