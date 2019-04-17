<a name="unreleased"></a>
## [Unreleased]

### Feat
- add an addon to jsonlog2elasticsearch
- add plugin name in mfadmin logs
- add private util for circus management
- better circus reload (reload only what it is necessary)
- corresponding changes for nodejs plugin refactor
- don't use plugin name in [general] section
- introduce mflog_addon
- remove old mflog library
- split #core# and #monitoring# in cpu/mem usage
- we count the memory usage with rss and not with pss

### Fix
- circus stop was too long in some corner cases
- fix exception in list_metwork_processes.py in some corner cases
- remove a warning during make develop
- remove a warning during make freeze with nodejs template

<a name="v0.5.8"></a>
## [v0.5.8] - 2019-03-31
### Feat
- split #core# and #monitoring# in cpu/mem usage
- we count the memory usage with rss and not with pss

### Fix
- circus stop was too long in some corner cases
- fix exception in list_metwork_processes.py in some corner cases

<a name="v0.6.0"></a>
## [v0.6.0] - 2019-03-31
### Feat
- add an addon to jsonlog2elasticsearch
- corresponding changes for nodejs plugin refactor
- don't use plugin name in [general] section
- remove old mflog library
- split #core# and #monitoring# in cpu/mem usage
- we count the memory usage with rss and not with pss

### Fix
- circus stop was too long in some corner cases
- fix exception in list_metwork_processes.py in some corner cases
- remove a warning during make develop
- remove a warning during make freeze with nodejs template

<a name="v0.5.7"></a>
## [v0.5.7] - 2019-03-16

<a name="v0.5.6"></a>
## [v0.5.6] - 2019-02-16

<a name="v0.5.5"></a>
## [v0.5.5] - 2019-02-09

<a name="v0.5.4"></a>
## [v0.5.4] - 2019-02-06
### Fix
- circus stop was too long in some corner cases

<a name="v0.5.3"></a>
## [v0.5.3] - 2019-01-31

<a name="v0.5.2"></a>
## [v0.5.2] - 2019-01-31

<a name="v0.5.0"></a>
## [v0.5.0] - 2019-01-28

<a name="v0.5.1"></a>
## [v0.5.1] - 2019-01-28
### Feat
- Add python and default layers
- add _nginx.reload utility
- add a way to display some warnings during plugin installation
- add home to plugins.list --json output
- introduce new autorestart plugin
- refactor node plugins build
- remove virtualenv sources after .plugin install
- run post_installation plugins tasks

### Fix
- avoid shellcheck warnings
- fix building issue with empty node plugins
- fix list metwork processes feature for dev usage (several modules as the same user)
- warning if plugin is already installed in dev

### BREAKING CHANGE

node_package.json must be renamed in
node_sources/package.json and node_package-lock.json must be renamed in
node_sources/node_package-lock.json

<a name="v0.4.1"></a>
## [v0.4.1] - 2019-01-09

<a name="v0.4.0"></a>
## [v0.4.0] - 2019-01-08
### Feat
- Add a "plugin succesfully created message" at the end of bootstrap_plugin.py
- add a list_metwork_processes util
- add a no-input option
- add a telegraf plugin to collect informations about metwork modules/plugins
- add get_file_size function in synutil_lua
- add new layerapi2 python wrapper
- better plugin build
- better plugin cleaning (again)
- better plugin management (with errors in pre/post scripts)
- new plugin_wrapper (with options)
- publish conf generation time as an env var

### Fix
- fix crontab exception in a basic docker container
- fix incomplete plugins removal (in some cases)
- fix list metwork processes feature for dev usage (several modules as the same user)
- fix metwork processes list
- fix missing postinstall scripts
- raise some timeouts for timeout problems on slow machines
- remove a debug message during some plugin operations
- remove a debug message in plugin_wrapper util
- rollback on plugin packaging around virtualenv

### BREAKING CHANGE

_plugins.postuninstall is renamed to
_plugins.preuninstall

