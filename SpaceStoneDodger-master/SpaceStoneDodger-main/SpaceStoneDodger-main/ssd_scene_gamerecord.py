# pylint: disable=no-member

# SpaceStoneDodger: Game Tutorial Class


import pygame
import ssd_constants as CST
import ssd_player as plr
import ssd_asteroid as ast
import ssd_starfield as stf
import ssd_background as bg
import ssd_powerup as pwr
import ssd_text_classes as txt
import ssd_scene_master_class as Scn



class GameRecord(Scn.Scene):
    def scene_related_init(self):

        SIZE_TEXT_BIG = 53
        SIZE_TEXT_MEDIUM = 29
        SIZE_TEXT_SMALL = 23
        SIZE_TEXT_TINY = 17
        FIRST_COL = 50
        SECOND_COL = 120
        THIRD_COL = 190
        ZERO_ROW = CST.SCREEN_HEIGHT // 5 * 1 -100
        FIRST_ROW = CST.SCREEN_HEIGHT // 5 * 2 -100
        SECOND_ROW = CST.SCREEN_HEIGHT // 5 * 3 -100
        THIRD_ROW = CST.SCREEN_HEIGHT // 5 * 4 -100
        BOTTOM_ROW = CST.SCREEN_HEIGHT - SIZE_TEXT_SMALL
        BOTTOM_UP_ROW = CST.SCREEN_HEIGHT - SIZE_TEXT_BIG
        
        if CST.TextDB.current_text_db["LANGUAGE"] == "English":
            CST.TextDB.set_text_db(CST.get_every_languages()[0])
        else:
            CST.TextDB.set_text_db(CST.get_every_languages()[1])


    
         

        self.level_background = bg.Background()
        self.starfield = stf.Starfield(15)
        #self.player = plr.Player_pawn(FIRST_COL, FIRST_ROW)
        #self.player_life_bar = plr.Lifebar(self.player)
        # self.asteroid = ast.Asteroid(FIRST_COL, SECOND_ROW, 0)
        # self.asteroid.set_scale(48)
        # self.powerup = pwr.PowerUp(FIRST_COL, THIRD_ROW, 0)
        # self.player_label = txt.AnimatedTypedText(CST.get_text("TUTORIAL001"), SIZE_TEXT_MEDIUM, (SECOND_COL, FIRST_ROW), 1)
        # self.asteroid_label = txt.AnimatedTypedText(CST.get_text("TUTORIAL002"), SIZE_TEXT_MEDIUM, (SECOND_COL, SECOND_ROW), 1)
        # self.powerup_label = txt.AnimatedTypedText(CST.get_text("TUTORIAL003"), SIZE_TEXT_MEDIUM, (SECOND_COL, THIRD_ROW), 1)
        # self.player_life_bar_label = txt.StaticText(CST.get_text("TUTORIAL004"), SIZE_TEXT_TINY, (CST.SCREEN_WIDTH, 50), CST.TXT.RIGHT)
        self.score1_label = txt.AnimatedTypedText(CST.get_text("RECORD001"), SIZE_TEXT_MEDIUM, (SECOND_COL, FIRST_ROW), 1)
        self.score2_label = txt.AnimatedTypedText(CST.get_text("RECORD002"), SIZE_TEXT_MEDIUM, (SECOND_COL, SECOND_ROW), 1)
        self.score3_label = txt.AnimatedTypedText(CST.get_text("RECORD003"), SIZE_TEXT_MEDIUM, (SECOND_COL, THIRD_ROW), 1)
        self.record_label = txt.AnimatedTypedText(CST.get_text("RECORD004"), SIZE_TEXT_BIG, (THIRD_COL+150, ZERO_ROW), 1)
        self.record1_label = txt.AnimatedTypedText(CST.get_text("RECORD005"), SIZE_TEXT_MEDIUM, (THIRD_COL + 100, FIRST_ROW), 1)
        self.record2_label = txt.AnimatedTypedText(CST.get_text("RECORD006"), SIZE_TEXT_MEDIUM, (THIRD_COL + 100, SECOND_ROW), 1)
        self.record3_label = txt.AnimatedTypedText(CST.get_text("RECORD007"), SIZE_TEXT_MEDIUM, (THIRD_COL +100, THIRD_ROW), 1)


        self.goto_menu_label = txt.StaticText("[M] " + CST.get_text("TUTORIAL005"), SIZE_TEXT_SMALL, (0, BOTTOM_ROW), CST.TXT.LEFT)
        self.goto_play_label = txt.StaticText("[P] " + CST.get_text("TUTORIAL006"), SIZE_TEXT_SMALL, (CST.SCREEN_WIDTH, BOTTOM_ROW), CST.TXT.RIGHT)
        self.goto_Infinity_label = txt.StaticText("[I] " + CST.get_text("TUTORIAL007"), SIZE_TEXT_SMALL, (0, BOTTOM_UP_ROW), CST.TXT.LEFT)
        # Append order is draw order
        self.updatelist.append(self.level_background)
        self.updatelist.append(self.starfield)
        self.updatelist.append(self.record_label)
        self.updatelist.append(self.score1_label)
        self.updatelist.append(self.score2_label)
        self.updatelist.append(self.score3_label)
        self.updatelist.append(self.record1_label)
        self.updatelist.append(self.record2_label)
        self.updatelist.append(self.record3_label)
        # self.updatelist.append(self.player)
        # self.updatelist.append(self.player_life_bar)
        # self.updatelist.append(self.asteroid)
        # self.updatelist.append(self.powerup)
        # self.updatelist.append(self.player_label)
        # self.updatelist.append(self.asteroid_label)
        # self.updatelist.append(self.powerup_label)
        # self.updatelist.append(self.player_life_bar_label)
        self.updatelist.append(self.goto_menu_label)
        self.updatelist.append(self.goto_play_label)
        self.updatelist.append(self.goto_Infinity_label)

        # self.player_label.skip_animation()
        # self.asteroid_label.skip_animation()
        # self.powerup_label.skip_animation()

        self.record_label.skip_animation()
        self.score1_label.skip_animation()
        self.score2_label.skip_animation()
        self.score3_label.skip_animation()
        self.record1_label.skip_animation()
        self.record2_label.skip_animation()
        self.record3_label.skip_animation()

    def keys_to_check(self, key_list: list) -> None:
        #self.player.handle_movement(key_list)
        if CST.pressed("M", key_list):
            self.quit_loop(CST.SCENES.GAME_MENU)
        if CST.pressed("P", key_list):
            self.quit_loop(CST.SCENES.GAME_LEVEL)
        if CST.pressed("I", key_list):
            self.quit_loop(CST.SCENES.GAME_Infinity)

    def scene_num(self) -> int:
        return CST.SCENES.GAME_Record




# TESTING
def main_game():
    pygame.init()

    # Defining our game window
    WIN = pygame.display.set_mode((CST.SCREEN_WIDTH, CST.SCREEN_HEIGHT))
    pygame.display.set_caption("Space Stone Dodger!")

    game_record = GameRecord(WIN)
    next_scene = 0

    # Scene sequence, each scene returns the index for the next one
    while True:
        next_scene = game_record.run()
        print("Next scene: ", next_scene)



if __name__ == "__main__":
    main_game()
    