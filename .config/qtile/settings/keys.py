# cSpell:disable
from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"
space = 'space'
shift = 'shift'
ctrl = 'control'
alt = 'alt'
tab = 'Tab'
enter = 'Return'
backSpace = 'BackSpace'
left = 'Left'
up = 'Up'
right = 'Right'
down = 'Down'


keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ---- Trying stuff -----

    # Navigating through groups
    ([mod], tab, lazy.screen.next_group()),
    ([mod, shift], tab, lazy.screen.prev_group()),
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], down, lazy.layout.down()),
    ([mod], up, lazy.layout.up()),
    ([mod], left, lazy.layout.left()),
    ([mod], right, lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, shift], "l", lazy.layout.grow()),
    ([mod, shift], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, shift], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, shift], "j", lazy.layout.shuffle_down()),
    ([mod, shift], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], 't', lazy.next_layout()),
    ([mod, shift], 't', lazy.prev_layout()),

    # Kill window
    ([mod, shift], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, shift], "r", lazy.restart()),

    ([mod, ctrl], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], space, lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, shift], space, lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("google-chrome-stable")),

    # File Explorer
    ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], enter, lazy.spawn("alacritty")),

    # Redshift --- dont need for now
    # ([mod], "r", lazy.spawn("redshift -O 2400")),
    # ([mod, shift], "r", lazy.spawn("redshift -x")),

    # Screenshot with flameshot
    ([mod], "s", lazy.spawn("flameshot gui")),
    ([mod, shift], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
