#!/usr/bin/env python3
from pathlib import Path
from setuptools import setup

CWD = Path(__file__).resolve().parent


setup(
    name="mnemonic",
    version="0.20",
    description="Implementation of Bitcoin BIP-0039",
    long_description="\n".join(
        (
            (CWD / "README.md").read_text(),
        )
    ),
    packages=["mnemonic"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
    ],
)
