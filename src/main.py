from src.insect import Insect

if __name__ == "__main__":
    insects = [Insect() for _ in range(4)]
    insects[0] = Insect()
    insects[1] = Insect("Scorpion", 6, False, True, True)
    insects[2] = Insect.get_instance()
    insects[3] = Insect.get_instance()

    for insect in insects:
        print("Is " + insect.name + " poisonous? - " + str(insect.is_poisonous()))

    insects[1].wake_up()
    insects[2].hibernate()

    for insect in insects:
        print(insect.__str__())

