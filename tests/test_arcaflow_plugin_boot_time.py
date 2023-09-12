#!/usr/bin/env python3
import unittest
import boot_time_plugin
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            boot_time_plugin.InputParams("John Doe")
        )

        plugin.test_object_serialization(
            boot_time_plugin.SuccessOutput("Hello, world!")
        )

        plugin.test_object_serialization(
            boot_time_plugin.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        input = boot_time_plugin.InputParams(name="Example Joe")

        output_id, output_data = boot_time_plugin.hello_world(input)

        # The example plugin always returns an error:
        self.assertEqual("success", output_id)
        self.assertEqual(
            output_data,
            boot_time_plugin.SuccessOutput("Hello, Example Joe!")
        )


if __name__ == "__main__":
    unittest.main()
