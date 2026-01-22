import qrcode
import time
import os
while True:
    option = input('''
    1 - QR Code
    Q - Quit
    What would you like to do? :
    ''').upper()
    if option == "1":
        try :
            data = input("Please enter site link : ")
            name = input("Please enter file name : ")
            if data == ""  or name == "":
                print("It cannot be empty")
                continue
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=1,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image()
            full_name = f"{name}.png"
            img.save(full_name)
            print("File saved successfully")
            print("Opening...")
            time.sleep(1)
            os.startfile(full_name)
        except Exception as e:
            print(f" Error occurred: {e}")
            print("Please try again with a valid name.")
    elif option == "Q":
        print("Goodbye👋")
        break
    else:
        print("Please enter a valid option")

