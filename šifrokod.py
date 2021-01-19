morseovka_dict = {'A': '.-', "Á": ".-", 'B': '-...', 'C': '-.-.', "Č": "-.-.", 'D': '-..', "Ď": "-..", 'E': '.',
                  "Ě": ".", "É": ".",
                  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', "Í": "..", 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', "Ó": "---", 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', "Ř": ".-.", 'S': '...', "Š": "...", 'T': '-', "Ť": "-", 'U': '..-', "Ú": "..-",
                  "Ů": "..-", 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', "Ý": "-.--", 'Z': '--..', "Ž": "--..",
                  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '',
                  '.': '//', }  # tady je for že MEZERU nahrazuju NEMEZEROU. Tedy " ":"". Ale pořád je to bráno jako znak. Takže níže v kodu se za to hodí "/"

abeceda_dict = {"A": "1", "Á": "1", "B": "2", "C": "3", "Č": "3", "D": "4", "Ď": "4", "E": "5", "É": "5", "Ě": "5",
                "F": "6", "G": "7", "H": "8", "I": "9", "Í": "9", "J": "10", "K": "11", "L": "12", "M": "13", "N": "14",
                "O": "15", "Ó": "15", "P": "16", "Q": "17", "R": "18", "Ř": "18", "S": "19", "Š": "19", "T": "20",
                "Ť": "20", "U": "21", "Ú": "21", "Ů": "21", "V": "22", "W": "23", "X": "24", "Y": "25", "Ý": "25",
                "Z": "26", "Ž": "26", ' ': '666'
                }

abeceda_2_dict = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", "10": "J",
                  "11": "K", "12": "L", "13": "M", "14": "N", "15": "O", "16": "P", "17": "Q", "18": "R", "19": "S",
                  "20": "T", "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y", "26": "Z", ' ': '666',
                  "27": "A", "28": "B", "29": "C", "30": "D", "31": "E", "32": "F", "33": "G", "34": "H", "35": "I",
                  "36": "J", "37": "K", "38": "L", "39": "M", "40": "N", "41": "O", "42": "P", "43": "Q", "44": "R",
                  "45": "S", "46": "T", "47": "U", "48": "V", "49": "W", "50": "X", "51": "Y", "52": "Z",
                  "666": " ", "667": " ", "668": " ", "669": " ", "670": " ", "671": " ", "672": " ", "673": " ",
                  "674": " ", "675": " ", "676": " ", "677": " ", "678": " ", "679": " ", "680": " ", "681": " ",
                  "682": " ", "683": " ", "684": " ", "685": " ", "686": " ", "687": " ", "688": " ", "689": " "
    , "690": " ", "691": " ",
                  "692": " "}  # Klíče nad "666" kodují mezery mezi písmeny. Jiných hodnot ta mezera neumí nabýt.

abeceda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]


# UMÍ TO zakodovat zprávu do klasické morseovky, klasické převrácené morseovky a do morsevky se znaky zadanými uživatelem. Umí to taky posuny o zvolený počet pozic. A umí to šneka do tabulky 5x5.
# Pracujeme se šifrovací abecedou (26 znaků)
def oddelovac():  # pro přehlednost
    print("-" * 60)


# dotaz jak chci šifrovat
user_input_choice = int(input(
    "Chcete-li šifrovat klasickou morseovkou, zadejte 1, chcete-li šifrovat klasickou převrácenou morseovkou, zadejte 2, chcete-li morseovku s vlastními znaky místo čárky a tečky, zadejte 3, chcete-li šifrovat posunem, zadejte 4, chcete-li šifrovat šnekem, zadejte 5: "))  # uživatel zadá jakou chce morseovku
oddelovac()

# zadej zprávu k zakodování
user_input = input("Zadej zprávu k zakodování: ")  # user_input je ve stringu
oddelovac()
user_input_all_upper = str(user_input.upper())  # přehodit input do velkejch písmen
print(user_input_all_upper)
oddelovac()

# zašifruje klasickou morseovkou
if user_input_choice == 1:
    print("Klasická morseovka")
    oddelovac()
    for letter in user_input_all_upper:
        encoded = morseovka_dict.get(letter) + "/"
        print(encoded, end="")  # (end="") hodí výstup printu na jeden řádek
    print("//")  # přidá "//" na konec zprávy

# zašifruje klasickou převrácenou morseovkou
elif user_input_choice == 2:
    print("Klasická převrácená morseovka")
    oddelovac()
    for letter in user_input_all_upper:
        encoded = morseovka_dict.get(letter) + "/"
        encoded_4 = encoded.replace(".", "X")  # musim to převést načtyřikrát, páč na dvakrát by to nešlo.
        encoded_5 = encoded_4.replace("-", "Y")
        encoded_6 = encoded_5.replace("X", "-")
        encoded_7 = encoded_6.replace("Y", ".")
        print(encoded_7, end="")  # (end="") hodí výstup printu na jeden řádek
    print("//")  # přidá "//" na konec zprávy

# zašifruje morseovkou se změněnými znaky
# XXX tohle by ještě mohlo umět uživatelův znak místo oddělovníku
elif user_input_choice == 3:
    print("Morseovka se změněnými znaky")
    oddelovac()
    user_dash = str(input("Zadej znak místo čárky: "))
    user_dot = str(input("Zadej znak místo tečky: "))
    print("čárka je:", user_dash, "tečka je:", user_dot)
    oddelovac()
    for letter in user_input_all_upper:
        encoded = morseovka_dict.get(letter) + "/"  # přiřadí textu k zakodování znak morseovky
        encoded_2 = encoded.replace(".", user_dot)  # místo tečky hodí to co zadal uživatel jako "místo tečky"
        encoded_3 = encoded_2.replace("-", user_dash)  # místo čárky hodí to, co zadal uživatel jako "místo čárky"
        print(encoded_3, end="")  # (end="") hodí výstup printu na jeden řádek
    print("//")

# Šifruje posuny. Neumí to záporný posun. Tento je nutno řešit kladným posunem o víc.
# XXX řešení mezer mezi slovy je sice funkční ale rozhodně není elegantní... jak hezčejc?
elif user_input_choice == 4:
    print("Posun")
    oddelovac()
    user_shift_plus = int(input("Zadejte hodnotu posunu (z rozmezí 1 až 26): "))  # o kolik se to má posunout
    if user_shift_plus > 0 and user_shift_plus < 27:  # číslo posunu je větší než 0 a menší než 27, aby to program schroustal. Záporný posun je nutno řešit kladným posunem o víc.
        list_of_indexes_user_input = []
        for letter in user_input_all_upper:  # pro písmeno ve zprávě k zadokování vrátí list pořadí dle slovníku abeceda
            encoded = abeceda_dict.get(letter)  # vezmi hodnotu dle klíče ze slovníku abeceda
            list_of_indexes_user_input.append(encoded)  # tu hodnotu přidej na konec listu
        list_of_indexes_user_input = list(map(int, list_of_indexes_user_input))  # přehodí list stringů na list integerů

        # přičíst k původnímu pořadí posun zadaný uživatelem
        list_of_indexes_aded = []
        for i in range(len(list_of_indexes_user_input)):
            list_of_indexes_user_input[i] += user_shift_plus  # k indexu [i] přičti číslo zvolené uživatelem

        oddelovac()
        list_of_indexes_user_input = list(map(str,
                                              list_of_indexes_user_input))  # musim nazpátek z integeru udělat string, páč v dict je to jako string.

        # Ze zakodovanýho pořadí na písmena. Mezery mezi slovama sou řešený 26 možnýma znakama pro mezeru ve slovníku. To není úplně elegantní... Jak to udělat jinak?
        for letter in list_of_indexes_user_input:
            encoded_8 = abeceda_2_dict.get(letter)
            print(encoded_8, end="")
    else:
        print("Posun o neplatnou hodnotu. Zadejte znovu.")

# šifruje šneka od prostředka. PRO tabulku 3x3, 4x4, 5x5 nebo 6x6.
    # možnost kdy zadám jiný počet písmen a další písmena se mi doplní náhodně sami ???
elif user_input_choice == 5:
    print("Šnek")
    oddelovac()
    user_input_all_upper_no_spaces = user_input.replace(" ", "")  # zbaví string mezer
    user_input_all_upper_no_spaces_all_upper = user_input_all_upper_no_spaces.upper()
    muj_list = list(user_input_all_upper_no_spaces_all_upper)

    tabulka_snek_6na6 = [[],
                         [],
                         [],
                         [],
                         [],
                         []]
# Šnek 3X3
    if len(muj_list) == 9:
        # Smyčky, které přiřazují písmena na pozice. Jedna smyčka pro jeden řádek.
        prvni_radek = [4, 3, 2]  # z tohodle beru čísla jako indexy
        i = 0
        for prvek in (muj_list[a] for a in
                      prvni_radek):  # (muj_list[a]for a in prvni_tri) - říká který znaky tisknout pomocí indexů
            i = i + 1
            if i > 3:  # pokud je i > 3, neproved zbytek kodu
                continue  # CONTINUE znamená VRAT SE NA ZAČÁTEK smyčky
            tabulka_snek_6na6[0].insert(i, prvek)

        druhy_radek = [5, 0, 1]
        j = 0
        for prvek in (muj_list[a] for a in druhy_radek):
            j = j + 1
            if j > 3:
                continue
            tabulka_snek_6na6[1].insert(j, prvek)

        treti_radek = [6, 7, 8]
        k = 0
        for prvek in (muj_list[a] for a in treti_radek):
            k = k + 1
            if k > 3:
                continue
            tabulka_snek_6na6[2].insert(k, prvek)

        # smyčka která vypisuje
        for prvek in tabulka_snek_6na6:
            for x in prvek:
                print(x + "  ", end="")  # + "  ": přidává mezery, end="" zarovná na řádek
            print()

# Šnek 4x4
    elif len(muj_list) == 16:
        # Smyčky, které přiřazují písmena na pozice. Jedna smyčka pro jeden řádek.
        prvni_radek = [15,14,13,12]  # z tohodle beru čísla jako indexy
        i = 0
        for prvek in (muj_list[a] for a in prvni_radek):  # (muj_list[a]for a in prvni_tri) - říká který znaky tisknout pomocí indexů
            i = i + 1
            if i > 4:  # pokud je i > 3, neproved zbytek kodu
                continue  # CONTINUE znamená VRAT SE NA ZAČÁTEK smyčky
            tabulka_snek_6na6[0].insert(i, prvek)

        druhy_radek = [4,3,2,11]
        j = 0
        for prvek in (muj_list[a] for a in druhy_radek):
            j = j + 1
            if j > 4:
                continue
            tabulka_snek_6na6[1].insert(j, prvek)

        treti_radek = [5,0,1,10]
        k = 0
        for prvek in (muj_list[a] for a in treti_radek):
            k = k + 1
            if k > 4:
                continue
            tabulka_snek_6na6[2].insert(k, prvek)

        ctvrty_radek = [6, 7, 8, 9]
        l= 0
        for prvek in (muj_list[a] for a in ctvrty_radek):
            l = l + 1
            if l > 4:
                continue
            tabulka_snek_6na6[3].insert(l, prvek)

        # smyčka která vypisuje
        for prvek in tabulka_snek_6na6:
            for x in prvek:
                print(x + "  ", end="")  # + "  ": přidává mezery, end="" zarovná na řádek
            print()

# Šnek 5x5
    elif len(muj_list) == 25:
        # Smyčky, které přiřazují písmena na pozice. Jedna smyčka pro jeden řádek.
        prvni_radek = [16, 15, 14, 13, 12]  # z tohodle beru čísla jako indexy
        i = 0
        for prvek in (muj_list[a] for a in prvni_radek):  # (muj_list[a]for a in prvni_tri) - říká který znaky tisknout pomocí indexů
            i = i + 1
            if i > 5:  # pokud je i > 4, neproved zbytek kodu
                continue  # CONTINUE znamená VRAT SE NA ZAČÁTEK smyčky
            tabulka_snek_6na6[0].insert(i, prvek)

        druhy_radek = [17, 4, 3, 2, 11]
        j = 0
        for prvek in (muj_list[a] for a in druhy_radek):
            j = j + 1
            if j > 5:
                continue
            tabulka_snek_6na6[1].insert(j, prvek)

        treti_radek = [18, 5, 0, 1, 10]
        k = 0
        for prvek in (muj_list[a] for a in treti_radek):
            k = k + 1
            if k > 5:
                continue
            tabulka_snek_6na6[2].insert(k, prvek)

        ctvrty_radek = [19, 6, 7, 8, 9]
        l = 0
        for prvek in (muj_list[a] for a in ctvrty_radek):
            l = l + 1
            if l > 5:
                continue
            tabulka_snek_6na6[3].insert(l, prvek)

        paty_radek = [20, 21, 22, 23, 24]
        m = 0
        for prvek in (muj_list[a] for a in paty_radek):
            m = m + 1
            if m > 5:
                continue
            tabulka_snek_6na6[4].insert(m, prvek)

        for prvek in tabulka_snek_6na6:
            for x in prvek:
                print(x + "  ", end="")  # + "  ": přidává mezery, end="" zarovná na řádek
            print()

# Šnek 6x6
    elif len(muj_list) == 36:
        prvni_radek = [35, 34, 33, 32, 31, 30]  # z tohodle beru čísla jako indexy
        i = 0
        for prvek in (muj_list[a] for a in prvni_radek):  # (muj_list[a]for a in prvni_tri) - říká který znaky tisknout pomocí indexů
            i = i + 1
            if i > 6:  # pokud je i > 4, neproved zbytek kodu
                continue  # CONTINUE znamená VRAT SE NA ZAČÁTEK smyčky
            tabulka_snek_6na6[0].insert(i, prvek)

        druhy_radek = [16, 15, 14, 13, 12, 29]
        j = 0
        for prvek in (muj_list[a] for a in druhy_radek):
            j = j + 1
            if j > 6:
                continue
            tabulka_snek_6na6[1].insert(j, prvek)

        treti_radek = [17, 4, 3, 2, 11, 28]
        k = 0
        for prvek in (muj_list[a] for a in treti_radek):
            k = k + 1
            if k > 6:
                continue
            tabulka_snek_6na6[2].insert(k, prvek)

        ctvrty_radek = [18, 5, 0, 1, 10, 27]
        l = 0
        for prvek in (muj_list[a] for a in ctvrty_radek):
            l = l + 1
            if l > 6:
                continue
            tabulka_snek_6na6[3].insert(l, prvek)

        paty_radek = [19, 6, 7, 8, 9, 26]
        m = 0
        for prvek in (muj_list[a] for a in paty_radek):
            m = m + 1
            if m > 6:
                continue
            tabulka_snek_6na6[4].insert(m, prvek)

        sesty_radek = [20, 21, 22, 23, 24, 25]
        n = 0
        for prvek in (muj_list[a] for a in sesty_radek):
            n = n + 1
            if n > 6:
                continue
            tabulka_snek_6na6[5].insert(m, prvek)

        for prvek in tabulka_snek_6na6:
            for x in prvek:
                print(x + "  ", end="")  # + "  ": přidává mezery, end="" zarovná na řádek
            print()

    else:
        print("Vaše zprává má:", len(muj_list), "Znaků. Upravte zprávu tak, aby měla 9, 16, 25 nebo 36 znaků.")

# všechny ostatní případy
else:
    print("Nepovolený znak. Zadejte 1, 2, 3, 4 nebo 5")
