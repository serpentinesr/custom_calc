import customtkinter
from buttons import button_callback

app = customtkinter.CTk()

app.title("custom_calc")
app.geometry("700x500")

button = customtkinter.CTkButton(
    master=app,
    text="Hello!",
    command=button_callback
)
button.pack()





app.mainloop()