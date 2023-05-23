import time
import tkinter
import tkinter.messagebox
import customtkinter
import threading
from Pinterest import Pinterest,chat,shortner
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{800}x{450}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Settings", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        import os
        import subprocess
        import platform
        def open_excel_file2(filename='accounts.xlsx'):
            # Check if the file exists
            if not os.path.isfile(filename):
                return
            # Open the file
                # Open the file
            if platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', filename], check=True)
            elif platform.system() == 'Windows':  # Windows
                os.startfile(filename)
            else:  # linux variants
                subprocess.run(['xdg-open', filename], check=True)
        def open_excel_file():
            thread = threading.Thread(target=open_excel_file2)
            thread.start()
        def Creative_login2():
            import time
            from selenium.webdriver.common.by import By
            import undetected_chromedriver as uc
            import getpass
            chrome_options2 = uc.ChromeOptions()
            chrome_options2.add_argument("start-maximized")
            chrome_options2.add_argument("--window-size=1920,1080")
            username = getpass.getuser()
            chrome_options2.add_argument(
                f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\zaws")
            driver2 = uc.Chrome(chrome_options=chrome_options2)
            with driver2:
                driver2.get('https://www.creativefabrica.com/')
                driver2.maximize_window()
                while True:
                    try:
                        driver2.find_element(By.XPATH,'//*[@id="menu-item-icon-my-account"]')
                        break
                    except:
                        continue
                current_text = self.textbox.get("1.0", "end")
                if "posting logs" in current_text:
                    new_text = current_text.replace("posting logs", "")
                    self.textbox.delete("1.0", "end")
                    self.textbox.insert("1.0", new_text)
                self.textbox.insert("end","--------------------------\nLogged into Creative fabrica with Success!\n--------------------------\nPlease restart the app before using Pinterest...")
                time.sleep(4)
        def Creative_login():
            thread = threading.Thread(target=Creative_login2)
            thread.start()
        def quit():
            exit()
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=open_excel_file, text='account settings')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=Creative_login, text='Creativefabrica')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        switch1 = customtkinter.CTkSwitch(self.sidebar_frame, text="save backup")
        switch1.grid(row=3, column=0,padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=quit, text='quit')
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="keyword")
        self.entry1.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        validate_cmd = self.register(validate_only_digits)
        self.num = customtkinter.CTkLabel(self, text="Amount:")
        self.num.grid(row=3, column=2, sticky="nsew")

        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Amount", validate="key", validatecommand=(validate_cmd, '%d', '%P'))
        self.entry2.grid(row=3, column=3, padx=(20, 0), pady=(20, 20), sticky="nsew")

        def my_function_threadeds():
            thread = threading.Thread(target=self.pulls)
            thread.start()
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text='START',command=my_function_threadeds)
        self.main_button_1.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250,height=6)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=3)

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Platforms")
        self.scrollable_frame.grid(row=0, column=4,padx=(10, 0), pady=(10, 0), sticky="nsew",  columnspan=3)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        def funs():
            if switch1.get():
                import pandas as pd

                # Load the data from the Excel file
                df = pd.read_excel('accounts.xlsx')

                # Extract data from columns
                self.email = df.loc[0, 'Email']
                self.password = df.loc[0, 'Password']
                self.username = df.loc[0, 'Username']
                self.board = df.loc[0, 'Board(name or id)']

                # Check if board is a number or a string
                try:
                    # Try to convert to numeric
                    board = pd.to_numeric(self.board)
                    pass
                except ValueError:
                    # If it raises a ValueError, it's a string
                    pass
                current_text = self.textbox.get("1.0", "end")
                if "posting logs" in current_text:
                    new_text = current_text.replace("posting logs", "")
                    self.textbox.delete("1.0", "end")
                    self.textbox.insert("1.0", new_text)
                self.textbox.insert("end", f"Success!\nEmail: {self.email}\nPassword: {self.password}\nUsername: {self.username}\nBorad: {self.board}")
                time.sleep(2)
                self.textbox.insert("end","\n--------------------------\nLogin in ...")
                pinterest = Pinterest.Pinterest(email=self.email, password=self.password, username=self.username)

                # ------------------------------------------

                pinterest.login()
                self.textbox.insert("end", "\n--------------------------\nSuccess!\n--------------------------\n")
        def my_function_threaded():
            thread = threading.Thread(target=funs)
            thread.start()
        switch1 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Pinterest",command=my_function_threaded)
        switch1.grid(row=0, column=0, padx=5, pady=(0, 10))
        switch2 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Ebay")
        switch2.grid(row=1, column=0, padx=5, pady=(0, 10))

        switch4 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Instagram")
        switch4.grid(row=4, column=0, padx=5, pady=(0, 10))
        switch5 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Facebook")
        switch5.grid(row=3, column=0, padx=5, pady=(0, 10))
        switch3 = customtkinter.CTkSwitch(master=self.scrollable_frame, text="KDP AMAZON")
        switch3.grid(row=5, column=0, padx=5, pady=(0, 10))
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "posting logs")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def only_numeric_input(P):
        # check if string is a number or empty and return an appropriate boolean
        if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
            return True
        return False
    def canva(self,keyword,amount,email,password,usernames,boardid):
        import time
        from selenium import webdriver
        from selenium.webdriver import Keys
        from selenium.webdriver.common.by import By
        import undetected_chromedriver as uc
        import getpass
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        username = getpass.getuser()
        chrome_options.add_argument(
            f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\zaws")
        driver = uc.Chrome(chrome_options=chrome_options)
        with driver:
            driver.get('https://www.creativefabrica.com/')
            driver.maximize_window()
            key = keyword
            limit = amount
            while True:
                try:
                    driver.find_element(By.CSS_SELECTOR, '#woocommerce-product-search-field').send_keys(key)
                    break
                except:
                    continue
            while True:
                try:
                    driver.find_element(By.CSS_SELECTOR, '#woocommerce-product-search-field').send_keys(Keys.ENTER)
                    break
                except:
                    continue
            limit = int(limit) + 1
            p = 0
            for i in range(1, limit):
                p += 1
                while True:
                    try:
                        driver.find_element(By.CSS_SELECTOR,
                                            '#hits > div.masonry__item-container > div:nth-child(' + str(
                                                i) + ')').click()
                        break
                    except:
                        continue

                # specify the directory to scan
                directory = "downloads"
                time.sleep(3)
                # loop through all files in the directory
                while True:
                    try:
                        title = driver.find_element(By.CSS_SELECTOR, '#product-title').text
                        break
                    except:
                        continue

                while True:
                    try:
                        desc = driver.find_element(By.CSS_SELECTOR, '#single-product-description > p').text
                        break
                    except:
                        continue
                while True:
                    try:
                        img = driver.find_element(By.XPATH,
                                                  '//*[@id="content"]/div/div[1]/div[3]/div[1]/div/div[3]/div/div[1]/div[1]/div[1]/img').get_attribute(
                            'src')
                        break
                    except:
                        continue
                pinterest = Pinterest.Pinterest(email=email, password=password, username=usernames)
                link = shortner.short_link(img)
                pinterest.pin(boardid, img, desc, link, title)
                current_text = self.textbox.get("1.0", "end")
                if "posting logs" in current_text:
                    new_text = current_text.replace("posting logs", "")
                    self.textbox.delete("1.0", "end")
                    self.textbox.insert("1.0", new_text)
                self.textbox.insert("end",f"Image posted\n"
                                          f"Title: {title}\n"
                                          f"Link: {link}\n"
                                          f"description: {desc}")
                time.sleep(2)
                self.textbox.insert("end", "\n--------------------------\n")
                driver.back()
                if p >= 2:
                    l = p // 2
                    for i in range(1, l + 1):
                        while True:
                            try:
                                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
                                break
                            except:
                                continue
                time.sleep(2)
    def pulls(self):
        keyword = self.entry1.get()
        amount = self.entry2.get()
        import pandas as pd

        # Load the data from the Excel file
        df = pd.read_excel('accounts.xlsx')

        # Extract data from columns
        email = df.loc[0, 'Email']
        password = df.loc[0, 'Password']
        usernames = df.loc[0, 'Username']
        board = df.loc[0, 'Board(name or id)']
        board = str(board)
        self.canva(keyword,amount,email,password,usernames,board)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        pass

if __name__ == "__main__":
    def validate_only_digits(action, value_if_allowed):
        if action == '1':  # insert operation
            if value_if_allowed.isdigit():
                return True
            return False
        return True
    app = App()
    validate_cmd = app.register(validate_only_digits)
    app.mainloop()