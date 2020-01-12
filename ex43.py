from sys import exit # exit from Python
from random import randint #returns a random integer
from textwrap import dedent # removes any common leading whitespace from every line of text. This can be used to make triple-quoted strings line up with the left edge of the display, while still presenting them in the source code in indented form.

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_screne_name(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()