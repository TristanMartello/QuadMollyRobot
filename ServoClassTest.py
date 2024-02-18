from time import sleep
from BigServoLibrary import BigServo


# Servo control notes:
#   - Start by meshing the gear with the servo at 180
#   - Going from 180 to 90 raises the arm mostly, 70 is the absolute max
#   - Going back to 180 lowers the arm the full extent

def main()
    bigBoy = BigServo()
    
    while True:
        direction = input()
        if direction == "a":
            

def fullTest(bigBoy):
    print("MinOut")
    bigBoy.minOut()

    print("MaxOut")
    bigBoy.maxOut()

    sleep(2)
    print("MaxOut Again")
    bigBoy.minOut()
    sleep(1)

    print("Full sweep")
    bigBoy.fullSweep()

main()