class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percent):
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount
        print(f"Applied {discount_percent}% discount. New price: ${self.price:.2f}")

if __name__ == "__main__":
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    price = float(input("Enter the book price: "))
    book = Book(title, author, price)

    print("\nBook Details:")
    book.display_details()
    discount = float(input("\nEnter discount percentage to apply: "))
    book.apply_discount(discount)
