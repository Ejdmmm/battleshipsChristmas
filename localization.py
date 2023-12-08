LANG_EN = "en"
LANG_CS = "cs"

SUPPORTED_LANG = {LANG_CS, LANG_EN}

TEXT = {
    "welcome.text" : {
        "en": "welcome"
    },
    "language_sel": {
        "en": "Choose language, en = English, cs = Czech",
    },
    "selected" : {
        "cs": "Vybral jsi cesky jazyk, dobra volba!",
        "en": "You choose English, you traitor!"
    },
    "bad_lang" : {
        "en": "You choose bad language, choose other please."
    },
    "board_size" : {
        "cs": "Vyber velikost pole, na kterem chces hrat.",
        "en": "Choose board size."
    },
    "bad_type_choose" : {
        "cs": "Vybral jsi spatny typ.",
        "en": "You choode bad type."

    }, 
    "enter_x" : {
        "cs": "Vyber x-ovou souradnici.",
        "en": "Choose x coordinate."

    }, 
    "enter_y" : {
        "cs": "Vyber y souradnici.",
        "en": "Choose y coordinate."
    },
    "miss": {
        "cs": "Netrefil ses vole",
        "eng": "Sorry you missed",
    },
    "hit": {
        "cs": "Nekecej, zasah!",
        "eng": "You sunk my ship :-(",
    }
}
def print_localization(lang, text):
    if text in TEXT.keys():
        print(TEXT[text][lang])
    else:
        print(f"NO LOCALIZATION for {text}")