# supuner 0.3 (2024-03-08)

* Better cross-platform installation (e.g. respecting `DESTDIR`). The
  `Makefile` now requires `gmake`.

* Various suggestions from `shellcheck`.

* Clarify why -e is forbidden unless -o is also specified.


# supuner 0.2 (2020-02-17)

* Document that `-e` sends *combined* stderr/stdout output to stdout.

* Error if `-e` is specified without `-o`, since the previous behaviour of `-e`
  without `-o` had no use (and mildly surprising semantics).

* Use the OS's `basename` program rather than a hand-rolled alternative.


# supuner 0.1 (2011-06-19)

First release.
