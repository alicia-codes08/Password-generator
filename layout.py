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

window = tk.Tk()
window.title("Using/keeping-password generator")
window.resizable(False, False) 

frame = tk.Frame(window) 

label = tk.Label(frame, text="", font=("Arial", 40), background=blue,
                 foreground=black, width=20, height=10)
label.grid(row=0, column=0, columnspan=30)


frame.pack() 


window.mainloop() 