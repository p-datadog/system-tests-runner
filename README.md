# System Tests Runner

## Overview

This repository implements a facade to
[system tests'](https://github.com/datadog/system-tests)
`build.sh` and `run.sh` scripts.

System Tests Runner aims to simplify the usage of system tests and
to handle some of the system tests' "gotchas", with the ultimate goal being
that the first execution of STR provides the developer with the results that
they were looking for.

At this time, STR is tailored to Ruby Dynamic Instrumentation tests.

## Features

- One script that executes both `run.sh` and `build.sh`, as necessary.
No more having to
re-run `run.sh` because you needed to also run `build.sh` and did not.
- Straightforward option to use the local Ruby library (`datadog`) tree.
- Convenient option to run all Dynamic Instrumentation/Debugger scenarios.
- Straightforward option to enable verbose output, which also patches
pytest to provide the list of tests that will be executed prior to the
setup phase (thus the list of tests is available without having to wait for
the test run to complete).
- Convenient shortcuts for debugger system tests and other commonly used
options.
- Automatically sets scenarios to run based on requested test files
