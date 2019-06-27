# release_0.7 CHANGELOG


## [Unreleased]

### New Features
- better stop ui
- add is_interactive binary


### Bug Fixes
- uninstall plugin if installation failed





## v0.7.0 (2019-06-04)

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
- add a cwd option to plugin_wrapper
- use new --cwd option when calling postinstall script
- jsonlog2elasticsearch is classified as monitoring process


### Bug Fixes
- fix an automatic reload issue in some corner cases
- fix typo
- fix bug CHANGELOGS not generated when CHANGELOGS.md doesn't exist (for the first time)
- fix conf_monitor behaviour during plugins (un)install
- fix some corner issues during plugins.install/uninstall
- fix conf_monitor issues in random cases





