# tackle

Convert tabular data into another format

**Status:** This project is not ready for mainstream use nor under active development.
I'm using it to convert CSV into json or XLS, but I'm not developing
it further unless I have a real use case for it.

Tips for working with tabular data or json in general:

* [jq](https://stedolan.github.io/jq/) command-line tool is great (`brew install jq`)
* Python [tablib](http://docs.python-tablib.org/) library (`pip install tablib`)
* OpenOffice lets you select the character set when opening a CSV file

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

## Examples

All examples can be found under the `tests/data` directory.

Convert a CSV file (utf-8 encoding) into an XLS spreadsheet:

    $ tackle utf8.csv -t utf8.xls

Convert a CSV file (isolatin encoding) into an XLS spreadsheet:

    $ tackle isolatin.csv --charset iso-8859-1 -t iso.xls

## Plan

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
