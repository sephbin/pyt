link = "https://youtu.be/dDxF6OrtPBA?t=%s"


spots = [[732,"Intro"],
[3610,"How to create a book"],
[10854,"Check for errors across the book"],
[14867,"Q: Is there a way to split the book up without creating duplicate files?"],
[16356,"Page numbering and double page spreads"],
[21405,"Adding pages to a chapter"],
[22288,"Synchronising paragraph styles across chapters"],
[32587,"Writing content for InDesign"],
[44656,"Placing InCopy text into InDesign"],
[50112,"Editing assignments in InCopy and InDesign"],
[51829,"Opening InDesign files in InCopy"],
[57633,"Preparing InDesign files for InCopy editors"],
[62978,"Q: Do any of the directors already use InCopy?"],
[63691,"Q: Should we be using InCopy with all our InDesign documents?"],
[67639,"Q: Do assignments need to stay after someone has completed editing them?"],
[68701,"Q: Should we create an InDesign document first, and then import to InCopy?"],
[71787,"Q: Does making text and assignment in InDesign allow people to edit in InCopy?"],
[73423,"Using Dropbox with InDesign, InCopy and Assignments"],
[79322,"Place-holder Text demonstration"]]

for s in spots:
	print(s[1])
	print(link%int(s[0]/30),"\n")