# Restaurant Review Analyzer

This Python script calculates and sorts average review scores for restaurants from a JSON file.

## Features

- Reads restaurant review data from a JSON file (`recensioni.json`)
- Calculates average review scores for each restaurant
- Handles cases where restaurants have no reviews (defaults to 0.0)
- Sorts restaurants by their average score in descending order
- Saves the results to a new JSON file (`recensioni_medie.json`)

## Requirements

- Python 3.x
- No external dependencies required (uses built-in `json` module)

## Usage

1. Prepare your input file `recensioni.json` with the following format:
   ```json
   [
       {
           "nome": "Restaurant Name",
           "recensioni": [4, 5, 3, ...]
       },
       ...
   ]
   ```

2. Run the script:
   ```bash
   python restaurant_review_analyzer.py
   ```

3. The output will be saved to `recensioni_medie.json` with the following format:
   ```json
   [
       {
           "nome": "Top Rated Restaurant",
           "media": 4.8
       },
       ...
   ]
   ```

## Example

Input (`recensioni.json`):
```json
[
    {"nome": "Pizza Place", "recensioni": [4, 5, 3]},
    {"nome": "Burger Joint", "recensioni": [5, 5]},
    {"nome": "Empty Cafe", "recensioni": []}
]
```

Output (`recensioni_medie.json`):
```json
[
    {"nome": "Burger Joint", "media": 5.0},
    {"nome": "Pizza Place", "media": 4.0},
    {"nome": "Empty Cafe", "media": 0.0}
]
```

## Notes

- The script overwrites the output file if it already exists
- All reviews are treated equally (no weighting)
- The sorting is done using a simple bubble-sort like algorithm

## License

This project is open-source and available for use under the MIT License.
