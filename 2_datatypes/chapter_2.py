spice_mix = set()

print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")


spice_mix.add("Ginger")
spice_mix.add("cardmom")

print(f"Final spice mix id: {spice_mix}")
print(f"Final spice mix id: {id(spice_mix)}")