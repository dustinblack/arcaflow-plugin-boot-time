#!/usr/bin/env python3
import unittest
import arcaflow_plugin_boot_time
from arcaflow_plugin_sdk import plugin


class HelloWorldTest(unittest.TestCase):
    @staticmethod
    def test_serialization():
        plugin.test_object_serialization(
            arcaflow_plugin_boot_time.InputParams("John Doe")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_boot_time.SuccessOutput("Hello, world!")
        )

        plugin.test_object_serialization(
            arcaflow_plugin_boot_time.ErrorOutput(error="This is an error")
        )

    def test_functional(self):
        input = arcaflow_plugin_boot_time.InputParams(name="Example Joe")

        output_id, output_data = arcaflow_plugin_boot_time.hello_world(input)

        # The example plugin always returns an error:
        self.assertEqual("success", output_id)
        self.assertEqual(
            output_data,
            arcaflow_plugin_boot_time.SuccessOutput("Hello, Example Joe!")
        )


if __name__ == "__main__":
    unittest.main()
