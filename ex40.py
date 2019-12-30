# practice creating a class
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Go Shawty, It's ya burfday",
                    "We gon' party like it's ya burfday",
                    "Sip bacardi like it's ya burfday"])

how_you_feeling = Song(["I do my hair toss",
                        "Check my nails",
                        "Baby how you feeling?",
                        "Feeling good as hell!"])

shining = ['Mouth talking dirty but my lips so clean',
            'On my body like a bumper car sticker']

happy_bday.sing_me_a_song()
how_you_feeling.sing_me_a_song()
# ---Lyrics in a separate var and passed to the class
print("*" * 20)
bey = Song(shining)
bey.sing_me_a_song()