from __future__ import annotations


class TV:
    def __init__(self) -> None:
        self._is_on: bool = False
        self._is_muted: bool = False
        self._available_channels: list[int] = [2, 3, 4, 5, 7, 9, 11, 12, 14, 21]
        self._channel_index: int = 0
        self._MAX_VOLUME: int = 10
        self._MIN_VOLUME: int = 0
        self._volume: int = 0

    @property
    def is_on(self) -> bool:
        return self._is_on

    @property
    def is_muted(self) -> bool:
        return self._is_muted

    @property
    def available_channels(self) -> list[int]:
        return self._available_channels

    @property
    def volume(self) -> int:
        return self._volume

    def power_button(self) -> None:
        """Toggles the power status."""
        self._is_on = not self._is_on
        print(f"TV is {'ON' if self.is_on else 'OFF'}.")
        input()

    def volume_up(self) -> None:
        """Raises de volume by one. Stops at maximum volume."""
        if self._volume < self._MAX_VOLUME:
            self._volume += 1
        print(f"Volume: {self.volume}")

    def volume_down(self) -> None:
        """Lowers volume by one. Stops at minimum volume."""
        if self._volume > self._MIN_VOLUME:
            self._volume -= 1
        print(f"Volume: {self.volume}")

    def channel_up(self) -> None:
        """Changes the channel one step upwards in the available channel list."""
        # If channel index is the highest, we "overflow" the list.
        if self._channel_index == len(self.available_channels) - 1:
            self._channel_index = 0
        else:
            self._channel_index += 1
        print(f"New current channel: {self.available_channels[self._channel_index]}")

    def channel_down(self) -> None:
        """Changes the channel one step downwards ins the available channel list."""
        # If channel index is the lowest, we "overflow" the list.
        if self._channel_index == 0:
            self._channel_index = len(self.available_channels) - 1
        else:
            self._channel_index -= 1
        print(f"New current channel: {self.available_channels[self._channel_index]}")

    def mute(self) -> None:
        """Toggles the mute status."""
        self._is_muted = not self._is_muted
        if self.is_muted:
            print("TV is muted.")
        else:
            print(f"Volume: {self.volume}")

    def select_channel(self) -> None:
        while True:
            new_channel_str: str = input("Please enter the desired channel: ")
            new_channel_int: int = 0
            try:
                new_channel_int = int(new_channel_str)
            except ValueError:
                print(f"'{new_channel_str}' is not a valid option. Try again.\n")
                continue
            if new_channel_int in self.available_channels:
                self._channel_index = self.available_channels.index(new_channel_int)
                print(f"Channel changed to {new_channel_int}")
                break
            else:
                print(f"Channel '{new_channel_int}' is not available. Try again.\n")

    def show_info(self) -> None:
        """Prints the status of the TV."""
        print(f"\nTV is {'on' if self.is_on else 'off'}.")
        if not self.is_on:
            return
        print(f"Channel: '{self.available_channels[self._channel_index]}'")
        print(f"Volume: {self.volume}{'(muted)' if self.is_muted else ''}.")

    @staticmethod
    def print_options() -> None:
        print("1. Press power.")
        print("2. Press volume up.")
        print("3. Press volume down.")
        print("4. Press channel up.")
        print("5. Press channel down.")
        print("6. Press to select channel.")
        print("7. Press mute.")
        print("8. Press 'Show info'.")

    @staticmethod
    def get_valid_option() -> str:
        while True:
            message: str = (
                "Enter the number of the action you want to perform ('q' to quit): "
            )
            entered: str = input(message).strip()
            if entered not in ["1", "2", "3", "4", "5", "6", "7", "8", "q"]:
                print(f"'{entered}' is not a valid option. Please try again.")
                continue
            else:
                return entered

    def action_trigger(self, valid_option: str) -> None:
        from time import sleep

        if valid_option == "1":
            self.clear_terminal()
            self.power_button()
            return
        if self.is_on:
            self.clear_terminal()
            match valid_option:
                case "2":
                    if self.is_on:
                        self.volume_up()
                case "3":
                    if self.is_on:
                        self.volume_down()
                case "4":
                    if self.is_on:
                        self.channel_up()
                case "5":
                    if self.is_on:
                        self.channel_down()
                case "6":
                    if self.is_on:
                        self.select_channel()
                case "7":
                    if self.is_on:
                        self.mute()
                case "8":
                    if self.is_on:
                        self.show_info()
        input("Press ENTER to continue...")

    @staticmethod
    def clear_terminal() -> None:
        """Clears the terminal, regardless of the OS platform."""
        from os import system, name

        if name == "nt":
            system("cls")
        else:
            system("clear")

    def start_tv_interface(self) -> None:
        while True:
            self.clear_terminal()
            self.print_options()
            desired_action: str = self.get_valid_option()
            if desired_action == "q":
                print("OK bye!")
                break
            self.action_trigger(desired_action)


tv: TV = TV()

tv.start_tv_interface()
