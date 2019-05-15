# CHANGELOG


## [Unreleased]

### New Features
- better circus reload (reload only what it is necessary)
- add private util for circus management
- add plugin name in mfadmin logs
- introduce mflog_addon
- add a plugin name validation in bootstrap
- add a validate_plugin_name feature in mfutil
- allow plugin template inheritance
- better plugin Makefile
- add nginxfmt.py utility (moved from mfserv)
- add more hooks for circus
- fix_system feature moved to mfcom (sysctl stuff)
- add inside_a_plugin_env() function to mfutil.plugins
- a plugin name can't be 'base' and can't start with '__'
- don't use plugin dirname as name
- better table output and add plugin homes to raw output
- add a --just-home option to plugins.info
- prevent plugins.install/uninstall to be used in a plugin_env


### Bug Fixes
- fix an automatic reload issue in some corner cases
- fix typo
- fix bug CHANGELOGS not generated when CHANGELOGS.md doesn't exist (for the first time)





## v0.6.0 (2019-03-31)

### New Features
- don't use plugin name in [general] section
- remove old mflog library
- split #core# and #monitoring# in cpu/mem usage
- we count the memory usage with rss and not with pss
- add an addon to jsonlog2elasticsearch
- corresponding changes for nodejs plugin refactor


### Bug Fixes
- remove a warning during make freeze with nodejs template
- remove a warning during make develop
- circus stop was too long in some corner cases
- fix exception in list_metwork_processes.py in some corner cases





