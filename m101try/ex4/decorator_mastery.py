#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: myohann- <myohann-@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/20 06:58:58 by myohann-            #+#    #+#            #
#   Updated: 2026/08/20 16:18:01 by myohann-           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from functools import wraps
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if (("power" in kwargs.keys() and kwargs["power"] >= min_power)
                    or (len(args) > 0 and args[0] >= min_power)):
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                            )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(min_power=10)
        def cast(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return str(cast(power, spell_name))


@power_validator(10)
def power(power: int) -> int:
    return (power)


if __name__ == "__main__":
    print("==========================================")
    @spell_timer
    def fireball() -> str:
        time.sleep(1)
        return f"Result: {fireball.__name__.capitalize()} cast!\n"
    print("\nTesting spell timer...")
    print(fireball())
    print("==========================================")
    print("Testing power validator")
    reslut = power(power=5)
    print(reslut, end="\n\n")
    print("==========================================")
    print("Testing retrying spell...")
    
    @retry_spell(max_attempts=3)
    def unstable_spell() -> bool:
        raise ValueError("Error")
    print(unstable_spell())
    print("Waaaaaaagh spelled!")
    print("==========================================")
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("G"))
    print(MageGuild.validate_mage_name("G1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
