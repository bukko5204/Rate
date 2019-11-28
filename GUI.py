import tkinter as tk

user_data = {
    "Lara Croft":"1234"


}


class App(tk.Tk):

    def log_in(self):
        username = username_entry.get()
        password = password_entry.get()

        if username in user_data:
            if password == user_data[username]:
                print("Logged in!")

            else:
                print("Wrong password!")

        else:
            print("This username doesn't exist!")

    def __init__(self):
        tk.Tk.__init__(self)

        self.username_label = tk.Label(self, text = "Username")
        self.password_label = tk.Label(self, text = "Password")

        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self)

        self.entry_button = tk.Button(self, text = "Log in!", command = self.log_in())

        self.username_entry.grid(row = 0, column = 1)
        self.password_entry.grid(row = 1, column = 1)
        self.entry_button.grid(row = 2)
        self.username_label.grid(row = 0)
        self.password_label.grid(row = 1)

        def log_in(self):
            username = username_entry.get()
            password = password_entry.get()

            if username in user_data:
                if password == user_data[username]:
                    print("Logged in!")

                else:
                    print("Wrong password!")

            else:
                print("This username doesn't exist!")








app = App()
app.mainloop()
