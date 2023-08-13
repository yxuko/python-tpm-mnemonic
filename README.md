# Python-mnemonic

<img src="https://badge.fury.io/py/mnemonic.svg"/>

Reference implementation of BIP-0039: Mnemonic code for generating deterministic keys.

## Abstract

This BIP describes the implementation of a mnemonic code or mnemonic sentence -- a group of easy to remember words -- for the generation of deterministic wallets.

It consists of two parts: generating the mnenomic, and converting it into a binary seed. This seed can be later used to generate deterministic wallets using BIP-0032 or similar methods.

## BIP Paper

See https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki for full specification.

## Installation

Please make sure that you have python 3.7 or higher.

To install this library and its dependencies use, run the following command in the current directory:

 ```console 
 python setup.py install develop
 ```

## Usage examples

Import library into python project via:

```python 
from mnemonic import Mnemonic
```

Initialize class instance, picking from available dictionaries:

- english
- chinese_simplified
- chinese_traditional
- french
- italian
- japanese
- korean
- spanish
- turkish
- czech
- portuguese

```python 
mnemo = Mnemonic(language)
mnemo = Mnemonic("english")
```

Generate word list given the strength (128 - 256):

```python 
words = mnemo.generate(strength=256)
```

Given the word list and custom passphrase (empty in example), generate seed:

```python 
seed = mnemo.to_seed(words, passphrase="")
```

