# pylint: disable=no-member

# SpaceStoneDodger: Game Menu Class


import pygame
import ssd_constants as CST
import ssd_player as plr
import ssd_asteroid as ast
import ssd_starfield as stf
import ssd_background as bg
import ssd_powerup as pwr
import ssd_text_classes as txt
import ssd_scene_master_class as Scn



class GameMenu(Scn.Scene):
    def scene_related_init(self):
        SIZE_TEXT_BIG = 53
        SIZE_TEXT_MEDIUM = 29
        SIZE_TEXT_TINY = 19
        TITLE_COORDS = (CST.SCREEN_WIDTH // 2, CST.SCREEN_HEIGHT * 0.2)
        SUBTITLE_COORDS = (CST.SCREEN_WIDTH // 2, CST.SCREEN_HEIGHT * 0.2 + 48)
        BOTTOM_TEXT_COORDS_LEFT = (0, CST.SCREEN_HEIGHT - SIZE_TEXT_MEDIUM)
        BOTTOM_TEXT_COORDS_RIGHT = (CST.SCREEN_WIDTH, CST.SCREEN_HEIGHT - SIZE_TEXT_MEDIUM)
        BOTTOM_TEXT_COORDS_LEFT_UP = (0,CST.SCREEN_HEIGHT - 60)
        BOTTOM_TEXT_COORDS_CENTER = (CST.SCREEN_WIDTH/2, CST.SCREEN_HEIGHT - SIZE_TEXT_BIG * 3)

        self.level_background = bg.Background()
        self.starfield = stf.Starfield(15)
        self.player = plr.Player_pawn(CST.SCREEN_WIDTH // 2 - 16, CST.SCREEN_HEIGHT // 2 - 16)
        self.text_title = txt.StaticText("Space Stone Dodger", SIZE_TEXT_BIG, TITLE_COORDS, CST.TXT.CENTER)
        self.text_subtitle = txt.StaticText(CST.get_text("MENU001"), SIZE_TEXT_TINY, SUBTITLE_COORDS, CST.TXT.CENTER)
        self.text_goto_play = txt.StaticText("[P] " + CST.get_text("MENU002"), SIZE_TEXT_MEDIUM, BOTTOM_TEXT_COORDS_LEFT, CST.TXT.LEFT)
        self.text_goto_tutorial = txt.StaticText("[T] " + CST.get_text("MENU003"), SIZE_TEXT_MEDIUM, BOTTOM_TEXT_COORDS_RIGHT, CST.TXT.RIGHT)
        self.text_goto_Infinite = txt.StaticText("[I] " + CST.get_text("MENU004"), SIZE_TEXT_MEDIUM, BOTTOM_TEXT_COORDS_LEFT_UP, CST.TXT.LEFT)
        self.text_Lang = txt.StaticText("[L] " + CST.get_text("MENU005"), SIZE_TEXT_MEDIUM, BOTTOM_TEXT_COORDS_CENTER,CST.TXT.CENTER )

        # Append order is draw order
        self.updatelist.append(self.level_background)
        self.updatelist.append(self.starfield)
        self.updatelist.append(self.player)
        self.updatelist.append(self.text_title)
        self.updatelist.append(self.text_subtitle)
        self.updatelist.append(self.text_goto_play)
        self.updatelist.append(self.text_goto_tutorial)
        self.updatelist.append(self.text_goto_Infinite)
        self.updatelist.append(self.text_Lang)


    def keys_to_check(self, key_list: list):
        LANG_ENG = 0
        LANG_KOR = 1
        
        self.player.handle_movement(key_list)
        if CST.pressed("P", key_list):
            self.quit_loop(CST.SCENES.GAME_LEVEL)
        if CST.pressed("T", key_list):
            self.quit_loop(CST.SCENES.GAME_TUTORIAL)
        if CST.pressed("I", key_list):
            self.quit_loop(CST.SCENES.GAME_Infinity)
        if CST.pressed("L", key_list):
            #현재 언어가 영어라면
            if(CST.TextDB.current_text_db == CST.get_every_languages()[LANG_ENG]):
                #영어->한국어
                CST.set_text_db(CST.get_every_languages()[LANG_KOR])
            else:
                #한국어->영어
                CST.set_text_db(CST.get_every_languages()[LANG_ENG])
            
            WIN = pygame.display.set_mode((CST.SCREEN_WIDTH, CST.SCREEN_HEIGHT))
            pygame.display.set_caption("Space Stone Dodger!")    
            self.__init__(WIN)         






# TESTING
def main_game():
    pygame.init()

    # Defining our game window
    WIN = pygame.display.set_mode((CST.SCREEN_WIDTH, CST.SCREEN_HEIGHT))
    pygame.display.set_caption("Space Stone Dodger!")

    game_menu = GameMenu(WIN)
    next_scene = 0

    # Scene sequence, each scene returns the index for the next one
    while True:
        next_scene = game_menu.run()
        print("Next scene: ", next_scene)



if __name__ == "__main__":
    main_game()
    