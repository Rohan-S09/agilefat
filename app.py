def calculate_total(price, quantity, discount_percent=0):
  if price < 0 or quantity < 0 or not (0 <= discount_percent <= 100):
    raise ValueError("Invalid input values")
  subtotal = price * quantity
  discount_amount = subtotal * (discount_percent / 100.0)
  return subtotal - discount_amount


def main():
  print("=== Shopping Bill Calculator (with Discount) ===")
  try:
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    discount = float(input("Enter discount % (0 if none): "))
    total = calculate_total(price, quantity, discount)
    print(f"Discounted Total Bill: ${total:.2f}")
  except ValueError as e:
    print(f"Error: {e}")


if __name__ == "__main__":
  main()
