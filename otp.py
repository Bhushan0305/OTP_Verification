import math                  #mathematical
import random                # to generate random number
import smtplib               # to send emails using SMTP

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
    
    otp = OTP + " is your OTP"
    msg = otp
    
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("Your Gmail Account", "You app password")

emailid = input("enter your email:")
s.sendmail('Your gmail ID ',emailid,msg)

a = input("Enter your OTP>>:")
if a==OTP:
    print("Verified")
else:
    print("Please Check Your OTP again")
