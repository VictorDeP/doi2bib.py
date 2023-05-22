# doi2bib.py
Python script to generate BibTeX from DOI.

# Example
Input in command line
```
./doi2bib.py 10.1137/s0036144504446096
```
Output
```
@article{gill2005,
  doi = {10.1137/s0036144504446096},
  year = {2005},
  month = {jan},
  publisher = {Society for Industrial {\&} Applied Mathematics ({SIAM})},
  volume = {47},
  number = {1},
  pages = {99--131},
  author = {Philip E. Gill and Walter Murray and Michael A. Saunders},
  title = {{SNOPT}: An {SQP} Algorithm for Large-Scale Constrained Optimization},
  journal = {{SIAM} Review}
}
```
Or change doi = '*DOI*' in **use_doi2bib.py** file and run it.

## Changes from original jwangac/doi2bib
- Tag id does not contain first word of title
- Possibility to exempt tags (month, url, ...) using remove = [*tags as strings*] in convert function: convert(doi, remove = ['month', 'url'])


# Requirement
Python 3

# Usage
```
doi2bib.py [-h] [-i] [-x PROXY] ...

Generate BibTeX from DOI.

positional arguments:
  DOI

optional arguments:
  -h, --help            show this help message and exit
  -i                    run interactively
  -x PROXY, --proxy PROXY
                        set HTTP proxy
```

# License
This project is licensed under the terms of the MIT license.
