#!/bin/sh

# ./halite --replay-directory replays/ -vvv --width 32 --height 32 --turn-limit 200 "python3 OneShipCollection.py oneShip" "python3 OneShipCollection.py sent"
# ./halite --replay-directory replays/ -vvv --width 32 --height 32 --turn-limit 200 "python3 OneShipCollection.py oneShip"
# ./halite --replay-directory replays/ -vvv --width 32 --height 32 --turn-limit 100 "python3 OneShipCollection.py game_training_data/oneShip"
./halite --replay-directory replays/ -vvv --width 32 --height 32 --turn-limit 100 "python3 training_bot.py game_training_data/oneShip"