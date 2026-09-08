# PY Barcode Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![CI](https://github.com/webkolog/py-barcode-generator/actions/workflows/python-tests.yml/badge.svg)](https://github.com/webkolog/py-barcode-generator/actions)

**Version:** 1.0

**Created Date:** 2026-09-08

**Last Updated:** 2026-09-05

**Compatibility:** Python 3.x

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

**PY Barcode Generator** is a lightweight Python script that allows you to easily encode user input into Code128 barcodes and export them as high-resolution images. It supports visual rendering via Pillow and inline display for IPython/Jupyter environments.

## Installation

Install the required Python packages using `pip`:

```bash
pip install python-barcode pillow ipython

```

## Usage

### Running the Script

Execute the main script file to start the generator:

```bash
python py-barcode-generator.py

```

When prompted, enter the string or data you wish to encode. The script generates a Code128 barcode image, saves it locally as `clcoding_barcode.png`, and displays the image output.

### Code Overview

```python
import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

user_data = input("Enter the data to encode in the barcode: ")
code = barcode.get('code128', user_data, writer=ImageWriter())
filename = code.save("clcoding_barcode")
display(Image(filename=filename))

```

## Dependencies

* **python-barcode:** Library for generating standard barcode formats.
* **Pillow (PIL):** Required by `ImageWriter` to render barcodes into image formats (PNG, JPEG).
* **IPython:** Required for displaying the generated barcode image directly in Jupyter or IPython environments.

## License

This PY Barcode Generator script is open-source software licensed under the [MIT license](https://mit-license.org/).

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For questions or support regarding PY Barcode Generator, please refer to the project's GitHub repository or contact the author.

```
