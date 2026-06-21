def main():
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "NVDA": 450.0,
        "MSFT": 380.0
    }

    print("--- Available Stocks and prices ---")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")
    print("-" * 35)

    stock_name = input("\nEnter the stock ticker symbol (e.g., AAPL): ").strip().upper()

    if stock_name not in stock_prices:
        print(f"Error: stock '{stock_name}' is not in the system database.")
        return

    try:
        quantity = int(input(f"Enter the number of shares of {stock_name} you own: "))
        if quantity < 0:
            print("Error: quantity cannot be negative.")
            return
    except ValueError:
        print("Error: Please enter a valid whole number for the quantity.")
        return

    price_per_share = stock_prices[stock_name]
    total_value = quantity * price_per_share

    summary_text = (
        f"\n--- Portfolio Summary ---\n"
        f"Stock: {stock_name}\n"
        f"Quantity: {quantity}\n"
        f"Price per share: ${price_per_share:.2f}\n"
    )

    print(summary_text)

    save_choice = input("Would you like to save this summary to a .txt file? (yes/no): ").strip().lower()
    if save_choice in ['yes', 'y']:
        filename = "portfolio_summary.txt"
        try:
            with open(filename, "w") as file:
                file.write(summary_text)
            print(f"Successfully saved portfolio data to '{filename}'!")
        except IOError:
            print("Error: Could not write data to file.")

if __name__ == "__main__":
    main()
    