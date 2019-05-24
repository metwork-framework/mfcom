# release_0.7 CHANGELOG


## [Unreleased]

### New Features
- use new --cwd option when calling postinstall script
- add a cwd option to plugin_wrapper
- prevent plugins.install/uninstall to be used in a plugin_env
- add inside_a_plugin_env() function to mfutil.plugins
- a plugin name can't be 'base' and can't start with '__'
- don't use plugin dirname as name
- better table output and add plugin homes to raw output
- add a --just-home option to plugins.info
- fix_system feature moved to mfcom (sysctl stuff)
- add more hooks for circus
- add nginxfmt.py utility (moved from mfserv)
- better plugin Makefile
- allow plugin template inheritance
- add a validate_plugin_name feature in mfutil
- add a plugin name validation in bootstrap
- introduce mflog_addon
- add plugin name in mfadmin logs
- add private util for circus management
- better circus reload (reload only what it is necessary)


### Bug Fixes
- fix some corner issues during plugins.install/uninstall
- fix conf_monitor behaviour during plugins (un)install
- fix bug CHANGELOGS not generated when CHANGELOGS.md doesn't exist (for the first time)
- fix typo
- fix an automatic reload issue in some corner cases





