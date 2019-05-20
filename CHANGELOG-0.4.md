# release_0.4 CHANGELOG



## v0.4.1 (2019-01-09)

- No interesting change


## v0.4.0 (2019-01-08)

### New Features
- better plugin build
- better plugin cleaning (again)
- add get_file_size function in synutil_lua
- add a no-input option
- better plugin management (with errors in pre/post scripts)
- Add a "plugin succesfully created message"
- publish conf generation time as an env var
- add a list_metwork_processes util
- add a telegraf plugin to collect informations about metwork
- new plugin_wrapper (with options)
- add new layerapi2 python wrapper


### Bug Fixes
- remove a debug message in plugin_wrapper util
- remove a debug message during some plugin operations
- rollback on plugin packaging around virtualenv
- raise some timeouts for timeout problems on slow machines
- fix incomplete plugins removal (in some cases)
- fix missing postinstall scripts
- fix crontab exception in a basic docker container
- fix metwork processes list
- fix list metwork processes feature for dev usage (several modules





