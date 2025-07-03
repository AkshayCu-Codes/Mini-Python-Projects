import streamlit as st
import re

# --- Card Logos ---
CARD_LOGOS = {
    "Visa": "https://logo.clearbit.com/visa.com",
    "MasterCard": "https://logo.clearbit.com/mastercard.com",
    "American Express": "https://logo.clearbit.com/americanexpress.com",
    "Discover": "https://cdn-icons-png.flaticon.com/512/196/196561.png",
    "Unknown": "https://cdn-icons-png.flaticon.com/512/633/633611.png"
}

# --- Luhn Check ---
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
    return total % 10 == 0, total

# --- Card Type Detector ---
def detect_card_type(card):
    if card.startswith('4'):
        return 'Visa'
    elif card.startswith(('51', '52', '53', '54', '55')):
        return 'MasterCard'
    elif card.startswith(('34', '37')):
        return 'American Express'
    elif card.startswith('6'):
        return 'Discover'
    else:
        return 'Unknown'

# --- Mask all but last 4 digits ---
def mask_card(card):
    return '*' * 12 + card[-4:]

# --- Clear card from session ---
def reset():
    st.session_state.card_number = ""
    st.session_state.translated_card = ""

# --- Main App ---
def main():
    st.set_page_config(page_title="Card Validator", page_icon="💳")
    st.title("🔐 Card Validator")

    # --- Setup session ---
    if "card_number" not in st.session_state:
        st.session_state.card_number = ""
    if "translated_card" not in st.session_state:
        st.session_state.translated_card = ""

    # --- If card number already entered, show results ---
    if st.session_state.translated_card:
        translated_card = st.session_state.translated_card

        # Masked display
        st.markdown(f"🔒 Card Entered: `{mask_card(translated_card)}`")

        # Detect card type & logo
        card_type = detect_card_type(translated_card)
        logo_url = CARD_LOGOS.get(card_type, CARD_LOGOS["Unknown"])

        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(logo_url, width=60)
        with col2:
            st.info(f"💳 Detected Card Type: **{card_type}**")

        # Toggle checksum
        show_checksum = st.checkbox("🔍 Show Checksum Value", value=False)
        is_valid, checksum = verify_card_number(translated_card)

        if show_checksum:
            st.code(f"Checksum Total: {checksum}")

        if is_valid:
            st.success("✅ VALID card number!")
        else:
            st.error("❌ INVALID card number.")

        # Option to clear and enter again
        st.button("🔁 Check Another Card", on_click=reset)

        # Luhn explanation
        with st.expander("ℹ️ What is Luhn Check?"):
            st.markdown("""
            The **Luhn algorithm**, also known as the **Mod 10** algorithm, is a simple checksum formula used to validate a variety of identification numbers, most commonly credit card numbers.

            **How it works:**
            1. Starting from the right, double every second digit.
            2. If doubling results in a number ≥ 10, add the digits of the result (e.g. `14 → 1 + 4 = 5`).
            3. Add all digits (doubled and untouched).
            4. If the total modulo 10 is 0, the card number is **valid**.

            **Why it's important:**
            - Helps **detect errors** such as a mistyped digit.
            - Prevents **obvious invalid inputs** from being processed.
            - Used by **all major card issuers** worldwide as a first-level validation.

            This app uses Luhn’s algorithm to check whether your card number structure is mathematically valid before any further processing.
            """)

    else:
        # Input field with tooltip
        col1, col2 = st.columns([4, 1])
        with col1:
            card_number = st.text_input(
                "💳 Enter your card number",
                placeholder="4111 1111 1111 1111",
            )
        with col2:
            st.markdown(
                "<span title='16 digits, spaces or hyphens allowed&#10;Examples:&#10;• 4111 1111 1111 1111&#10;• 4111111111111111&#10;• 4111-1111-1111-1111'>ℹ️</span>",
                unsafe_allow_html=True
            )

        if card_number:
            translated_card = card_number.translate(str.maketrans({'-': '', ' ': ''}))

            if not re.fullmatch(r'\d{16}', translated_card):
                st.warning("⚠️ Please enter exactly 16 digits (spaces/hyphens allowed).")
            else:
                # Save to session and rerun to show results
                st.session_state.card_number = card_number
                st.session_state.translated_card = translated_card
                st.rerun()

if __name__ == "__main__":
    main()
