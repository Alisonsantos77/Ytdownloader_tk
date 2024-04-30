# importando Custom Tkinter
import customtkinter as ctk
from tkinter import filedialog
import time
import os
# Importando PyTube
from pytube import YouTube


# Cores ----------------------------------------------------------------
preto = '#000000'
azul_escuro = '#14213D'
amarelo = '#FCA311'
cinza = '#E5E5E5'
branco = '#FFFFFF'
rose_ebony = '#513b3c'


# Criando a janela
janela = ctk.CTk()
janela.title("PYT")
janela.geometry('250x300')


# Variável global para armazenar o diretório selecionado
select_dir = None

#  Funções

def new_download():
    global select_dir
    # Obtém a URL do vídeo do campo link_input
    url = link_input.get()
    # Cria um objeto YouTube com a URL
    yt = YouTube(url)
    # Seleciona o stream de vídeo com a resolução mais alta
    video_stream = yt.streams.get_highest_resolution()

    # Vai usar a variavel select_dir caso já tenha sido selecionada
    if select_dir:
        base_name = os.path.splitext(video_stream.default_filename)[0]
        video_stream.download(select_dir, filename=f'{base_name}.mp4')
        print("Download Completo")
        print("Insira um novo link")
    else:
        # caso contrario, chama a função save_dir para obter o diretório
        select_dir = save_dir()
        if select_dir:
            base_name = os.path.splitext(video_stream.default_filename)[0]

            video_stream.download(select_dir, filename=f'{base_name}.mp4')
            print("Download Completo")
        else:
            print('Selecione um diretório')
    # Limpa o campo de entrada após o download
    link_input.delete(0, 'end')

def save_dir():
    global select_dir  # Acessa a variável global
    new_dir = filedialog.askdirectory()
    if new_dir:
        select_dir = new_dir  # Armazena o diretório selecionado na variável global
        return new_dir
    else:
        print('Selecione um diretório')
        return None


def new_mp3():
    global select_dir
    input_mp3 = ctk.CTkInputDialog(text="Somente audio", title="PYT MP3")

    audio_url = input_mp3.get_input()
    yt = YouTube(audio_url)
    # Filtra para buscar somente o primeiro audio
    filter_mp3 = yt.streams.filter(only_audio=True).first()

    if select_dir:
        # Remove a extensão do nome do arquivo original e adiciona o sufixo
        base_name = os.path.splitext(filter_mp3.default_filename)[0]
        unique_filename = f"{base_name}_mp3_{int(time.time())}.mp3"
        filter_mp3.download(select_dir, filename=unique_filename)
        print("Download Completo")
    else:
        select_dir = save_dir()
        if select_dir:
            # Remove a extensão do nome do arquivo original e adiciona o sufixo
            base_name = os.path.splitext(filter_mp3.default_filename)[0]
            unique_filename = f"{base_name}_mp3_{int(time.time())}.mp3"
            filter_mp3.download(select_dir, filename=unique_filename)
            print("Download Completo")
        else:
            print('Selecione um diretório')
            
    # Limpa o campo de entrada após o download
    link_input.delete(0, 'end')

# Widgets
texto = ctk.CTkLabel(janela, text='Baixe aqui',
                    font=ctk.CTkFont(family='roboto', size=16))
texto.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky='n')

link_input = ctk.CTkEntry(janela, placeholder_text='Seu link')
link_input.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='ew')

# Criando e organizando os botões em uma grade
botao_format = ctk.CTkButton(janela, text='Formatos', command=new_mp3, fg_color=azul_escuro, text_color=amarelo, width=5)
botao_format.grid(row=2, column=0, padx=30, pady=30)

botao_dir = ctk.CTkButton(janela, text='Diretório', width=5, fg_color=branco, text_color=azul_escuro, command=save_dir, font=ctk.CTkFont(family='roboto', size=12))
botao_dir.grid(row=2, column=1, padx=30, pady=30)

botao_submit = ctk.CTkButton(janela, text='Baixar', command=new_download, font=ctk.CTkFont(family='roboto', size=16))
botao_submit.grid(row=3, column=0, columnspan=2, padx=20, pady=30)

janela.mainloop()
