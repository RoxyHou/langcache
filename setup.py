from setuptools import setup, find_packages

setup(
    name='langcache',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "../evadb_milvus",
        "openai>=0.27.8"
    ],
)