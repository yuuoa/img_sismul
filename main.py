from PIL import Image
import base64
import hashlib
import os

def encrypt(image, key):
    myimg = image

    for x in range(myimg.width):
        for y in range(myimg.height):
            coord = (x, y)
            pixel = myimg.getpixel(coord) #menghasilkan tuple berisi (r,g,b,a)

            # Melakukan Prime Component Alteration Technique.
            # Melakukan looping terhadap isi tuple.
            # Jika c genap maka c+1, jika ganjil tidak dilakukan operasi apapun.
            #coprime_pixel = ((c+1 if c % 2 == 0 else c) for c in pixel)

            #myimg.putpixel(coord, tuple(int(c**43 % 256)for c in coprime_pixel))

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
    print("Pengamanan PNG versi 1.6")

    os.rename(r'sf',r'sf.png')
    im = Image.open("sf.png")

    # password = sistemmultimedia
    passkey = "c39d849dabfe3301af378c4dcf3486ce"
    xorkey  = 150

    password = input("Enter first key (to open data): ")

    if hashlib.md5(password.encode()).hexdigest() == passkey:
        print("Password correct! image decrypted")

        mkey = int(input("Enter second key (to descramble color): "))

        lim = decrypt(im, mkey)
        lim.save("decrypted.png")
    else:
        print("Password incorrect! image encrypted")
        lim = encrypt(im, xorkey)
        lim.save("encrypted.png")
    
    os.rename(r'sf.png',r'sf')


if __name__ == "__main__":
    main()
