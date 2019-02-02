# hashfuzz
HashFuzz:
* Detect similarity between strings
* Generate a similarity hash

# Distance/likeness Ratio Examples
```
>>> import hashfuzz as hf
>>> from difflib import SequenceMatcher
>>> #
... # Compare difflib.SequenceMatcher() to hashfuzz.ratio()
... #
...
>>> a = 'apple'
>>> b = 'apple'

>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=100.00 SequenceMatcher=100.00'

>>> b = 'appel'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=99.99 SequenceMatcher=80.00'

>>> b = 'Apple'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=80.00 SequenceMatcher=80.00'

>>> b = 'Apples'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=72.72 SequenceMatcher=72.73'

>>> b = 'An apple'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=57.65 SequenceMatcher=76.92'


>>> a = 'Hi Mr. Belvedere,\nYour next scheduled appointment is at 3pm on Tuesday.'
>>> b = 'Hi Mr. Anderson,\nYour next scheduled appointment is at 2pm on Friday.'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=87.14 SequenceMatcher=85.71'

>>> b = 'Hello Mr. Torvalds,\nYour next scheduled appointment is at 8:30am on Tuesday.'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=75.13 SequenceMatcher=84.35'

>>> a = 'This text will not be like that of b'
>>> b = 'Not many words of a are in b, but this also matches near characters'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=41.51 SequenceMatcher=11.65'


>>> a = 'Nothing similar'
>>> b = 'Everything different'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=52.75 SequenceMatcher=45.71'

>>> a = 'Nothing similar'
>>> b = 'GREAT FUTURE'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=10.26 SequenceMatcher=7.41'

>>> a = 'Nothing similar'
>>> b = 'GREATFUTURE'
>>> 'hashfuzz=%.2f SequenceMatcher=%.2f' % (hf.ratio(a, b), SequenceMatcher(None, a, b).ratio() * 100)
'hashfuzz=0.00 SequenceMatcher=0.00'
```

# Hash Examples
```python
>>> import hashfuzz as hf
>>> a = 'Guido van Rossum'
>>> b = 'Guido van Rossum'
>>> hf.ratio(a, b)
100.0
>>> hf.hash(a, b)
'b825e62e86b6ec7824bc4e8d68965136d0396c30aebd8ced9a09dfab3a5cbcee'

>>> b = 'Guido van Rossums'
>>> hf.ratio(a, b)
96.96
>>> hf.hash(a, b)
'b825e62e86b6ec7824bc4e8d68965136d0396c30aebd8ced9a09dfab3a5cbcee'

>>> b = 'Guido van Rossumss'
>>> hf.ratio(a, b)
94.11
>>> hf.hash(a, b)
'b825e62e86b6ec7824bc4e8d68965136d0396c30aebd8ced9a09dfab3a5cbcee'

>>> b = 'GGuido van Rossumss'
>>> hf.ratio(a, b)
94.1633
>>> hf.hash(a, b)
'b825e62e86b6ec7824bc4e8d68965136d0396c30aebd8ced9a09dfab3a5cbcee'

>>> b = 'Mr. Guido van Rossum'
>>> hf.ratio(a, b)
53.36
>>> hf.hash(a, b)
'6c179f21e6f62b629055d8ab40f454ed02e48b68563913473b857d3638e23b28'

>>> b = 'Mr. Guido van Rossums'
>>> hf.ratio(a, b)
60.85
>>> hf.hash(a, b)
'6c179f21e6f62b629055d8ab40f454ed02e48b68563913473b857d3638e23b28'
```
