
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
        "en": "You choose English!",
        "cs": "Vybral jsi cesky jazyk, dobra volba!"
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
        "en": "Sorry, you missed"
    },
    "hit": {
        "cs": "Nekecej, zasah!",
        "en": "You sunk my ship :-("
    },
    "over": {
        "cs": "Konec hry!",
        "en":"Game over!"
            },
    "date":{
        "cs": "Dneska je:",
        "en": "Today is:"
    },
    "time":{
        "cs": "Čas je:",
        "en": "Time is:"
    },
}
def print_localization(lang, text):

    if text in TEXT.keys():
        print(TEXT[text][lang])
    else:
        print(f"NO LOCALIZATION for {text}")