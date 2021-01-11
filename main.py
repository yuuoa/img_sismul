from PIL import Image
import base64
import hashlib
import os
import PySimpleGUI as sg
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# pip install pillow
# pycryptodome required to use AES.


def encrypt(image, key):
    myimg = image

    for x in range(myimg.width):
        for y in range(myimg.height):
            coord = (x, y)
            pixel = myimg.getpixel(coord) #menghasilkan tuple berisi (r,g,b,a)

            # Melakukan Prime Component Alteration Technique.
            # Melakukan looping terhadap isi tuple.
            # Jika c genap maka c+1, jika ganjil tidak dilakukan operasi apapun.
            
            da = tuple((p ^ key) for p in pixel)
            myimg.putpixel(coord, da)

    return myimg


def decrypt(image, key):
    myimg = image

    for x in range(myimg.width):
        for y in range(myimg.height):
            coord = (x, y)
            pixel = myimg.getpixel(coord) #menghasilkan tuple berisi (r,g,b,a)

            da = tuple((p ^ key) for p in pixel)
            myimg.putpixel(coord, da)

            #myimg.putpixel(coord, tuple(int(c**3 % 256) for c in pixel))

    return myimg

def main():

    os.rename(r'sf',r'sample.png')
    im = Image.open("sample.png")
    
    passkey = "098f6bcd4621d373cade4e832627b4f6" #password = test
    xorkey = 150
        
    lim = encrypt(im, xorkey)
    lim = encrypt(im, xorkey)
    lim.save("dice.png")

    text = str(sg.popup_get_text('Enter first key (to open data): ', 'Pengamanan PNG cersi 1.6'))

    password = hashlib.md5(text.encode())

    if password.hexdigest() == passkey:
        sg.popup('Password correct! Image decrypted')
        mkey = int(sg.popup_get_text("Enter second key (to descramble color): "))

        if mkey == xorkey:
            lim = decrypt(im, mkey)
            os.remove("dice.png")
            lim.save("dice.png")
            sg.popup('Second key correct! Image descrambled')
        
        else:
            sg.popup('Second key incorrect! Image still encrypted')

    else:
        sg.popup("Password incorrect! image encrypted")

    os.rename(r'sample.png',r'sf')

if __name__ == "__main__":
    main()
