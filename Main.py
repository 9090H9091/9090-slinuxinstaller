import tkinter as tk
import pyglet
from tkinter import PhotoImage

# Load custom font
pyglet.font.add_file('inter.ttf')

# Create the main window
root = tk.Tk()
root.title("Linux but easier")
root.geometry("640x480")
root.configure(background='#545454')

# Add a label with custom font
label = tk.Label(root, text="Test", font=('inter', 25), bg='#545454', fg='white')
label.pack(pady=20)

# Load images
mint = PhotoImage(file=r"/home/ace/Documents/9090-slinuxinstaller/Mint.png")
ubuntu = PhotoImage(file=r"/home/ace/Documents/9090-slinuxinstaller/Ubuntu.png")
endeavour = PhotoImage(file=r"/home/ace/Documents/9090-slinuxinstaller/Endeavour.png")

# Add images to labels
mint_label = tk.Label(root, image=mint, bg='#545454')
mint_label.pack(pady=10)

ubuntu_label = tk.Label(root, image=ubuntu, bg='#545454')
ubuntu_label.pack(pady=10)

endeavour_label = tk.Label(root, image=endeavour, bg='#545454')
endeavour_label.pack(pady=10)

# Button click event handler
def on_button_click():
    label.config(text="Button Clicked!", font=('inter', 25))

# Add buttons
button1 = tk.Button(root, text="Click Me 1", command=on_button_click)
button1.pack(pady=10)

button2 = tk.Button(root, text="Click Me 2", command=on_button_click)
button2.pack(pady=10)

button3 = tk.Button(root, text="Click Me 3", command=on_button_click)
button3.pack(pady=10)

# Run the application
root.mainloop()
