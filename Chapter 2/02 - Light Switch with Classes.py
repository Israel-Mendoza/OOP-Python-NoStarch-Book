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
    

ls: LightSwitch = LightSwitch()
print(ls)
# LightSwitch object @ 0X7FA173C66C10 is currently off.
ls.turn_on()
print(ls)
# LightSwitch object @ 0X7FA173C66C10 is currently on.
ls.turn_off()
print(ls)
# LightSwitch object @ 0X7FA173C66C10 is currently off.
ls.turn_on()
print(ls)
# LightSwitch object @ 0X7FA173C66C10 is currently on.
ls.print_switch_status()
# The switch is currently on.
print(ls.switch_status)
# True
