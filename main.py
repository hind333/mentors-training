import tkinter as tk
from PIL import Image, ImageTk
import re
from datetime import datetime
from validate_email import validate_email
root = tk.Tk()
root.geometry("768x1366")
root.title("تسجيل في  Kuwait Codes")
image = Image.open("kw.jpg")
image = image.resize((1268, 766), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
name_label = tk.Label(root, text="Name:")
name_label.pack(side=tk.LEFT, padx=10, pady=10)
name_entry = tk.Entry(root, font=("Arial", 14))
name_entry.pack(side=tk.LEFT, padx=10, pady=10)
email_label = tk.Label(root, text="Email")
email_label.pack(side=tk.LEFT, padx=10, pady=10)
email_entry = tk.Entry(root,font=("Arial", 14))
email_entry.pack(side=tk.LEFT, padx=10, pady=10)
civil_id_label = tk.Label(root, text="Civil ID")
civil_id_label.pack( side=tk.LEFT ,padx=10, pady=210)
civil_id_entry = tk.Entry(root)
civil_id_entry.pack(side=tk.LEFT, padx=10, pady=10)
# gender
gender_label = tk.Label(root, text="gender")
gender_label.pack(side=tk.LEFT ,padx=10, pady=210)
#للاحتفاظ بقيمة gender
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="male", variable=gender_var, value="male")
female_radio = tk.Radiobutton(root, text="female", variable=gender_var, value="female")
male_radio.pack(side=tk.LEFT, padx=10, pady=210)
female_radio.pack(side=tk.LEFT, padx=10, pady=210)
#  للرسائل الخطأ
error_label = tk.Label(root, fg="red")
error_label.pack(side=tk.LEFT, padx=10, pady=210)
# لرسالة الشكر
thank_you_label = tk.Label(root, font=("Arial", 20, "bold"))
thank_you_label.pack(side=tk.LEFT, padx=10, pady=210)

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True
# إستخراج العمر من الرقم المدني
def extract_age(civil_id):
    year = int(civil_id[0:2])
    month = int(civil_id[2:4])
    day = int(civil_id[4:6])
    if year >= 0 and year <= 21:
        year += 2000
    else:
        year += 1900
    birthday = datetime(year, month, day)
    today = datetime.now()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    civil_id = civil_id_entry.get()
    gender = gender_var.get()
#التحقق من ID
    if len(civil_id) != 12:
        error_label.config(text="يرجى إدخال رقم مدني صحيح.")
        return
#التحقق من email
    if not validate_email(email):
        error_label.config(text="يرجى إدخال بريد إلكتروني صحيح.")
        return

    age = extract_age(civil_id)
    birthday = datetime.now().year - age
    if age < 13:
        error_label.config(text="عذراً، يجب أن تكون أكبر من 13 سنة للتسجيل في برنامج صيف Kuwait Codes.")
        return
    if age > 18:
        error_label.config(text="عذراً، هذا البرنامج مخصص للأطفال فقط!")
        return
    
    if gender == "female":
        thank_you_label.config(text=f"شكراً {name}! 😊")
    else:
        thank_you_label.config(text=f"شكراً {name}! 💙")
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(side=tk.LEFT ,padx=10, pady=10)

                              
root.mainloop()