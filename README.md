# System Tests Runner

## Overview

This repository implements a facade to
[system tests'](https://github.com/datadog/system-tests)
`build.sh` and `run.sh` scripts.

System Tests Runner aims to:

- Simplify the usage of system tests and
to handle some of the system tests' gotchas, so that the developer
does not need to remember them;
- Provide convenient shortcuts where system tests' API is awkward
(for example, for test selection);
- Speed up test execution.

At this time, STR is tailored to Ruby Dynamic Instrumentation tests.

## Usage

STR handles setting up the local virtualenv for ST, building the
images and running them - all in one command. STR is meant to be executed
from the system tests directory.

The basic usage is to run a particular test file in a certain language:

```
str --ruby -t tests/debugger/test_debugger_pii.py
```

STR will (hopefully) determine which scenarios are being used by the
tests in that file, and pass those to ST.

If you are developing the Ruby tracer, STR provides a handy shortcut
to test against the local tree:


```
str --ruby -t tests/debugger/test_debugger_pii.py
```

dd-trace-rb must be checked out in a sibling directory to the
system tests directory that you are in (e.g., if you are running STR
from `~/dev/system-tests`, it expects to find dd-trace-rb in
`~/dev/dd-trace-rb`).

If you omit the language, you'll get ST's default language,
and if you do not specify a test file to run you'll execute all
test in the default scenario.

### Build Options

STR by default asks Docker to rebuild the images on every invocation.
This means you don't need to worry about the images being out of date
with your code, but it does take some time to invoke ST's build script.
You can use the following options to control building behavior:

`--no-build`: Do not build docker images. Use this to speed up the
test run if you know you haven't made any changes to the weblogs or
the tracer.
`--rebuild`: Force rebuild the virtualenv environment and all of the
docker images. Mostly useful if something got messed up.
`--build-only`: Build the docker images if necessary but do not run
any tests. Useful if you are reusing containers (see below).

`-V VARIANT, --variant=VARIANT`: Specify weblog variant to use.

### Language Options

`-l LANG, --language=LANG`: Use specified language. The argument is
whatever ST accepts for languages.

Specific language shortcuts:

`--ruby`: Use Ruby.
`--python`: Use Python.
`--java`: Use Java.

Specific language development shortcuts:

`--ruby-dev`: Use Ruby at `../dd-trace-rb`.
