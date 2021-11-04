sheetno = [
"1", "", "", "", "2", "3", "4", "5", "6", "7", "8", "1025", "9", "10", "11", "13", "14", "15", "1004", "16", "1007", "", "17", "18", "19", "20", "21", "22", "23", "", "", "", "", "", "", "", "24", "25", "26", "29", "28", "30", "", "31", "32", "1072", "33", "", "34", "35", "36", "", "37", "38", "1077", "1078", "45A", "", "39", "40", "41", "1088", "42", "43", "1124", "1131", "1132", "44", "45", "", "", "", "46", "47", "48", "49", "", "50", "51", "52", "", "", "", "53", "1001", "54", "55", "56", "1024", "57", "1052", "1057", "58", "1003", "59", "1070", "60", "1119", "61", "1071", "62", "1092", "9999", "", "63", "64", "65", "66", "", "66.B", "", "", "67", "68", "69", "70", "71", "72", "73", "1021", "73.A", "", "74", "75", "76", "77", "78", "1069", "79", "80", "73.B", "", "81", "82", "83", "84", "", "85", "86", "1128", "1129", "1130", "87", "88", "", "", "", "89", "90", "91", "92", "93", "", "94", "95", "96", "97", "1014", "1109", "1108", "1105", "1106", "98", "99", "", "100", "101", "102", "103", "104", "105", "1011", "106", "", "107", "108", "109", "", "", "", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "1125", "121", "122", "123", "124", "125", "126", "127", "128", "129", "", "130", "", "", "131", "1079", "", "132", "", "9999", "1122", "1005", "1006", "", "134", "135", "136", "137", "", "", "", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "148.A", "", "1083", "1084", "1086", "1085", "", "", "", "152", "153", "9999", "155", "156", "157", "", "158", "159", "", "256", "", "", "", "257", "138.A", "258", "1065", "160", "161", "259", "162", "163", "164", "", "165", "166", "167", "168", "169", "", "170", "171", "1064", "172", "173", "", "174", "", "175", "176", "177", "178", "179", "180", "", "181", "", "", "", "182.A", "1095", "182", "183", "184", "185", "186", "1098", "1097", "189", "190", "191", "1023", "192", "1094", "1096", "182.B", "", "193", "194", "", "195", "1076", "197", "1075", "199", "", "200", "201", "202", "", "203", "204", "1100", "1099", "205", "206", "", "207", "208", "", "209", "210", "1087", "", "211", "", "212", "1115", "1114", "1116", "215", "", "", "", "", "216", "217", "218", "", "", "219", "220", "1048", "222", "223", "224", "1051", "1067", "1068", "1035", "1036", "1060", "1061", "1037", "225", "", "226", "227", "228", "229", "230", "231", "1034", "1016", "1028", "1066", "1055", "1091", "1027", "1029", "232", "", "233", "234", "235", "236", "237", "238", "1090", "239", "1033", "1013", "1039", "1040", "1049", "1050", "1041", "1042", "1062", "1045", "1118", "1047", "1059", "1054", "1089", "1121", "1123", "1126", "240", "", "241", "1043", "242", "243", "244", "245", "1030", "1053", "1032", "1046", "1056", "246", "", "247", "248", "249", "250", "251", "1044", "1074", "1063", "252", "1058", "1026", "1107", "1103", "253", "", "254", "255", "", "", "", "", "1002", "1012", "1073", "1120", "1018", "1127", "1020", "1080", "1081", "1082", "1019",
 ]

dniids = {"9999":"",
 "1":"3",
 "2":"4",
 "3":"5",
 "4":"6",
 "5":"7",
 "6":"8", "7":"9", "8":"10", "9":"11", "10":"12", "11":"13", "13":"14", "14":"15", "15":"16", "16":"17", "17":"18", "18":"19", "19":"20", "20":"21", "21":"22", "22":"23", "23":"24", "24":"25", "25":"26", "26":"27", "27":"28", "28":"29", "29":"30", "30":"31", "31":"32", "32":"33", "33":"34", "34":"35", "35":"36", "36":"37", "37":"38", "38":"39", "39":"40", "40":"41", "41":"405", "42":"43", "43":"44", "44":"45", "45":"46", "45A":"47", "46":"48", "47":"49", "48":"50", "49":"51", "50":"52", "51":"53", "52":"54", "53":"55", "54":"56", "55":"57", "56":"58", "57":"59", "58":"60", "59":"61", "60":"62", "61":"63", "62":"64", "63":"65", "64":"66", "65":"67", "66":"68", "66.A":"69", "66.B":"70", "67":"71", "68":"72", "69":"73", "70":"74", "71":"75", "72":"76", "73":"77", "73.A":"78", "73.B":"79", "74":"80", "75":"81", "76":"82", "77":"83", "78":"84", "79":"85", "80":"86", "81":"87", "82":"88", "83":"89", "84":"90", "85":"91", "86":"92", "87":"93", "88":"94", "89":"95", "90":"96", "91":"97", "92":"98", "93":"99", "94":"100", "95":"101", "96":"102", "97":"103", "98":"104", "99":"105", "100":"106", "101":"107", "102":"108", "103":"109", "104":"110", "105":"111", "106":"112", "107":"113", "108":"114", "109":"115", "110":"116", "111":"117", "112":"118", "113":"119", "114":"120", "115":"121", "116":"122", "117":"123", "118":"124", "119":"125", "120":"126", "121":"127", "122":"128", "123":"129", "124":"130", "125":"131", "126":"132", "127":"133", "128":"", "129":"135", "130":"136", "131":"137", "132":"138", "1005":"139", "1006":"140", "134":"141", "135":"142", "136":"143", "137":"144", "138":"145", "139":"146", "140":"147", "141":"148", "142":"149", "143":"150", "144":"151", "145":"152", "146":"153", "147":"154", "148":"155", "149":"156", "150":"157", "151":"158", "152":"159", "153":"160", "155":"161", "156":"162", "157":"163", "158":"164", "159":"165", "160":"166", "161":"167", "162":"168", "163":"169", "164":"170", "165":"171", "166":"172", "167":"173", "168":"174", "169":"175", "170":"176", "171":"177", "172":"178", "173":"179", "174":"180", "175":"181", "176":"182", "177":"183", "178":"184", "179":"185", "180":"186", "181":"187", "200":"188", "182":"189", "183":"190", "184":"191", "185":"192", "186":"193", "187":"194", "188":"195", "189":"196", "190":"197", "191":"198", "192":"199", "193":"200", "194":"201", "195":"202", "196":"203", "197":"204", "198":"205", "199":"206", "201":"207", "202":"208", "203":"209", "204":"210", "205":"211", "206":"212", "207":"213", "208":"214",
"209":"215", "1003":"216", "210":"217", "211":"218", "212":"219", "213":"220", "214":"221", "215":"222", "216":"223", "217":"224", "218":"225", "219":"226", "220":"227", "221":"228", "222":"229", "223":"230", "224":"231", "225":"232", "226":"233", "227":"234", "228":"235", "229":"236", "230":"237", "231":"238", "232":"239", "233":"240", "234":"241", "235":"242", "236":"243", "237":"244", "1004":"245", "238":"246", "239":"247", "240":"248", "241":"249", "242":"250", "243":"251", "244":"252", "245":"253", "246":"254", "247":"255", "248":"256", "249":"257", "250":"258", "251":"259", "252":"260", "253":"261", "254":"262", "255":"263", "1002":"264", "256":"265", "257":"266", "258":"267", "259":"268", "1001":"269", "182.A":"270", "182.B":"271", "138.A":"272", "148.A":"273", "1010":"274", "1011":"275", "1012":"276", "1013":"277", "1014":"278", "1016":"279", "1017":"280", "1018":"281", "1019":"282", "1020":"283", "1021":"284", "1023":"285", "1024":"286", "1025":"287", "1026":"288", "1027":"289", "1028":"290", "1029":"291", "1030":"292", "1032":"293", "1033":"294", "1034":"295", "1035":"296", "1036":"297", "1037":"298", "1039":"299", "1040":"300", "1041":"301", "1042":"302", "1043":"303", "1044":"304", "1045":"305", "1046":"306", "1047":"307", "1048":"308", "1049":"309", "1050":"310", "1051":"311", "1052":"312", "1053":"313", "1054":"314", "1055":"315", "1056":"316", "1057":"317",
"1058":"318", "1059":"319", "1060":"320", "1061":"321", "1062":"322", "1063":"323", "1064":"324", "1065":"325", "1066":"326", "1067":"327", "1068":"328", "1069":"329", "1070":"330", "1071":"331", "1072":"332", "1073":"333", "1074":"334", "1075":"335", "1076":"336", "1077":"337", "1078":"338", "1079":"339", "1080":"396", "1081":"397", "1082":"404", "1083":"402", "1084":"401", "1085":"381", "1086":"403", "1087":"390", "1088":"42", "1089":"407", "1090":"382", "1091":"383", "1092":"384", "1094":"385", "1095":"386", "1096":"387", "1097":"388", "1098":"389", "1099":"391", "1100":"392", "1103":"394", "1105":"395", "1106":"406", "1107":"398", "1108":"399", "1109":"400", "1114":"409", "1115":"410", "1116":"411", "1118":"408", "1119":"428", "1120":"", "1121":"", "1122":"540", "1123":"", "1124":"541", "1125":"539", "1126":"", "1127":"542", "1128":"", "1129":"", "1130":"", "1131":"", "1132":""
}

for s in sheetno:
	try:
		print(dniids[s])
	except:
		print("")

