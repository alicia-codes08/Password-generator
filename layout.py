import tkinter as tk 
import generator as gr


# using layout 
blue = "#1CC7D6" 
black = "#1C1C1C"
white = "#F9F9F9" 
red = "#F01111"
grey = "#A7A7A7"


# setting up the window and frames
window = tk.Tk()
window.title("Using/keeping-password generator")
window.geometry("600x600")
window.resizable(False, False) 
window.config(background=blue)
frame = tk.Frame(window) 

# showing passwords and moved number 
label_1 = tk.Label(window, text="", font=("Arial", 25), relief="solid")
label_1.place(x=170, y=50, width=290, height=70)

label_2 = tk.Label(window, text="", font=("Arial", 25), relief="solid")
label_2.place(x=170, y=165, width=290, height=70)

label_3 = tk.Label(window, text="", font=("Arial", 25), relief="solid")
label_3.place(x=200, y=330, width=210, height=70)

# global variables for the text in the labels
label_1["text"] = "using password"
label_2["text"] = "keeping password"
label_3["text"] = "moved place" 

# act after klicking a button 
def clear():
    """Clear text."""
    label_1["text"] = "using password"
    label_2["text"] = "keeping password"
    label_3["text"] = "moved place"

def klicked():
    """acting after clicking buttons"""
    generator = gr.Generator()
    generator.using_password_gen()
    generator.highest_lowest_index()
    generator.moved_place()
    generator.getting_keeping_password()

    # change text on labels
    label_1["text"] = generator.use_password
    label_2["text"] = generator.keep_password
    label_3["text"]= generator.moved_place_num

    ### print-tests
    print(f"using-password: {generator.use_password}")
    print(f"move: {generator.keep_password}") 
    print(f"keeping-password: {generator.moved_place_num}") 


# buttons to press 
button_press = tk.Button(window, text="PRESS", font=("Arial", 30), 
                         command=lambda: klicked())
button_press.config(foreground=black, background=grey, relief="groove")
button_press.place(x=10, y=590, anchor="sw")

button_ac = tk.Button(window, text="AC", font=("Arial", 30), 
                         command=lambda: clear())
button_ac.config(foreground=black, background=red, relief="groove")
button_ac.place(x=590, y=590, anchor="se")    


frame.pack() 
window.mainloop() 