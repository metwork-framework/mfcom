<a name=""></a>
# [](https://github.com/metwork-framework/mfcom/compare/v0.4.0...v) (2019-01-09)



<a name="0.4.0"></a>
# [0.4.0](https://github.com/metwork-framework/mfcom/compare/ce9da6d...v0.4.0) (2019-01-08)


### Bug Fixes

* fix crontab exception in a basic docker container ([ff54e2c](https://github.com/metwork-framework/mfcom/commit/ff54e2c)), closes [#55](https://github.com/metwork-framework/mfcom/issues/55)
* fix incomplete plugins removal (in some cases) ([cffe11c](https://github.com/metwork-framework/mfcom/commit/cffe11c)), closes [#49](https://github.com/metwork-framework/mfcom/issues/49)
* fix list metwork processes feature for dev usage (several modules ([3e479dd](https://github.com/metwork-framework/mfcom/commit/3e479dd))
* fix metwork processes list ([d7390f4](https://github.com/metwork-framework/mfcom/commit/d7390f4))
* fix missing postinstall scripts ([b92b2ba](https://github.com/metwork-framework/mfcom/commit/b92b2ba))
* raise some timeouts for timeout problems on slow machines ([7fd3515](https://github.com/metwork-framework/mfcom/commit/7fd3515)), closes [#46](https://github.com/metwork-framework/mfcom/issues/46)
* remove a debug message during some plugin operations ([d79ff6e](https://github.com/metwork-framework/mfcom/commit/d79ff6e))
* remove a debug message in plugin_wrapper util ([ce9da6d](https://github.com/metwork-framework/mfcom/commit/ce9da6d))
* rollback on plugin packaging around virtualenv ([077616b](https://github.com/metwork-framework/mfcom/commit/077616b)), closes [metwork-framework/mfserv#41](https://github.com/metwork-framework/mfserv/issues/41)


### Features

* Add a "plugin succesfully created message" ([8e86e1f](https://github.com/metwork-framework/mfcom/commit/8e86e1f)), closes [#66](https://github.com/metwork-framework/mfcom/issues/66)
* add a list_metwork_processes util ([9b6745b](https://github.com/metwork-framework/mfcom/commit/9b6745b)), closes [metwork-framework/resources#22](https://github.com/metwork-framework/resources/issues/22)
* add a no-input option ([a21a8d3](https://github.com/metwork-framework/mfcom/commit/a21a8d3))
* add a telegraf plugin to collect informations about metwork ([f39626f](https://github.com/metwork-framework/mfcom/commit/f39626f)), closes [metwork-framework/resources#22](https://github.com/metwork-framework/resources/issues/22)
* add get_file_size function in synutil_lua ([8143d08](https://github.com/metwork-framework/mfcom/commit/8143d08))
* add new layerapi2 python wrapper ([9e23b59](https://github.com/metwork-framework/mfcom/commit/9e23b59))
* better plugin build ([24a484d](https://github.com/metwork-framework/mfcom/commit/24a484d))
* better plugin cleaning (again) ([8c84417](https://github.com/metwork-framework/mfcom/commit/8c84417))
* better plugin management (with errors in pre/post scripts) ([8944a95](https://github.com/metwork-framework/mfcom/commit/8944a95))
* new plugin_wrapper (with options) ([0272488](https://github.com/metwork-framework/mfcom/commit/0272488)), closes [metwork-framework/resources#24](https://github.com/metwork-framework/resources/issues/24)
* publish conf generation time as an env var ([ca04ab2](https://github.com/metwork-framework/mfcom/commit/ca04ab2)), closes [metwork-framework/resources#10](https://github.com/metwork-framework/resources/issues/10)


### BREAKING CHANGES

* _plugins.postuninstall is renamed to
_plugins.preuninstall



