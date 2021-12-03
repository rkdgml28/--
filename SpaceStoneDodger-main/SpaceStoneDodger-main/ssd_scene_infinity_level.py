import pygame
import ssd_constants as CST
import ssd_player as plr
import ssd_asteroid as ast
import ssd_starfield as stf
import ssd_background as bg
import ssd_powerup as pwr
import ssd_text_classes as txt
import ssd_scene_master_class as Scn
import ssd_movie_effect as mov


class InfinityLevel(Scn.Scene):
    def scene_related_init(self):
        self.keypress_allowed = False
        self.num_power_ups = 0
        self.num_asteroids = 0
        self.num_stars = 24
        self.score = 0

        self.level_background = bg.Background()
        self.starfield = stf.Starfield(self.num_stars)
        self.player = plr.Player_pawn(-50, CST.SCREEN_HEIGHT // 2)
        self.ui_lifebar = plr.Lifebar(self.player)
        self.asteroid_field = ast.AsteroidField(self.num_asteroids, self.player)
        self.powerup_field = pwr.PowerUpField(self.num_power_ups, self.player)
        self.score_label = txt.StaticText(CST.get_text("LEVEL000") + ":", 19, (0,0), CST.TXT.LEFT)
        self.navigator_text = txt.AnimatedTypedText("", 19, (30, 300), 20, autostart=False)
        self.movie_effect = mov.MovieEffect(80, 20)

        # Append order is draw order
        self.updatelist.append(self.level_background)
        self.updatelist.append(self.powerup_field)
        self.updatelist.append(self.starfield)
        self.updatelist.append(self.player)
        self.updatelist.append(self.asteroid_field)
        self.updatelist.append(self.ui_lifebar)
        self.updatelist.append(self.score_label)
        self.updatelist.append(self.navigator_text)
        self.updatelist.append(self.movie_effect)

        self.timeline = { # Keys are seconds of play, values are methods
            1: self.tml_begin,
            2: self.tml_playing_phase_start,
            6: self.tml_playing_phase_3_1,
            8: self.tml_playing_phase_3_2,
            11: self.tml_playing_phase_3_3,
            15: self.tml_calm_before_the_swarm_3,
            20: self.tml_swarm_3,
            24: self.tml_swarm_passed_3,
        }

        self.set_timer_step(1) # Setting the internal timer
        self.timer_seconds_passed = 0

    def timer_duty(self) -> None:
        # What happens when the timer goes off
        self.timer_seconds_passed += 1 # 숫자가 늘어날수록 시간이 빨리감
        self.check_timeline_progress(self.timer_seconds_passed)

        #반복시킴
        if self.timer_seconds_passed > 25 :
            print(self.timer_seconds_passed)
            self.timeline = { #타임라인 재생성
            1: self.tml_begin,
            2: self.tml_playing_phase_start,
            6: self.tml_playing_phase_3_1,
            8: self.tml_playing_phase_3_2,
            11: self.tml_playing_phase_3_3,
            15: self.tml_calm_before_the_swarm_3,
            20: self.tml_swarm_3,
            24: self.tml_swarm_passed_3,
            }
            self.timer_seconds_passed = 4

    def event_checking(self, this_event: pygame.event) -> None:
        super().event_checking(this_event) # for quitting handling
        if this_event.type == CST.PLAYER_HIT:
            self.player.got_hit(CST.PLAYER_DEAD)
        if this_event.type == CST.PLAYER_DEAD:
            self.quit_loop(CST.SCENES.GAME_LOSING_SCREEN)
        if this_event.type == CST.POWER_UP_COLLECTED:
            self.score += 1
            self.score_label.set_text(CST.get_text("LEVEL000") + ": " + str(self.score))


    def keys_to_check(self, key_list: list) -> None:
        if not self.keypress_allowed:
            return
        self.player.handle_movement(key_list)
        self.asteroid_field.handle_movement(key_list)
        self.powerup_field.handle_movement(key_list)
        self.starfield.handle_movement(key_list)

    def reset_state(self):
        self.__init__(self.GAME_WINDOW) # Forcing the level to initial state when playing again

    # Timeline related methods
    def check_timeline_progress(self, time_now) -> None:
        """ Calls timeline events when it's the right time """
        if not self.timeline:
            return
        next_event_in_line = min(self.timeline.keys())

        while self.timer_seconds_passed > next_event_in_line: # Used to skip phases during tests
            self.timeline.pop(next_event_in_line)
            next_event_in_line = min(self.timeline.keys())

        if time_now == next_event_in_line:
            self.timeline[time_now]()
            self.timeline.pop(time_now)


    def tml_begin(self) -> None:
        """ Beginning of the game """
        self.player.automove_to(50, CST.SCREEN_HEIGHT // 2)


    def tml_playing_phase_start(self) -> None:
        self.movie_effect.start_animation()
        self.navigator_text.hide()
        self.keypress_allowed = True
        self.player.user_controlled()


    def tml_playing_phase_3_1(self) -> None:
        self.num_asteroids = 6
        self.num_power_ups = 4
        self.asteroid_field.resize(self.num_asteroids)
        self.powerup_field.resize(self.num_power_ups)

    def tml_playing_phase_3_2(self) -> None:
        self.num_asteroids = 8
        self.num_power_ups = 5
        self.asteroid_field.resize(self.num_asteroids)
        self.powerup_field.resize(self.num_power_ups)

    def tml_playing_phase_3_3(self) -> None:
        self.num_asteroids = 10
        self.num_power_ups = 6
        self.asteroid_field.resize(self.num_asteroids)
        self.powerup_field.resize(self.num_power_ups)

    def tml_calm_before_the_swarm_3(self) -> None:
        self.num_asteroids = 5
        self.num_power_ups = 8
        self.asteroid_field.resize(self.num_asteroids)
        self.powerup_field.resize(self.num_power_ups)
        self.navigator_text.set_text(CST.get_text("LEVEL005"))
        self.navigator_text.start()

    def tml_swarm_3(self) -> None:
        self.navigator_text.hide()
        self.num_asteroids = 25
        self.num_power_ups = 8
        self.asteroid_field.resize(self.num_asteroids)
        self.powerup_field.resize(self.num_power_ups)

    def tml_swarm_passed_3(self) -> None:
        self.num_asteroids = 4
        self.num_power_ups = 3
        self.asteroid_field.resize(self.num_asteroids)
        self.powerup_field.resize(self.num_power_ups)
    def tml_end_of_scene(self) -> None:
        """ End of scene, onward to credits! """
        self.quit_loop(CST.SCENES.GAME_MENU)

    def scene_num(self) -> int:
        return CST.SCENES.GAME_Infinity




# TESTING
def main_game():
    pygame.init()

    # Defining our game window
    WIN = pygame.display.set_mode((CST.SCREEN_WIDTH, CST.SCREEN_HEIGHT))
    pygame.display.set_caption("Space Stone Dodger!")

    game_level = InfinityLevel(WIN)
    next_scene = 0

    game_level.player.god_mode(True) # Keep player invulnerable for testing purpose"""

    # Scene sequence, each scene returns the index for the next one
    while True:
        next_scene = game_level.run()
        print("Next scene: ", next_scene)



if __name__ == "__main__":
    main_game()
    