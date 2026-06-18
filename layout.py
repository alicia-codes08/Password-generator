import tkinter as tk 
import generator as gr

# important variables
u_password = gr.use_password
k_password = gr.keep_password
k_num = gr.choose_num

r_max = gr.right_max
l_max = gr.left_max 

### print-tests
print(f"using-password: {u_password}")
print(f"range: right=> {r_max}, left=> {l_max}")  
print(f"move: {k_num}") 
print(f"keeping-password: {k_password}") 


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

label_1 = tk.Label(window, text="using password", font=("Arial", 25),
                   relief="solid")
label_1.place(x=170, y=50, width=290, height=70)

label_2 = tk.Label(window, text="keeping password", font=("Arial", 25),
                   relief="solid")
label_2.place(x=170, y=300, width=290, height=70)

# act after klicking a button 
def klicked(value):
    """acting after clicking buttons"""
    if value == "PRESS":
        pass
    elif value == "AC":
        pass 


button_press = tk.Button(window, text="PRESS", font=("Arial", 30), 
                         command=lambda: klicked("PRESS"))
button_press.config(foreground=black, background=grey, relief="groove")
button_press.place(x=10, y=590, anchor="sw")

button_ac = tk.Button(window, text="AC", font=("Arial", 30), 
                         command=lambda: klicked("AC"))
button_ac.config(foreground=black, background=red, relief="flat")
button_ac.place(x=590, y=590, anchor="se") 

    


frame.pack() 
window.mainloop() 