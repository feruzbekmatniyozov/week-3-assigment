general = 9
special = 14
vip = 20
counter = 0
subtotal = 0
discount_amount = 8
print("=== Museum Admission Calculator ===")
print("Enter exhibit type: general, special, or vip")
print("Type 'done' when finished selecting exhibits\n")



while True:
    exhibit = input("Enter exhibit type: ")
    if exhibit == "done":
        print()
        print("=== Admission Summary ===")
        print(f"Subtotal: ${subtotal:.2f}")
        if subtotal >= 55:
            discounted_total = subtotal-discount_amount
            print(f"Group visit discount: -${discount_amount:.2f}")
            print(f"Final total: ${discounted_total:.2f}")
        else:
            print("Group visit discount: N/A")
            print(f"Final total: ${subtotal:.2f}")            
        break
    elif exhibit == 'general':
        subtotal = subtotal + general
        print(f"Current total: ${subtotal:.2f}")
    elif exhibit == 'special':
        subtotal = subtotal + special
        print(f"Current total: ${subtotal:.2f}")
    elif exhibit == 'vip':
        subtotal = subtotal + vip
        print(f"Current total: ${subtotal:.2f}")