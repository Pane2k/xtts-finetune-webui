import os
import platform

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="xtts-finetune-webui",
    py_modules=["xtts-finetune-webui"],
    version="1.0.0",
    description="xtts with webui for conda fork.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain",
    url="https://github.com/Pane2k/xtts-finetune-webui",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
    + [f"pyannote.audio==3.1.1"],
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
