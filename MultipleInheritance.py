#smartphone system
class Camera:
    def __init__(self,camera_quality):
        self.camera_quality=camera_quality
    def display_camera_details(self):
        print("camera quality:",self.camera_quality)
        
class MusicPlayer:
    def __init__(self,sound_quality):
        self.sound_quality=sound_quality
    def display_music_details(self):
        print("sound quality:",self.sound_quality)
class Smartphone(Camera,MusicPlayer):
    def __init__(self,brand,camera_quality,sound_quality):
        self.brand=brand
        Camera.__init__(self,camera_quality)
        MusicPlayer.__init__(self,sound_quality)
        
    def display_smartphone_details(self):
        print("Brand:",self.brand)
       # Camera.display_camera_details(self) #super().display_camera_details()
        #MusicPlayer.display_music_details(self)
SP=Smartphone("apple","56pixel",78)
SP.display_smartphone_details()
SP.display_camera_details()
SP.display_music_details()