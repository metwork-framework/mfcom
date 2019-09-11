[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/logos/metwork-white-logo-small.png)](http://www.metwork-framework.org)
# mfcom

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/README.md)

**Status (master branch)**



[![Drone CI](http://metwork-framework.org:8000/api/badges/metwork-framework/mfcom/status.svg)](http://metwork-framework.org:8000/metwork-framework/mfcom)
[![Maintenance](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)]()
[![License](https://github.com/metwork-framework/resources/blob/master/badges/bsd.svg)]()
[![Gitter](https://github.com/metwork-framework/resources/blob/master/badges/community-en.svg)](https://gitter.im/metwork-framework/community-en?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Gitter](https://github.com/metwork-framework/resources/blob/master/badges/community-fr.svg)](https://gitter.im/metwork-framework/community-fr?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


[//]: # (TABLE_OF_CONTENTS_PLACEHOLDER)

## What is MFCOM?

This is the **M**etwork **F**ramework "**COM**mon **module**. This module does not contain any services, it is just a bunch of files and directories.

Usually **MFCOM** is just a dependency of other MetWork Framework **modules** (like [mfserv](https://github.com/metwork-framework/mfserv) or [mfdata](https://github.com/metwork-framework.org/mfdata)) but it can also be used alone.

**MFCOM** depends on [mfext](https://github.com/metwork-framework/mfext) module.

## Note about MFCOM future

The split between **MFCOM** and **MFEXT** module is primarily historical at a time when
MetWork was not opensource.

We want to fix that and transform **MFCOM** module as a **MFEXT layer**.

## Content

**MFCOM** module contains a lot of internal tools and libraries used by
other modules. They shouldn't be used by framework users.

The main exception is `mfutil` python library which can be really useful.

## Quickstart

### Installation

**On a Linux CentOS 7 box**

```bash

# AS ROOT USER

# First, we configure the Metwork Framework repository for stable release on CentOS 7
cat >/etc/yum.repos.d/metwork.repo <<EOF
[metwork_stable]
name=MetWork Stable
baseurl=http://metwork-framework.org/pub/metwork/releases/rpms/stable/centos7/
gpgcheck=0
enabled=1
metadata_expire=0
EOF

# Then we install a minimal version of mfcom module
yum -y install metwork-mfcom-minimal

# Done :-)

# Then let's install (for the example only) an extra layer
# (to add Python2 support)
yum -y install metwork-mfcom-layer-python2
```

### Usage

```console

$ # AS ANY USER (can be root or a non priviligied one)

$ # We load the mfcom (interactive) profile for the current session
$ # (note: there is also a regular profile (without banner and custom bash prompt)
$ # for non-interactive stuff)
$ . /opt/metwork-mfcom/share/interactive_profile
           __  __      ___          __        _
          |  \/  |    | \ \        / /       | |
          | \  / | ___| |\ \  /\  / /__  _ __| | __
          | |\/| |/ _ \ __\ \/  \/ / _ \| '__| |/ /
          | |  | |  __/ |_ \  /\  / (_) | |  |   <
          |_|  |_|\___|\__| \/  \/ \___/|_|  |_|\_\

 11:24:50 up 61 days, 57 min,  1 user,  load average: 1.26, 1.77, 2.13

$ # Test your python version (recent Python3 version)
$ python --version
Python 3.7.3

$ # Try mfutil library
$ python
>>> from mfutil import get_unique_hexa_identifier
>>> get_unique_hexa_identifier()
'89a4c8c3da6b44caa0ca22a8fb0f97f6'
```

## More details

After installation, there is no service to initialize or to start.

All the files are located in `/opt/metwork-mfcom-{BRANCH}` directory with probably
a `/opt/metwork-mfcom => /opt/metwork-mfcom-{BRANCH}` symbolic link (in very particular
and advanced use cases, you can choose not to install the symbolic link).

Because `/opt` is not used by default on [standard Linux](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard), **the installation shouldn't break anything.**

Therefore, if you do nothing specific after the installation, you won't benefit
from any included software components!

So, to use this module, you have to load a kind of "mfcom environment". There are several ways to do that.

> Note: When you load the "mfcom environment", it will automatically load the "mfext environment"
> (because "mfcom" depends on "mfext"). But, if you load the "mfext environment", it won't
> (of course) automatically load the "mfcom environment".

In the following, we use `{MFCOM_HOME}` as the installation directory of the `mfcom` module. It's probably something like `/opt/metwork-mfcom-{BRANCH}` or `/opt/metwork-mfcom`. Have a look in `/opt` directory.

### Load the mfcom environment (for one command only)

If you want to load the "mfcom environment" for one command only and return back to a standard running environment after that, you can use the specific wrapper:

```console
$ # what is the version of the python command ?
$ python --version
Python 2.6.6
$ # => this is a very old python version

$ # what is the version of the python command (with mfcom environment loaded) ?
$ {MFCOM_HOME}/bin/mfcom_wrapper python --version
Python 3.7.3
$ # => this is a recent python version

$ # what is the version of the python command ?
$ python --version
Python 2.6.6
$ # => We are back to our original system python command
```

> Note: The recent python version is (in fact) provided by "mfext" environment.

### Load the mfcom environment (for the whole shell session)

If you are tired to use `mfcom_wrapper` repeatedly, you can load the "mfcom environment"
for the whole shell session with:

- `. {MFCOM_HOME}/share/interative_profile`
- (or) `. {MFCOM_HOME}/share/profile` (for non interactive stuff)

See "Quickstart" section below for a complete example.

### Load the mfcom environment (automatically for one user)

If you want to have a unix user with "always loaded" metwork environment, you can add:

```
source {MFCOM_HOME}/share/interactive_profile
```

in (for example) in the user `.bash_profile` file.

**Note: we do not recommend to use this for a user with a full graphical interface because of possible side effects with desktop environment.**

An alternative way is to add

```
alias mfcom="source {MFCOM_HOME}/share/interactive_profile"
```

in `.bash_profile` file and use this `mfcom` alias when you want to quickly load the "mfcom environment".

### Unloading the mfcom environment

If you want to "unload" the "mfcom environment" to launch an external command which doesn't play well with metwork libraries
or tools (because of version conflicts for example), you can use the `outside` command wrapper.

```console

$ # . {MFCOM_HOME}/share/interactive_profile
[...]

$ python --version
Python 3.7.3
$ # => the mfcom environment is loaded

$ outside python --version
Python 2.7.5
$ # => we lauched the python command outside the mfcom environment
$ #    (so we got the system version)

$ python --version
Python 3.7.3
$ # => the mfcom environment is still loaded
```

> Note: The recent python version is (in fact) provided by "mfext" environment.








## Reference documentation

- (for **master (development)** version), see [this dedicated site](http://metwork-framework.org/pub/metwork/continuous_integration/docs/master/mfcom/) for reference documentation.
- (for **latest released stable** version), see [this dedicated site](http://metwork-framework.org/pub/metwork/releases/docs/stable/mfcom/) for reference documentation.

For very specific use cases, you might be interested in
[reference documentation for integration branch](http://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/mfcom/).

And if you are looking for an old released version, you can search [here](http://metwork-framework.org/pub/metwork/releases/docs/).

## Installation guide

See [this document](.metwork-framework/install_a_metwork_package.md).




## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
