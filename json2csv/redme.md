# JSON to CSV Converter

This Python script converts JSON files into CSV files. It is capable of handling complex, nested JSON structures thanks to the `flatten_json` package. The script is interactive and prompts users to enter the paths of their input JSON file and the output CSV file. If multiple lists of dictionaries are found in the JSON file, the script will create multiple CSV files accordingly.

## Installation

1. Make sure you have Python 3 installed. If not, download it [here](https://www.python.org/downloads/).

2. Clone this repository or download the Python script.

3. Install the `flatten_json` package with pip:
    ```
    pip install flatten_json
    ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where the Python script is located.

3. Run the script by entering `python json2csv.py`.

4. When prompted, enter the full path to the JSON file you want to convert, then press enter.

5. Enter the full path template where you want to save the resulting CSV files. Use `{i}` in the template where you want the index of the list of dictionaries to be inserted.

## Notes

* The script is designed to work with JSON files that have lists of dictionaries. These can be at the top level or nested within the JSON file.

* The script returns all the lists of dictionaries it encounters. If your JSON file contains multiple lists of dictionaries at different levels or under different keys, the script will process all of them, each into its own CSV file.

## License

This project is licensed under the MIT License.

