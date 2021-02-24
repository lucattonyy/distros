# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"], "h", lazy.layout.grow()),
    Key([mod, "shift"], "l", lazy.layout.shrink()),

    # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
 
    # Applications
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "o", lazy.spawn("obs")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod], "a", lazy.spawn("atom")),
    Key([mod], "p", lazy.spawn("pycharm")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "   ", "   ", " 爵  ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layout_conf = {
    'border_focus': ["focus"],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wname': 'branchdialog'},
        {'wname': 'pinentry'},
        {'wmclass': 'ssh-askpass'},
    ],
    border_focus=["color4"][0]
)

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    foreground=['#0f101a'], 
                    background=['#0f101a'],
                    linewidth=0, 
                    padding=5
                ),
                widget.GroupBox(
                    foreground=['#0f101a'],
                    background=['#0f101a'],
                    font='UbuntuMono Nerd Font',
                    fontsize=16,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=['#f1ffff'],
                    inactive=['#4c566a'],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=['#F07178'],
                    this_current_screen_border=['#a151d3'],
                    this_screen_border=['#353c4a'],
                    other_current_screen_border=['#0f101a'],
                    other_screen_border=['#0f101a'],
                    disable_drag=True
                ),
                widget.Sep(
                    foreground=['#0f101a'], 
                    background=['#0f101a'],
                    linewidth=0, 
                    padding=5
                ),
                widget.WindowName(
                    foreground=['#a151d3'], 
                    background=['#0f101a'],
                    fontsize=14, 
                    padding=5
                ),
                widget.Sep(
                    foreground=['#0f101a'], 
                    background=['#0f101a'],
                    linewidth=0, 
                    padding=5
                ),
                widget.Sep(
                    foreground=['#0f101a'], 
                    background=['#0f101a'],
                    linewidth=0, 
                    padding=5
                ),
                widget.TextBox(
                    foreground=['#ffd47e'],
                    background=['#0f101a'],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-2
                ),
                widget.Systray(
                    background=['#ffd47e']
                ),
                widget.TextBox(
                    foreground=['#0f101a'],
                    background=['#ffd47e'],
                    fontsize=16,
                    text=' ',
                    padding=3
                ),
                widget.TextBox(
                    foreground=['#fb9f7f'],
                    background=['#ffd47e'],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-2
                ),
                widget.TextBox(
                    foreground=['#0f101a'],
                    background=['#fb9f7f'],
                    fontsize=16,
                    text=' ',
                    padding=3
                ),
                widget.TextBox(
                    foreground=['#F07178'],
                    background=['#fb9f7f'],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-2
                ),
                widget.CurrentLayoutIcon(
                    foreground=['#0f101a'],
                    background=['#F07178'], 
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=['#0f101a'], 
                    background=['#F07178'],
                    padding=5
                ),
                widget.TextBox(
                    foreground=['#a151d3'],
                    background=['#F07178'],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-2
                ),
                widget.TextBox(
                    foreground=['#0f101a'],
                    background=['#a151d3'],
                    fontsize=16,
                    text=' ',
                    padding=3
                ),
                widget.Clock(
                    foreground=['#0f101a'], 
                    background=['#a151d3'],
                    format='%d/%m/%Y - %H:%M '
                ),
                widget.TextBox(
                    foreground=['#0f101a'],
                    background=['#a151d3'],
                    text="", # Icon: nf-oct-triangle_left
                    fontsize=37,
                    padding=-2
                ),
            ],  
            26,
            opacity=9
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

{
    "dark": [
        "#0f101a",
        "#0f101a"
    ],
    "grey": [
        "#353c4a",
        "#353c4a"
    ],
    "light": [
        "#f1ffff",
        "#f1ffff"
    ],
    "text": [
        "#0f101a",
        "#0f101a"
    ],
    "focus": [
        "#a151d3",
        "#a151d3"
    ],
    "active": [
        "#f1ffff",
        "#f1ffff"
    ],
    "inactive": [
        "#4c566a",
        "#4c566a"
    ],
    "urgent": [
        "#F07178",
        "#F07178"
    ],
    "color1": [
        "#a151d3",
        "#a151d3"
    ],
    "color2": [
        "#F07178",
        "#F07178"
    ],
    "color3": [
        "#fb9f7f",
        "#fb9f7f"
    ],
    "color4": [
        "#ffd47e",
        "#ffd47e"
    ]
}