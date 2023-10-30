import math
from karelPupper import Pupper, BehaviorState

# e4:5f:01:95:40:b4e

# Initialize Pupper
pupper = Pupper()

# Wake up the Pupper
pupper.wakeup()

# Move forward
pupper.forward_for_time(1.5, 0.5, behavior=BehaviorState.TROT)

# Walk in a square
for i in range(4):
    # Turn right
    pupper.turn(math.pi/2, 0.5, behavior=BehaviorState.TROT)
    # Walk forward
    pupper.forward_for_time(1.5, 0.5, behavior=BehaviorState.TROT)

# Rest the Pupper
pupper.rest()

