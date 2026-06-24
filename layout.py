import tkinter as tk 
import generator as gr


# colors 
blue = "#1CADE6" 
black = "#1C1C1C"
white = "#F9F9F9" 
red = "#F01111"
grey = "#999999"

# action after klicking a button 
def clear():
    """Clear text in the white fields"""
    label_1["text"] = ""
    label_2["text"] = ""
    label_3["text"] = ""

def klicked():
    """change text in the white fields after klicking 'press'."""
    # getting passwords and moved number
    generator = gr.Generator()
    generator.using_password_gen()
    generator.highest_lowest_index()
    generator.moved_place()
    generator.getting_keeping_password()

    # change text in the white fields
    label_1["text"] = generator.use_password
    label_2["text"] = generator.keep_password
    label_3["text"] = generator.moved_place_num * -1


# setting up windows and frames 
window = tk.Tk()
window.title("Using/keeping-password generator")
window.geometry("650x650")
window.resizable(False, False) 
window.config(background=blue)
frame = tk.Frame(window) 

# showing passwords and number of moved place
label_title_1 = tk.Label(window, text="using password:", font=("Arial", 25), 
                         bg=blue)
label_title_1.place(x=190, y=5, width=290, height=60)
label_1 = tk.Label(window, text="", font=("Arial", 25), relief="solid")
label_1.place(x=200, y=60, width=290, height=60)

label_title_2 = tk.Label(window, text="keeping password:", font=("Arial", 25), 
                        bg=blue)
label_title_2.place(x=200, y=140, width=290, height=60)
label_2 = tk.Label(window, text="", font=("Arial", 25), relief="solid")
label_2.place(x=200, y=200, width=290, height=60)

label_title_3 = tk.Label(window, text="moved place:", font=("Arial", 25), 
                         bg=blue)
label_title_3.place(x=240, y=300, width=190, height=60)
label_3 = tk.Label(window, text="", font=("Arial", 25), relief="solid")
label_3.place(x=280, y=355, width=85, height=60)

# Overview of all elements 
text = "If you got a negative number, your real password ist moved to the left."\
"\nOtherwise it's moved to the right."
message = tk.Label(window, text=text, font=("Arial", 12), background=blue)
message.place(x=5, y= 445, width=635, height=50) 

elements_list = gr.Generator().elements_list
password_elements = tk.Label(window, text=elements_list, font=("Arial", 12), 
                            relief="solid")
password_elements.place(x=10, y= 490, width=635, height=50) 

# buttons to press 
button_press = tk.Button(window, text="PRESS", font=("Arial", 30), 
                         command=lambda: klicked())
button_press.config(foreground=black, background=grey, relief="groove")
button_press.place(x=10, y=640, anchor="sw")

button_ac = tk.Button(window, text="AC", font=("Arial", 30), 
                         command=lambda: clear())
button_ac.config(foreground=black, background=red, relief="groove")
button_ac.place(x=640, y=640, anchor="se")    


frame.pack() 
window.mainloop() 