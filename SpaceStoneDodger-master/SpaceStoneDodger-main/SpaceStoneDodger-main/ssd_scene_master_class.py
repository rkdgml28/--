# pylint: disable=no-member

# SpaceStoneDodger: Scene Master class
# This class implements the basic methods for running a scene

# Thanks to William Hou from
# https://gamedev.stackexchange.com/questions/102586/locking-the-frame-rate-in-pygame
# for a mean to stabilyze the frame rate

import pygame, sys
import time as t
import ssd_constants as CST



class Scene:
    def __init__(self, GAME_WINDOW: pygame.Surface) -> None:
        """ Inizalization phase, always call the super().__init__ at the end of an overridden __init__ """
        self.GAME_WINDOW = GAME_WINDOW
        self.looping_active = True
        self.updatelist = []
        self.game_timer_step = 1 # Every X seconds
        self.scene_related_init()


    def scene_related_init(self):
        """ To be overridden by each object to define their working variables
            Already defined in __init__:
            self.GAME_WINDOW: pygame.Surface
            self.updatelist: list """
        pass


    def event_checking(self, this_event: pygame.event) -> None:
        """ Overridable to check different events """
        if this_event.type == pygame.QUIT: # Handling of quit event
            pygame.quit()
            sys.exit() # ensures we quit game AND program


    def keys_to_check(self, key_list: list) -> None:
        """ Overridable to check different keys pressed """
        pass


    def set_timer_step(self, seconds: int):
        """ Allows to set a new seconds threshold for the internal game timer """
        self.game_timer_step = int(seconds)


    def timer_duty(self) -> None:
        """ What needs to be done each time the timer goes off """
        pass


    def quit_loop(self, data_to_return: int) -> None:
        """ Method to exit from the run() loop that tells it what to return """
        self.looping_active = False
        self.scene_return_data = data_to_return


    def reset_state(self) -> None:
        """ Method for resetting the state of a Scene after moving on """
        self.looping_active = True


    def scene_num(self) -> int:
        #화면 번호를 반환하는 함수
        pass  

    def run(self) -> int:
        """ Main loop method """
        time = t.time()
        unprocessed = 0
        FRAME_CAP = 1.0 / CST.FPS # How many millisecons needs to pass each frame
        game_timer = 0
        self.updatelist.clear() #scene.updatelist 초기화
        self.scene_related_init() #언어 변경을 위한 scene_related_init()
        
        # Main game loop
        while self.looping_active:
            can_render = False
            time_2 = t.time()
            passed = time_2 - time
            unprocessed += passed
            time = time_2

            for event in pygame.event.get():
                self.event_checking(event)
                #언어 변경 이벤트 처리
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_l:
                        if (self.scene_num() == CST.SCENES.GAME_MENU):
                            self.change_lang()

                    
            # Key state capturing
            keys_pressed = pygame.key.get_pressed() # Gets the bool state of all keyboard buttons
            # Frame stabilyzer
            while unprocessed >= FRAME_CAP:
                unprocessed -= FRAME_CAP
                can_render = True

            # What happens each frame
            if can_render:
                game_timer += 1
                # Key press checking
                self.keys_to_check(keys_pressed)

                # Drawing sequence
                for gameobj in self.updatelist:
                    gameobj.game_tick_update(self.GAME_WINDOW) # All classes have this methods
                pygame.display.update()

                # Game timer, used by scenes as thery want                
                if game_timer % (self.game_timer_step * CST.FPS) == 0: # every X seconds
                    game_timer = 0
                    self.timer_duty()
                
        self.reset_state()
        return self.scene_return_data