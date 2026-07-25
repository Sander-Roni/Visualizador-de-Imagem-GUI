import requests  
from dotenv import load_dotenv
import os 
import random
from PIL import ImageDraw,Image
from urllib.request import urlretrieve #essa biblioteca aqui faz download de uma URL ela que eu queria
load_dotenv()


def buscar_imagem(busca_informada):
    array = []
    acesso = os.getenv("api_key")
    response = requests.get(f"https://api.unsplash.com/search/photos?per_page=30&query={busca_informada}&client_id={acesso}")
    Imagens = response.json()
    for i in range(len(Imagens["results"])):
        array.append(Imagens["results"][i]["urls"]["small"])
    random.shuffle(array)

    url = array[0]
    if not url:
        print("Imagem não encontrada")
    else:
        filename = "image.png"
        if not filename:
            print("Imagem não encontrada")
        urlretrieve(url, filename) #ver se a Imagem da API pode ser redimensionada

        rad = 100
        image_open = Image.open(filename)
        circle = Image.new('L',(rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0,0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', image_open.size, 255)
        w, h = image_open.size 
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0)) #Canto superior direito
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad)) # Canto inferior esquerdo
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0)) # Canto superior direito
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad)) #Canto inferior direito
        image_open.putalpha(alpha)
        image_open.save("image.png")

        

