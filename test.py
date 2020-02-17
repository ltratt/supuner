#! /usr/bin/env python3

import re, subprocess, sys, tempfile

# These regular expressions need to be as specific as possible while still
# catering for the different possible outputs that occur on real platforms.
RE_BIN_SH = re.compile("/bin/sh")
# On Debian:
#   $ ls /doesntexist
#   ls: cannot access '/doesntexist': No such file or directory
# On OpenBSD:
#   $ ls /doesntexist
#   ls: /doesntexist: No such file or directory
RE_DOESNT_EXIST = re.compile("ls: (cannot access ')?/doesntexist'?: No such file or directory")

def assert_in(l, res):
    for r in res:
        if r.match(l) is not None:
            return
    print("No match for '%s'" % l)
    sys.exit(1)

s = subprocess.run(["./supuner", "ls", "/bin/sh"], \
      capture_output=True, encoding="utf-8")
assert s.returncode == 0
assert s.stderr.strip() == ""
assert s.stdout.strip() == ""

s = subprocess.run(["./supuner", "ls", "/bin/sh", "/doesntexist"],
      capture_output=True, encoding="utf-8")
assert s.returncode != 0
assert len(s.stderr.strip().split("\n")) == 2
for l in s.stderr.strip().split("\n"):
    l = l.strip()
    assert_in(l, [RE_BIN_SH, RE_DOESNT_EXIST])
assert s.stdout.strip() == ""

s = subprocess.run(["./supuner", "-e", "ls", "/bin/sh"],
      capture_output=True, encoding="utf-8")
assert s.returncode == 0
assert s.stderr.strip() == ""
assert s.stdout.strip() == "/bin/sh"

s = subprocess.run(["./supuner", "-e", "ls", "/bin/sh", "/doesntexist"],
      capture_output=True, encoding="utf-8")
assert s.returncode != 0
assert s.stderr.strip() == ""
assert len(s.stdout.strip().split("\n")) == 2
for l in s.stdout.strip().split("\n"):
    l = l.strip()
    assert_in(l, [RE_BIN_SH, RE_DOESNT_EXIST])

with tempfile.NamedTemporaryFile() as tf:
    s = subprocess.run(["./supuner", "-e", "-o", tf.name, "ls", "/bin/sh", "/doesntexist"],
          capture_output=True, encoding="utf-8")
    assert s.returncode != 0
    assert s.stderr.strip() == ""
    assert len(s.stdout.strip().split("\n")) == 2
    for l in s.stdout.strip().split("\n"):
        l = l.strip()
        assert_in(l, [RE_BIN_SH, RE_DOESNT_EXIST])

    with open(tf.name) as f:
        d = f.read()
        assert len(d.strip().split("\n")) == 2
        for l in d.strip().split("\n"):
            l = l.strip()
            assert_in(l, [RE_BIN_SH, RE_DOESNT_EXIST])
