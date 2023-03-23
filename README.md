# Robot Framework - Test Library Example Python

Licensed under the MIT License. See file [LICENSE](./LICENSE).

[Robot Framework](https://robotframework.org/) example for test library implemented in Python. Example includes code written in Robot Framework and Python.

[![CodeQL](https://github.com/mneiferbag/robot-python-test-library/actions/workflows/codeql.yml/badge.svg)](https://github.com/mneiferbag/robot-python-test-library/actions/workflows/codeql.yml)

## How To Run

This example can be run as follows.

Create virtual environment with `python -m venv .venv`.

Activate virtual environment with `source .venv/bin/activate` for Linux bash. Or with `.venv\Scripts\activate.bat` for Windows command line.

Restore packages with `pip install -r requirements.txt`.

Check installation with `robot --version`.

Run test with Python keywords using `robot --pythonpath src --outputdir ./log ./python_tests/python_keywords.robot`.

Command line option `--pythonpath`is not necessary when you set environment variable `PYTHONPATH`.

For more information on extending Robot Framework with test libraries written in Python, see chapter [Creating test libraries](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries) in the user guide.

## Links

- Robot Framework
  - [FTP and Database Example](https://github.com/mneiferbag/robot-ftp-db)
  - [Test Library Example Rust](https://github.com/mneiferbag/robot-rust-test-library)

## Tasks

- [ ] Create dictionary variable example
- [x] Create list variable example
