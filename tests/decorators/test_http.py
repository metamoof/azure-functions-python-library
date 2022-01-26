#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License.
import unittest

from azure.functions import DataType, AuthLevel
from azure.functions.decorators.core import BindingDirection
from azure.functions.decorators.http import HttpMethod, HttpTrigger, HttpOutput


class TestHttp(unittest.TestCase):
    def test_http_method_enum(self):
        self.assertEqual([e for e in HttpMethod],
                         [HttpMethod.GET, HttpMethod.POST, HttpMethod.DELETE,
                          HttpMethod.HEAD, HttpMethod.PATCH, HttpMethod.PUT,
                          HttpMethod.OPTIONS])

    def test_http_trigger_valid_creation_with_methods(self):
        http_trigger = HttpTrigger(name='req', methods={HttpMethod.GET},
                                   data_type=DataType.UNDEFINED,
                                   auth_level=AuthLevel.ANONYMOUS,
                                   route='dummy')

        self.assertEqual(http_trigger.get_binding_name(), "httpTrigger")
        self.assertEqual(http_trigger.get_dict_repr(), {
            "authLevel": str(AuthLevel.ANONYMOUS),
            "type": "httpTrigger",
            "direction": BindingDirection.IN.value,
            "name": 'req',
            "dataType": DataType.UNDEFINED.value,
            "route": 'dummy',
            "methods": [str(HttpMethod.GET)]
        })

    def test_http_output_valid_creation(self):
        http_output = HttpOutput(name='req', data_type=DataType.UNDEFINED)

        self.assertEqual(http_output.get_binding_name(), "http")
        self.assertEqual(http_output.get_dict_repr(), {
            "type": "http",
            "direction": BindingDirection.OUT.value,
            "name": "req",
            "dataType": DataType.UNDEFINED.value,
        })
