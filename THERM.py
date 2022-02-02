from thermalprinter import *
from PIL import Image

with ThermalPrinter(port='COM3') as printer:
	# printer.image(Image.open(r'C:\Users\Andrew\Downloads\therm.png'))
	# printer.out("; ".join(dir(printer)))
	# printer.out(printer.__doc__)
	# printer.test()
	
	lines = [('                                ',{"bold":True, "inverse":True}), (' Goblin                  CR 1/3 ',{"bold":True, "inverse":True}), ('                                ',{"bold":True, "inverse":True}), ('XP 135                          ',{"bold":True}), ("Goblin warrior 1"), ("NE Small humanoid (goblinoid)"), ("Init",{"line_feed":False, "bold":True}), (" +6; "), ("Senses",{"line_feed":False, "bold":True}), (" darkvision 60 ft.; Perception -1"), ('-'*32), ("DEFENSE"), ('-'*32), ("AC",{"line_feed":False, "bold":True}), (" 16, touch 13, flat-footed 14 (+2 armor, +2 Dex, +1 shield, +1 size)"), ("hp",{"line_feed":False, "bold":True}), (" 6 (1d10+1)"), ("Fort",{"line_feed":False, "bold":True}), (" +3, ",{"line_feed":False}), ("Ref",{"line_feed":False, "bold":True}), (" +2, ",{"line_feed":False}), ("Will",{"line_feed":False, "bold":True}), (" –1"), ('-'*32), ("OFFENSE"), ('-'*32), ("Speed 30 ft."), ("Melee short sword +2 (1d4/19-20)"), ("Ranged short bow +4 (1d4/x3)"), ('-'*32), ("STATISTICS"), ('-'*32), ("Str 11, Dex 15, Con 12, Int 10, Wis 9, Cha 6"), ("Base Atk +1; CMB +0; CMD 12"), ("Feats Improved Initiative"), ("Skills Ride +10, Stealth +10, Swim +4; Racial Modifiers +4 Ride, +4 Stealth"), ("Languages Goblin"), ]
	lines = [
("█┌─────┐        ┌───┬─────────┐█"),
("█│  1  └───══───┘   ║     3   │█"),
("█│          2       │  ┌─══─┐ │█"),
("█└──────────────────┴──┘    └─┘█"),
  # ("         +++ CHOICE +++         "),
  # ("    +++ 1. OVERIDE ADMIN +++    "),
  # ("    +++ 2. REBOOT DEVICE +++    "),

	]

	for index, l in enumerate(lines):
		printer.line_spacing(25)
		
		# if index < 3:
		# 	printer.line_spacing(10)
		# else:
		# 	printer.line_spacing(30)
		if type(l) == type(""):
			content = l
		else:
			content = l[0]
		kwargs = l[1]
		if type(kwargs) != type({}):
			kwargs = {}
		printer.out(content, **kwargs)

	# printer.out('Strike', strike=True)
	# printer.barcode_height(80)
	# printer.barcode_position(BarCodePosition.BELOW)
	# printer.barcode_width(3)
	# printer.barcode('012345678901', BarCode.EAN13)

	# # Styles
	# printer.out('Bold', bold=True)
	# printer.out('Double height', double_height=True)
	# printer.out('Double width', double_width=True)
	# printer.out('Inverse', inverse=True)
	# printer.out('Rotate 90°', rotate=True, codepage=CodePage.ISO_8859_1)
	# printer.out('Strike', strike=True)
	# printer.out('Underline', underline=1)
	# printer.out('Upside down', upside_down=True)

	# # Chinese (almost all alphabets exist)
	# printer.out('现代汉语通用字表', chinese=True,
	# 			chinese_format=Chinese.UTF_8)

	# # Greek (excepted the ΐ character)
	# printer.out('Στην υγειά μας!', codepage=CodePage.CP737)

	# # Accents
	# printer.out('Voilà !', justify='C', strike=True,
	# 			underline=2, codepage=CodePage.ISO_8859_1)

	# Line feeds
	printer.line_spacing(30)
	printer.feed(2)