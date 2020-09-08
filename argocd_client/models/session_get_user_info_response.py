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


class SessionGetUserInfoResponse(object):
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
        'groups': 'list[str]',
        'iss': 'str',
        'logged_in': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'groups': 'groups',
        'iss': 'iss',
        'logged_in': 'loggedIn',
        'username': 'username'
    }

    def __init__(self, groups=None, iss=None, logged_in=None, username=None, local_vars_configuration=None):  # noqa: E501
        """SessionGetUserInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._groups = None
        self._iss = None
        self._logged_in = None
        self._username = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if iss is not None:
            self.iss = iss
        if logged_in is not None:
            self.logged_in = logged_in
        if username is not None:
            self.username = username

    @property
    def groups(self):
        """Gets the groups of this SessionGetUserInfoResponse.  # noqa: E501


        :return: The groups of this SessionGetUserInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this SessionGetUserInfoResponse.


        :param groups: The groups of this SessionGetUserInfoResponse.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def iss(self):
        """Gets the iss of this SessionGetUserInfoResponse.  # noqa: E501


        :return: The iss of this SessionGetUserInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._iss

    @iss.setter
    def iss(self, iss):
        """Sets the iss of this SessionGetUserInfoResponse.


        :param iss: The iss of this SessionGetUserInfoResponse.  # noqa: E501
        :type: str
        """

        self._iss = iss

    @property
    def logged_in(self):
        """Gets the logged_in of this SessionGetUserInfoResponse.  # noqa: E501


        :return: The logged_in of this SessionGetUserInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._logged_in

    @logged_in.setter
    def logged_in(self, logged_in):
        """Sets the logged_in of this SessionGetUserInfoResponse.


        :param logged_in: The logged_in of this SessionGetUserInfoResponse.  # noqa: E501
        :type: bool
        """

        self._logged_in = logged_in

    @property
    def username(self):
        """Gets the username of this SessionGetUserInfoResponse.  # noqa: E501


        :return: The username of this SessionGetUserInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SessionGetUserInfoResponse.


        :param username: The username of this SessionGetUserInfoResponse.  # noqa: E501
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
        if not isinstance(other, SessionGetUserInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionGetUserInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
