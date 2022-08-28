[![ci](https://github.com/sumbono/json_parser/actions/workflows/ci.yml/badge.svg)](https://github.com/sumbono/json_parser/actions/workflows/ci.yml)

# json_parser

A json file parser package to demonstrate python cli module and tool packaging.

## Testing (using poetry command)

```bash
$ git clone https://github.com/sumbono/json_parser.git
$ cd json_parser
$ poetry run pytest --cov=json_parser
```

## Installation

```bash
$ git clone https://github.com/sumbono/json_parser.git
$ cd json_parser
$ pip install .
```

## Usage Python Module

```python
from json_parser import json_parser

file_path = "data/test.json" #a path to your text file
result = json_parser(file_path)
```

## Usage CLI
- The result will be printed on terminal and stored in the dest_path file.
```bash
$ json_parser <filepath> -o <dest_path>
```

## Assumption
- The value of each commodity in source file is a daily based and from one store/place.
- All value converted to integer. 
- For not integer value (a.k.a float), do roundup.


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`json_parser` was created by Sumbono. It is licensed under the terms of the MIT license.
