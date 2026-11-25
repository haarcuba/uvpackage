---
description: forces maximum function length of 10 on the code
disable-model-invocation: true
argument-hint: <path>
---

run

    $ lizard -L 10 $ARGUMENTS

and fix the code so that there are no warnings.
if you can't lose all the warnings after ten runs of `lizard`, then stop

you don't need to install lizard, it's available. just run it.
