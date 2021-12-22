import tkinter as tk
from PIL import ImageTk, Image
from pyp2p.net import *
import socket

HOST = "127.0.0.1"
PORT = 65432

root = tk.Tk()
# root.wm_attributes('-transparentcolor', 'white')
root.geometry("300x1000+0+0")
root.title("Emoji Overlay")
root.iconbitmap("resources/img/favicon.ico")

img = ImageTk.PhotoImage(Image.open("resources/img/neutral.png"))
img_label = tk.Label(root, image=img)

static_img_1 = ImageTk.PhotoImage(Image.open("resources/img/thinking.png"))
static_img_1_label = tk.Label(root, image=static_img_1)

static_img_2 = ImageTk.PhotoImage(Image.open("resources/img/happy.png"))
static_img_2_label = tk.Label(root, image=static_img_2)

text = tk.StringVar()
text_label = tk.Label(root, textvariable=text, font=("Times New Roman", 15))
text.set("Chris")

static_text_1 = tk.StringVar()
static_text_1_label = tk.Label(root, textvariable=static_text_1, font=("Times New Roman", 15))
static_text_1.set("Rory")

static_text_2 = tk.StringVar()
static_text_2_label = tk.Label(root, textvariable=static_text_2, font=("Times New Roman", 15))
static_text_2.set("Abraham")


img_label.grid(row = 0, column = 0)
text_label.grid(row = 1, column = 0)

static_img_1_label.grid(row = 2, column = 0)
static_text_1_label.grid(row = 3, column = 0)

static_img_2_label.grid(row = 4, column = 0)
static_text_2_label.grid(row = 5, column = 0)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        
        while 1:
            data = conn.recv(1024)
            if(data):
                data = str(data.decode())
                data = data.split(" ")[0]
                data = data.rstrip()
                img=ImageTk.PhotoImage(Image.open("resources/img/" + data + ".png"))
                img_label.configure(image=img)
                img_label.image=img
            root.update()