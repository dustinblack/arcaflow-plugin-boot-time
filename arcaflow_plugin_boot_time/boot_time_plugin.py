#!/usr/bin/env python3

import sys
import typing
import subprocess
from arcaflow_plugin_sdk import plugin
from boot_time_schema import (
    InputParams,
    SuccessOutput,
    ErrorOutput,
)


@plugin.step(
    id="boot-time",
    name="Boot Time Metrics",
    description="Collects and organizes metrics related to system boot time.",
    outputs={"success": SuccessOutput, "error": ErrorOutput},
)
def hello_world(
    params: InputParams,
) -> typing.Tuple[str, typing.Union[SuccessOutput, ErrorOutput]]:

    print("==>> Running the systemd-analyze collection...")

    systemd_cmd = ["systemd-analyze", "plot", "--json=pretty"]

    try:
        systemd_out = subprocess.check_output(
            systemd_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except:
        return "error", ErrorOutput("Error collecting systemd-analyze data!")

    return "success", SuccessOutput(systemd_out)


if __name__ == "__main__":
    sys.exit(
        plugin.run(
            plugin.build_schema(
                # List your step functions here:
                hello_world,
            )
        )
    )
