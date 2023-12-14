
LANG_EN = "en"
LANG_CS = "cs"

SUPPORTED_LANG = {LANG_EN, LANG_CS}

TEXT = {
    "welcome.text" : {
        "en": "Welcome", 
        "cs": "Vítej"
    },
    "language_sel": {
          "en": "Choose language English, or Czech, en = English, cs = Czech.",
          "cs": "Vyber si jazyk, cs= Cestina, en = Anglictina."
    },
    "selected" : {
        "en": "You choose English!",
        "cs": "Vybral jsi cesky jazyk."
    },
    "bad_lang" : {
        "en": "You choose bad language, choose other please.",
         "cs": "Vybral jsi špatný jazyk, vyber prosím jiný."
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
        "cs": "Konec hry, prohral jsi!",
        "en":"Game over, you lost!"
            },
    "date":{
        "cs": "Dneska je:",
        "en": "Today is:"
    },
    "time":{
        "cs": "Čas je:",
        "en": "Time is:"
    },
     "wining":{
        "cs": "Gratuluju, vyhrál jsi!",
        "en": "CongratZ, you won!"
    }
}
def print_localization(lang, text):

    if text in TEXT.keys():
        print(TEXT[text][lang])
    else:
        print(f"NO LOCALIZATION for {text}")