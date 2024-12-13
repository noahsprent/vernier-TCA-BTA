# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="vernier-FPH-BTA",
    version="0.0.2",
    license_files = ('LICENSE.txt',),
    description="The plugin allows you to read pH into the pioreactor app using the Vernier FPH-BTA sensor.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="noahsprent@gmail.com",
    author="Noah Sprent",
    url="https://github.com/noahsprent",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["serial", "json", "pioreactor>=24.10.0", "click", "time"], # PROVIDE OTHER PYTHON REQUIREMENTS, ex: "pioreactor>=23.6.0", "numpy>=1.0"
    entry_points={
        "pioreactor.plugins": "vernier_fph_bta = vernier_fph_bta"
    },
)
