# Task 3 : Creating payment receipt


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from datetime import datetime, date

# Get customer details
Customer_name = input("Enter customer name: ")

# Define the list of items and their prices
Items_list = {"Juice": 50, "Cold Drinks": 40, "Chips": 20, "Biscuit":15, "Cake":30, "Chocolate":10}

# Display the available items and their prices
print("Items Available to buy :")
for item, price in Items_list.items():
    print(f"{item}: ₹{price} ")    
print("-"*60)


# Initialize a dictionary to store bought items and their quantities
Bought_Items = {}

# Allow the user to input quantities for each item
while True:
    Choice = input("Enter the item name to buy  else press 'No' to complete order: ")
    if Choice.lower() == "no":
        break

    if Choice in Items_list:
        quantity = int(input(f"Enter quantity for {Choice}: "))
        Bought_Items[Choice] = {"Qty": quantity, "Price": Items_list[Choice], "Amount": quantity * Items_list[Choice]}
    else:
        print("This Item is not available")


# creating the pdf 
file = "store_payment_receipt.pdf"
now = datetime.now()
date_today = date.today()
time = now.strftime("%H:%M:%S")

r = canvas.Canvas(file, pagesize=letter)


# r.drawstring(x,y,text) here x and y are coordinate in the pdf list
# PDF Header Information

r.drawString(250, 750, "XYZ  STORE")
r.drawString(250, 730, "Invoice Generated ")
r.drawString(250, 710, f"Date: {date_today}")
r.drawString(250, 690, f"Time: {time}")
r.drawString(250, 670, f"Customer Name : {Customer_name}")

# Draw a line to separate header and items
r.drawString(50, 650, "*" * 100)

# Draw the table header
r.drawString( 50, 610, "Item")
r.drawString(150, 610, "Qty")
r.drawString(250, 610, "Price")
r.drawString(350, 610, "Amount")

# Display items, quantities, and amounts in the PDF table
y = 590
for item, details in Bought_Items.items():
    r.drawString(50, y, item)
    r.drawString(150, y, str(details['Qty']))
    r.drawString(250, y, f"Rs. {details['Price']}")
    r.drawString(350, y, f"Rs. {details['Amount']}")
    y -= 20

# Draw a line to separate items and total amount
r.drawString(50, y - 20, "*" * 100)

# Calculate and display the total amount
Total = sum(details['Amount'] for details in Bought_Items.values())
r.drawString(50, y - 50, f"Total Amount to be Paid: Rs. {Total}")


# Creating the  QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Infomation to be loaded when scanning the QR
qr.add_data(f"Payment Receipt for {Customer_name}\n Total Amount {Total}")
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img_path = "qr_code.png"
qr_img.save(qr_img_path)
r.drawImage(qr_img_path, 250, 300, width=100, height=100)


# Saving the PDF file and informing the user that receipt is ready
r.save()
print(f"PDF of Payment Receipt is: {file}")

