import tkinter as tk

class Login():
    """Class representing a login prompt that asks for a
    username and password, and validates whether or not
    password is correct. Account login data is stored in
    username,password format in a local file called
    logindata.txt"""

    def __init__(self):
        self.account_data = "logindata.txt"
        self.root = tk.Tk()
        self.root.geometry("220x100")
        self.root.title("Login")

        self.user_label = tk.Label(self.root, text = "Username:")
        self.user_entry = tk.Entry(self.root)

        self.pass_label = tk.Label(self.root, text = "Password:")
        self.pass_entry = tk.Entry(self.root)

        self.login_button = tk.Button(self.root, text = "Login", command=self.validate_login)

        self.user_label.grid(row=0, column=0)
        self.user_entry.grid(row=0, column=1, columnspan=2)

        self.pass_label.grid(row=1, column=0)
        self.pass_entry.grid(row=1,column=1, columnspan=2)

        self.login_button.grid(row=2, column=1)

        for widget in self.root.winfo_children():
            widget.grid_configure(padx = 5, pady = 5)

    def validate_login(self):
        """Command function for login button that gets the values of the
        username and password entries, then iterates through data file to
        check if input values match an existring account (username, password)"""
        
        # get entry values for username and password
        username = self.user_entry.get()
        password = self.pass_entry.get()

        # open account data file and iterate through it
        with open(self.account_data, "r") as f:
            for line in f:
                user_parse, pass_parse = line[:-1].split(',', maxsplit=1)
                
                # check if username and password match existing values in file
                if username == user_parse:
                    if password == pass_parse:
                        print("valid")
                        valid_attempt = tk.Toplevel()
                        valid_label = tk.Label(valid_attempt, text="Login Successful", fg="green")
                        valid_label.pack()
                        valid_attempt.mainloop()
                        
                    else:
                        print("Invalid")
                        invalid_attempt_label = tk.Label(self.root, text="Invalid username or password.\nPlease try again", fg="red")
                        invalid_attempt_label.grid(row=10, column=0, columnspan=2, padx=20, pady=5)
                        self.root.geometry("220x150")
                    break

                else:
                    print("Invalid")
                    invalid_attempt_label = tk.Label(self.root, text="Invalid username or password.\nPlease try again", fg="red")
                    invalid_attempt_label.grid(row = 10, column=0, columnspan=2, padx=20, pady=5)
                    self.root.geometry("220x150")


if __name__ == "__main__":
    gui = Login()
    gui.root.mainloop()
