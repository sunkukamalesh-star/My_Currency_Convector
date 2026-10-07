import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Kamalesh Currency Converter",
    page_icon="💱",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .converter-box {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #dddddd;
        margin-bottom: 20px;
    }

    .result-box {
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #4CAF50;
        text-align: center;
        margin-top: 20px;
    }

    .result-label {
        font-size: 18px;
        font-weight: bold;
    }

    .result-value {
        font-size: 32px;
        font-weight: bold;
        margin-top: 10px;
    }

    .rate-text {
        text-align: center;
        font-size: 16px;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="title">💱 Kamalesh Currency Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Convert your money between different currencies easily</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Currency Exchange Rates
# Rates are based on USD
# -----------------------------
rates = {
    "USD": 1.00,
    "EUR": 0.86,
    "INR": 92.00,
    "GBP": 0.75,
    "JPY": 149.00,
    "AUD": 1.52,
    "CAD": 1.38,
    "AED": 3.67,
    "SGD": 1.28,
    "CHF": 0.80
}

# -----------------------------
# Currency Names
# -----------------------------
currency_names = {
    "USD": "🇺🇸 US Dollar",
    "EUR": "🇪🇺 Euro",
    "INR": "🇮🇳 Indian Rupee",
    "GBP": "🇬🇧 British Pound",
    "JPY": "🇯🇵 Japanese Yen",
    "AUD": "🇦🇺 Australian Dollar",
    "CAD": "🇨🇦 Canadian Dollar",
    "AED": "🇦🇪 UAE Dirham",
    "SGD": "🇸🇬 Singapore Dollar",
    "CHF": "🇨🇭 Swiss Franc"
}

# -----------------------------
# Converter Box
# -----------------------------
st.markdown('<div class="converter-box">', unsafe_allow_html=True)

# Amount
amount = st.number_input(
    "💰 Enter Amount",
    min_value=0.0,
    value=100.0,
    step=1.0
)

# Currency selection
col1, col2 = st.columns(2)

with col1:
    from_currency = st.selectbox(
        "From Currency",
        list(rates.keys()),
        format_func=lambda x: currency_names[x]
    )

with col2:
    to_currency = st.selectbox(
        "To Currency",
        list(rates.keys()),
        index=2,
        format_func=lambda x: currency_names[x]
    )

# Convert button
convert_button = st.button(
    "🔄 Convert Currency",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Conversion Logic
# -----------------------------
if convert_button:

    if amount <= 0:
        st.error("Please enter an amount greater than 0.")

    else:
        # Convert source currency to USD
        usd_amount = amount / rates[from_currency]

        # Convert USD to target currency
        converted_amount = usd_amount * rates[to_currency]

        # Calculate exchange rate
        exchange_rate = (
            rates[to_currency] / rates[from_currency]
        )

        # Display result
        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-label">Converted Amount</div>
                <div class="result-value">
                    {converted_amount:,.2f} {to_currency}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="rate-text">
                💱 1 {from_currency} = {exchange_rate:.4f} {to_currency}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success(
            f"{amount:,.2f} {from_currency} = "
            f"{converted_amount:,.2f} {to_currency}"
        )

# -----------------------------
# Supported Currencies
# -----------------------------
st.subheader("🌍 Supported Currencies")

currency_columns = st.columns(5)

for index, currency in enumerate(rates.keys()):
    with currency_columns[index % 5]:
        st.metric(
            currency,
            currency_names[currency].split(" ", 1)[1]
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer">
        💱 Kamalesh Currency Converter<br>
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)