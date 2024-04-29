material_icons_codepoints = set()

material_symbols_codepoints = set()


not_in_sybols = set()

with open("MaterialIconsOutlined-Regular.codepoints", "r") as f:
    for line in f:
        material_icons_codepoints.add(line.strip().split()[0])

with open("MaterialSymbolsOutlined[FILL,GRAD,opsz,wght].codepoints", "r") as f:
    for line in f:
        material_symbols_codepoints.add(line.strip().split()[0])

for icon in material_icons_codepoints:
    if icon not in material_symbols_codepoints:
        not_in_sybols.add(icon)
        print(icon)


print(len(not_in_sybols))  # 84 e.g. wallet_travel

not_in_icons = set()
for icon in material_symbols_codepoints:
    if icon not in material_icons_codepoints:
        not_in_icons.add(icon)
        print(icon)

print(len(not_in_icons))  # 1368 e.g. audio_description
