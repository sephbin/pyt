import emails


message = emails.html(html="<p>Hi!<br>Here is your receipt...",
	subject="Your receipt No. 567098123",
	mail_from=('Cox Sync Boat', 'cox.sync.boat@gmail.com'))

r = message.send(to='andrew.butler@cox.com.au', smtp={'host': 'smtp.gmail.com', 'timeout': 5, "port": 465, 'user': 'cox.sync.boat@gmail.com', 'password': 'Britvahcritson10%'})