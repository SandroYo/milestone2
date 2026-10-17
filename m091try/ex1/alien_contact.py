#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   alien_contact.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/18 07:30:59 by myohann-            #+#    #+#            #
#   Updated: 2026/08/19 01:46:21 by myohann-           ###   ########.fr      #
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


class ContactType(Enum):
    RAd = "radio"
    VIS = "visual"
    PHY = "physical"
    TEL = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def f_validator(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if self.contact_type == ContactType.PHY and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.TEL and self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7 and self.message_received is None:
            raise ValueError("Strong signals should include received messages")
        return self

    def show(self) -> None:
        print("Valid contact report:")
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        if self.duration_minutes > 1:
            print(f"Duration: {self.duration_minutes} minutes")
        else:
            print(f"Duration: {self.duration_minutes} minute")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: '{self.message_received}'")


if __name__ == "__main__":
    try:
        print("Alien Contact Log Validation")
        print("=============================================")
        a_contact = AlienContact(
            contact_id="AC_2026_003",
            timestamp=datetime(2026, 8, 10, 14, 30),
            location="New Mexico",
            contact_type=ContactType.VIS,
            signal_strength=7.1,
            duration_minutes=9,
            witness_count=60,
            is_verified=True,
            message_received="We are friends"
        )
        a_contact.show()
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
        print("\n============================================")
        a_contact = AlienContact(
            contact_id="AC_2026_003",
            timestamp=datetime(2026, 8, 10, 14, 30),
            location="New Mexico",
            contact_type=ContactType.PHY,
            signal_strength=7.1,
            duration_minutes=5,
            witness_count=2,
            is_verified=False,
            message_received="Hatsiro ity eval ity"
        )
        a_contact.show()
    except ValidationError as e:
        for error in e.errors():
            if error['type'] == 'value_error':
                print(f"{error['msg']}")
            else:
                for loc in error['loc']:
                    print(f"{loc}: {error['msg']}")
    except Exception as e:
        print(e)
