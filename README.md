# Py CTakes Parser
Python utilities to parse the output of cTAKES 4.0.

# Installation
## From PyPi

```python
pip install ctakes_parser
```

# Examples

## Parse Single File

```python
import ctakes_parser as parser

df = parser.parse_file(file_path='notes_in/1152.xml')
```

## Parse Entire Directory

```python
import ctakes_parser as parser

parser.parse_dir(in_directory_path='notes_in/',
                 out_directory_path='notes_out/')
```
