#!/usr/bin/env python3
from setuptools import setup

setup(
    # Set the name so that github correctly tracks reverse dependencies.
    # https://github.com/popsim-consortium/stdvoidsim/network/dependents
    name="stdvoidsim",
    use_scm_version={"write_to": "stdvoidsim/_version.py"},
)
