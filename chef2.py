#---Inharitance---
from chef1 import chef1

class chef2(chef1):
    #         ^inharitance
    def make_fride_rice(self):
        print("the chef makes fried rice ")

print(chef2.make_chiken)