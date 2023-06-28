import customtkinter as ctk
import os

# Created by Rikey
# https://github.com/semazurek/

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title('SH-Timer ver. 1.0')
root.geometry("500x220")
root.resizable(False,False)

root.wm_attributes('-toolwindow', 'True')

root.message_text = ctk.StringVar()

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Select Time to Turn Off", font=("Roboto", 24))
label.pack(pady=10, padx=10)

button1 = ctk.CTkButton(master=frame, text="12h", width=80, command= lambda: os.system('shutdown /s /t 43200'), font=("Roboto", 20))
button1.place(y=50, x=10)

button2 = ctk.CTkButton(master=frame, text="10h", width=80, command= lambda: os.system('shutdown /s /t 36000'), font=("Roboto", 20))
button2.place(y=50, x=100)

button3 = ctk.CTkButton(master=frame, text="8h", width=80, command= lambda: os.system('shutdown /s /t 28800'), font=("Roboto", 20))
button3.place(y=50, x=190)

button4 = ctk.CTkButton(master=frame, text="6h", width=80, command= lambda: os.system('shutdown /s /t 21600'), font=("Roboto", 20))
button4.place(y=50, x=280)

button5 = ctk.CTkButton(master=frame, text="4h", width=80, command= lambda: os.system('shutdown /s /t 14400'), font=("Roboto", 20))
button5.place(y=50, x=370)


button6 = ctk.CTkButton(master=frame, text="45min", width=80, command= lambda: os.system('shutdown /s /t 2700'), font=("Roboto", 20))
button6.place(y=90, x=10)

button7 = ctk.CTkButton(master=frame, text="30min", width=80, command= lambda: os.system('shutdown /s /t 1800'), font=("Roboto", 20))
button7.place(y=90, x=100)

button8 = ctk.CTkButton(master=frame, text="15min", width=80, command= lambda: os.system('shutdown /s /t 900'), font=("Roboto", 20))
button8.place(y=90, x=190)

button9 = ctk.CTkButton(master=frame, text="10min", width=80, command= lambda: os.system('shutdown /s /t 600'), font=("Roboto", 20))
button9.place(y=90, x=280)

button10 = ctk.CTkButton(master=frame, text="5min", width=80, command= lambda: os.system('shutdown /s /t 300'), font=("Roboto", 20))
button10.place(y=90, x=370)

buttoncancel = ctk.CTkButton(master=frame, text="Cancel Shutdown", width=80, fg_color='red', command= lambda: os.system('shutdown /a'), font=("Roboto", 20))
buttoncancel.place(y=135, x=150)


root.mainloop()