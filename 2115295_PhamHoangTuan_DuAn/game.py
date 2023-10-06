import curses
from . import environment
from .environment import draw_background, draw_tracks, draw_statusbar, \
                    draw_debris, draw_horizon, draw_car, draw_money
from . import hud
from .hud import draw_hud
from .mechanics import update_state
from .config import GAME_SIZE, FPS, BASE_SPEED
from .misc import limit_fps


SCENE = [draw_statusbar, draw_hud, draw_horizon, draw_tracks,
         draw_debris, draw_car, draw_money, draw_background]
state = {'frames': 0,
         'time': 0.0,  
         'speed': BASE_SPEED,  
         'car': None,
         'car_x': 0,  
         'car_steer_tuple': None,
         'car_speed_tuple': None,
         'debris': [],  
         'money': [],  
         'score': 0,
         'pdb': False}  


@limit_fps(fps=FPS)
def draw_scene(screen):
    for draw_element in reversed(SCENE):
        draw_element(screen, state)
    screen.refresh()


def main(screen):
    screen.resize(*GAME_SIZE)
    screen.nodelay(True)
    environment.init(screen)
    hud.init(screen)
    while True:
        draw_scene(screen)
        key = screen.getch()
        if key == ord('q'):
            break
        elif key == ord('p'):
            state['pdb'] = True
        else:
            update_state(key, state)
        state['frames'] += 1
        state['time'] += 1/FPS
    screen.clear()
    screen.getkey()


def run():
    curses.wrapper(main)
