#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_station.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/17 05:07:48 by myohann-            #+#    #+#            #
#   Updated: 2026/08/19 00:36:46 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from importlib import metadata
import sys
try:
    metadata.version("pydantic")
except metadata.PackageNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)
else:
    from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, default="")

    def show(self) -> None:
        print("=======================================")
        print("ID: ", self.station_id)
        print("Name: ", self.name)
        print("Crew: ", self.crew_size)
        print("Power: ", self.power_level, "%")
        print("Oxygen: ", self.oxygen_level, "%")
        print(
            "Status: ", "Operational"
            if self.is_operational
            else "Out Of Order")
        print("Last maintenance: ", self.last_maintenance.date())
        print("Note: ", self.notes)
        print("\n=======================================")


def main() -> None:
    print("Space Station Data Validation")
    print()
    print("# VALID Space Station:")
    space_x = SpaceStation(
        station_id="SXSS042",
        name="SpaceX SS",
        crew_size=20,
        power_level=80.5,
        oxygen_level=70.5,
        last_maintenance=datetime.now(),
        notes="Welcome voyager!"
    )
    space_x.show()

    print("# INVALID Space Station:")
    space_x = SpaceStation(
        station_id="SXSS042",
        name="Space X SS",
        crew_size=21,
        power_level=100,
        oxygen_level=70.5,
        last_maintenance=datetime.now(),
        is_operational=False,
        notes="Welcome !"
    )


if __name__ == "__main__":
    try:
        main()
    except ValidationError as e:
        for error in e.errors():
            field = ".".join(str(loc) for loc in error["loc"])
            print(f"Invalid : '{field}' -> {error['msg']}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
