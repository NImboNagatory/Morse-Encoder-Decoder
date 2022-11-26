from func import prepare_text, play_dot, play_dash
from tkinter import *
from PIL import Image, ImageTk
import pyperclip
import time
from tkinter import messagebox


# Functions ----------
def dot():
    morse_input.insert(END, '.')
    tk.update()
    play_dot()


def dash():
    morse_input.insert(END, '-')
    tk.update()
    play_dash()


def clear():
    morse_input.delete(0, END)


def switch():
    if first_button["text"] == 'Decode':
        dash_button.grid_forget()
        dot_button.grid_forget()
        first_button["text"] = 'Encode'
        input_label["text"] = 'Enter Text To Encode:'
        hint_label["text"] = 'Hint: . and - not allowed in Encode'
        second_button["text"] = 'Switch to Decode'
    elif first_button["text"] == 'Encode':
        dash_button.grid(row=4, column=0, sticky="sw")
        dot_button.grid(row=4, column=0, sticky='se')
        first_button["text"] = 'Decode'
        input_label["text"] = 'Enter Text To Decode:'
        hint_label["text"] = 'Hint: Mark the end of the Word with /'
        second_button["text"] = 'Switch to Encode'


def encode_decode():
    if morse_input.get() != "":
        # inner global func
        save_morse = morse_input.get()

        def copy():
            pyperclip.copy(f"{filtered_data}")

        def play():
            encoded_text.delete(1.0, END)
            encoded_text.insert(END, f"Text Input:\n{save_morse}\n\nMorse code Output:\n{filtered_data}\n")
            encoded_text.insert(END, "Playing:\n")
            for morse in filtered_data:

                if morse == ' ':
                    encoded_text.insert(END, f"{morse}")
                    time.sleep(0.01)
                    encoded_window.update()
                elif morse == '\n':
                    encoded_text.insert(END, f"{morse}")
                    encoded_window.update()
                    time.sleep(0.5)
                elif morse == ".":
                    encoded_text.insert(END, f"{morse}")
                    encoded_window.update()
                    play_dot()
                elif morse == "-":
                    encoded_text.insert(END, f"{morse}")
                    encoded_window.update()
                    play_dash()
            encoded_text.delete(1.0, END)
            encoded_text.insert(END, f"Text Input:\n{save_morse}\n\nMorse code Output:\n{filtered_data}")

        # inner global func
        if first_button["text"] == 'Encode' and '-' not in morse_input.get() and '.' not in morse_input.get():
            data = prepare_text(morse_input.get(), mode='encode')
            filtered_data = ''
            for char in data:
                for data_ch in range(len(char)):
                    if data_ch == len(char) - 1:
                        filtered_data += f" {char[data_ch]} / \n"
                    else:
                        filtered_data += f" {char[data_ch]}"

            # Encoded text window --------

            encoded_window = Tk()
            encoded_window.config()
            encoded_window.title('Output')
            encoded_text = Text(encoded_window)
            copy_button = Button(encoded_window, text="Copy", bg="white", width=7, command=copy)
            play_button = Button(encoded_window, text="Play Morse", bg="white", width=9, command=play)
            encoded_text.pack()
            play_button.pack()
            copy_button.pack()
            encoded_text.insert(END, f"Text Input:\n{morse_input.get()}\n\nMorse code Output:\n{filtered_data}")
            morse_input.delete(0, END)
            tk.mainloop()
            # Encoded text window --------
        elif first_button["text"] == 'Decode':
            data = prepare_text(morse_input.get(), mode='decode')
            if data[0] is None:
                yesno = messagebox.askyesno(title='Error', message="Do you want to Encode?")
                if yesno:
                    switch()
                else:
                    clear()
            elif not data[0] is None:
                filter_1_data = ''
                filtered_data = ''
                for char in data:
                    filter_1_data += char[0]
                filter_2_data = filter_1_data.split('/')
                for chara in filter_2_data:
                    filtered_data += f" {chara}"
                    # Decoded text window -------------
                decoded_window = Tk()
                decoded_window.title('Output')
                copy_button = Button(decoded_window, text="Copy", bg="white", width=7, command=copy)
                decoded_text = Text(decoded_window)
                decoded_text.pack()
                copy_button.pack()
                decoded_text.insert(END, f"Morse Input:\n{morse_input.get()}\n\nText Output:\n{filtered_data}")
                morse_input.delete(0, END)
                tk.mainloop()

            # Decoded text window -------------


# Functions ----------

# ---------------------------- UI SETUP ------------------------------- #
# Tkinter UI ----
tk = Tk()
tk.option_add('*Dialog.msg.font', 'Helvetica 20')
tk.title("Morse Code Generator/Translator")
tk.config(pady=40, padx=20, bg="Gray")
# Tkinter UI ----

# img -----
img_canvas = Canvas(width=290, height=300)
morse_img = Image.open("data/steps_morcod morse code index.png")
resized_image = morse_img.resize((250, 250), Image.Resampling.LANCZOS)
pic = ImageTk.PhotoImage(resized_image)
img_canvas.create_image(150, 150, image=pic)
img_canvas.config(bg="Gray", highlightthickness=0)
img_canvas.grid(row=0, column=0)
morse_label = Label(text="International Morse Code", font='Helvetica 14 bold')
morse_label.config(bg="Gray")
morse_label.grid(row=0, column=0, columnspan=2, sticky='n')
# img -----

# text input ----
input_label = Label(text="Enter Text To Encode:")
input_label.config(bg="Gray")
input_label.grid(row=0, column=0, columnspan=2, sticky='s')
morse_input = Entry(width=50)
morse_input.focus()
morse_input.grid(row=1, column=0, columnspan=2, pady=5)
# text input ----

# encode button ----
first_button = Button(text="Encode", width=7, command=encode_decode)
first_button.grid(row=2, column=0, columnspan=2, sticky='W', pady=5)
# encode button ----

# decode button ----
second_button = Button(text="Switch to Decode", width=13, command=switch)
second_button.grid(row=2, column=0, columnspan=2, sticky='E')
# decode button ----
# clear button ----
clr_button = Button(text='Clear', width=5, command=clear)
clr_button.grid(row=0, column=0, sticky='se')
# clear button ----
# dot button -----
dot_button = Button(text=".", width=3, command=dot)
# dot button -----
# dash button -----
dash_button = Button(text="-", width=3, command=dash)
# dash button -----
# hint label
hint_label = Label(text="Hint: . and - not allowed in Encode", bg='gray')
hint_label.grid(row=3, column=0, sticky='sw')
# hint label
# mainloop ----
tk.mainloop()
# mainloop ----
# ---------------------------- UI SETUP ------------------------------- #
