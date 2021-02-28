from setuptools import setup

version = "<REPLACE_WITH_VERSION>"

# use current date & time for dev version

setup(
    name="ai2thor_colab",
    packages=["ai2thor_colab"],
    version=version,
    license="Apache",
    description="Support to run AI2-THOR freely in Google Colab!",
    long_description="Support to run AI2-THOR freely in Google Colab!",
    author_email="ai2thor@allenai.org",
    author="Allen Institute for AI",
    install_requires=["numpy", "moviepy"],
    url="https://github.com/allenai/ai2thor-colab",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)