from talon import Module, actions, ctrl, noise, cron
from talon_plugins import eye_mouse, eye_zoom_mouse
from time import sleep, time

start = 0
running = False
noise_length_threshold = "500ms"
threshold_passed = False

mod = Module()
setting_mouse_enable_hiss_drag = mod.setting(
    "mouse_enable_hiss_drag",
    type=int,
    default=0,
    desc="Enable hiss to drag when control mouse is enabled.",
)


def still_running():
    global running
    global threshold_passed
    if running:
        threshold_passed = True
        toggle_mouse_drag(True)
        print('hiss duration passed threshold, starting gaze drag')


def cursor_drag_on_hiss(is_active):
    global start
    global running
    global threshold_passed
    if is_active:
        start = time()
        running = True
        cron.after(noise_length_threshold, still_running)
    else:
        running = False
        if threshold_passed:
            threshold_passed = False
            toggle_mouse_drag(False)
            print('end of hiss detected, disabling gaze drag')


noise.register('hiss', cursor_drag_on_hiss)


def toggle_mouse_drag(active: bool):
    if setting_mouse_enable_hiss_drag.get() == 0 and active: # allow turning off just not on
        return

    #if eye_zoom_mouse.zoom_mouse.enabled or eye_mouse.mouse.attached_tracker is None:
    #    return

    if active:
        ctrl.mouse_click(button=0, down=True)
    else:
        ctrl.mouse_click(button=0, up=True)