# Semantic Caching with EvaDB

## Overview
The ```langcache``` Python package provides a semantic caching solution using EvaDB. It allows you to efficiently store and retrieve text data based on their semantic meaning.


This package is powered by [EvaDB](https://github.com/georgia-tech-db/eva), a Python-based database system for AI applications developed by Georgia Tech's DB Group.

## Install
Install and run the Milvus Standalone Server following the instruction in:

```bat
https://milvus.io/docs/install_standalone-docker.md
```
Install the Milvus Extension of EvaDB to the same parent folder of langcache from [evadb_milvus](https://github.com/RoxyHou/evadb_milvus.git):

```bat
git clone https://github.com/RoxyHou/evadb_milvus.git
```

## Setup
Ensure that the local Python version is >= 3.8. If using MacOS with Intel chip, ensure that you are uing Python with version == 3.7. Install the required libraries:

```bat
conda create --name [ENV_NAME] python=3.7.16
conda activate [ENV_NAME]
pip install -r requirements.txt
```

Installation for different device can be different, ```pip install [package_name]``` for any package not installed correctly.

## Build
Build the local package:

```bat
pip install -e .
```

## Run
Run the following command to run the large_test.py:
```bat
python test/large_test.py
```
