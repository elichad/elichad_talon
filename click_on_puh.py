from talon import Module, noise
from time import sleep, time

from user.knausj_talon.code.mouse import on_pop

mod = Module()
setting_mouse_enable_puh_click = mod.setting(
    "mouse_enable_puh_click",
    type=int,
    default=0,
    desc="Enable puh to click when control mouse is enabled.",
)

def on_puh():
    print("puh registered")
    if setting_mouse_enable_puh_click.get() == 0:
        print("doing nothing")
    else:
        print("executing pop")
        on_pop()

# DOES NOT WORK
noise.register('puh', on_puh)
