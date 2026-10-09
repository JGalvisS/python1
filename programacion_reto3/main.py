"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia
"""
"""English Tkinter interface for the smart home controller."""

import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional, Tuple

from central_controller import Central_controller


class SmartHomeApp:
    """Builds the interface and sends validated commands to the controller."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the main window and its device input fields."""
        self.root = root
        self.root.title("Smart Home Control")
        self.root.geometry("500x680")
        self.root.minsize(500, 680)

        self.fields = {}
        self.room_options = ("room1", "room2", "room3", "living room")
        
        self._configure_style()
        self._build_interface()

    def _configure_style(self) -> None:
        """Set the visual styles used by the interface."""
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Segoe UI", 12, "bold"))
        style.configure("Section.TLabelframe.Label", font=("Segoe UI", 9, "bold"))
        style.configure("Action.TButton", padding=2)

    def _build_interface(self) -> None:
        """Create the device sections, input fields, and control buttons."""
        container = ttk.Frame(self.root, padding=6)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container,
            text="SMART HOME CONTROL",
            style="Title.TLabel",
        ).pack(pady=(0, 12))
        
        
        # Section Curtain
        self._add_device_section(
            container,
            "🪟  Curtain",
            [
                ("Turn on time (HH:MM) [Optional]", "curtain_on_time", ""),
                ("Turn off time (HH:MM) [Optional]", "curtain_off_time", ""),
            ],
            None,
            [
                ("OPEN", lambda: self._submit_curtain(True)),
                ("CLOSE", lambda: self._submit_curtain(False)),
                ("CONFIGURE", lambda: self._submit_curtain(None)),
            ],
            "curtain_name"
        )

        # Section Lightbulb
        self._add_device_section(
            container,
            "💡  Lightbulb",
            [
                ("Brightness (0-100)", "light_brightness", ""),
            ],
            self._add_light_fields,
            [
                ("ON", lambda: self._submit_light(True)),
                ("OFF", lambda: self._submit_light(False)),
                ("CONFIGURE", lambda: self._submit_light(None)),
            ],
            "light_name"
        )

        # Section Thermostat
        self._add_device_section(
            container,
            "🌡️  Thermostat",
            [
                ("Turn on time (HH:MM) [Optional]", "thermostat_on_time", ""),
                ("Turn off time (HH:MM) [Optional]", "thermostat_off_time", ""),
                ("Temperature (0-35 °C)", "thermostat_temperature", ""),
            ],
            None,
            [
                ("ON", lambda: self._submit_thermostat(True)),
                ("OFF", lambda: self._submit_thermostat(False)),
                ("CONFIGURE", lambda: self._submit_thermostat(None)),
            ],
            "thermostat_name"
        )
        
        #Global system buttons
        actions = ttk.Frame(container)
        actions.pack(fill="x", pady=(14, 4))

        ttk.Button(
            actions,
            text="TURN ON ALL",
            style="Action.TButton",
            command=Central_controller.turn_on_all,
        ).pack(fill="x", pady=3)

        ttk.Button(
            actions,
            text="TURN OFF ALL",
            style="Action.TButton",
            command=Central_controller.turn_off_all,
        ).pack(fill="x", pady=3)

        ttk.Button(
            actions,
            text="SYSTEM STATUS",
            style="Action.TButton",
            command=Central_controller.get_status_all,
        ).pack(fill="x", pady=3)

    def _add_device_section(
        self,
        parent: ttk.Frame,
        title: str,
        fields: list,
        extra_field,
        buttons: list,
        name_key: str,
    ) -> None:
        """Add one device panel, its input fields, and its action buttons."""
        section = ttk.LabelFrame(
            parent,
            text=title,
            style="Section.TLabelframe",
            padding=6,
        )
        section.pack(fill="x", pady=5)
        
        # Name field in first line
        ttk.Label(section, text="Name").grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=3,
        )
        self.fields[name_key] = tk.StringVar(value="living room")
        ttk.Combobox(
            section,
            textvariable=self.fields[name_key],
            values=self.room_options,
            state="readonly",
            width=19,
        ).grid(row=0, column=1, sticky="ew", pady=3)

        # Others fields to configure
        for i, (label, key, initial_value) in enumerate(fields):
            row_idx = i + 1
            ttk.Label(section, text=label).grid(
                row=row_idx,
                column=0,
                sticky="w",
                padx=(0, 10),
                pady=3,
            )

            variable = tk.StringVar(value=initial_value)
            self.fields[key] = variable

            ttk.Entry(section, textvariable=variable, width=22).grid(
                row=row_idx,
                column=1,
                sticky="ew",
                pady=3,
            )

        next_row = len(fields) + 1
        if extra_field is not None:
            extra_field(section, next_row)
            next_row += 1

        button_row = ttk.Frame(section)
        button_row.grid(
            row=next_row,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(8, 0),
        )

        for text, command in buttons:
            ttk.Button(
                button_row,
                text=text,
                command=command,
                style="Action.TButton",
            ).pack(side="left", expand=True, fill="x", padx=2)

        section.columnconfigure(1, weight=1)

    def _add_light_fields(self, section: ttk.LabelFrame, row: int) -> None:
        """Add mode selector for lightbulb."""
        ttk.Label(section, text="Mode").grid(
            row=row,
            column=0,
            sticky="w",
            padx=(0, 10),
            pady=3,
        )

        self.fields["light_mode"] = tk.StringVar(value="warm")
        ttk.Combobox(
            section,
            textvariable=self.fields["light_mode"],
            values=("warm", "white"),
            state="readonly",
            width=19,
        ).grid(row=row, column=1, sticky="ew", pady=3)

    def _get_name(self, key: str) -> str:
        """Return the selected device name."""
        return self.fields[key].get().strip()

    def _parse_time(
        self,
        value: str,
    ) -> Optional[Tuple[int, int]]:
        """Validate an optional HH:MM value and return hour and minute if present."""
        val = value.strip()
        if not val:
            return None, None
        try:
            parts = val.split(":")
            if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
                raise ValueError

            hour, minute = int(parts[0]), int(parts[1])
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError

            return hour, minute
        except ValueError:
            messagebox.showwarning(
                "Invalid input",
                "Time must use 24-hour HH:MM format, for example 09:00.",
            )
            return False, False

    def _submit_light(self, state: Optional[bool]) -> None:
        """Validate lightbulb inputs and call the compatible controller method."""
        name = self._get_name("light_name")
        mode = self.fields["light_mode"].get().strip().lower()
        
        brightness = None
        bright_str = self.fields["light_brightness"].get().strip()
        if bright_str:
            try:
                brightness = float(bright_str)
                if not 0 <= brightness <= 100:
                    raise ValueError
            except ValueError:
                messagebox.showwarning(
                    "Invalid input",
                    "Brightness must be a number between 0 and 100.",
                )
                return

        Central_controller.configure_lightbulb(
            name=name,
            state=state,
            mode=mode,
            brightness=brightness,
        )

    def _submit_curtain(self, state: Optional[bool]) -> None:
        """Validate curtain inputs and pass parsed times to the controller."""
        name = self._get_name("curtain_name")

        on_time_raw = self.fields["curtain_on_time"].get()
        on_parsed = self._parse_time(on_time_raw)
        if on_parsed == (False, False):
            return
        on_h, on_m = on_parsed if on_parsed else (None, None)

        off_time_raw = self.fields["curtain_off_time"].get()
        off_parsed = self._parse_time(off_time_raw)
        if off_parsed == (False, False):
            return
        off_h, off_m = off_parsed if off_parsed else (None, None)

        Central_controller.configure_curtain(
            name=name,
            state=state,
            turn_on_time_h=on_h,
            turn_on_time_m=on_m,
            turn_off_time_h=off_h,
            turn_off_time_m=off_m,
        )

    def _submit_thermostat(self, state: Optional[bool]) -> None:
        """Validate thermostat inputs and call its controller configuration method."""
        name = self._get_name("thermostat_name")

        on_time_raw = self.fields["thermostat_on_time"].get()
        on_parsed = self._parse_time(on_time_raw)
        if on_parsed == (False, False):
            return
        on_h, on_m = on_parsed if on_parsed else (None, None)

        off_time_raw = self.fields["thermostat_off_time"].get()
        off_parsed = self._parse_time(off_time_raw)
        if off_parsed == (False, False):
            return
        off_h, off_m = off_parsed if off_parsed else (None, None)

        temperature = None
        temp_str = self.fields["thermostat_temperature"].get().strip()
        if temp_str:
            try:
                temperature = float(temp_str)
                if not 0 <= temperature <= 35:
                    raise ValueError
            except ValueError:
                messagebox.showwarning(
                    "Invalid input",
                    "Temperature must be a number between 0 and 35 °C.",
                )
                return

        Central_controller.configure_thermostat(
            name=name,
            state=state,
            temperature=temperature,
            turn_on_time_h=on_h,
            turn_on_time_m=on_m,
            turn_off_time_h=off_h,
            turn_off_time_m=off_m,
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()