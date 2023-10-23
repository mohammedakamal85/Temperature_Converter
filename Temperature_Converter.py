#first import tkinter
import tkinter as tk

#define function to convert from fahrenheit to celsius
def fahrenheit_to_celsius():
    fahrenheit = float(ent_temperature.get())
    celsius = (fahrenheit - 32) * 5/9
    lbl_result.config(text=f"{celsius:.2f} \N{DEGREE CELSIUS}")
    return celsius

#create tkinter window and resize it
window = tk.Tk()
window.title('Tempersture Converter')
window.resizable(width=200, height=200)

#adjust the label and temperature using grid method
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text='\N{DEGREE FAHRENHEIT}')
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

#create button to convert from fahrenheit to celsius
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

#create a label widget to display the result of the conversion in celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

#use grid method to arrange the frame, button and result label widgets
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
    