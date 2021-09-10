h = "48b0b0"
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))

newColor = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
insideIndicator = f"background-color: rgb{newColor};"
insideStyleSheet = f"QCheckBox::indicator{insideIndicator}"
print(insideStyleSheet)
print("QCheckBox::indicator{background-color: rgb(72, 176, 176);}")

test = "QCheckBox::indicator{background-color: rgb" + f"{newColor}"+";}"
print(test)


