def calculate_total(price, quantity):
  if price < 0 or quantity < 0:
    raise ValueError("Price and quantity cannot be negative")
  return price * quantity


def main():
  print("=== Shopping Bill Calculator ===")
  try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    total = calculate_total(price, quantity)
    print(f"Total Bill: ${total:.2f}")
  except ValueError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  main()
