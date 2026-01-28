from PIL import Image
import streamlit as st
from backend.backend import cesar_cipher, cesar_uncipher, vigenere_cipher, vigenere_uncipher
import random
from pathlib import Path

def change_pixel(location, img, color):
    # while ((img.format == 1 and (color != 1 and color != 0)) or \
    #     (img.format == "L" and not (type(color) == int and color >0 and color<255)) or \
    #         ((img.format == "RGB" or img.format == "RGBA" or img.format == "CMYK") and \
    #             not (type(color)[i] == int and color[i] >0 and color[i]<255) for i in range (0,len(color)-1)) or \
    #                 type(color)!= int):
    #     color=input("Give a right color format please : ")
    # while type(location) != tuple and len(location) != 2 and location[0]<=img.size and location[0]>=0 and location[1]<=img.size and location[1]>=0:
    #     location=input("Give a right location please : ")
    # while type(img)[:12] != "<class 'PIL.":
    #     img = Image.open(st.file_uploader("Chargez une image", type=["jpg", "jpeg", "png"]))
    img.putpixel(location, color)
def test():
    crypted = False
    assets_path = Path(__file__).resolve().parent / "assets" / "ravus.jpg"
    if assets_path.exists():
        img = Image.open(assets_path)
    else:
        # fallback to original relative path if the assets folder is located elsewhere
        img = Image.open("./Deuxième_année/Python/Cryptage/watermarking/assets/ravus.jpg")

    img = img.convert("L")

    txt = "Hello World!"
    cesar_key = int(1/random.random())
    txt = str(cesar_key) + cesar_cipher(txt,cesar_key)
    password = "Password"
    if password != "" and txt != "":
        txt = vigenere_cipher(txt, password)
        print(txt)
        encode_image(img,txt)
        crypted = True
    if crypted != False:
        decrypted_message = even_and_read_image(img)
        # decrypted_message = [decrypted_message[i:i+min(21,len(decrypted_message[i:]))] for i in range(0, len(decrypted_message), 21)]
        print(decrypted_message)
        decrypted_message = vigenere_uncipher(switch_str_bin(decrypted_message), password)
        print(decrypted_message)
        decrypted_message = cesar_uncipher(decrypted_message[2:],int(decrypted_message[:2]))
        print(decrypted_message)

def show():
    st.title("Stéganosnap")
    uploaded_file = False
    crypted = False
    if not uploaded_file:
        uploaded_file = st.file_uploader("Chargez une image", type=["jpg", "jpeg", "png"])
    if uploaded_file :
        st.subheader("Image originale")
        img = Image.open(uploaded_file)
        st.image(img, use_column_width=True)

        img = img.convert("L")
        st.image(img, use_column_width=True)

        txt = st.text_input("Entrez votre texte", placeholder="LOREM IPSUM", key="Clear message")
        cesar_key = int(1/random.random())
        txt = str(cesar_key) + cesar_cipher(txt,cesar_key)

        password = st.text_input("Entrez votre mot de passe", placeholder="Entrez votre mot de passe", key="password")

        if password != "" and txt != "":
            if st.button("Générer votre image cryptée", key="Run watermarking"):
                txt=vigenere_cipher(txt, password)
                print(txt)
                encode_image(img,txt)
                st.image(img, use_column_width=True)
                crypted = True
        elif st.button("Créer aléatoirement", key="random_password") and txt != "":
            password = randstr()
            txt=vigenere_cipher(txt, password)
            print(txt)
            encode_image(img,txt)
            st.image(img, use_column_width=True)
            crypted = True
        else:
            if txt == "":
                st.text("Veuillez entrer votre message")
            if password == "":
                st.text("Sans mot de passe, votre texte ne sera pas suffisement crypté")
            crypted = False
        if crypted != False:
            decrypted_message = even_and_read_image(img)
            # decrypted_message = [decrypted_message[i:i+min(21,len(decrypted_message[i:]))] for i in range(0, len(decrypted_message), 21)]
            # print(decrypted_message)
            decrypted_message = vigenere_uncipher(switch_str_bin(decrypted_message), password)
            print(decrypted_message)
            decrypted_message = cesar_uncipher(decrypted_message[2:],int(decrypted_message[:2]))
            print(decrypted_message)
            st.subheader(decrypted_message)

def randstr():
    return "".join([chr(int(nb/random.random())) for nb in range(random.randint(1,int(1/random.random())))])

def switch_str_bin(txt: str | int):
    """if string of char given, return binary value, else if binary int given, return string of char value"""
    output=""
    is_binary = all(elt in '01' for elt in txt)
    if not is_binary:
        for index in range(len(txt)):
            output += str(bin(ord(txt[index]))[2:]).zfill(21)
    else:
        for index in range(0,len(txt),21):
            temp = txt[index:index+21]
            print(temp)
            temp = int(temp,2)
            print(temp)
            output += chr(temp)
            print(output[-1], ":", temp)
    return output

def even_and_read_image(img, even: bool = False):
    """if no even, just read the image"""
    txt=""
    for i in range(img.size[0]):    
        for j in range(img.size[1]):
            txt+=str(img.getpixel((i,j)) %2)
            if even:
                img.putpixel((i,j), img.getpixel((i,j))-int(txt[-1]))
    return(txt)

def encode_image(img, txt):
    txt=switch_str_bin(txt)
    even_and_read_image(img)
    index=0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            index+=1
            if index < len(txt):
                img.putpixel((i,j), img.getpixel((i,j)) + int(txt[index]))
            else:
                return None

if __name__ == "__main__":
    # show()
    # print(switch_str_bin(switch_str_bin("Hello World!")))
    test()



