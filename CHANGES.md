# supuner 0.2 (2020-02-17)

* Document that `-e` sends *combined* stderr/stdout output to stdout.

* Error if `-e` is specified without `-o`, since the previous behaviour of `-e`
  without `-o` had no use (and mildly surprising semantics).

* Use the OS's `basename` program rather than a hand-rolled alternative.


# supuner 0.1 (2011-06-19)

First release.
