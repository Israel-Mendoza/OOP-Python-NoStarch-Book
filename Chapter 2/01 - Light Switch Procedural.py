from __future__ import annotations

# Defining global variable
switch_is_on: bool = False

# Defining functions to turn the switch on and off
def turn_switch_on() -> None:
    global switch_is_on
    switch_is_on = True


def turn_switch_off() -> None:
    global switch_is_on
    switch_is_on = False


def print_switch_status() -> None:
    print(f"The switch is currently {'on' if switch_is_on else 'off'}.")


print_switch_status()   # The switch is currently off.
turn_switch_on()
print_switch_status()   # The switch is currently on.
turn_switch_off()
print_switch_status()   # The switch is currently off.
turn_switch_on()
print_switch_status()   # The switch is currently on.
