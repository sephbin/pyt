from bs4 import BeautifulSoup
import pprint
import re
actor = [
{"name":"Giant Octopus (CR 8)","permission":{"default":0,"IPeKQhMz2Odi77tR":3},"flags":{"core":{"sourceId":"Compendium.world.besties1-3.FVLdRhcBcSqLecsG"},"scene-packer":{"sourceId":"JournalEntry.PulbExidwScUwfZZ"}},"content":"<p><strong>Source </strong>PFRPG Bestiary</p><div><p>Octopus, Giant </p><p><i>A storm of tentacles, each twenty feet in length, flails with deadly precision from the leathery body of this gigantic octopus.</i></p><br /></div><p><button id=\"importStatblock\">Import Giant Octopus with SBC</button></p><section id=\"GiantOctopus\"><div class=\"heading\"><p class=\"alignleft\">Giant Octopus</p><p class=\"alignright\">CR 8</p></div><div><p><b>XP </b>4,800</p><p>N Large animal (aquatic)</p><p><b>Init </b>+6; <b>Senses </b>low-light vision; Perception +8</p></div><hr /><div><p><b>DEFENSE</b></p></div><hr /><div><p><b>AC </b>18, touch 11, flat-footed 16 (+2 Dex, +7 natural, -1 size)</p><p><b>hp </b>90 (12d8+36)</p><p><b>Fort </b>+11, <b>Ref </b>+12, <b>Will </b>+7</p><p><b>Defensive Abilities </b>ink cloud (30-foot-radius sphere)</p></div><hr /><div><p><b>OFFENSE</b></p></div><hr /><div><p><b>Spd </b>20 ft., swim 30 ft., jet 200 ft.</p><p><b>Melee </b>bite +13 (1d8+5 plus poison), 8 tentacles +11 (1d4+2 plus grab)</p><p><b>Space </b>10 ft.; <b>Reach </b>10 ft. (20 ft. with tentacle)</p><p><b>Special Attacks </b>constrict (tentacle, 1d4+2)</p></div><hr /><div><p><b>STATISTICS</b></p></div><hr /><div><p><b>Str</b> 20, <b>Dex</b> 15, <b>Con</b> 17, <b>Int</b> 2, <b>Wis</b> 12, <b>Cha</b> 3</p><p><b>Base Atk </b>+9; <b>CMB </b>+15 (+19 grapple); <b>CMD </b>27 (can't be tripped)</p><p><b>Feats </b>Combat Reflexes, Improved Initiative, Iron Will, Lightning Reflexes, MultiattackB, Skill Focus (Stealth), Stealthy</p><p><b>Skills </b>Escape Artist +18, Perception +8, Stealth +18, Swim +13; <b>Racial Modifiers </b>+10 Escape Artist, +8 Stealth</p></div><hr /><div><p><b>ECOLOGY</b></p></div><hr /><div><p><b>Environment </b> any ocean</p><p><b>Organization </b>solitary</p><p><b>Treasure </b>incidental</p></div><hr /><div><p><b>SPECIAL ABILITIES</b></p></div><hr /><div><p><b>Poison (Ex)</b> Bite-injury; save Fort DC 19; frequency 1/round for 6 rounds; effect 1d3 Str; cure 2 saves.</p></div><hr /><div><strong>DESCRIPTION</strong></div><hr /><div><h4><p>The giant octopus is a true monster capable of catching and eating sharks, humans, or anything else it can grab with its tentacles.</p></h4></div></section>","img":"systems/pf1/icons/races/creature-types/animal.png","_id":"06b0geDZQUcGrRKB"},
{"name":"Spriggan (CR 3)","permission":{"default":0,"IPeKQhMz2Odi77tR":3},"flags":{"core":{"sourceId":"Compendium.world.besties1-3.H6rODqBCK7QSvB7n"},"scene-packer":{"sourceId":"JournalEntry.DonjEwmmZ4mUobaA"}},"content":"<p><strong>Source </strong>PFRPG Bestiary 2</p><div><p>Spriggan</p><p><i>Flecks of saliva drip from the corners of this filthy and ill-smelling humanoid, and his large pointed ears twitch at every sound.</i></p><br /></div><p><button id=\"importStatblock\">Import Spriggan with SBC</button></p><section id=\"Spriggan\"><div class=\"heading\"><p class=\"alignleft\">Spriggan</p><p class=\"alignright\">CR 3</p></div><div><p><b>XP </b>800</p><p>CE Small humanoid (gnome)</p><p><b>Init </b>+4; <b>Senses </b>low-light vision; Perception +7</p></div><hr /><div><p><b>DEFENSE</b></p></div><hr /><div><p><b>AC </b>17, touch 15, flat-footed 13 (+2 armor, +4 Dex, +1 size)</p><p><b>hp </b>22 (4d8+4)</p><p><b>Fort </b>+5, <b>Ref </b>+5, <b>Will </b>+1</p></div><hr /><div><p><b>OFFENSE</b></p></div><hr /><div><p><b>Spd </b>20 ft.</p><p><b>Melee </b>mwk morningstar +5 (1d6-1)</p><p><b>Ranged </b>light crossbow +8 (1d6/19-20)</p><p><b>Space </b>5 ft.; <b>Reach </b>5 ft.</p><p><b>Special Attacks </b>sneak attack +2d6</p><p><b>Spell-Like Abilities</b> (CL 4th; concentration +4)<br />At will—<i>flare</i> (DC 10), <i>scare</i> (DC 12), <i>shatter</i> (DC 12)</p></div><hr /><div><p><b>STATISTICS</b></p></div><hr /><div><p><b>Str </b>9, <b>Dex </b>19, <b>Con </b>12, <b>Int </b> 10,  <b>Wis </b>10, <b>Cha </b>9</p><p><b>Base Atk </b>+3; <b>CMB </b>+1; <b>CMD </b>15</p><p><b>Feats </b>Combat Reflexes, Weapon Focus (morningstar)</p><p><b>Skills </b>Climb +1, Disable Device +11, Perception +7, Sleight of Hand +11, Stealth +15; <b>Racial Modifiers </b>+2 Climb, +2 Disable Device, +2 Perception, +2 Sleight of Hand, +2 Stealth</p><p><b>Languages </b>Aklo, Gnome</p><p><b>SQ </b>size alteration, spriggan magic, spriggan skills</p></div><hr /><div><p><b>ECOLOGY</b></p></div><hr /><div><p><b>Environment </b> any hills or forests</p><p><b>Organization </b>solitary, pair, or mob (3-12)</p><p><b>Treasure </b>NPC Gear (leather armor, masterwork morningstar, light crossbow with 10 bolts, other treasure)</p></div><hr /><div><p><b>SPECIAL ABILITIES</b></p></div><hr /><div><p><b>Size Alteration (Su)</b> At will as a standard action, a spriggan can change his size between Small and Large. Weapons, armor, and other objects on the spriggan's person grow proportionally when he changes size (objects revert to normal size 1 round after a spriggan releases them). When a spriggan becomes Large, his speed increases to 30 feet, he gains +12 Strength, -2 Dexterity, and +6 Constitution, and he takes a -2 size penalty to his AC. While Large, a spriggan cannot use his sneak attack or his racial spell-like abilities (although if he possesses either from class levels or templates, he retains their use in both sizes).  </p><p><b>Spriggan Magic (Ex)</b> A spriggan gains a +1 racial bonus on concentration checks and to save DCs for all of its racial spell-like abilities.  </p><p><b>Spriggan Skills (Ex)</b> Climb, Disable Device, Perception, Sleight of Hand, and Stealth are class skills for spriggans.</p></div><hr /><div><strong>DESCRIPTION</strong></div><hr /><div><h4><p>When the gnomes first traveled to the mortal realm from the distant land of the fey, some found the Material Plane so strange and terrifying that they lost their sense of joy. Seeing only the threats of the new world but none of its wonders, they grimly resolved to survive no matter the cost. Their innate magic responded to this twisted goal by reshaping them in mind and body over the course of many generations, transforming them into the creatures known as spriggans. Love, happiness, and beauty have no meaning for these poor souls, so they lead lives of violence and malice. The best they can manage in place of positive emotions is a muted satisfaction when they make another suffer.</p><p>Spriggans resemble ugly gnomes with an alien, feral appearance. Many are gaunt and haggard. When magically enlarged, they look the same except much more hale and muscular.</p></h4></div></section>","img":"systems/pf1/icons/races/creature-types/humanoid.jpg","_id":"0HKfeRTsGOCeIhUQ"},
{"name":"Shadow (CR 3)","permission":{"default":0,"IPeKQhMz2Odi77tR":3},"flags":{"core":{"sourceId":"Compendium.world.besties1-3.hH2RJzd1Tq8VpGwL"},"scene-packer":{"sourceId":"JournalEntry.eRHeTFzN8mqNhnHe"}},"content":"<p><strong>Source </strong>PFRPG Bestiary</p><div><p>Shadow</p><p><i>Barely seen out of the corner of the eye, this wisp of shadow is vaguely humanoid in outline and writhes with unholy life.</i></p><br /></div><p><button id=\"importStatblock\">Import Shadow with SBC</button></p><section id=\"Shadow\"><div class=\"heading\"><p class=\"alignleft\">Shadow</p><p class=\"alignright\">CR 3</p></div><div><p><b>XP </b>800</p><p>CE Medium undead (incorporeal)</p><p><b>Init </b>+2; <b>Senses </b>darkvision 60 ft.; Perception +8</p></div><hr /><div><p><b>DEFENSE</b></p></div><hr /><div><p><b>AC </b>15, touch 15, flat-footed 12 (+2 deflection, +2 Dex, +1 dodge)</p><p><b>hp </b>19 (3d8+6)</p><p><b>Fort </b>+3, <b>Ref </b>+3, <b>Will </b>+4</p><p><b>Defensive Abilities </b>incorporeal, channel resistance +2; <b>Immune </b>undead traits</p></div><hr /><div><p><b>OFFENSE</b></p></div><hr /><div><p><b>Spd </b>fly 40 ft. (good)</p><p><b>Melee </b>incorporeal touch +4 (1d6 Strength damage)</p><p><b>Special Attacks </b>create spawn</p></div><hr /><div><p><b>STATISTICS</b></p></div><hr /><div><p><b>Str</b> -, <b>Dex</b> 14, <b>Con</b> -, <b>Int</b> 6, <b>Wis</b> 12, <b>Cha</b> 15</p><p><b>Base Atk </b>+2; <b>CMB </b>+4; <b>CMD </b>17</p><p><b>Feats </b>Dodge, Skill Focus (Perception)</p><p><b>Skills </b>Fly +11, Perception +8, Stealth +8 (+12 in dim light, +4 in bright light); <b>Racial Modifiers </b>+4 Stealth in dim light (-4 in bright light)</p></div><hr /><div><p><b>ECOLOGY</b></p></div><hr /><div><p><b>Environment </b> any</p><p><b>Organization </b>solitary, pair, gang (3-6), or swarm (7-12)</p><p><b>Treasure </b>standard</p></div><hr /><div><p><b>SPECIAL ABILITIES</b></p></div><hr /><div><p><b>Create Spawn (Su)</b> A humanoid creature killed by a shadow's Strength damage becomes a shadow under the control of its killer in 1d4 rounds.  </p><p><b>Strength Damage (Su)</b> A shadow's touch deals 1d6 points of Strength damage to a living creature. This is a negative energy effect. A creature dies if this Strength damage equals or exceeds its actual Strength score.</p></div><hr /><div><strong>DESCRIPTION</strong></div><hr /><div><h4><p>The sinister shadow skirts the border between the gloom of darkness and the harsh truth of light. The shadow prefers to haunt ruins where civilization has moved on, where it hunts living creatures foolish enough to stumble into its territory. The shadow is an undead horror, and as such has no goals or outwardly visible motivations other than to sap life and vitality from living beings.</p></h4></div></section>","img":"systems/pf1/icons/races/creature-types/undead.png","_id":"xi8Z8c0XpfU2yMn4"},
{"name":"Great White Whale (CR 14)","permission":{"default":0,"IPeKQhMz2Odi77tR":3},"flags":{"core":{"sourceId":"Compendium.world.besties1-3.Gewi7RbItAoHWiKw"},"scene-packer":{"sourceId":"JournalEntry.R1SqWgxNdYOWoQM3"}},"content":"<p><strong>Source </strong>PFRPG Bestiary 2</p><div><p>Whale, Great White </p><p><i>This immense whale has an enormous, box-shaped head over a massive, toothy maw. Its rough white hide is laced with scars.</i></p><br /></div><p><button id=\"importStatblock\">Import Great White Whale with SBC</button></p><section id=\"GreatWhiteWhale\"><div class=\"heading\"><p class=\"alignleft\">Great White Whale</p><p class=\"alignright\">CR 14</p></div><div><p><b>XP </b>38,400</p><p>N Colossal animal </p><p><b>Init </b>-2; <b>Senses </b>blindsight 120 ft., low-light vision; Perception +13</p></div><hr /><div><p><b>DEFENSE</b></p></div><hr /><div><p><b>AC </b>28, touch 0, flat-footed 28 (-2 Dex, +28 natural, -8 size)</p><p><b>hp </b>225 (18d8+144)</p><p><b>Fort </b>+21, <b>Ref </b>+9, <b>Will </b>+8</p></div><hr /><div><p><b>OFFENSE</b></p></div><hr /><div><p><b>Spd </b>swim 40 ft.</p><p><b>Melee </b>bite +25 (6d6+20/19-  20), tail slap +20 (3d6+10)</p><p><b>Space </b>30 ft.; <b>Reach </b>30 ft.</p><p><b>Special Attacks </b>capsize, smashing breach</p></div><hr /><div><p><b>STATISTICS</b></p></div><hr /><div><p><b>Str </b>50, <b>Dex </b>6,  <b>Con </b>27, <b>Int </b> 2,  <b>Wis </b>11, <b>Cha </b>5</p><p><b>Base Atk </b>+13; <b>CMB </b>+41; <b>CMD </b>49 (can't be tripped)</p><p><b>Feats </b>Critical Focus, Diehard, Endurance, Great Fortitude, Improved Bull Rush, Improved Critical (bite), Iron Will, Power Attack, Staggering Critical</p><p><b>Skills </b>Perception +13, Swim +39</p><p><b>SQ </b>hold breath</p></div><hr /><div><p><b>ECOLOGY</b></p></div><hr /><div><p><b>Environment </b> any oceans</p><p><b>Organization </b>solitary, pair, or pod (3-16)</p><p><b>Treasure </b>none</p></div><hr /><div><p><b>SPECIAL ABILITIES</b></p></div><hr /><div><p><b>Smashing Breach (Ex)</b> As a full-round action, a great white whale can make a special charge attack against creatures on the surface of the water. At the end of its charge, the whale breaches, then slams down onto the target with incredible force. Any Huge or smaller creatures in the whale's space must make a DC 27 Reflex save or take 4d8+30 points of bludgeoning damage and be forced into the nearest square that is adjacent to the whale. This breach automatically attempts to capsize any boats caught wholly or partially in this area. The save DC is Constitution-based.</p></div><hr /><div><strong>DESCRIPTION</strong></div><hr /><div><h4><p>Legendary in size and temper, great white whales are far more aggressive than their smaller kin.</p></h4></div></section>","img":"systems/pf1/icons/races/creature-types/animal.png","_id":"uyZ4qRccv4j7H26F"},
]

pp = pprint.PrettyPrinter(indent=4)
def toInt(text, search=None):
	try:	out = int(text)
	except:	out = text
	return out
def toList(text, search=None):
	try:	out = text.split(", ")
	except:	out = text
	return out
def remove_chars(text, search=None):
	numeric_filter = filter(str.isdigit, text)
	numeric_string = "".join(numeric_filter)
	return numeric_string
def remove_tags(html, search=None):
	# parse html content
	soup = BeautifulSoup(html, "html.parser")
	for data in soup(['style', 'script']):
		# Remove tags
		data.decompose()
	# return data by retrieving the tag content
	return ' '.join(soup.stripped_strings)
def remove_search(html, search=None):
	return html.replace(search,"").strip()
def extractValue(baseList, search, delimeters = [","], options=[]):
	out = None
	base = "__delimeter__".join(baseList)
	for d in delimeters:
		base = base.replace(d,"__delimeter__")
	base = base.split("__delimeter__")
	for i in base:
		m = re.search(search, i)
		if m:
			out = i
			for i in options:
				out = i(out, search)
	return out
def parse_title(soup, ob):
	upOb = {
	"title":soup.findAll("p")[0].getText(),
	"cr":int(soup.findAll("p")[1].getText().replace("CR ","")),
	}
	ob.update(upOb)
	return ob
def parse_xp(soup, ob):
	try:
		# print("+"*20)
		tagless = list(map(lambda x: remove_tags(x.getText()), soup.findAll("p")))
		# print(tagless)
		# print("+"*20)
		upOb = {
		"xp":			extractValue(tagless,"XP", delimeters=["(",")"], options=[remove_chars, toInt]),
		"type":			extractValue(tagless,"[LG|NG|CG|LN|N|CN|LE|NE|CE] ", delimeters=[","], options=[]),
		"initiative":	extractValue(tagless,"Init", delimeters=[";"], options=[remove_search, toInt]),
		"senses":		extractValue(tagless,"Senses", delimeters=[";"], options=[remove_search, toList]),
		"perception":	extractValue(tagless,"Perception", delimeters=[";"], options=[remove_search, toInt]),
		}
		ob.update(upOb)
	except Exception as e:	print("parse_xp", e)

	return ob
def parse_defense(soup, ob):
	try:
		# print("-"*20)
		tagless = list(map(lambda x: remove_tags(x.getText()), soup.findAll("p")))
		# print(tagless)
		# print("-"*20)

		upOb = {
			"ac": extractValue(tagless,"AC", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"touch": extractValue(tagless,"touch", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"flat-footed": extractValue(tagless,"flat", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"hp": extractValue(tagless,"hp", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"hd": extractValue(tagless,"[0-9]d[0-9]", delimeters=[",","(",")"], options=[]),
			"fortitude": extractValue(tagless,"Fort", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"reflex": extractValue(tagless,"Ref", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"will": extractValue(tagless,"Will", delimeters=[",","(",")"], options=[remove_chars, toInt]),
			"defensive_abilities": extractValue(tagless,"Defensive Abilities", delimeters=[";"], options=[remove_search, toList]),
			"defensive_abilities_immune": extractValue(tagless,"Immune", delimeters=[";"], options=[remove_search, toList]),
			"sr": extractValue(tagless,"SR", delimeters=[";"], options=[remove_chars, toInt]),
		}
		ob.update(upOb)
	except Exception as e:	print("parse_defense", e)
	return ob
def parse_offense(soup, ob):
	try:
		# print("-"*20)
		tagless = list(map(lambda x: remove_tags(x.getText()), soup.findAll("p")))
		# print(tagless)
		# print("-"*20)
		upOb = {
			"speed": extractValue(tagless,"Spd", delimeters=[",","(",")"], options=[remove_search, toList]),
			"melee": extractValue(tagless,"Melee", delimeters=[";"], options=[remove_search, toList]),
			"space": extractValue(tagless,"Space", delimeters=[";"], options=[remove_search]),
			"reach": extractValue(tagless,"Reach", delimeters=[";"], options=[remove_search]),
			"special_attacks": extractValue(tagless,"Special Attacks", delimeters=[";"], options=[remove_search, toList]),
			"spell_like_abilities": extractValue(tagless,"Spell-Like Abilities", delimeters=[], options=[remove_search]),
		}
		ob.update(upOb)
	except Exception as e:	print("parse_offense", e)
	return ob
def parse_statistics(soup, ob):
	# print("-"*20)
	tagless = list(map(lambda x: remove_tags(x.getText()), soup.findAll("p")))
	# print(tagless)
	# print("-"*20)
	upOb = {
		"strength": extractValue(tagless,"Str", delimeters=[",","(",")"], options=[remove_chars, toInt]),
		"dexterity": extractValue(tagless,"Dex", delimeters=[",","(",")"], options=[remove_chars, toInt]),
		"constitution": extractValue(tagless,"Con", delimeters=[",","(",")"], options=[remove_chars, toInt]),
		"intelligence": extractValue(tagless,"Int", delimeters=[",","(",")"], options=[remove_chars, toInt]),
		"wisdom": extractValue(tagless,"Wis", delimeters=[",","(",")"], options=[remove_chars, toInt]),
		"charisma": extractValue(tagless,"Cha", delimeters=[",","(",")"], options=[remove_chars, toInt]),
		"bab": extractValue(tagless,"Base Atk", delimeters=[";"], options=[remove_chars, toInt]),
		"cmb": extractValue(tagless,"CMB", delimeters=[";"], options=[remove_chars]),
		"cmd": extractValue(tagless,"CMD", delimeters=[";"], options=[remove_chars]),
		"feats": extractValue(tagless,"Feats", delimeters=[";"], options=[remove_search, toList]),
		"skills": extractValue(tagless,"Skills", delimeters=[";"], options=[remove_search, toList]),
		"special_qualities": extractValue(tagless,"SQ", delimeters=[";"], options=[remove_search]),
	}
	ob.update(upOb)
	return ob
def parse_environment(soup, ob):
	print("-"*20)
	tagless = list(map(lambda x: remove_tags(x.getText()), soup.findAll("p")))
	print(tagless)
	print("-"*20)
	upOb = {
		"environment": extractValue(tagless,"Environment", delimeters=[], options=[remove_search]),
		"organization": extractValue(tagless,"Organization", delimeters=[], options=[remove_search]),
		"treasure": extractValue(tagless,"Treasure", delimeters=[], options=[remove_search]),
	}
	ob.update(upOb)
	return ob
def parse_specialAbilities(soup, ob):
	# print(soup)
	upOb = {
	}
	ob.update(upOb)
	return ob
def parse_description(soup, ob):
	# print(soup)
	upOb = {
	}
	ob.update(upOb)
	return ob

fList = [
{"search": ">CR", "function":"title", "offset":0},
{"search": ">XP", "function":"xp", "offset":0},
{"search": ">AC", "function":"defense", "offset":0},
{"search": ">Spd", "function":"offense", "offset":0},
{"search": "Base Atk", "function":"statistics", "offset":0},
{"search": ">Environment ", "function":"environment", "offset":0},
{"search": ">SPECIAL ABILITIES", "function":"specialAbilities", "offset":2},
{"search": ">DESCRIPTION", "function":"description", "offset":2},
]

for a in actor:
	outOb = {}
	soup = BeautifulSoup(a["content"], 'html.parser')
	# print(soup.prettify())
	section = soup.section
	usedIndexs = []
	for i,s in enumerate(section):
		# print(i, s)
		for func in fList:
			if func["search"] in str(s):
				try:
					usedIndexs.append(i)
					usedIndexs.append(i+func["offset"])
					function = globals()["parse_"+func["function"]]
					outOb = function(list(section)[i+func["offset"]], outOb)
					continue
				except Exception as e:
					pass
					# print("e:",e)
	# print(usedIndexs)
	# for i,s in enumerate(section):
	# 	if i not in usedIndexs:
	# 		print("--",s)
	pp.pprint(outOb)
	print("-"*80)