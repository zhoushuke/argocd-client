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


class ApplicationLogEntry(object):
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
        'content': 'str',
        'time_stamp': 'V1Time'
    }

    attribute_map = {
        'content': 'content',
        'time_stamp': 'timeStamp'
    }

    def __init__(self, content=None, time_stamp=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationLogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._time_stamp = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def content(self):
        """Gets the content of this ApplicationLogEntry.  # noqa: E501


        :return: The content of this ApplicationLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ApplicationLogEntry.


        :param content: The content of this ApplicationLogEntry.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def time_stamp(self):
        """Gets the time_stamp of this ApplicationLogEntry.  # noqa: E501


        :return: The time_stamp of this ApplicationLogEntry.  # noqa: E501
        :rtype: V1Time
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this ApplicationLogEntry.


        :param time_stamp: The time_stamp of this ApplicationLogEntry.  # noqa: E501
        :type: V1Time
        """

        self._time_stamp = time_stamp

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
        if not isinstance(other, ApplicationLogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationLogEntry):
            return True

        return self.to_dict() != other.to_dict()
