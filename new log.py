import sqlite3
import customtkinter as ctk
from PIL import Image, ImageFilter
from tkcalendar import Calendar
import datetime

sky2=Image.open("images/sky2.jpg")
sky2p=sky2.resize((1400, 800)).filter(ImageFilter.GaussianBlur(radius=3))

def frame_crop_log(x, y, w, h):
    return ctk.CTkImage(dark_image=sky2p.crop((x+15, y+180, x+15+w,y+180+ h)),size=(w,h))

class main(ctk.CTk):
    def __init__(self):
        super().__init__()

        window_width = 1400
        window_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        im = ctk.CTkImage(dark_image=sky2, size=(1400, 800))

        self.logo = ctk.CTkLabel(self, image=im, text="")
        self.logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.cal = Calendar(self, selectmode="day", date_pattern="dd-mm-yyyy", year=2026, month=1, day=1)
        self.cal.place(x=15, y=20)
        self.cal.bind("<<CalendarSelected>>")

        self.frame = ctk.CTkFrame(self, border_color="#00F0FF", border_width=5, height=560, width=520,)
        self.frame.place(x=15, y=180)

        self.logo = ctk.CTkLabel(self.frame, image=frame_crop_log(0, 0, 520, 560), text="")
        self.logo.place(x=5.5, y=5.5, relwidth=0.978, relheight=0.983)

        self.time_from = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 10, 160, 30),text="Time(From)                  :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.time_from.place(x=10, y=10)
        self.time_from_inputx = ctk.CTkEntry(self.frame, width=300, height=30, placeholder_text="Ex-20:30")
        self.time_from_inputx.place(x=200, y=10)

        self.time_to = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 60, 160, 30),text="Time(To)                     :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.time_to.place(x=10, y=60)
        self.time_to_inputx = ctk.CTkEntry(self.frame, width=300, height=30, placeholder_text="Ex-20:30")
        self.time_to_inputx.place(x=200, y=60)

        self.lp = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 110, 160, 30),text="Appx. Light Pollution :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.lp.place(x=10, y=110)
        self.lp.inputcb = ctk.CTkComboBox(self.frame, values=["0","1","2","3","4","5","6","7","8","9"], width=300)
        self.lp.inputcb .place(x=200, y=110)
        self.lp.inputcb .set("Select Bortle Level")

        self.weather = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 160, 160, 30),text="Weather                       :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.weather.place(x=10, y=160)
        self.weather_inputcb = ctk.CTkComboBox(self.frame, values=[], width=300)
        self.weather_inputcb.place(x=200, y=160)
        self.weather_inputcb.set("Select Weather Condition")

        self.star_name = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 210, 160, 30),text="Star Name                   :", font=("Segoe UI", 15,"bold"), anchor="w", text_color="#F0F4F8")
        self.star_name.place(x=10, y=210)
        self.star_name_inputcb = ctk.CTkComboBox(self.frame, values=[], width=300)
        self.star_name_inputcb.place(x=200, y=210)
        self.star_name_inputcb.set("Enter Star Nmae")

        self.hip_id = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 260, 160, 30),text="HIP ID                         :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.hip_id.place(x=10, y=260)
        self.hip_id_inputx = ctk.CTkEntry(self.frame, width=300, height=30, placeholder_text="Enter HIP ID")
        self.hip_id_inputx.place(x=200, y=260)

        self.direction = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 310, 160, 30),text="Direction                   :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.direction.place(x=10, y=310)
        self.direction_inputcd = ctk.CTkComboBox(self.frame, values=["N", "NE", "E", "SE","S","SW","W","NW","Zenith"], width=300)
        self.direction_inputcd.place(x=200, y=310)
        self.direction_inputcd.set("Select Direction")

        self.brightness = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(10, 360, 160, 30),text="Brightness                  :", font=("Segoe UI", 15, "bold"), anchor="w", text_color="#F0F4F8")
        self.brightness.place(x=10, y=360)
        self.brightness_inputcb = ctk.CTkComboBox(self.frame, values=["High", "Medium", "low", "Faint"], width=300)
        self.brightness_inputcb.place(x=200, y=360)
        self.brightness_inputcb.set("Select Brightness")

        self.add = ctk.CTkButton(self.frame, text="Add", border_color="black", fg_color="blue", width=120,command=self.alu)
        self.add.place(x=100, y=430)

        self.save = ctk.CTkButton(self.frame, text="Save", border_color="black", fg_color="blue", width=120)
        self.save.place(x=300, y=430)

        self.moto = ctk.CTkLabel(self.frame, width=160, height=30, image=frame_crop_log(150, 500, 160, 30),text="Keep Looking Up!!!", font=("Segoe UI", 18, "bold"), anchor="w",text_color="#F0F4F8")
        self.moto.place(x=180, y=500)

        self.textbox=ctk.CTkTextbox(self,width=300, height=100,border_color="#00F0FF",border_width=5)
        self.textbox.place(x=1070,y=15)
        self.textbox.insert("end","Added Stars\n")
        self.textbox.configure(state="disabled")

    def alu(self):
        print(int(self.hip_id_inputx.get()))





ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app=main()
app.mainloop()