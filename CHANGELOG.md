# release_0.6 CHANGELOG


## [Unreleased]

### New Features


### Bug Fixes
- fix conf_monitor behaviour during plugins (un)install
- fix some corner issues during plugins.install/uninstall





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





