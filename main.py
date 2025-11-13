from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def change_pixel(location, img, color):
    while ((img.format == 1 and (color != 1 and color != 0)) or \
        (img.format == "L" and not (type(color) == int and color >0 and color<255)) or \
            ((img.format == "RGB" or img.format == "RGBA" or img.format == "CMYK") and \
            not (type(color)[i] == int and color[i] >0 and color[i]<255) for i in range (0,len(color)-1)) or \
                type(color)!= int):
        color=input("Give a right color format please : ")
    while type(location) != tuple and len(location) != 2 and location[0]<=img.size and location[0]>=0 and location[1]<=img.size and location[1]>=0:
        location=input("Give a right location please : ")
    while type(img)[:12] != "<class 'PIL.":
        img = Image.open(askopenfilename(title="Sélectionnez une image", \
                                         filetypes=[("Images", "*.jpg *.png *.jpeg"), ("Tous les fichiers", "*.*")]))
    img.putpixel(location, color)

Tk().withdraw()  # Masquer la fenêtre principale de Tkinter
file_path = askopenfilename(title="Sélectionnez une image", filetypes=[("Images", "*.jpg *.png *.jpeg"), ("Tous les fichiers", "*.*")])

if file_path:
    # Charger l'image sélectionnée
    img = Image.open(file_path)
    print(f"Image chargée : {file_path}")
    print(f"Taille de l'image : {img.size}")
    
    # Exemple : Modifier un pixel
    change_pixel((10, 10), img, (255, 0, 0))  # Modifier le pixel (10, 10) en rouge
    img.show()  # Afficher l'image modifiée
else:
    print("Aucun fichier sélectionné.")
