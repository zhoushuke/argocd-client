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


class V1MicroTime(object):
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
        'nanos': 'int',
        'seconds': 'str'
    }

    attribute_map = {
        'nanos': 'nanos',
        'seconds': 'seconds'
    }

    def __init__(self, nanos=None, seconds=None, local_vars_configuration=None):  # noqa: E501
        """V1MicroTime - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nanos = None
        self._seconds = None
        self.discriminator = None

        if nanos is not None:
            self.nanos = nanos
        if seconds is not None:
            self.seconds = seconds

    @property
    def nanos(self):
        """Gets the nanos of this V1MicroTime.  # noqa: E501

        Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.  # noqa: E501

        :return: The nanos of this V1MicroTime.  # noqa: E501
        :rtype: int
        """
        return self._nanos

    @nanos.setter
    def nanos(self, nanos):
        """Sets the nanos of this V1MicroTime.

        Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context.  # noqa: E501

        :param nanos: The nanos of this V1MicroTime.  # noqa: E501
        :type: int
        """

        self._nanos = nanos

    @property
    def seconds(self):
        """Gets the seconds of this V1MicroTime.  # noqa: E501

        Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.  # noqa: E501

        :return: The seconds of this V1MicroTime.  # noqa: E501
        :rtype: str
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this V1MicroTime.

        Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive.  # noqa: E501

        :param seconds: The seconds of this V1MicroTime.  # noqa: E501
        :type: str
        """

        self._seconds = seconds

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
        if not isinstance(other, V1MicroTime):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1MicroTime):
            return True

        return self.to_dict() != other.to_dict()
