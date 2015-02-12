# tackle
Convert tabular data into another format

Status: very early in development, just converts csv into json as of now.

## Idea

Getting data in spreadsheets that needs to be imported into a system is usually
a tedious task. Tackle tries to make good guesses and point out inconsistencies.
Most importantly, you can write your own readers and writers for the specific data
and run them easily.

## Developing

Set up virtualenv in tackle directory:

    $ virtualenv env
    $ source env/bin/activate
    $ pip install --editable .

and you're ready to tackle:

    $ tackle tests/data/test.csv -n foos

## TODO

* Python 3 compliance (currently requires 2.7 due to the importlib import)
* support custom readers and writers
* read from multiple sources (idea)
