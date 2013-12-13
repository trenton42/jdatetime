===============================
Julian Datetime
===============================

A Julian date time replacement

* Free software: BSD license

Features
--------

* Rid thyself of pesky timezones and daylight saving time
* Sort of works as a limited replacement to datetime (with text formatting, too!)
* New Day names and Month names that were badly picked during a sleepless night

Usage
-----

```python
from jdatetime import jdatetime

d = jdatetime.now()  # Today's date

print "{:%m/%d/%Y}".format(d)

# '06/40/2456'

```