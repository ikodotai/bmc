![coverage](https://gitlab.com/big-mama-tech/bmc/badges/master/coverage.svg?job=test)

# bmc


bmc is a Python wrapper for MinIO's command line interface mc and minio. MinIO has a useful client library which unfortunately lacks administrative capabilities, such as adding users and hosts, which we need to do for the [iko](https://iko.ai) machine learning platform.


## Installation

```bash
pip install bmc
```

[![asciicast](https://asciinema.org/a/8CTCfGKzCHHt7IaL7wNCvoyJe.svg)](https://asciinema.org/a/8CTCfGKzCHHt7IaL7wNCvoyJe)

## Development

```bash
git clone https://gitlab.com/big-mama-tech/bmc
cd bmc
pip install -e .

# Generate documentation
sphinx-build -b html docs docs/html
```


[[_TOC_]]



