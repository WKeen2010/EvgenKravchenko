a = input("Привіт, як тебе звати?  ")
print("Радий понайомитись, " + a)

b = input("Як у тебе справи? ")
if b == "Добре":
    print("О, у мене теж!")

elif b == "Погано":
    c = input("Оу-у, а чому? ")
    print("Я, впевнений, ти все виправиш.")

else:
    print("Е-е, повтори, будь ласка.")

    b = input("Як у тебе справи? ")
    if b == "Добре":
        print("О, у мене теж!")

    elif b == "Погано":
        c = input("Оу-у, а чому? ")
        print("Я, впевнений, ти все виправиш.")

    else:
        print("Е-е, повтори, будь ласка.")

        b = input("Як у тебе справи? ")
        if b == "Добре":
            print("О, у мене теж!")

        elif b == "Погано":
            c = input("Оу-у, а чому? ")
            print("Я, впевнений, ти все виправиш.")

a = input("Тоді пока?")
print(a)