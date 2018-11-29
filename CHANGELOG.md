<a name=""></a>
# (unreleased)


### Bug Fixes

* fix crontab exception in a basic docker container ([ff54e2c](https://github.com/metwork-framework/mfcom/commit/ff54e2c)), closes [#55](https://github.com/metwork-framework/mfcom/issues/55)
* fix incomplete plugins removal (in some cases) ([cffe11c](https://github.com/metwork-framework/mfcom/commit/cffe11c)), closes [#49](https://github.com/metwork-framework/mfcom/issues/49)
* fix missing postinstall scripts ([b92b2ba](https://github.com/metwork-framework/mfcom/commit/b92b2ba))
* raise some timeouts for timeout problems on slow machines ([7fd3515](https://github.com/metwork-framework/mfcom/commit/7fd3515)), closes [#46](https://github.com/metwork-framework/mfcom/issues/46)
* remove a debug message during some plugin operations ([d79ff6e](https://github.com/metwork-framework/mfcom/commit/d79ff6e))
* remove a debug message in plugin_wrapper util ([ce9da6d](https://github.com/metwork-framework/mfcom/commit/ce9da6d))
* rollback on plugin packaging around virtualenv ([077616b](https://github.com/metwork-framework/mfcom/commit/077616b)), closes [metwork-framework/mfserv#41](https://github.com/metwork-framework/mfserv/issues/41)


### Features

* Add a "plugin succesfully created message" ([8e86e1f](https://github.com/metwork-framework/mfcom/commit/8e86e1f)), closes [#66](https://github.com/metwork-framework/mfcom/issues/66)
* add a no-input option ([a21a8d3](https://github.com/metwork-framework/mfcom/commit/a21a8d3))
* add get_file_size function in synutil_lua ([8143d08](https://github.com/metwork-framework/mfcom/commit/8143d08))
* better plugin build ([24a484d](https://github.com/metwork-framework/mfcom/commit/24a484d))
* better plugin cleaning (again) ([8c84417](https://github.com/metwork-framework/mfcom/commit/8c84417))
* better plugin management (with errors in pre/post scripts) ([8944a95](https://github.com/metwork-framework/mfcom/commit/8944a95))


### BREAKING CHANGES

* _plugins.postuninstall is renamed to
_plugins.preuninstall



