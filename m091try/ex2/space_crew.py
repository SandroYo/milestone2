#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   space_crew.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/18 12:31:40 by myohann-            #+#    #+#            #
#   Updated: 2026/08/19 01:51:07 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from importlib import metadata
import sys


try:
    metadata.version("pydantic")
except metadata.PackageNotFoundError as e:
    print(f"Error: {e}")
    sys.exit()

from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CA = "cadet"
    OF = "officer"
    LI = "lieutenant"
    CAP = "captain"
    CO = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode="after")
    def Mission_validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        i = 0
        j = 0
        for c in self.crew:
            i += 1
            j += 1
            if c.rank == Rank.CO or c.rank == Rank.CAP:
                i -= 1
            elif i == len(self.crew):
                raise ValueError("Must have at least one Commander or Captain")
            if self.duration_days > 365:
                if c.years_experience >= 5:
                    j -= 1
                elif j < (len(self.crew) / 2):
                    raise ValueError("Long missions need 50% "
                                     "experienced crew")
            if not c.is_active:
                raise ValueError("All crew members must be active")
        return self

    def show(self) -> None:
        print("Valid mission created:")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: {self.budget_millions}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for c in self.crew:
            print(f"- {c.name} ({c.rank.value}) - {c.specialization}")


if __name__ == "__main__":
    try:
        print("=============================================")
        cr1 = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=Rank.CAP,
            age=30,
            specialization="Mission Command",
            years_experience=7,
            is_active=True,
        )
        cr2 = CrewMember(
            member_id="002",
            name="John Smith",
            rank=Rank.LI,
            age=47,
            specialization="Navigation",
            years_experience=8,
            is_active=True,
        )
        cr3 = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=Rank.OF,
            age=27,
            specialization="Engineering",
            years_experience=5,
            is_active=True,
        )
        m_secret = SpaceMission(
            mission_id="M_S_2078",
            mission_name="Adora",
            destination="Vulcain",
            launch_date=datetime(2078, 5, 10, 14, 15),
            duration_days=400,
            crew=[cr1, cr2, cr3],
            budget_millions=1000,
        )
        m_secret.show()
    except ValidationError as e:
        for error in e.errors():
            if error['type'] == 'value_error':
                print(f"{error['msg']}")
            else:
                for loc in error['loc']:
                    print(f"{loc}: {error['msg']}")
    except Exception as e:
        print(e)
    try:
        print("\n=============================================")
        print("Expected validation error:")
        cr1 = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=Rank.CA,
            age=30,
            specialization="Mission Command",
            years_experience=7,
            is_active=True,
        )
        cr2 = CrewMember(
            member_id="002",
            name="John Smith",
            rank=Rank.LI,
            age=47,
            specialization="Navigation",
            years_experience=8,
            is_active=True,
        )
        cr3 = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=Rank.OF,
            age=27,
            specialization="Engineering",
            years_experience=5,
            is_active=True,
        )
        m_secret = SpaceMission(
            mission_id="M_S_2078",
            mission_name="Adora",
            destination="Vulcain",
            launch_date=datetime(2078, 5, 10, 14, 15),
            duration_days=400,
            crew=[cr1, cr2, cr3],
            budget_millions=1005,
        )
        m_secret.show()

    except ValidationError as e:
        for error in e.errors():
            if error['type'] == 'value_error':
                print(f"{error['msg']}")
            else:
                for loc in error['loc']:
                    print(f"{loc}: {error['msg']}")
    except Exception as e:
        print(e)
