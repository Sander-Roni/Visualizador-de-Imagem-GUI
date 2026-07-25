from dotenv import load_dotenv 
from customtkinter import CTk
import customtkinter
from PIL import Image,ImageDraw
import generative.requisicao as dados
load_dotenv()

class screen_main(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("350x450")
        self.resizable(False,False)
        self.title("Visualizador de Imagens")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.config(bg="#f4ffc1")
        self.frames()
        self.mainloop()

    def Generate_Image(self):
        rad = 100
        save_type = Image.open("images/ImageAPI.jpg").save("image.png","PNG")
        load_type = Image.open("image.png")
        circle = Image.new('L',(rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0,0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', load_type.size, 255)
        x,y = load_type.size 
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0)) #Canto superior direito
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, y - rad)) # Canto inferior esquerdo
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (x - rad, 0)) # Canto superior direito
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (x - rad, y - rad)) #Canto inferior direito
        load_type.putalpha(alpha)
        load_type.save("image.png")

    def frames(self):
        frame1 = customtkinter.CTkFrame(self, corner_radius=20, width=300, height=100, bg_color="#f4ffc1", fg_color="#4eb8ff")
        frame1.place(x=20, y=10)
        frame2 = customtkinter.CTkFrame(self, corner_radius=20, width=300, height=300, bg_color="#f4ffc1",fg_color="#4eb8ff")
        frame2.place(x=20,y=120)

        self.Generate_Image()

        c_Image = customtkinter.CTkImage(light_image=Image.open("image.png"),size=(240,200))
        _Label = customtkinter.CTkLabel(frame2, text=" ",image=c_Image, height=80) # pega um arquivo PIL
        _Label.place(x=25,y=50)
        self.ImageSearch(frame1, c_Image)

    def ImageSearch(self, frame1, param):
        search_campus = customtkinter.CTkEntry(frame1, width=260, text_color="#000000", corner_radius=20,height=60, placeholder_text="Pesquise Imagens")
        search_campus.place(x=20,y=20)
        button_campus = customtkinter.CTkButton(search_campus,text="🔍",text_color="#4B4A4A",fg_color="#dfff4f", font=("Verdana",12,"bold"), width=20, height=30, corner_radius=20, command=lambda:Search_())
        button_campus.place(x=200,y=15)

        def Search_():
            target = search_campus.get()
            if target:
                dados.buscar_imagem(target)
                param.configure(light_image=Image.open("image.png")) #Acertei em Cheio

            else:
                print("dados não encontrados")

screen_main()