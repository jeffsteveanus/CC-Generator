# Written by Jeff Steveanus
# Date: 2024-10-20
#
# Usage:
# python ccgen.py [-h] --Bin BIN [--Exp EXP] [--CVV CVV] [--Random] [--Total TOTAL]
# Example: python ccggen.py --Bin BIN 123456 --CVV 123 --Random --Total 10

import random
import argparse

def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    
    return checksum % 10 == 0

def generate_expiry():
    month = random.randint(1, 12)
    year = random.randint(24, 29)
    return f"{month:02d}/{year:02d}"

def generate_cvv():
    return f"{random.randint(100, 999):03d}"

def generate_card_number(bin_code):
    card_number = [int(digit) for digit in bin_code]
    while len(card_number) < 15:
        card_number.append(random.randint(0, 9))

    checksum_digit = 0
    for i in range(10):
        if luhn_check(int(''.join(map(str, card_number + [i])))):
            checksum_digit = i
            break
    
    card_number.append(checksum_digit)
    return ''.join(map(str, card_number))

def generate_cards(bin_code, total, expiry=None, cvv=None, random_mode=False):
    cards = []
    for _ in range(total):
        card_number = generate_card_number(bin_code)
        
        if random_mode:
            expiry = generate_expiry()
            cvv = generate_cvv()
        
        card = {
            "Card Number": card_number,
            "Expiry Date": expiry if expiry else generate_expiry(),
            "CVV": cvv if cvv else generate_cvv()
        }
        
        if luhn_check(card_number):
            cards.append(card)
        else:
            print(f"Invalid card generated: {card_number}")

    return cards

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate credit/debit card numbers based on BIN")
    parser.add_argument("--Bin", type=str, required=True, help="6-digit BIN code for the card")
    parser.add_argument("--Exp", type=str, help="Expiry date in MM/YY format (optional)")
    parser.add_argument("--CVV", type=str, help="3-digit CVV number (optional)")
    parser.add_argument("--Random", action="store_true", help="Generate random expiry date and CVV")
    parser.add_argument("--Total", type=int, default=1, help="Total number of cards to generate (default 1)")

    args = parser.parse_args()

    cards = generate_cards(args.Bin, args.Total, expiry=args.Exp, cvv=args.CVV, random_mode=args.Random)

    for card in cards:
        print(f"{card['Card Number']}|{card['Expiry Date']}|{card['CVV']}")
