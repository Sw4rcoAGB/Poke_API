import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# Lista de Pokémon para el carrusel
pokemon_lista = [ "frogadier", "bulbasaur", "pikachu", "charmander",  "squirtle", "eevee", "snorlax", "mewtwo", "jigglypuff", "charizard",  "machamp"]

current_index = 0

def pokemon_data(pokemon):
  
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#Actualiza la información mostrada en el carrusel
def actualizar_ventana(index):
    
    global current_index
    current_index = index % len(pokemon_lista)  
    pokemon = pokemon_lista[current_index]

    # Datos obtenidos json para mostrar del pokemon
    data = pokemon_data(pokemon)
    if data:
        name = data['name']
        height = data['height']
        weight = data['weight']
        image_url = data['sprites']['front_default']

        
        label_nombre.config(text=f"Nombre: {name.capitalize()}")
        label_altura.config(text=f"Altura: {height} decímetros")
        label_peso.config(text=f"Peso: {weight} hectogramos")
        
        
        response_image = requests.get(image_url)
        if response_image.status_code == 200:
            img_data = BytesIO(response_image.content)
            img = Image.open(img_data)
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            label_imagen.config(image=img_tk)
            label_imagen.image = img_tk  
        
        else:
            label_imagen.config(image="", text="Imagen no disponible.")
    else:
        label_nombre.config(text="No se pudo obtener la información.")
        label_altura.config(text="")
        label_peso.config(text="")
        label_imagen.config(image="", text="")

def Siguiente():
    
    actualizar_ventana(current_index + 1)

def Anterior():
   
    actualizar_ventana(current_index - 1)

#Framework
root = tk.Tk()
root.title("Pokedex")

#Se aplico un cambio en el primer commit ya se le agrego un fondo tkinter
print("Se hizo el primer cambio se agrego un fondo")
root.config(bg="Lightblue")

#Etiquetas de informacion e imagen
label_nombre = tk.Label(root, text="Nombre: ", font=("Georgia", 18))
label_altura = tk.Label(root, text="Altura: ", font=("Georgia", 18))
label_peso = tk.Label(root, text="Peso: ", font=("Georgia", 18))
label_imagen = tk.Label(root)

#Botones de carrusel 
btn_anterior = tk.Button(root, text="Anterior", command=Anterior)
btn_siguiente = tk.Button(root, text="Siguiente", command=Siguiente)


label_nombre.pack(pady=5)
label_altura.pack(pady=5)
label_peso.pack(pady=5)
label_imagen.pack(pady=10)
btn_anterior.pack(side=tk.LEFT, padx=20)
btn_siguiente.pack(side=tk.RIGHT, padx=20)


actualizar_ventana(current_index)


root.mainloop()
