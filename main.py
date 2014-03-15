__author__ = 'octopuscabbage'
from ghoster import Ghoster
def main():
    g = Ghoster()
    g.load_dict("SOWPODS.txt")
    while(True):
        letters = input("What's the round at [-1 for challenge] >> ")
        output = g.do_round(letters)
        g.last_input = letters + output
        print(output)

main()
