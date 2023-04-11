from __future__ import annotations


class LightSwitch:

    def __init__(self) -> None:
        self._switch_status: bool = False

    @property
    def switch_status(self) -> bool:
        return self._switch_status
    
    def turn_on(self) -> None:
        self._switch_status = True
    
    def turn_off(self) -> None:
        self._switch_status = False

    def print_switch_status(self) -> None:
        print(f"The switch is currently {'on' if self.switch_status else 'off'}.")

    def __str__(self) -> str:
        return f"LightSwitch object @ {hex(id(self)).upper()} is currently {'on' if self.switch_status else 'off'}."
    

def play_with_light_switch(switch: LightSwitch) -> None:
    switch.turn_on()
    print(switch)
    switch.turn_off()
    print(switch)
    switch.turn_on()
    print(switch)
    switch.print_switch_status()
    print(switch.switch_status)
    print()


ls_one: LightSwitch = LightSwitch()
ls_two: LightSwitch = LightSwitch()


play_with_light_switch(ls_one)
# LightSwitch object @ 0X7FA1309872D0 is currently on.
# LightSwitch object @ 0X7FA1309872D0 is currently off.
# LightSwitch object @ 0X7FA1309872D0 is currently on.
# The switch is currently on.
# True

play_with_light_switch(ls_two)
# LightSwitch object @ 0X7FA130985690 is currently on.
# LightSwitch object @ 0X7FA130985690 is currently off.
# LightSwitch object @ 0X7FA130985690 is currently on.
# The switch is currently on.
# True

print(ls_one)
# LightSwitch object @ 0X7FA1309872D0 is currently on.

print(ls_two)
# LightSwitch object @ 0X7FA130985690 is currently on.
