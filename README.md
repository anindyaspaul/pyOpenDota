
# pyOpenDota
[![PyPI](https://img.shields.io/pypi/v/opendota.svg?style=flat-square)](https://pypi.python.org/pypi/opendota) [![Travis](https://img.shields.io/travis/anindyaspaul/pyOpenDota.svg?style=flat-square)](https://travis-ci.org/anindyaspaul/pyOpenDota) [![Codecov](https://img.shields.io/codecov/c/github/anindyaspaul/pyOpenDota.svg?style=flat-square)](https://codecov.io/gh/anindyaspaul/pyOpenDota) [![license](https://img.shields.io/github/license/anindyaspaul/pyOpenDota.svg?style=flat-square)](https://github.com/anindyaspaul/pyOpenDota/blob/master/LICENSE)  

Python client for the [OpenDota API](https://www.opendota.com)

## Installation

```bash
$ pip install opendota
```

## Usage

```python
>>> from opendota.player import Player
>>>
>>> player = Player(account_id=243478749)
>>> player
<opendota.player.Player object at 0x103f64208>
>>> solo_mmr = player.solo_competitive_rank
>>> solo_mmr
2518
>>> tracked_until = player.tracked_until
>>> tracked_until
datetime.datetime(2017, 11, 19, 21, 18, 41)
```