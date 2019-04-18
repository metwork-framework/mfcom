# release_0.5 branch CHANGELOG



## v0.5.8 (2019-03-31)

### New Features
- split #core# and #monitoring# in cpu/mem usage
- we count the memory usage with rss and not with pss


### Bug Fixes
- fix exception in list_metwork_processes.py in some corner cases





## v0.5.7 (2019-03-16)

- No interesting change


## v0.5.6 (2019-02-16)

- No interesting change


## v0.5.5 (2019-02-09)

- No interesting change


## v0.5.4 (2019-02-06)

### New Features


### Bug Fixes
- circus stop was too long in some corner cases





## v0.5.3 (2019-01-31)

- No interesting change


## v0.5.2 (2019-01-31)

- No interesting change


## v0.5.1 (2019-01-28)

- No interesting change


## v0.5.0 (2019-01-28)

### New Features
- refactor node plugins build
- introduce new autorestart plugin
- add home to plugins.list --json output
- remove virtualenv sources after .plugin install
- run post_installation plugins tasks
- add _nginx.reload utility
- Add python and default layers
- add a way to display some warnings during plugin installation


### Bug Fixes
- fix list metwork processes feature for dev usage (several modules
- fix building issue with empty node plugins
- avoid shellcheck warnings
- warning if plugin is already installed in dev





