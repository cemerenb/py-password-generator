import random

liste = ("A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G",
         "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m",
         "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T",
         "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "~", "`", "!", "@", "#",
         "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|",
         ":", ";", '"', "'", "<", ",", ">", ".", "?", "/", "\\")
liste_lower = ("a", "b", "c", "d", "e", "f",
               "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z")
liste_upper = ("A", "B", "C", "D", "E", "F", "G",
               "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T",
               "U", "V", "W", "X", "Y", "Z")
liste_number = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

liste_spec = ("~", "`", "!", "@", "#",
              "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|",
              ":", ";", '"', "'", "<", ",", ">", ".", "?", "/", "\\")


def func():
    global lower, upper, number, spec
    lower = 0
    upper = 0
    number = 0
    spec = 0
    i_1 = random.choice(liste)
    i_2 = random.choice(liste)
    i_3 = random.choice(liste)
    i_4 = random.choice(liste)
    i_5 = random.choice(liste)
    i_6 = random.choice(liste)
    i_7 = random.choice(liste)
    i_8 = random.choice(liste)
    i_9 = random.choice(liste)
    i_10 = random.choice(liste)

    if i_1 in liste_lower:
        lower = 1
    if i_1 in liste_upper:
        upper = 1
    if i_1 in liste_number:
        number = 1
    if i_1 in liste_spec:
        spec = 1

    if i_2 in liste_lower:
        lower = 1
    if i_2 in liste_upper:
        upper = 1
    if i_2 in liste_number:
        number = 1
    if i_2 in liste_spec:
        spec = 1

    if i_3 in liste_lower:
        lower = 1
    if i_3 in liste_upper:
        upper = 1
    if i_3 in liste_number:
        number = 1
    if i_3 in liste_spec:
        spec = 1

    if i_4 in liste_lower:
        lower = 1
    if i_4 in liste_upper:
        upper = 1
    if i_4 in liste_number:
        number = 1
    if i_4 in liste_spec:
        spec = 1

    if i_5 in liste_lower:
        lower = 1
    if i_5 in liste_upper:
        upper = 1
    if i_5 in liste_number:
        number = 1
    if i_5 in liste_spec:
        spec = 1

    if i_6 in liste_lower:
        lower = 1
    if i_6 in liste_upper:
        upper = 1
    if i_6 in liste_number:
        number = 1
    if i_6 in liste_spec:
        spec = 1

    if i_7 in liste_lower:
        lower = 1
    if i_7 in liste_upper:
        upper = 1
    if i_7 in liste_number:
        number = 1
    if i_7 in liste_spec:
        spec = 1

    if i_8 in liste_lower:
        lower = 1
    if i_8 in liste_upper:
        upper = 1
    if i_8 in liste_number:
        number = 1
    if i_8 in liste_spec:
        spec = 1

    if i_9 in liste_lower:
        lower = 1
    if i_9 in liste_upper:
        upper = 1
    if i_9 in liste_number:
        number = 1
    if i_9 in liste_spec:
        spec = 1

    if i_10 in liste_lower:
        lower = 1
    if i_10 in liste_upper:
        upper = 1
    if i_10 in liste_number:
        number = 1
    if i_10 in liste_spec:
        spec = 1

    if lower == 1 and upper == 1 and number == 1 and spec == 1:
        print("\n")
        print("-------------------------------------------")
        print("\t\t" + i_1, end="")
        print(i_2, end="")
        print(i_3, end="")
        print(i_4, end="")
        print(i_5, end="")
        print(i_6, end="")
        print(i_7, end="")
        print(i_8, end="")
        print(i_9, end="")
        print(i_10)
        print("-------------------------------------------")
        print("\n")
        main()
    else:
        func()


def main():
    print("Şifre üretmek için Y")
    data = input("Çıkış için N\n")
    if data == "Y" or data == "y":
        func()
    elif data == "N" or data == "n" :
        exit()
    else:
        print("Yanlış veri girişi")
        main()


if __name__ == '__main__':
    main()
