# Credit Card Generator

This project is a credit/debit card number generator based on a given BIN (Bank Identification Number). It generates valid card numbers using the Luhn algorithm, along with optional expiry dates and CVV numbers.

## Usage

To run the script, use the following command:

```sh
python ccgen.py --Bin BIN [--Exp EXP] [--CVV CVV] [--Random] [--Total TOTAL]
```

### Arguments

- `--Bin`: **(Required)** 6-digit BIN code for the card.
- `--Exp`: **(Optional)** Expiry date in MM/YY format.
- `--CVV`: **(Optional)** 3-digit CVV number.
- `--Random`: **(Optional)** Generate random expiry date and CVV.
- `--Total`: **(Optional)** Total number of cards to generate (default is 1).

### Example

Generate 10 random cards with a specific BIN and CVV:

```sh
python ccgen.py --Bin 123456 --CVV 123 --Random --Total 10
```

## Functions

### `luhn_check(card_number)`

Validates a card number using the Luhn algorithm.

### `generate_expiry()`

Generates a random expiry date in MM/YY format.

### `generate_cvv()`

Generates a random 3-digit CVV number.

### `generate_card_number(bin_code)`

Generates a valid card number based on the provided BIN code.

### `generate_cards(bin_code, total, expiry=None, cvv=None, random_mode=False)`

Generates a list of card details including card number, expiry date, and CVV.

## Author

Written by Jeff Steveanus

## Date

2024-10-20
