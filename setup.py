# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="vernier-TMP-BTA",
    version="0.1.0",
    license_files = ('LICENSE.txt',),
    description="The plugin allows you to read temperature into the pioreactor app using the Vernier TMP-BTA sensor.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="noahsprent@gmail.com",
    author="Noah Sprent",
    url="https://github.com/noahsprent",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],#"pyserial", "click", "pioreactor>24.10.0"],
    entry_points={
        "pioreactor.plugins": "vernier_tmp_bta = vernier_tmp_bta"
    },
)
