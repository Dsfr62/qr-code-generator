import qrcode
from time import sleep

data = input("\ninsert the data....: ")

print("------- loading -------")

try:
    print("\ncreating qr code...")
    result = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    result.add_data(data=data)
    result.make(fit=True)
    sleep(4)
    print("\nsaving img")
    sleep(3)
    img = result.make_image(fill_color="black", back_color="white")
    img.save(stream=f"output/qr_code.png")
    print(f"\nimage created at /output/qr_code.png\n")
    sleep(2)
except:
    raise Exception("\nscript failed when creating qrcode\n")
finally:
    print("\n------- finished -------\n")