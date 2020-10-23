# biotools
One off scripts and tools I use for bioinformatics things

## Tools in this repository have no guarantee of accuracy or broad applicability but may be useful to someone

## Tool List

* ***metaphlan_parser.py***
  * This program is designed to take metaphlan2 data converted with `metaphlan2krona.py` and format everything into a nice table for downstream work in `R`.
  
* ***plateo_order.py***
  * This program generates a dictionary of 96-well plate locations and a numerical ordering as well as a regular expression pattern for parsing files.
    * Sample names should be of the format `[Some text]_[0-9]+[A-H]_[Some more text]`.
    * The pattern can be run simply on an individual string as: `pattern.search([target string]).group(0)` ***This will fail if the string does not contain the pattern.***


## Accesory Files List

* ***well_table.txt***
  * Easy to import data table numbering wells on a plate, order is column first.
