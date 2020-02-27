
# první funkce která se bude hodit
def which_text(text_index):
    if text_index == 1:
        selected_text = TEXTS[0]
    elif text_index == 2:
        selected_text = TEXTS[1]
    else:
        selected_text = TEXTS[2]

    return selected_text

# druhá funkce která se bude hodit
def oddelovac():
    print ("-"*60)

# TEXTS je v listu... a v něm je to string
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# greetings
print ("Hello user. Lets analyze some texts.")
oddelovac()

# pristup
security = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user_input_username = input ("Insert username: ")
user_input_password = input ("Insert password: ")

# rozhodni zda username a password sedí k sobě
if security.get(user_input_username) != user_input_password:
    print ("Login failed")
else:
    print ("Login succefull")
oddelovac()

# Uživatel vybere který text chce analyzovat
print ("We have 3 text to analyze")
user_insert_number_2 = input ("Insert number from 1 to 3: ")
user_insert_number = int(user_insert_number_2) # neudělám-li z toho integer, funkce to neschroustá
oddelovac()

text = which_text(user_insert_number) # funkce "which text" přiřadí dle čísla zadaného uživatelem text k zanalyzování

# úprava stringu: Zbavím se znaků, který mi v tom dělaj bordel.
text = text.replace("\n", " ") # nahrazuju zalomení řádku mezerou
text = text.replace(",", " ") # nahrazuju čárku mezerou
text = text.replace(".", " ") # nahrazuju tečku mezerou
text = text.split()

# 1) celkový počet slov
print("Celkový počet slov je: ", (len(text)))

# 2) počet slov začínajících velkým písmenem
list_words_starts_uppercase = []
for word in text:
    if word[0].isupper():
        list_words_starts_uppercase.append(word)
print("Počet slov začínajících velkým písmen je: ", (len(list_words_starts_uppercase)))

# 3) počet slov složených jen z velkých písmen
list_words_all_uppercase = []
for word in text:
    if word.isupper():
        list_words_all_uppercase.append(word)
print("Počet slov složených jen z velkých písmen je: ", (len(list_words_all_uppercase)))

# 4) počet slov která jsou celé z malých písmen
list_words_all_lovercase = []
for word in text:
    if word.islower():
        list_words_all_lovercase.append(word)
print("Počet slov, která jsou zcela složena z malých písmen je: ", (len(list_words_all_lovercase)))

# 5) počet slov jen z číslic
list_words_only_numeric = []
for word in text:
    if word.isnumeric():
        list_words_only_numeric.append(int(word))
print("Počet slov složených jen z číslic je: ", (len(list_words_only_numeric)))

# 6) bar chart depicting the frequencies of word lengths
list_words_length = []
for word in text: # smyčka spočítá délku slov listu a vyhodí to novej list s délkama slov
    word_length = len(word)
    list_words_length.append(word_length)
oddelovac()

# no a teď si to spočítáme.... tahle magořina musí jít nějak jinak....!!! JAK?
# a mělo by jít nějak strojově říct kolikapísmenný slovo je nejdelší a tím končit ! JAK?
print ("GRAF:")
lenght_one = list_words_length.count(1)
lenght_two = list_words_length.count(2)
lenght_three = list_words_length.count(3)
lenght_four = list_words_length.count(4)
lenght_five = list_words_length.count(5)
lenght_six = list_words_length.count(6)
lenght_seven = list_words_length.count(7)
lenght_eight = list_words_length.count(8)
lenght_nine = list_words_length.count(9)
lenght_ten = list_words_length.count(10)
lenght_eleven = list_words_length.count(11)
lenght_twelve = list_words_length.count(12)
lenght_13 = list_words_length.count(13)
print("1)", "*" *(lenght_one), (lenght_one))
print("2)", "*" *(lenght_two), (lenght_two))
print("3)", "*" *(lenght_three), (lenght_three))
print("4)", "*" *(lenght_four), (lenght_four))
print("5)", "*" *(lenght_five), (lenght_five))
print("6)", "*" *(lenght_six), (lenght_six))
print("7)", "*" *(lenght_seven), (lenght_seven))
print("8)", "*" *(lenght_eight), (lenght_eight))
print("9)", "*" *(lenght_nine), (lenght_nine))
print("10)", "*" *(lenght_ten), (lenght_ten))
print("11)", "*" *(lenght_eleven), (lenght_eleven))
print("12)", "*" *(lenght_twelve), (lenght_twelve))
print("13)", "*" *(lenght_13), (lenght_13))
oddelovac()

# 7) sum of all the numeric "words" in the given text
print("Součet hodnot slov vyjádřených čísly je: ", (sum(list_words_only_numeric)))


