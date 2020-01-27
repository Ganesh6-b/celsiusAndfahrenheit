conv = input("Enter Celsius to Fahrenheit(1) or Fahrenheit to Celsius(2):\nJust enter 1 or 2 :")

if conv == "1":
    val = int(input("Enter the Celsius :"))
    fah = (val * (9/5)) +32
    print("{} degree celsius is equal to {} degree fahrenheit".format(val,fah))
elif conv == "2":
    val = int(input("Enter the fahrenheit :"))
    cel = (val - 32) * (5/9)
    print("{} degree fahrenheit is equal to {} degree celsius".format(val,cel))
else:
    print("Enter the valid number:")
