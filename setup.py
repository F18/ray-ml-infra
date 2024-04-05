"""Python setup.py for ray_ml_infra package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("ray_ml_infra", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ray_ml_infra",
    version=read("ray_ml_infra", "VERSION"),
    description="Awesome ray_ml_infra created by F18",
    url="https://github.com/F18/ray-ml-infra/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="F18",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["ray_ml_infra = ray_ml_infra.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
