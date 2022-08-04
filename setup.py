from setuptools import setup

version = "<REPLACE_WITH_VERSION>"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ai2thor_colab",
    packages=["ai2thor_colab"],
    version=version,
    license="Apache 2.0",
    description="Utility functions for using AI2-THOR with Google Colab.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="ai2thor@allenai.org",
    author="Allen Institute for AI",
    install_requires=["numpy", "moviepy>=1.0.3", "pandas", "ai2thor", "Pillow"],
    url="https://github.com/allenai/ai2thor-colab",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
