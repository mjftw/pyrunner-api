# pyrunner-api

[![Build Status](https://travis-ci.com/mjftw/pyrunner-api.svg?branch=master)](https://travis-ci.com/mjftw/pyrunner-api)
[![Coverage Status](https://coveralls.io/repos/github/mjftw/pyrunner-api/badge.svg?branch=master)](https://coveralls.io/github/mjftw/pyrunner-api?branch=master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d1fde7a229654f8e9b3852e90aa3a931)](https://www.codacy.com/manual/mjftw/pyrunner-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mjftw/pyrunner-api&amp;utm_campaign=Badge_Grade)

A service which lets you submit python code to be run via a REST interface, and get the results.

## running the tests

A makefile is provided to make running some simple tasks easier.

Run the tests inside a virtualenv:

``` shell
make test
```

See the other possible make targets:

```shell
make help
```

## Security

Currently the server has awful security, with no auth and no isolation of the injected code.  
The plan is to move to running the injected code within a Docker container to prevent the server from being affected.
We're not there yet though, so **use with caution**.