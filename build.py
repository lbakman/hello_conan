#!/usr/bin/env python3

from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(use_docker=True,
                                 docker_image_skip_pull=False,
                                 docker_image_skip_update=True,
                                 build_policy="missing",
                                 upload_dependencies="all",
                                 skip_check_credentials=True
                                 )
    builder.add(settings={"arch": "x86_64", "build_type": "Debug",
                          "compiler": "gcc", "compiler.libcxx": "libstdc++11"})
    builder.run()

