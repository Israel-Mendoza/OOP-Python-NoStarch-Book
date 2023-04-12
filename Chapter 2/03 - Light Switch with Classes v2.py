class DimmerSwitch:

    def __init__(self) -> None:
        self._level: int = 0
        self._is_on: bool = False


    @property
    def level(self) -> int:
        return self._level
    
    @property
    def is_on(self) -> bool:
        return self._is_on
    
    def turn_on(self) -> None:
        if self.is_on:
            print("Switch is already on!")
        else:
            self._is_on = True
            self._level = 5

    def turn_off(self) -> None:
        if self.is_on:
            self._is_on = False
            self._level = 0
        else:
            print("Switch is already off!")

    def raise_level(self) -> None:
        if self.level < 5:
            self._level += 1
        if self.level == 1:
            self._is_on = True

    def lower_level(self) -> None:
        if self.level > 0:
            self._level -= 1
        if self.level == 0:
            self._is_on = False

    def status(self) -> None:
        on_levels: int = self.level
        off_levels: int = 5 - self.level
        level_display: str = f"{'O' * on_levels}{'-' * off_levels}"
        print(f"\nSwitch is {'on' if self.is_on else 'off'}. Level {self.level}.")
        print(f"{level_display}")
        print("-", " " * 3, "+", sep="", end="\n\n")


d: DimmerSwitch = DimmerSwitch()

d.status()
# Switch is off. Level 0.
# -----
# -   +

for i in range(10):
    d.raise_level()
    d.status()

# Switch is on. Level 1.
# O----
# -   +

# Switch is on. Level 2.
# OO---
# -   +

# Switch is on. Level 3.
# OOO--
# -   +

# Switch is on. Level 4.
# OOOO-
# -   +

# Switch is on. Level 5.
# OOOOO
# -   +

# Switch is on. Level 5.
# OOOOO
# -   +

# Switch is on. Level 5.
# OOOOO
# -   +

# Switch is on. Level 5.
# OOOOO
# -   +

# Switch is on. Level 5.
# OOOOO
# -   +

# Switch is on. Level 5.
# OOOOO
# -   +

d.turn_on()
# Switch is already on!

for i in range(10):
    d.lower_level()
    d.status()

# Switch is on. Level 4.
# OOOO-
# -   +

# Switch is on. Level 3.
# OOO--
# -   +

# Switch is on. Level 2.
# OO---
# -   +

# Switch is on. Level 1.
# O----
# -   +

# Switch is off. Level 0.
# -----
# -   +

# Switch is off. Level 0.
# -----
# -   +

# Switch is off. Level 0.
# -----
# -   +

# Switch is off. Level 0.
# -----
# -   +

# Switch is off. Level 0.
# -----
# -   +

# Switch is off. Level 0.
# -----
# -   +

d.turn_off()
# Switch is already off!

d.turn_on()
d.status()
# Switch is on. Level 5.
# OOOOO
# -   +

d.turn_off()
d.status()
# Switch is off. Level 0.
# -----
# -   +
