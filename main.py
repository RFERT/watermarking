from PIL import Image
import streamlit as st
import cryptography as crypto
import random


def change_pixel(location, img, color):
    # while ((img.format == 1 and (color != 1 and color != 0)) or \
    #     (img.format == "L" and not (type(color) == int and color >0 and color<255)) or \
    #         ((img.format == "RGB" or img.format == "RGBA" or img.format == "CMYK") and \
    #         not (type(color)[i] == int and color[i] >0 and color[i]<255) for i in range (0,len(color)-1)) or \
    #             type(color)!= int):
    #     color=input("Give a right color format please : ")
    # while type(location) != tuple and len(location) != 2 and location[0]<=img.size and location[0]>=0 and location[1]<=img.size and location[1]>=0:
    #     location=input("Give a right location please : ")
    # while type(img)[:12] != "<class 'PIL.":
    #     img = Image.open(st.file_uploader("Chargez une image", type=["jpg", "jpeg", "png"]))
    img.putpixel(location, color)

def test(uploaded_file):
    st.markdown("""<script>
        console.log("Image chargée avec succès !");
        console.log("Taille de l'image : %s");
        </script>""" % str(img.size), unsafe_allow_html=True)

    if isinstance(img, Image.Image):
        st.subheader("Image originale")
        st.image(img, caption="Image originale", use_column_width=True)
    else:
        st.error("L'objet chargé n'est pas une image valide.")
    
    try:
        rotated_img = img.rotate(90, expand=True)
        st.subheader("Image tournée à 90°")
        st.image(rotated_img, caption="Image tournée", use_column_width=True)
    except Exception as e:
        st.error(f"Erreur lors de la rotation de l'image : {e}")

    st.markdown("""
        <script>
        console.log("Il ne manque plus que le pixel");
        </script>""")
    change_pixel((10, 10), img, (255, 0, 0))
    st.markdown("""
        <script>
        console.log("le pixel est placé");
        </script>""")
    st.subheader("pixel placé en (10,10)")
    st.image(img, caption="Image modifiée", use_column_width=True)
    st.markdown("""
        <script>
        console.log("Carré dans l'axe");
        </script>""")

def show():
    st.title("Stéganosnap")

    uploaded_file = False
    rand_password = False
    if not uploaded_file:
        uploaded_file = st.file_uploader("Chargez une image", type=["jpg", "jpeg", "png"])
    if uploaded_file :
        st.subheader("Image originale")
        img = Image.open(uploaded_file)
        st.image(img, use_column_width=True)

        img = img.convert("L")
        st.image(img, use_column_width=True)

        txt = st.text_input("Entrez votre texte", value="LOREM IPSUM", key="Clear message")
        txt = crypto.cesar_cipher(txt,int(1/random.random()))
        st.text_input("Entrez votre mot de passe", value="Entrez votre mot de passe", key="password")
        if st.button("Créer aléatoirement", key="random_password"):
            password = randstr()
            rand_password = True
            st.success("Mot de passe aléatoire affecté.\n Cliquez sur le bouton ci-dessous pour afficher")
        if rand_password:
            if st.button("Afficher mot de passe", key="print_random_password"):
                st.write(password)
        if not rand_password and st.session_state.password != "":
            pass###################################################################""
        if st.button("Cacher votre texte", key="Run watermarking"):
            txt=crypto.vigenere_cipher(txt, password)
            crypted_image = encode_image(img,txt)
            st.image(crypted_image, use_column_width=True)


def randstr():
    return "".join([chr(int(nb/random.random())) for nb in range(random.randint(1,int(1/random.random())))])


def switch_str_bin(txt):
    output=""
    is_binary = all(elt in '01' for elt in txt)
    if not is_binary:
        for index in range(len(txt)):
            output += str(bin(ord(txt[index]))[2:]).zfill(21)
    else:
        for index in range(0,len(txt),8):
            output += chr(int(txt[index:index+8],2))

    return output

def even_image(img):
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            img.putpixel((j,i), img.getpixel((j,i))-img.getpixel((j,i)) %2)

def encode_image(img, txt):
    txt=switch_str_bin(txt)
    img=even_image(img)
    index=0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            index+=1
            if index < len(txt):
                img.putpixel((i,j), img.getpixel(i,j)+txt[index])
            else:
                break

show()