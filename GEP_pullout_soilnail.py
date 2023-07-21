import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from math import exp


image_path = r"C:\Users\shamsher\Downloads\GUI\Final\1.png"

def gepModelquCDG(d):
    
    G1C9 = 9.62523270363475
    G1C5 = 7.23563341166417
    G2C2 = 1.45529158149103
    G2C4 = -4.31679032415509
    G3C5 = -4.97970519119846
    G3C0 = 4.03145902923368
    G4C0 = -9.50889393150235
    G4C7 = 1.36382020789652
    G4C6 = -7.06411938840907
    G5C4 = -11.1923134025422
    G5C6 = -7.25652109415106
    G5C9 = 8.78175917943554

    L = 0
    DD = 1
    i = 2
    sigma_v = 3
    c = 4
    phi = 5

    y = 0.0

    y = ((d[DD]+(((((d[sigma_v]/d[DD])-d[sigma_v])+(d[c]-d[sigma_v]))/2.0)/(G1C9/(G1C5/d[L]))))/2.0)
    y = y + ((d[L]/((d[i]+(G2C2+(G2C4-d[L])))/2.0))/exp(d[DD]))
    y = y + ((d[L]/d[DD])-((((d[L]+G3C5)+G3C5)+(((G3C0*d[i])+d[sigma_v])/2.0))/2.0))
    y = y + (d[phi]*(((((((d[phi]+G4C7)/2.0)+exp(G4C6))/2.0)+((G4C0+d[L])/2.0))/2.0)-d[DD]))
    y = y + (d[DD]/((exp((G5C6/d[L]))-(d[i]/(G5C9+d[sigma_v])))/G5C4))

    return y

def calculate():
    variables = [
        float(entry_D.get()),
        float(entry_L.get()),
        float(entry_i.get()),
        float(entry_sigma.get()),
        float(entry_c.get()),
        float(entry_phi.get())
    ]

    result = gepModelquCDG(variables)

    result_label.config(text="Result: Predicted Bond Strength (kPa): " + str(result))


# Create the GUI
window = tk.Tk()
window.title("© 2023 Myoung-Soo Won & Shamsher Sadiq, Kunsan National University, South Korea (Email: shamsher.sadiq79@gmail.com)")
window.geometry("1000x900")  # Set the size of the GUI window
#window.resizable(False, False)  # Fix the GUI size

# Add a title frame
title_frame = tk.LabelFrame(window, text="Title", font=("Arial", 14))

title_frame.pack(pady=10)

# Add a title label
title_label = tk.Label(title_frame, text="Predicting Soil-Nail Pullout Bond Strength: A Novel Empirical Model based on Evolutionary Algorithm Optimization", font=("Arial", 14))
title_label.pack()


# Create a frame for variable input fields and image
variables_frame = tk.LabelFrame(window, text="Input Variables", font=("Arial", 14))
variables_frame.pack(pady=10)

# Load and resize the image
image = Image.open(image_path)
image = image.resize((400, 300), Image.LANCZOS)

# Convert the image to Tkinter-compatible format
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(variables_frame, image=photo)
image_label.grid(row=0, column=2, rowspan=6, sticky="W")

# Create labels and input fields for variables
#d_label = tk.Label(variables_frame, text="Drill hole diameter, m (D)", font=("Arial", 14))
d_label = tk.Label(variables_frame, text="Drill hole diameter, D (m)", font=("Arial", 14))
d_label.grid(row=1, column=0, sticky="W")
entry_D = tk.Entry(variables_frame)
entry_D.grid(row=1, column=1)

l_label = tk.Label(variables_frame, text="Nail length, L (m)", font=("Arial", 14))
l_label.grid(row=2, column=0, sticky="W")
entry_L = tk.Entry(variables_frame)
entry_L.grid(row=2, column=1)

i_label = tk.Label(variables_frame, text="Nail inclination angle, degrees,i (deg.)", font=("Arial", 14))
i_label.grid(row=3, column=0, sticky="W")
entry_i = tk.Entry(variables_frame)
entry_i.grid(row=3, column=1)

sigma_label = tk.Label(variables_frame, text="Overburden pressure, σ (kPa)", font=("Arial", 14))
sigma_label.grid(row=4, column=0, sticky="W")
entry_sigma = tk.Entry(variables_frame)
entry_sigma.grid(row=4, column=1)

c_label = tk.Label(variables_frame, text="Soil cohesion, c (kPa)", font=("Arial", 14))
c_label.grid(row=5, column=0, sticky="W")
entry_c = tk.Entry(variables_frame)
entry_c.grid(row=5, column=1)

phi_label = tk.Label(variables_frame, text="Friction angle, φ (deg.)", font=("Arial", 14))
phi_label.grid(row=6, column=0, sticky="W")
entry_phi = tk.Entry(variables_frame)
entry_phi.grid(row=6, column=1)

# Create a frame for the result
result_frame = tk.LabelFrame(window, text="Result", font=("Arial", 14))
result_frame.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(result_frame, text="Predicted Bond Strength, q (kPa) ", font=("Arial", 14))
result_label.pack()

# Create a button to calculate the result
calculate_button = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 14))
calculate_button.pack(pady=10)

# Create a frame for the note
note_frame = tk.Frame(window, height=30)
note_frame.pack(pady=10)

# Create a table for the notes
notes_table = ttk.Treeview(note_frame, show="headings", columns=("soil_type", "L", "D", "i", "sigma", "c", "phi", "q"))
notes_table.heading("soil_type", text="Soil Type/Variable range", anchor="center")
notes_table.heading("L", text="L (m)", anchor="center")
notes_table.heading("D", text="D (m)", anchor="center")
notes_table.heading("i", text="i (degrees)", anchor="center")
notes_table.heading("sigma", text="σ (kPa)", anchor="center")
notes_table.heading("c", text="c (kPa)", anchor="center")
notes_table.heading("phi", text="φ (degrees)", anchor="center")
notes_table.heading("q", text="q (kPa)", anchor="center")

notes_table.column("soil_type", width=150)
notes_table.column("L", width=50)
notes_table.column("D", width=50)
notes_table.column("i", width=50)
notes_table.column("sigma", width=50)
notes_table.column("c", width=50)
notes_table.column("phi", width=50)
notes_table.column("q", width=50)

notes_table.insert("", tk.END, values=("CDV (Fine grain soils)", "6-20", "0.1-0.15", "10-45", "57-342", "0-9", "31-39", "65-685"))

notes_table.pack(fill=tk.BOTH, expand=True)

# Create a note label
note_label = tk.Label(window, text="", font=("Arial", 14))
note_label.pack(pady=5)


# Add a copyright notice
copyright_label = tk.Label(window, text="© 2023 Myoung-Soo Won & Shamsher Sadiq, Kunsan National University, South Korea (Email: shamsher.sadiq79@gmail.com)")
copyright_label.pack()

# Start the GUI event loop
window.mainloop()
