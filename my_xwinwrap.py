#!/usr/bin/env python3
# coding: utf8

import os
import time
from datetime import datetime

command = "xwinwrap -ni -o 1 -fs -s -st -b -nf -- mplayer -wid WID -nosound -loop 0"

kills = ["xwinwrap", "mplayer"]
killCommand = "killall -KILL"

# Ici tu ajoutes tes vidéos, l'heure de début et la durée
# ex: ("/Chemin/de/ta/vidéo", heureDeDébut, durée)
# c'est un tableau donc tu met une ',' à la fin de chacune de tes entrées sauf la dernière ^^
videos = [
	("/Chemin/LifeIsStrange2.mp4", 6, 6),
	("other2", 12, 4),
	("other3", 16, 4),
	("other3", 20, 4),
	("other3", 0, 6)
]

actualId = None

while (42):
	timeNow = datetime.now()
	for idVideo, video in enumerate(videos):
		if (timeNow.hour >= video[1]
			and timeNow.hour < video[1] + video[2]
			and actualId != idVideo):
			[os.system("{} {}".format(killCommand, kill)) for kill in kills]
			os.system("{} {} &".format(command, video[0]))
			actualId = idVideo
			time.sleep(60)
