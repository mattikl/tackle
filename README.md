# tackle

Convert tabular data into another format

Status: basic functionality is starting to be there, but still changing the
interface a lot.

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
* idea: custom plugins in git
* tests
* travis.yml
* use chardet
    * also not to print binary data to stdout
* add --test to test parsing input
* add tackle-mgmt --testall to test all readers and writers with
  a test fixture
