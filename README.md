# test-pre-commit
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Getting Started

How to use `pre-commit`:
1. Install app using brew
    - `brew install pre-commit`
2. Once installed pre-commit need to be installed in the repo. This is simply done by typing
    - `pre-commit install`
3. The first commit after installing will apply all the hooks defined in `.pre-commit-config.yaml` and run them
    ![install pre-commit](./docs/images/first_commit_after_install.png)