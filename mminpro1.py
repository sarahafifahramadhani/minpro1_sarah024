artwork = [
    ["Penangkapan Diponegoro", "Raden Saleh", "1857"],
    ["Camile Monet on her Deathbed", "Oscar Claude Monet", "1879"],
    ["Roots", "Frida Kahlo", "1943"],
    ["The Persistence of Memory", "Salvador Dali", "1931"],
    ["Ayam Tarung", "Affanfi Koesoema", "1979"]
]

while True:
    print("=" * 57)
    print("\n               WELCOME TO ART GALLERY             ")
    print("=" * 57)
    print("\n                       -Menu-                    ")
    print("1. View Art")
    print("2. Add Art")
    print("3. Change Art Data")
    print("4. Delete Art Data")
    print("5. Home")
    print("=" * 57)

    pil_menu = input("Select: ")
# view data seni
    print("=" * 57)
    if pil_menu == "1":
        print("\n=              WELCOME TO ART GALLERY                   =")
        print("=" * 57)
        if len(artwork) == 0:
            print("There is no Art data found. Please add an artwork first")
        else:
            for i in range(len(artwork)):
                print(i + 1, artwork[i][0], ",", artwork[i][1], "-", artwork[i][2])
# tambah data seni
    elif pil_menu == "2":
        j_m = input("Name of the Painting: ")
        a_m = input("Artist: ")
        t_m = input("Year Created: ")

        artwork.append([j_m, a_m, t_m])
        print("Art added succesfully!")
# ubah data seni
    elif pil_menu == "3":
        if len(artwork) == 0:
            print("There is no Art data found. Please add an artwork first")
        else:
            print("\n=              WELCOME TO ART GALLERY                   =")
            for i in range(len(artwork)):
                print(str(i + 1), artwork[i][0], ",", artwork[i][1], "-", artwork[i][2])

            no_m = int(input("Select number of art you want to change: "))

            if 1 <= no_m <= len(artwork):
                j_m = input("New Painting: ")
                a_m = input("Artist Name: ")
                t_m = input("Year Created: ")

                artwork[no_m - 1] = [j_m, a_m, t_m]
                print("\nArt updated succesfully!")
            else:
                print("Data not found")
# hapus
    elif pil_menu == "4":
            if len(artwork) == 0:
                print("There is no Art data found. Please add an artwork first")
            else:
                print("\n=              WELCOME TO ART GALLERY                   =")
                for i in range(len(artwork)) :
                    print(i + 1, artwork[i][0], ",", artwork[i][1], "-", artwork[i][2])

                no_m = int(input("Select the number of art you want to delete: "))
                if 1 <= no_m <= len(artwork):
                        hps = artwork.pop(no_m - 1)
                        print("Art delete: ", hps)
                else:
                        print("\nThere is no Art data found. Please add an artwork first")
# exit
    elif pil_menu == "5":
        print("Thankyou!")
        break
    else:
        print("System error. Try again later")