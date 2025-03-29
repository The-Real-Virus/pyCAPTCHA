import os
import string
from io import BytesIO
from random import randint
import tkinter as tk
from tkinter import ttk, messagebox
from captcha.image import ImageCaptcha

# Function to display banner
def show_banner():
    banner = r"""
                       ______
                    .-"      "-.
                   /  *ViRuS*   \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(_0_/\_0_)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/                                    \_)
 ____________________________________________________
 ----------------------------------------------------        
        #  pyCAPTCHA
        #  Author : The-Real-Virus
        #  https://github.com/The-Real-Virus
 ____________________________________________________
 ----------------------------------------------------
"""
    print(banner)

# Show banner at script startup
show_banner()

# Ask user for input
choice = input("\nPress 'y' to continue or 'n' to exit: ").strip().lower()

if choice == 'n':
    print("\nExiting the script. Goodbye!")
    exit()
elif choice == 'y':
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear screen on Linux/Mac ('clear') or Windows ('cls')
else:
    print("\nInvalid choice. Exiting the script.")
    exit()

def logo():
    logo = r"""
██████╗ ██╗   ██╗      ██████╗ █████╗ ██████╗ ████████╗ ██████╗██╗  ██╗ █████╗ 
██╔══██╗╚██╗ ██╔╝     ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔══██╗
██████╔╝ ╚████╔╝█████╗██║     ███████║██████╔╝   ██║   ██║     ███████║███████║
██╔═══╝   ╚██╔╝ ╚════╝██║     ██╔══██║██╔═══╝    ██║   ██║     ██╔══██║██╔══██║
██║        ██║        ╚██████╗██║  ██║██║        ██║   ╚██████╗██║  ██║██║  ██║
╚═╝        ╚═╝         ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                                                           
"""
    print(logo)

# Get script directory to make font paths dynamic
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS = [
    os.path.join(BASE_DIR, 'ChelseaMarketsr.ttf'),
    os.path.join(BASE_DIR, 'DejaVuSanssr.ttf')
]

class CaptchaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAPTCHA Verification")
        self.root.geometry("350x300")
        self.root.resizable(False, False)
        
        self.image_captcha = ImageCaptcha(fonts=FONTS)
        self.captcha_text = ""
        
        # UI Elements
        self.label_title = ttk.Label(root, text="Enter the CAPTCHA", font=("Arial", 12, "bold"))
        self.label_title.pack(pady=10)
        
        self.image_label = ttk.Label(root)
        self.image_label.pack()
        
        self.entry_var = tk.StringVar()
        self.entry_captcha = ttk.Entry(root, textvariable=self.entry_var, font=("Arial", 14))
        self.entry_captcha.pack(pady=5)
        
        self.button_submit = ttk.Button(root, text="Submit", command=self.verify_captcha)
        self.button_submit.pack(pady=5)
        
        self.button_refresh = ttk.Button(root, text="Refresh", command=self.generate_captcha)
        self.button_refresh.pack()
        
        self.generate_captcha()
        
    def generate_captcha(self):
        """Generates a new CAPTCHA image"""
        self.captcha_text = str(randint(100000, 999999))
        self.image_captcha.write(self.captcha_text, "captcha.png")
        self.update_image()
        
    def update_image(self):
        """Updates the CAPTCHA image in the UI"""
        self.captcha_photo = tk.PhotoImage(file="captcha.png")
        self.image_label.configure(image=self.captcha_photo)
        
    def verify_captcha(self):
        """Validates user input"""
        user_input = self.entry_var.get().strip()
        
        if not user_input.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter numbers only!")
            return
        
        if user_input == self.captcha_text:
            messagebox.showinfo("Success", "CAPTCHA Verified!")
        else:
            messagebox.showerror("Error", "Incorrect CAPTCHA! Generating a new one.")
            self.generate_captcha()
        
        self.entry_var.set("")  # Clear input field

# Run Application
if __name__ == "__main__":
    logo()
    root = tk.Tk()
    app = CaptchaApp(root)
    root.mainloop()
