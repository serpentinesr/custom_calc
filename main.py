import customtkinter
from buttons import button_callback

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('custom_calc')
        self.geometry('700x500')
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(
            master=self,
            text='Hello!',
            command=button_callback
        )

        self.button.grid(
            row=0,
            column=0,
            padx=20,
            pady=20
        )


app = App()
app.mainloop()