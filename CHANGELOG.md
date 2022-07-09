# Changelog

All notable changes to this project will be documented in this file.

## [8.1.18.post2] - 2022-07-09

### Bug Fixes

- add typing to Java code (#29)

### Refactor

- use java.lang.String (#30)

### Revert

- undo change on `mypy` ([34492d7](https://github.com/ignition-api/8.1/commit/34492d7fabe3f3f0b6bcafb15a1e1763bd1e5655))

## [8.1.18.post1] - 2022-07-05

### CI

- use Python 2 mode for mypy (#25)

### Features

- implement all LoggerEx functions (#27)

### Miscellaneous Tasks

- improve typing for `ignition-api-stubs` (#24)

### Build

- pre-commit autoupdate (#26)

## [8.1.18] - 2022-06-20

### Features

- add fields to Results class (#22)
- add `readRaw`, `writeRaw` to `bacnet` module (#23)

### Build

- bump actions/setup-python from 3 to 4 (#21)

## [8.1.17] - 2022-05-13

### Bug Fixes

- update type hint for `html` arg (#20)

### Refactor

- update type hint for payload arg ([b8995ab](https://github.com/ignition-api/8.1/commit/b8995ab50a1118e8fa440987d0167141a0cb94ed))

### Build

- update pylint configuration (#18)

## [8.1.16.post1] - 2022-04-08

### Features

- add perspective.authenticationChallenge (#17)

## [8.1.16] - 2022-04-06

### Bug Fixes

- fix `ci.yml` (#5)

### CI

- fix packaging issues (#2)
- update build action (#4)
- maintenance (#6)
- use `deps` scope for pre-commit.ci (#10)

### Documentation

- update downloads badge ([f162972](https://github.com/ignition-api/8.1/commit/f1629728b95b15c77812e2fe62b99af9c634bdc5))
- add discussions badge ([7c2aa6f](https://github.com/ignition-api/8.1/commit/7c2aa6f063fb12cb0efc47f7f41efdef86ed200f))
- replace old project name (#3)
- use pepy.tech for counting downloads (#13)
- add link to org CONTRIBUTING.md (#14)
- fix link to CONTRIBUTING header ([72023b6](https://github.com/ignition-api/8.1/commit/72023b68917c436ec538aeba357d354c057242bc))

### Features

- add version argument to httpClient (#16)

### Miscellaneous Tasks

- move project to github org ([240c95f](https://github.com/ignition-api/8.1/commit/240c95f0d272e4b1c9da99b16b6daa632bfc5911))

### Refactor

- change parent class to Java `Object` ([8aaa459](https://github.com/ignition-api/8.1/commit/8aaa45969901a8c75b0ca32b89e1cba681fbd66d))
- Sourcery refactored main branch (#1)
- improve Version comparison logic (#11)

### Build

- bump actions/checkout from 2 to 3 (#7)
- bump actions/setup-python from 2 to 3 (#8)
- bump .pylintrc from 2.12.2 to 2.13.2 (#12)
- pre-commit autoupdate (#15)

### Revert

- remove condition from job (#9)

## [8.1.15] - 2022-03-02

### Features

- add `system.user.getUserSources` function ([9dcfa9a](https://github.com/ignition-api/8.1/commit/9dcfa9a3433f0f23e9556a24fdd5276b080d5f15))

### Miscellaneous Tasks

- cleanup `.pylintrc` ([11a9218](https://github.com/ignition-api/8.1/commit/11a92187ffd8210a8324141b7a334617f2b922f8))

### Styling

- format `pyproject.toml` with `pyproject-fmt` ([1340e23](https://github.com/ignition-api/8.1/commit/1340e23127e91f7c06fead73c5bb333a1fe03346))

### Build

- update black from 21.12b0 to 22.1.0 ([df5d6e9](https://github.com/ignition-api/8.1/commit/df5d6e999405f4e5d09f644c215eaa88fc0552d5))
- add `sort-all@v1.2.0` ([3eeeb97](https://github.com/ignition-api/8.1/commit/3eeeb970ea96f3b1807af0a35d37f5fae7cb6e81))

## [8.1.13.post1] - 2022-01-20

### Features

- update type hinting on `translate` ([3e0ef7f](https://github.com/ignition-api/8.1/commit/3e0ef7f7c9285472bb831ae5c0d721d8aa3aead5))

### Miscellaneous Tasks

- update .gitignore ([485ef22](https://github.com/ignition-api/8.1/commit/485ef2285a3ecc26bdeedb1d5a08195d7ec6c794))
- prepare from v8.1.13.post1 ([7de177a](https://github.com/ignition-api/8.1/commit/7de177ada0d015244e2579b54b60185fd08236ee))

### Revert

- undo `java.lang.String` ([8b9c99c](https://github.com/ignition-api/8.1/commit/8b9c99c77ff4e47e53fd9813218ef5a38aa64c09))

## [8.1.13] - 2021-12-22

### CI

- update CI workflow ([385ba77](https://github.com/ignition-api/8.1/commit/385ba776d5aeef99afde2aaae0ca48af080d1c1f))
- fix `mypy` step ([49620da](https://github.com/ignition-api/8.1/commit/49620da52802a9bd70db4c6da3d61624741b771a))

### Documentation

- update packages' descriptions ([275e1c7](https://github.com/ignition-api/8.1/commit/275e1c7f82ae4395bc3e063d2808530adcdf2f8b))

### Features

- simplify `beep` code ([5074d09](https://github.com/ignition-api/8.1/commit/5074d09498e2eb6b45d553f435a8145da5c9686d))
  - **BREAKING**: `system.util.beep()` will print "Beep!" when called
regardless of platform

### Miscellaneous Tasks

- add `cliff.toml` file for changelog generation ([e63ff91](https://github.com/ignition-api/8.1/commit/e63ff91ef1617c8b4c6d5a64a01d2e5f276647f4))
- format setup.cfg file ([5915921](https://github.com/ignition-api/8.1/commit/5915921282302c40ffbea5ad20b8213530591b8f))
- update `.pylintrc` remove `unused-import` ([832cb11](https://github.com/ignition-api/8.1/commit/832cb1131a22b237c6311be7a2f8e8116fcd64b2))
- prepare from v8.1.13 ([cbbe7c5](https://github.com/ignition-api/8.1/commit/cbbe7c5242cba5529393395b9a8209db6cfce6ed))

### Refactor

- change return type to `unicode` ([ddb184d](https://github.com/ignition-api/8.1/commit/ddb184dfc0edabb937c399a85cf64146c6a75380))
- rename argument from pageID to pageId ([45bbf4f](https://github.com/ignition-api/8.1/commit/45bbf4f7704e814f3a3d326f671c9538dba17ada))
- integrate minor changes ([a008eed](https://github.com/ignition-api/8.1/commit/a008eed420bf112fd2bdc2876cf61f4315340362))
- define ColType as a type alias ([d18d44d](https://github.com/ignition-api/8.1/commit/d18d44dd40acd985cf3c22ec1d04ff435722a185))
- move `String` alias to `java.util` ([ea530ac](https://github.com/ignition-api/8.1/commit/ea530ac1918b3e1e0204793ce1b607646c8c4c89))

### Styling

- tell `isort` to sort using Python 2.7 ([72fd6d0](https://github.com/ignition-api/8.1/commit/72fd6d060c26dd82b3492983f2e0ac63f8e42d40))

### Build

- update `pydocstyle` hook ([b04be0b](https://github.com/ignition-api/8.1/commit/b04be0b7e87834ec0c94f1ec96abcab1b9e82ff4))
- pre-commit autoupdate (#52)
- remove files from `MANIFEST.in` ([d0fa375](https://github.com/ignition-api/8.1/commit/d0fa3755815b7f224b3268b00ee4776be07ff517))

## [8.1.12.post3] - 2021-11-29

### Features

- add `String` type ([215ad67](https://github.com/ignition-api/8.1/commit/215ad67d968c19af2d213bd37e014b4d5ed15112))

### Miscellaneous Tasks

- release 8.1.12.post3 ([f6a5ae1](https://github.com/ignition-api/8.1/commit/f6a5ae12c1b316a55d1156f633fbd71531ec7166))

## [8.1.12.post2] - 2021-11-26

### Miscellaneous Tasks

- release 8.1.12.post2 ([7324f0b](https://github.com/ignition-api/8.1/commit/7324f0bc66f71a6e3931ad6f4394c88b07930039))

### Build

- update `.pylintrc` ([8b536ba](https://github.com/ignition-api/8.1/commit/8b536ba7b4c58b3d22c6c2ae0bd582717ab4e79d))
- Python 2 Only ([e697f09](https://github.com/ignition-api/8.1/commit/e697f09f4c4b05abc53ebffab3bb76e8b8553032))

## [8.1.12.post1] - 2021-11-26

### Bug Fixes

- install now requires `typing` ([7ed8b2b](https://github.com/ignition-api/8.1/commit/7ed8b2b284a0f6982a4520cbde0b8af0ee64f535))

### Miscellaneous Tasks

- release 8.1.12.post1 ([e9bebaf](https://github.com/ignition-api/8.1/commit/e9bebaf38c976bae15eccd510f35291799ffcd7c))

## [8.1.12] - 2021-11-23

### Documentation

- include `org.python` package ([b0ec4b5](https://github.com/ignition-api/8.1/commit/b0ec4b510750218e0815ad0c84ac90112a4730d5))

### Features

- add symbols to `format` to cover most cases ([9948292](https://github.com/ignition-api/8.1/commit/9948292c55a0b9912cd66073637e5b173d8baf26))
- improve `date.format` ([0e527d2](https://github.com/ignition-api/8.1/commit/0e527d26d679c90fd99afefb90063044baf56126))
- add type hints on all system functions ([51ed6a2](https://github.com/ignition-api/8.1/commit/51ed6a2a0e3e5a20b02bd3dab82bc927729594f2))
  - **BREAKING**: * Python versions below or above 2.7.18 are not supported
* `system.date` and Java's Date are no longer using `datetime` functions
* remove deprecated functions from `system.tag`

### Miscellaneous Tasks

- ignore `pyenv` files ([c10787a](https://github.com/ignition-api/8.1/commit/c10787a2b1f17d843aeafae44f3943f9fee658f2))
- release 8.1.12 ([ca1e665](https://github.com/ignition-api/8.1/commit/ca1e665585c5178cd9cac0252bd0e3c302adc282))

### Styling

- use `black` default settings ([5b1da1f](https://github.com/ignition-api/8.1/commit/5b1da1f212541b1f4ff5f51aee13106b8430123e))

### Build

- add project_urls ([8a37d41](https://github.com/ignition-api/8.1/commit/8a37d41a0ddd0243efb097c26fff3e5401ff9500))
- add setup.py ([4c4cae6](https://github.com/ignition-api/8.1/commit/4c4cae65ecb9b5f71aa193087cf89c627c29a7b0))
- update `black` hook ([a39dcdc](https://github.com/ignition-api/8.1/commit/a39dcdca750cca6ffa2b5d842c0e83691d229506))
- pre-commit autoupdate (#51)
- deprecate Python 2.7 ([3c79759](https://github.com/ignition-api/8.1/commit/3c79759ad291b47f464dd42a9121b6aa21eb8f02))
- pre-commit autoupdate ([3556987](https://github.com/ignition-api/8.1/commit/35569875c9d9d48a2411e11fa103d31ffdf98bbf))
- pre-commit autoupdate ([d250949](https://github.com/ignition-api/8.1/commit/d250949865cc6aa4436442576c40b9e1d0137661))
- pre-commit autoupdate ([4e067e3](https://github.com/ignition-api/8.1/commit/4e067e304cc4798ceb278f43b0d98bedbc88a60c))

## [8.1.11] - 2021-10-20

### Documentation

- update usage instructions ([63e6c14](https://github.com/ignition-api/8.1/commit/63e6c143ab67daafd8691b1faf9573c5669df18f))

### Features

- add Iterable Java interface ([c23a469](https://github.com/ignition-api/8.1/commit/c23a4692f1c6180b6a9aa999026e19e43640f79f))
- add org.python.core package ([bb8ac0c](https://github.com/ignition-api/8.1/commit/bb8ac0c0eeb8eb5a442c42d022a2f2f44228280c))
- add AlarmEvent, PyAlarmEvent, and PyAlarmEventImpl ([13907c9](https://github.com/ignition-api/8.1/commit/13907c991fd814ee493fd40f11e1d7820ef4eee9))

### Miscellaneous Tasks

- switch to static metadata ([ac01e1b](https://github.com/ignition-api/8.1/commit/ac01e1b390bab245e3d38b9e581920c1b418061c))
- archive `jython` branch ([894b055](https://github.com/ignition-api/8.1/commit/894b055b3a6c84919e5a31bd57270ef04d5f8055))
- release 8.1.11 ([520919d](https://github.com/ignition-api/8.1/commit/520919d16371974563f65f693d6ffc628dd77e84))

### Build

- pre-commit autoupdate (#49)
- require setuptools >= 42 ([c784e57](https://github.com/ignition-api/8.1/commit/c784e573530a217f4c430bd110889ce569152747))

## [8.1.10.post7] - 2021-10-11

### Features

- add PrintStream class to java.io package ([32d0479](https://github.com/ignition-api/8.1/commit/32d0479df461bb41c66a8361bf9862c9347499e4))

### Miscellaneous Tasks

- git ignore dist-build directory ([368efb9](https://github.com/ignition-api/8.1/commit/368efb916ccd507eb7047794e9662638ed886f20))

## [8.1.10.post6] - 2021-10-10

### Bug Fixes

- PyUser now returns an instance of User ([65dbaaa](https://github.com/ignition-api/8.1/commit/65dbaaa5b450f56986ddc91e3790d4137b928422))

### CI

- update PyPI upload workflow ([93917b6](https://github.com/ignition-api/8.1/commit/93917b6de9990bb1ec4b870058cb57993fa7bfa9))

### Documentation

- fix markdownlint issues ([94ad494](https://github.com/ignition-api/8.1/commit/94ad494de9dcb3479db9aa3136ebda55843d7c36))
- fix PyCharm heading ([b8b53a1](https://github.com/ignition-api/8.1/commit/b8b53a108837fdc557e73692d3ed7a051aa4a6fa))
- update return type ([c6b9887](https://github.com/ignition-api/8.1/commit/c6b9887d161a367dde4be5cb3150d23e92efb965))

### Features

- return instance of BasicDataset ([2473ff4](https://github.com/ignition-api/8.1/commit/2473ff4eade0463026358e5ea4162e8e95e0e62e))
- add fields and implement more methods ([1f17c83](https://github.com/ignition-api/8.1/commit/1f17c83b144184a626d77ff8ba6c45bb2b9dc1fc))
- add Java supporting classes ([f56f2a4](https://github.com/ignition-api/8.1/commit/f56f2a444b63e9a4160f9900823248bae56ad9f5))

### Miscellaneous Tasks

- prepare for version 8.1.11 ([88c45c4](https://github.com/ignition-api/8.1/commit/88c45c4791a23241c320df1ca06ca9c6963a5ba5))
- prepare for v8.1.10.post6 ([54da8c2](https://github.com/ignition-api/8.1/commit/54da8c2ebc28231bc21fbf2ef39bd22c4d163879))

### Refactor

- turn fields into properties ([bcc57c2](https://github.com/ignition-api/8.1/commit/bcc57c25e918b93d30154cd6dfd15a4dabe69818))
- switch to informal interfaces ([aba37e1](https://github.com/ignition-api/8.1/commit/aba37e1a2a338da6c540da7fcbef1f315619bd9b))
- return instance of implementing classes ([e08bbf9](https://github.com/ignition-api/8.1/commit/e08bbf91414cf08487422a07ae5ccac6445aa7f0))
- informal interfaces ([b79ca39](https://github.com/ignition-api/8.1/commit/b79ca393d7e85a02b79e78e5a7ee90bcfb5d99ca))

### Build

- update pre-commit hooks ([1b538e6](https://github.com/ignition-api/8.1/commit/1b538e6bcb9fa1cfdefb7d01f2126026edded222))
- update pylint workflow ([684f4d5](https://github.com/ignition-api/8.1/commit/684f4d5bf38bdd9eecb8470a04e173f713dcb283))
- update workflows ([6977b00](https://github.com/ignition-api/8.1/commit/6977b009b47e6fbb95a45e82f3ebea32d49538eb))

## [8.1.10.post5] - 2021-09-24

### Bug Fixes

- remove builtins import statement ([3c62913](https://github.com/ignition-api/8.1/commit/3c62913d967f5a76a71ca3e7f3068e87bad7344f))

## [8.1.10.post4] - 2021-09-22

### Documentation

- update installation and usage ([2acc3c0](https://github.com/ignition-api/8.1/commit/2acc3c05849653905817d699d64ce187a7e7dc52))

### Features

- make code compatible with Python3 ([29d87d1](https://github.com/ignition-api/8.1/commit/29d87d190b7e723b397b4ec9cf7a969363c53fd3))

## [8.1.10.post3] - 2021-09-21

### Features

- make PyDataSet iterable ([ccea300](https://github.com/ignition-api/8.1/commit/ccea30071a576805e72a9688fac85a8f28666b31))

## [8.1.10.post2] - 2021-09-20

### Bug Fixes

- move `WindowUtilities` to the correct package ([5af2ad8](https://github.com/ignition-api/8.1/commit/5af2ad84a90ba0f130e5aa1707962d841eac2464))

### CI

- disable consider-using-f-string ([347607a](https://github.com/ignition-api/8.1/commit/347607a8868e5c9c3e65a71870dd55e1c0a724d5))

### Features

- disallow installation on Python 3 ([4397007](https://github.com/ignition-api/8.1/commit/4397007a37627842bec46ed38e224f223cc7e442))
- add `com` package to `pip` release ([533169b](https://github.com/ignition-api/8.1/commit/533169baed2c349119166c9afe4c8281db5536aa))

### Refactor

- add `com` package ([55f7a73](https://github.com/ignition-api/8.1/commit/55f7a7333d04820db8ef27df5e613764baa3e8f3))
- improve code quality ([3abb414](https://github.com/ignition-api/8.1/commit/3abb4146d12a85b1fa099565037c0893875aaad8))
- improve code quality ([5df0faa](https://github.com/ignition-api/8.1/commit/5df0faae4d58042d60c18023328edf988937562a))

### Styling

- put __all__ in a single line ([5d44f14](https://github.com/ignition-api/8.1/commit/5d44f1483c3ca41d749401e30a2cc72e840fc5e1))

### Build

- modify pylint workflow ([5cd6e27](https://github.com/ignition-api/8.1/commit/5cd6e27496ec25d56044df9373becf8acd11e606))
- pre-commit autoupdate ([68dad9f](https://github.com/ignition-api/8.1/commit/68dad9fb8e1cef359b84312176f1a4686587fa13))

## [8.1.10] - 2021-09-09

### Documentation

- fix broken link ([6aecd76](https://github.com/ignition-api/8.1/commit/6aecd76573157bd10c38a24b5d36c96fe000445d))
- :pencil2: fix typo ([e2be820](https://github.com/ignition-api/8.1/commit/e2be82075d9bfed5670df6c0c13f1699b87778d4))

### Features

- add setup.py ([84b53da](https://github.com/ignition-api/8.1/commit/84b53da99b5a7b256715b608b48acaee067382d8))
- 8.1.10 ([20a3a89](https://github.com/ignition-api/8.1/commit/20a3a89aec122d9ed15867afcd4393f36a4756cd))

### Refactor

- add pylint ([1b5a526](https://github.com/ignition-api/8.1/commit/1b5a52651ce78166b5a7bdc70916686d76c76652))
- allow any import level for winsound ([57ee2b6](https://github.com/ignition-api/8.1/commit/57ee2b699d440012cb9b652c98f9ff0173f57098))

### Styling

- fix pylint found errors ([ef8b662](https://github.com/ignition-api/8.1/commit/ef8b662f6d4efce7b0d56ac4e10f4216a40ca3d9))

### Build

- pre-commit autoupdate (#46)
- skip pylint ([7dc2336](https://github.com/ignition-api/8.1/commit/7dc23365a054b5a85efba496987674aeeefb7aca))
- add pylint workflow ([fb675a9](https://github.com/ignition-api/8.1/commit/fb675a9e18e7a6c5dd744c6d3e43aa6887e55442))

## [8.1.9] - 2021-08-09

### Documentation

- update README.md ([4cf18f4](https://github.com/ignition-api/8.1/commit/4cf18f4cf07e37cf23301c248333bad691cecf7d))
- update README.md ([95d2f88](https://github.com/ignition-api/8.1/commit/95d2f8820c9291ac0d5c364bbbb96cbd55de9d06))
- update README.md ([8531b0e](https://github.com/ignition-api/8.1/commit/8531b0e4c2860b0ff070a365e0ce28c0f8033215))
- replaced datetime for Date ([dbc151a](https://github.com/ignition-api/8.1/commit/dbc151a8178e956ec2c0535f6416bad57bb11867))
- add instructions for PyCharm (#42)

### Features

- add new OPC-UA functions ([6a4ba1b](https://github.com/ignition-api/8.1/commit/6a4ba1bb21eea36a9cded712f77ff34d08bffb29))

### Build

- add ci block ([a4626df](https://github.com/ignition-api/8.1/commit/a4626df596a6dd87dfba49a656056c717cf50569))
- pre-commit autoupdate (#40)
- check max complexity ([c9e185f](https://github.com/ignition-api/8.1/commit/c9e185f9f52c46c1931544f79ef0d21a811a71cf))
- pre-commit autoupdate (#43)
- pre-commit autoupdate (#44)
- pre-commit autoupdate (#45)

## [8.1.7] - 2021-06-05

### Features

- bump Ignition 8.1.5 -> 8.1.6 ([8e87ab4](https://github.com/ignition-api/8.1/commit/8e87ab430b7fa895baf8ff4c7fd9e9763fc56247))
- 8.1.7 ([91b4735](https://github.com/ignition-api/8.1/commit/91b47359a015c0081e950e05423511d0d2aab066))

### Refactor

- java.util.Date ([370503c](https://github.com/ignition-api/8.1/commit/370503c56f0b1d0f7a5f0579422412cde4606a02))

## [8.1.6] - 2021-05-24

### Miscellaneous Tasks

- update .gitignore ([cccd791](https://github.com/ignition-api/8.1/commit/cccd791a1e3156d774b6bf8256e56d3cf284dd70))
- add .wakatime-project ([d166ff3](https://github.com/ignition-api/8.1/commit/d166ff3e967091a715bdc70b97f45b80b47c651f))

### Styling

- change from single quotes to double quotes ([021ed8b](https://github.com/ignition-api/8.1/commit/021ed8b9175910287b001ef5895ad2da4302c8ea))

### Build

- rearrange hooks ([ada39b0](https://github.com/ignition-api/8.1/commit/ada39b0e0972c37e67a7a6c2af03d0be1c9b0ab9))
- add pydocstyle hook ([384dd21](https://github.com/ignition-api/8.1/commit/384dd216547e97f266df0d0c7b5bc287f4edbfa5))
- remove D209 from ignored codes ([35374c7](https://github.com/ignition-api/8.1/commit/35374c751bcf473b2385f05d31cbea56818fc05f))
- remove E211 and E99 from ignore ([0edf0ec](https://github.com/ignition-api/8.1/commit/0edf0eccd2661355f5929416c21c6ef9b112151f))
- remove W503 from ignore ([ac25bbe](https://github.com/ignition-api/8.1/commit/ac25bbeb64c8e08d521026965b6c7af5e0a6a412))

## [8.1.5-fix] - 2021-05-11

### Bug Fixes

- correct typo in docstring ([bfc95e9](https://github.com/ignition-api/8.1/commit/bfc95e9e223bbe6df4e301311d1221c16b56ae49))
- add missing parameter to… ([1185e03](https://github.com/ignition-api/8.1/commit/1185e038c1e7fc9deb15602244991038115a2f61))

### Features

- update black 21.4b2 -> 21.5b0 ([616009d](https://github.com/ignition-api/8.1/commit/616009d46d873fc562c06a3c5548d8e40d60a89d))
- update flake8 3.9.1 -> 3.9.2 ([b67503c](https://github.com/ignition-api/8.1/commit/b67503c5414c1c2eba9d9918ec8a5d90caa23979))
- update black 21.5b0 -> 21.5b1 ([9226438](https://github.com/ignition-api/8.1/commit/92264382a304639b2e79dde749cfb0e639e38e1d))

## [8.1.5] - 2021-04-28

### Features

- add build number and update all references ([7747ba5](https://github.com/ignition-api/8.1/commit/7747ba524b75b45138f94f561841f9bffa7b9235))
- add toParseableString implementation ([0224a9e](https://github.com/ignition-api/8.1/commit/0224a9edfbbf8dead48692d64cb894bbaf73cefe))
- bump flake8 to 3.9.1 ([5a5de40](https://github.com/ignition-api/8.1/commit/5a5de40e5e2aa4135466126fac6812c1f2ead602))
- update black 20.8b1 -> 21.4b0 ([e2f713e](https://github.com/ignition-api/8.1/commit/e2f713efe1b54cd2f8d4849d799d650c42686270))
- update black 21.4b0 -> 21.4b1 ([3845ac8](https://github.com/ignition-api/8.1/commit/3845ac81b2394cdaf38a300bd8ba078ff6547c0f))
- update black 21.4b1 -> 21.4b2 ([1aeb50a](https://github.com/ignition-api/8.1/commit/1aeb50a72fbd7ff9367f7917c4ab20c32243796d))
- add 8.1.5 changes ([4abd6fa](https://github.com/ignition-api/8.1/commit/4abd6fa9adbddf6d4bd8909129c4e9c78316a144))

### Styling

- update docstrings ([8f8ee33](https://github.com/ignition-api/8.1/commit/8f8ee33de651fe09b2cfeae2bcdb65d0d2b98700))

## [8.1.4] - 2021-04-02

### Documentation

- update the copyright notice date ([95cd608](https://github.com/ignition-api/8.1/commit/95cd608f68eb7ff53b2fa012568df2113ac645e8))

### Features

- add getSessionInfo ([7f64b25](https://github.com/ignition-api/8.1/commit/7f64b25d177fe605774a37bfd10a2cdf2be97b21))

### Build

- bump flake8 and isort to latest version ([f4d8fef](https://github.com/ignition-api/8.1/commit/f4d8fef980400e8357f11be8a74a28839b6b9fa0))

## [8.1.3] - 2021-03-04

### Features

- add new arguments to Perspective functions ([fd1beb3](https://github.com/ignition-api/8.1/commit/fd1beb3602d45af16a8324f8e4646fe7d0ae0575))

### Miscellaneous Tasks

- update .gitignore ([1be4f3c](https://github.com/ignition-api/8.1/commit/1be4f3c94e4e7aa02705bf2e68cebded4d619514))

### Styling

- :art: tell isort to use Python27 ([873015f](https://github.com/ignition-api/8.1/commit/873015fd0331fe44b240c3823f1591b753f01607))
- remove blank line ([8b62da4](https://github.com/ignition-api/8.1/commit/8b62da459e1009ae75fb25cba6410d22ac9b4ec4))

## [8.1.2] - 2021-02-12

### Features

- add flake8 and isort pre-commit hooks ([0288aab](https://github.com/ignition-api/8.1/commit/0288aab37a14869aefa7d13d622aa0d69175620b))

### Miscellaneous Tasks

- modify .py files permission ([7208fb0](https://github.com/ignition-api/8.1/commit/7208fb041642d58fae63d9d0499880a775bdde77))
- add targeted Ignition version ([5c89c85](https://github.com/ignition-api/8.1/commit/5c89c8504ccb5e7258476b88666231f095dbcc74))

### Styling

- flake8 [py27] ([2123ca8](https://github.com/ignition-api/8.1/commit/2123ca8fa6968193d40fda2c8b2fe65865ee0803))
- add flake8 and isort badges ([a0319f7](https://github.com/ignition-api/8.1/commit/a0319f7923f71624aa96f750357a247580914452))
- :art: make isort compatible with black ([df9d357](https://github.com/ignition-api/8.1/commit/df9d357859c5ce37f7020952bfee3661e4db131a))

## [8.1.1] - 2020-12-09

### Styling

- Black ([9db745d](https://github.com/ignition-api/8.1/commit/9db745d9b14fb6f5ced27a357db89ac53bfb4be1))

## [8.1.0] - 2020-11-15

### All

- Updated copyright legend. ([31c53f7](https://github.com/ignition-api/8.1/commit/31c53f7ad1f937a402cd52dd7fb0447fa508412f))

### Db

- Added getConnectionInfo and setDataSeourceEnabled. ([db6dfd6](https://github.com/ignition-api/8.1/commit/db6dfd69490d541557ca2cc15a11301ef746a331))

### File

- Fixed docstring. ([7f8a07d](https://github.com/ignition-api/8.1/commit/7f8a07d195ce4d77dbba7ab0732bdd54fc573f72))

### Incendium.gui

- added warning, modified error. Added java.lang, and javax.swing packages. Opting for JOptionPane over Ignition's own errorBox and warningBox. ([ff1c03e](https://github.com/ignition-api/8.1/commit/ff1c03edae7fb1bde5c4b9bc4cd67a6e439449c3))
- Modified info method in order to use JOptionPane. ([487231e](https://github.com/ignition-api/8.1/commit/487231e922023311c949f54093556c804c722567))
- Added input function. ([0d8320a](https://github.com/ignition-api/8.1/commit/0d8320a3dab50c997c95690f1b1105b7c064d54d))

### Incendium.util

- Added get_timer ([d9b0a70](https://github.com/ignition-api/8.1/commit/d9b0a706a8d011b43511708f16a3f28d1ea0c5d0))

### Java

- Updated copyright legend. ([b7a2f31](https://github.com/ignition-api/8.1/commit/b7a2f31b137d1cff24f55d97eb213dfd94a4485e))

### Javax

- Updated copyright legend. ([ab859d3](https://github.com/ignition-api/8.1/commit/ab859d36e2000bc7f2f737a5068216073a319e4c))

### Lang

- Throwable now inherits from BaseException. ([5f19240](https://github.com/ignition-api/8.1/commit/5f192403bad2fdea48f0103ec633c33772a4f942))

### Perspective

- Added missing methos to __all__ ([1f2dc97](https://github.com/ignition-api/8.1/commit/1f2dc9733ef33de55869cecb4888134a4a6f3a49))

### System

- Updated copyright legend. ([7b4852d](https://github.com/ignition-api/8.1/commit/7b4852d0a374777ec796bbf899d29f674f77be77))

### Tag

- Update docstring. ([f5e3cbc](https://github.com/ignition-api/8.1/commit/f5e3cbc981f252b025d77916d557f83eb748f12f))
- Code clean-up. ([fb53d8e](https://github.com/ignition-api/8.1/commit/fb53d8e0f1d5a2f1bfc2fdf217311d77f781cb8e))

### Util

- Added argument to winsound.MessageBeep funciton call. ([d06c492](https://github.com/ignition-api/8.1/commit/d06c492955347f2ca3b43ae7ad9ad442298c3638))

### Validate_form

- For numbers and collections we should compare to None. ([7a07ba5](https://github.com/ignition-api/8.1/commit/7a07ba5c278d40c620c189711be4a4f319858114))

<!-- generated by git-cliff -->
