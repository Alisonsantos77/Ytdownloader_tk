# importando Custom Tkinter
import customtkinter as ctk
from tkinter import filedialog

# Importando PyTube
from pytube import YouTube

from tkinter import font, Tk


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
janela.geometry('500x300')

#  Funções

# Variável global para armazenar o diretório selecionado
select_dir = None


def new_download():
    global select_dir
    url = link_input.get()
    yt = YouTube(url)

    video_stream = yt.streams.get_highest_resolution()

    # Vai usar a variavel select_dir caso já tenha sido selecionada
    if select_dir:
        video_stream.download(select_dir)
        print("Download Completo")
    else:
        # chama a função save_dir para obter o diretório
        select_dir = save_dir()
        if select_dir:
            video_stream.download(select_dir)
            print("Download Completo")
        else:
            print('Selecione um diretório')


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
    input_mp3 = ctk.CTkInputDialog(text="Baixar em MP3", title="PYT MP3")

    audio_url = input_mp3.get_input()
    yt = YouTube(audio_url)

    filter_mp3 = yt.streams.filter(only_audio=True).first()

    if select_dir:
        filter_mp3.download(select_dir)
        print("Download Completo")
    else:
        select_dir = save_dir()
        if select_dir:
            filter_mp3.download(select_dir)
            print("Download Completo")
        else:
            print('Selecione um diretório')

# Widgets


texto = ctk.CTkLabel(janela, text='Baixe aqui',
                     font=ctk.CTkFont(family='roboto', size=16))
texto.pack(padx=20, pady=20, anchor='center')

link_input = ctk.CTkEntry(janela, placeholder_text='Seu link')
link_input.pack(padx=20, pady=20, anchor='center')

# check_mp3 = ctk.CTkCheckBox(janela, text='.MP3')
# check_mp3.pack(padx=(0,  10), pady=10, anchor='center')

# check_mp4 = ctk.CTkCheckBox(janela, text='.MP4')
# check_mp4.pack( padx=(10,  0), pady=0, anchor='center')

botao_format = ctk.CTkButton(
    janela, text='Formatos', command=new_mp3, fg_color=azul_escuro, text_color=amarelo, width=5)
botao_format.pack(padx=10, pady=0, anchor='center')


botao_dir = ctk.CTkButton(janela, text='Diretório', width=5,
                          fg_color=branco, text_color=azul_escuro, command=save_dir, font=ctk.CTkFont(family='roboto', size=12))
botao_dir.pack(side='top', padx=(0, 30), pady=0, anchor='se')

botao_submit = ctk.CTkButton(
    janela, text='Baixar', command=new_download, font=ctk.CTkFont(family='roboto', size=16))
botao_submit.pack(padx=20, pady=2, anchor='center')


janela.mainloop()
