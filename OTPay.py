hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter Rate: ")
r = float(rate)

if(h <= 40):
    gp = h*r
elif(h > 40):
    oth = h - 40
    otp = (oth*1.5)*r
    rp = (h-oth)*r
    gp = otp+rp   

print(gp)

    
