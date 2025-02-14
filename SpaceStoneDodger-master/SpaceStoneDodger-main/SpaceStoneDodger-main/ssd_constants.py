# pylint: disable=no-member

# SpaceStoneDodger: Constants database
import pygame, os, json
from collections import defaultdict


# HELPER FUNCTIONS
# ----------------

def load_image(asset_folder: str, filename: str) -> pygame.Surface:
    """ Error handling image loading function """
    fullname = os.path.join(asset_folder, filename)
    try:    
        return pygame.image.load(fullname)
    except Exception as message:
        print("Cannot load image:", filename)
        raise SystemExit(message)


def pressed(direction: str, pressed_key: list) -> bool:
    """ Returns if one of the corresponding key of a direction is been pressed """
    return any( (pressed_key[binding] for binding in KEYBINDINGS[direction]) )


def get_text(text_db_id: str) -> str:
    """ Returns a string from the database based on provided id """
    return TextDB.get_text(text_db_id)


def set_text_db(chosen_language: dict) -> None:
    """ Allows to set a language as the current """
    TextDB.set_text_db(chosen_language)


def get_every_languages() -> list():
    """ Returns a list with every language dictionaries """
    filelist = [langfile for langfile in os.listdir(TRANSLATIONS_FOLDER)
                if langfile.endswith(".json")]

    langlist = []
    for langfile in filelist:
        fullpath = os.path.join(TRANSLATIONS_FOLDER, langfile)
        with open(fullpath, "r",encoding='UTF-8') as myfile:
            this_lang = json.load(myfile)
            # Every file NEEDS to have LANGUAGE key
            if this_lang.get("LANGUAGE", None):
                langlist.append(this_lang)

    return langlist





# CONSTANTS LIST
# --------------

# Game Parameters
FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500

STARS_SPEED = 2
STAR_SPRITE_RADIUS = 1

ASTEROID_STARTING_MIN_SPEED = 3
ASTEROID_STARTING_MAX_SPEED = 8

BOOST_SPEED_MODIFIER = 2

PLAYER_SHIP_SPEED = 5 # in PIXELS
PLAYER_STARTING_MAX_HEALTH = 3 # in PIXELS
PLAYER_REPAIR_TIME = 5 # how many SECONDS the player's ship takes for fully repairing
PLAYER_INVULNERABILITY_DURATION = 3 # how many SECONDS the player's ship invulnerability lasts

POWER_UP_SPEED = 3



# Key Bindings
KEYBINDINGS = {
    "UP": (
        pygame.K_w,
        pygame.K_UP
    ),
    "DOWN": (
        pygame.K_s,
        pygame.K_DOWN
    ),
    "LEFT": (
        pygame.K_a,
        pygame.K_LEFT
    ),
    "RIGHT": (
        pygame.K_d,
        pygame.K_RIGHT
    ),
    "SPACE": (
        pygame.K_SPACE,
    ),
    "P": (
        pygame.K_p,
    ),
    "M": (
        pygame.K_m,
    ),
    "T": (
        pygame.K_t,
    ),
    "Z": (
        pygame.K_z,
    ),
    "I": (
        pygame.K_i,
    ),
    "R":(
        pygame.K_r,
    )
}


# Assets Constants
ASSET_DIR = "SpaceStoneDodger-main/SpaceStoneDodger-main/assets"
TRANSLATIONS_FOLDER = "SpaceStoneDodger-main/SpaceStoneDodger-main/lang"
SHIP_SPRITE = pygame.image.load("SpaceStoneDodger-main/SpaceStoneDodger-main/assets/Ship.png")
ASTEROID_SPRITE = pygame.image.load("SpaceStoneDodger-main/SpaceStoneDodger-main/assets/asteroid.png")
SPACE_BG = pygame.image.load("SpaceStoneDodger-main/SpaceStoneDodger-main/assets/purple_space_bg.png") # by Digital Moons (https://digitalmoons.itch.io/)
METAL_SCRAP_SPRITE = pygame.image.load("SpaceStoneDodger-main/SpaceStoneDodger-main/assets/metal_scrap2.png")
TITLE_FONT = os.path.join(ASSET_DIR, "DungGeunMo.ttf") # Font by codeman38 | cody@zone38.net | http://www.zone38.net/


# Custom Pygame Events
PLAYER_HIT = pygame.USEREVENT + 1
PLAYER_DEAD = pygame.USEREVENT + 2
POWER_UP_COLLECTED = pygame.USEREVENT + 3


# Colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)



# Scenes
class SCENES:
    """ Object that groups all scenes """
    GAME_MENU = 0
    GAME_TUTORIAL = 1
    GAME_LEVEL = 2
    GAME_LOSING_SCREEN = 3
    GAME_Infinity = 4
    GAME_Record = 5

# Text alignment
class TXT:
    LEFT = 0
    CENTER = 1
    RIGHT = 2



# OBJECTS
# -------

class TextDB:
    """ Inner class to manage languages and text """
    current_text_db = { "LANGUAGE": "no_language_loaded"}
    placeholder_text = "???"

    # Setting English as default language (if present)
    for lang in get_every_languages():
        if lang["LANGUAGE"].lower() == "english":
            current_text_db = lang

    @classmethod
    def get_text(cls, text_db_id: str) -> str:
        """ Returns a string from the database based on provided id """
        return cls.current_text_db.get(text_db_id, cls.placeholder_text)

    @classmethod
    def set_text_db(cls, chosen_language: dict) -> None:
        """ Sets a language dict as the current one """
        cls.current_text_db = chosen_language

class Record:
    new_record = 0

    def set_record(r):

        with open('C:/Users/coj70/OneDrive/바탕 화면/SpaceStoneDodger-master/SpaceStoneDodger-main/SpaceStoneDodger-main/lang/english.json', 'r') as fe:
            
            json_data_e = json.load(fe)
            record_e1 = json_data_e['RECORD005']
            record_e2 = json_data_e['RECORD006']
            record_e3 = json_data_e['RECORD007']
            
        with open('C:/Users/coj70/OneDrive/바탕 화면/SpaceStoneDodger-master/SpaceStoneDodger-main/SpaceStoneDodger-main/lang/korean.json', 'r', encoding='utf-8') as fk:
            
            json_data_k = json.load(fk)
            record_k1 = json_data_k['RECORD005']
            record_k2 = json_data_k['RECORD006']
            record_k3 = json_data_k['RECORD007']
            

        if(r > int(record_e1)):
            json_data_e['RECORD005'] = str(r)
            json_data_e['RECORD006'] = record_e1
            json_data_e['RECORD007'] = record_e2
        elif(r > int(record_e2)):
            json_data_e['RECORD006'] = str(r)
            json_data_e['RECORD007'] = record_e2
        elif(r > int(record_e3)):
            json_data_e['RECORD007'] = str(r)

        if(r > int(record_k1)):
            json_data_k['RECORD005'] = str(r)
            json_data_k['RECORD006'] = record_k1
            json_data_k['RECORD007'] = record_k2
        elif(r > int(record_k2)):
            json_data_k['RECORD006'] = str(r)
            json_data_k['RECORD007'] = record_k2
        elif(r > int(record_k3)):
            json_data_k['RECORD007'] = str(r)

        with open('C:/Users/coj70/OneDrive/바탕 화면/SpaceStoneDodger-master/SpaceStoneDodger-main/SpaceStoneDodger-main/lang/english.json', 'w') as w:
            json.dump(json_data_e, w ,indent="\t")

        with open('C:/Users/coj70/OneDrive/바탕 화면/SpaceStoneDodger-master/SpaceStoneDodger-main/SpaceStoneDodger-main/lang/korean.json', 'w', encoding='utf-8') as w:
            json.dump(json_data_k, w ,indent="\t")
        


            




    def get_record():
        return Record.new_record





# Testing
if __name__ == "__main__":
    print(get_text("LOSE003"))
    Record.set_record(5)