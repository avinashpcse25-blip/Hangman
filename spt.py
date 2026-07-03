from datetime import datetime


class StockPortfolioTracker:
    """Encapsulates all portfolio operations: add, update, remove,
    search, analyze, and report stock holdings."""

    # Hardcoded market prices (acts as a simulated live feed)
    STOCK_PRICES = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "MSFT": 320,
        "AMZN": 145,
        "NFLX": 610,
        "META": 480,
        "NVDA": 1050,
    }

    def __init__(self):
        # portfolio holds {symbol: quantity}
        self.portfolio = {}

    # ---------- Display available stocks ----------
    def show_available_stocks(self):
        print("\nAvailable Stocks:")
        print(f"{'Symbol':<10}{'Price ($)':<10}")
        for symbol, price in self.STOCK_PRICES.items():
            print(f"{symbol:<10}{price:<10}")

    def add_stock(self):
        symbol = input("\nEnter stock symbol to add: ").upper().strip()

        if symbol not in self.STOCK_PRICES:
            print(f"'{symbol}' is not a recognized stock symbol.")
            return

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return
        except ValueError:
            print("Invalid input. Quantity must be a whole number.")
            return

        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
        print(f"{quantity} share(s) of {symbol} added successfully.")

    def view_portfolio_summary(self):
        if not self.portfolio:
            print("\nYour portfolio is currently empty.")
            return

        print("\nPORTFOLIO SUMMARY")
        print(f"{'Symbol':<10}{'Qty':<6}{'Price($)':<10}{'Value($)':<10}")

        total = 0
        for symbol, qty in self.portfolio.items():
            price = self.STOCK_PRICES[symbol]
            value = price * qty
            total += value
            print(f"{symbol:<10}{qty:<6}{price:<10}{value:<10}")

        print(f"\nTotal Portfolio Value: ${total}")

    def search_stock(self):
        symbol = input("\nEnter stock symbol to search: ").upper().strip()

        if symbol in self.portfolio:
            qty = self.portfolio[symbol]
            value = qty * self.STOCK_PRICES[symbol]
            print(f"\n{symbol} found: {qty} share(s), Value: ${value}")
        else:
            print(f"\n{symbol} is not present in your portfolio.")

    def update_quantity(self):
        symbol = input("\nEnter stock symbol to update: ").upper().strip()

        if symbol not in self.portfolio:
            print(f"{symbol} not found in your portfolio.")
            return

        try:
            new_qty = int(input(f"Enter new quantity for {symbol}: "))
            if new_qty <= 0:
                print(
                    "Quantity must be greater than zero. "
                    "Use 'Remove Stock' to delete a holding."
                )
                return
        except ValueError:
            print("Invalid input. Quantity must be a whole number.")
            return

        self.portfolio[symbol] = new_qty
        print(f"{symbol} quantity updated to {new_qty}.")

    def remove_stock(self):
        symbol = input("\nEnter stock symbol to remove: ").upper().strip()

        if symbol in self.portfolio:
            del self.portfolio[symbol]
            print(f"{symbol} removed from your portfolio.")
        else:
            print(f"{symbol} not found in your portfolio.")

    def calculate_total_investment(self):
        total = sum(
            qty * self.STOCK_PRICES[symbol]
            for symbol, qty in self.portfolio.items()
        )
        return total

    def show_statistics(self):
        if not self.portfolio:
            print("\nNo statistics available. Portfolio is empty.")
            return

        total_shares = sum(self.portfolio.values())
        total_value = self.calculate_total_investment()

        highest_stock = max(
            self.portfolio,
            key=lambda s: self.portfolio[s] * self.STOCK_PRICES[s]
        )
        highest_value = (
            self.portfolio[highest_stock] * self.STOCK_PRICES[highest_stock]
        )

        print("\nPORTFOLIO STATISTICS")
        print(f"Total Distinct Stocks   : {len(self.portfolio)}")
        print(f"Total Shares Owned      : {total_shares}")
        print(f"Total Investment Value  : ${total_value}")
        print(f"Highest Investment Stock: {highest_stock} (${highest_value})")

    def save_report(self):
        if not self.portfolio:
            print("\nCannot save report. Portfolio is empty.")
            return

        try:
            with open("portfolio_report.txt", "w") as file:
                file.write("STOCK PORTFOLIO REPORT\n")
                file.write(
                    "Generated on: "
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                )
                file.write(
                    f"{'Symbol':<10}{'Qty':<6}{'Price($)':<10}"
                    f"{'Value($)':<10}\n"
                )

                total = 0
                for symbol, qty in self.portfolio.items():
                    price = self.STOCK_PRICES[symbol]
                    value = price * qty
                    total += value
                    file.write(
                        f"{symbol:<10}{qty:<6}{price:<10}{value:<10}\n"
                    )

                file.write(f"\nTotal Portfolio Value: ${total}\n")

            print("\nReport saved successfully as 'portfolio_report.txt'.")
        except IOError:
            print("Error: Unable to write the report file.")

    # ---------- Menu Display ----------
    def display_menu(self):
        print("\n" + "STOCK PORTFOLIO TRACKER".center(40))
        print("1. Add Stock")
        print("2. View Portfolio Summary")
        print("3. Search Stock")
        print("4. Update Stock Quantity")
        print("5. Remove Stock")
        print("6. Calculate Total Investment")
        print("7. Save Report to File")
        print("8. Show Portfolio Statistics")
        print("9. Exit")
        
    def run(self):
        self.show_available_stocks()

        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-9): ").strip()

            if choice == "1":
                self.add_stock()
            elif choice == "2":
                self.view_portfolio_summary()
            elif choice == "3":
                self.search_stock()
            elif choice == "4":
                self.update_quantity()
            elif choice == "5":
                self.remove_stock()
            elif choice == "6":
                total = self.calculate_total_investment()
                print(f"\nTotal Investment Value: ${total}")
            elif choice == "7":
                self.save_report()
            elif choice == "8":
                self.show_statistics()
            elif choice == "9":
                print("\nThank you for using Stock Portfolio Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1-9.")


def main():
    """Entry point of the program."""
    tracker = StockPortfolioTracker()
    tracker.run()


if __name__ == "__main__":
    main()