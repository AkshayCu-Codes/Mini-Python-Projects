import re

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    print(f"Checksum Total: {total}")
    return total % 10 == 0

def main():
    print("🔐 Credit Card Verifier using Luhn Algorithm\n")
    print("💡 Enter a 16-digit card number in any of these formats:")
    print("   - Digits only:           4111111145551141")
    print("   - With spaces:           4111 1111 4555 1141")
    print("   - With hyphens:          4111-1111-4555-1141\n")

    card_number = input("Enter card number: ").strip()

    # Validate input format: only digits, spaces, or hyphens allowed
    if not re.fullmatch(r'[\d\s-]+', card_number):
        print("❌ Invalid format! Use only digits, spaces, or hyphens.")
        return

    # Remove spaces and hyphens
    translated_card_number = card_number.translate(str.maketrans({'-': '', ' ': ''}))

    # Check if the cleaned number is 16 digits
    if len(translated_card_number) != 16 or not translated_card_number.isdigit():
        print("❌ Card number must contain exactly 16 digits.")
        return

    if verify_card_number(translated_card_number):
        print("✅ VALID card number!")
    else:
        print("❌ INVALID card number.")

if __name__ == "__main__":
    main()
