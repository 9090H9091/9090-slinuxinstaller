import tkinter as tk
import pyglet
import requests
from PIL import Image, ImageTk
import threading
import webbrowser  as wb
import os as os


pyglet.font.add_file('/home/ace/Documents/9090-slinuxinstaller/inter.ttf')


root = tk.Tk()
root.title("Linux but easier")
root.geometry("640x480")
root.configure(background='#545454')


main_label = tk.Label(root, text="Test", font=('inter', 25), bg='#545454', fg='white')
main_label.grid(row=0, columnspan=3, pady=10)


message_label = tk.Label(
    root,
    text="Linux's easiest linux install.\nI want to fix the computer literature gap between Windows and Linux and I believe this is one of it.",
    font=('inter', 10),
    bg='#545454',
    fg='white',
    wraplength=600,
    justify="center"
)
message_label.grid(row=1, columnspan=3, pady=10)


def resize_image(image_path, size=(128, 128)):
    image = Image.open(image_path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)


mint = resize_image(r"/home/ace/Documents/9090-slinuxinstaller/Mint.png")
fedora = resize_image(r"/home/ace/Documents/9090-slinuxinstaller/fedora.png")
endeavour = resize_image(r"/home/ace/Documents/9090-slinuxinstaller/Endeavour.png")


mint_label = tk.Label(root, image=mint, bg='#545454')
mint_label.grid(row=2, column=0, padx=10, pady=10)

fedora_label = tk.Label(root, image=fedora, bg='#545454')
fedora_label.grid(row=2, column=1, padx=10, pady=10)

endeavour_label = tk.Label(root, image=endeavour, bg='#545454')
endeavour_label.grid(row=2, column=2, padx=10, pady=10)


def download_file(url, dest):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open(dest, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
    print(f'Download completed: {dest}')


def install_mint():
    threading.Thread(target=download_file, args=('https://mirrors.cicku.me/linuxmint/iso/stable/22/linuxmint-22-cinnamon-64bit.iso', '/home/ace/Downloads/linuxmint-22-cinnamon-64bit.iso')).start()

def install_fedora():
    threading.Thread(target=download_file, args=('https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso', '/home/ace/Downloads/Fedora-Workstation-Live-x86_64-40-1.14.iso')).start()

def install_endeavour():
    threading.Thread(target=download_file, args=('https://mirror.jingk.ai/endeavouros/iso/EndeavourOS_Endeavour-2024.06.25.iso', '/home/ace/Downloads/EndeavourOS_Endeavour-2024.06.25.iso')).start()


def show_try_install_buttons_mint():
    button1.grid_forget()
    try_button = tk.Button(root, text="Try", command=try_mint)
    try_button.grid(row=3, column=0, padx=5, pady=10, sticky='w')

    install_button = tk.Button(root, text="Install", command=install_mint)
    install_button.grid(row=3, column=0, padx=5, pady=10, sticky='e')

def show_try_install_buttons_fedora():
    button2.grid_forget()
    try_button = tk.Button(root, text="Try", command=try_fedora)
    try_button.grid(row=3, column=1, padx=5, pady=10, sticky='w')

    install_button = tk.Button(root, text="Install", command=install_fedora)
    install_button.grid(row=3, column=1, padx=5, pady=10, sticky='e')

def show_try_install_buttons_endeavour():
    button3.grid_forget()
    try_button = tk.Button(root, text="Try", command=try_endeavour)
    try_button.grid(row=3, column=2, padx=5, pady=10, sticky='w')

    install_button = tk.Button(root, text="Install", command=install_endeavour)
    install_button.grid(row=3, column=2, padx=5, pady=10, sticky='e')

def try_mint():
    wb.open_new('https://distrosea.com/start/linuxmint-21-Cinnamon/')

def try_fedora():
    wb.open_new('https://distrosea.com/start/fedora-40-Workstation/')

def try_endeavour():
    wb.open_new('https://distrosea.com/start/endeavouros-Gemini.2024.04.20-default/')


button1 = tk.Button(root, text="Mint", command=show_try_install_buttons_mint)
button1.grid(row=3, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="Fedora", command=show_try_install_buttons_fedora)
button2.grid(row=3, column=1, padx=10, pady=10)

button3 = tk.Button(root, text="Endeavour", command=show_try_install_buttons_endeavour)
button3.grid(row=3, column=2, padx=10, pady=10)


root.mainloop()
