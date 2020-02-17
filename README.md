# supuner

`supuner` (SUPpress UNless ERror) executes a command and manipulates its stderr
and stdout. By default, it captures both stderr and stdout and only outputs
their combined value to stdout if command fails. `supuner` is useful for
"chatty" commands whose output is only relevant if the command fails.


# Usage

```sh
supuner [-e] [-o file] command [options ...]
```

Options:

 * `-e` If `-o` is specified, then as well as sending output to a file, echo
   stdout and stderr combined to stdout.
 * `-o file` Send stdout and stderr to file.

`supuner` exits with the exit code of command.

# Examples

```sh
$ supuner ls /bin/sh
$ supuner ls /bin/sh /doesntexist
ls: /doesntexist: such file or directory
/bin/sh
$ supuner -o /tmp/o ls /bin/sh /doesntexist
$ echo $?
1
$ cat /tmp/o
ls: /doesntexist: such file or directory
/bin/sh
$ supuner -e -o /tmp/o ls /bin/sh /doesntexist
ls: /doesntexist: such file or directory
/bin/sh
$ echo $?
1
$ cat /tmp/o
ls: /doesntexist: such file or directory
/bin/sh
```

Using the fact that `supuner` exits with the exit code of command, one can use
the `||` operator to perform actions on the combined stdout / stderr output,
for example:

```
supuner -o /tmp/o ls /bin/sh /doesntexist >2 /dev/null \
  || mail -s 'Error from ls' somebody@example.com < /tmp/o
```
