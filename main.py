import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.geometry("800x500")

def click_button():

    boy = float(entry1.get())
    kilo = float(entry2.get())

    sonuc = float(kilo / (boy/100)**2)

    if sonuc > 10 and sonuc < 18.15:
        label4 = tkinter.Label(text="Zayıf")
        label4.pack()

    elif sonuc >= 18.15 and sonuc < 24.9:
        label5 = tkinter.Label(text="Sağlıklı")
        label5.pack()
    elif sonuc >=24.9 and sonuc <29.9:
        label6 = tkinter.Label(text="Kilolu")
        label6.pack()

    else:
        label7 = tkinter.Label(text="Sağlıksız")
        label7.pack()



#Boy
label1 = tkinter.Label(text="Boyunuzu Giriniz(cm)", font=('Arial', 20, 'italic'))
label1.pack()

entry1 = tkinter.Entry(width=20)
entry1.pack()

#Kilo
label2 = tkinter.Label(text="Kilonuzu Giriniz(kg)", font=('Arial', 20, 'italic'))
label2.pack()

entry2 = tkinter.Entry(width=20)
entry2.pack()

#Hesapla
button1 = tkinter.Button(text="Hesapla", width=10, height=5, bg="blue", command=click_button)
button1.pack()

label3 = tkinter.Label(text="Beden Kitle İndeksiniz")
label3.pack()




window.mainloop()
