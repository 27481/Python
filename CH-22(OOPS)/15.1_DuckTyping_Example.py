# Duck typing aka similar to  Function overriding 

class Winapp:
    def play(self):
        print("singing")

class Spotify:
    def play(self):
        print("sing with Ads")

class WindowsMediaPlayer:
    def hang(self):
        print("sing with Ads")


def doSomething(player): 
    player.play()


obj=Winapp()
obj1=Spotify()
onj2=WindowsMediaPlayer()

doSomething(obj1)