from pygame import mixer

mixer.init()
mixer.music.load('Checkmate.mp3')
mixer.music.play()
mixer.music.rewind()
input()