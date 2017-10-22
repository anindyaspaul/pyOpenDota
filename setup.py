from setuptools import setup, find_packages

setup(
    name="opendota",
    version="0.1.0",
    description="Thin python client for the OpenDota API",
    url="https://github.com/anindyaspaul/pyOpenDota",
    author="Anindya Sundar Paul",
    author_email="anindya@anindyaspaul.com",
    license="GPL-3.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    test_suite="tests",
    install_requires=[
        "requests"
    ],
)
