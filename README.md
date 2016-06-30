pocketsphinx-python-light
=========================

Python interface to CMU SphinxBase and PocketSphinx libraries created with SWIG.
Pocketsphinx packages include python support, however, it is not well supported on OpenWrt.

This package provides module created with Python distutils setup.

Supported Platforms
-------------------

- OpenWrt


Basic usage
-----------

```python
#!/usr/bin/env python
from os import environ, path

from pocketsphinx.pocketsphinx import *

MODELDIR = "pocketsphinx/model"
DATADIR = "pocketsphinx/test/data"

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us/en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'en-us/cmudict-en-us.dict'))
decoder = Decoder(config)

# Decode streaming data.
decoder = Decoder(config)
decoder.start_utt()
stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
while True:
  buf = stream.read(1024)
  if buf:
    decoder.process_raw(buf, False, False)
  else:
    break
decoder.end_utt()
print ('Best hypothesis segments: ', [seg.word for seg in decoder.seg()])
```
