# Test mixing int and float in different operations
mixed_division = 15.0 / 4        # float / int = float
mixed_floor = 15.0 // 4          # float // int = float
mixed_modulus = 17.0 % 5         # float % int = float
mixed_power = 2.0 ** 3           # float ** int = float

print(f"15.0 / 4 = {mixed_division} (type: {type(mixed_division)})")
print(f"15.0 // 4 = {mixed_floor} (type: {type(mixed_floor)})")
print(f"17.0 % 5 = {mixed_modulus} (type: {type(mixed_modulus)})")
print(f"2.0 ** 3 = {mixed_power} (type: {type(mixed_power)})")