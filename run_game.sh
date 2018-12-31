#!/bin/sh

# ./halite --replay-directory replays/ -vvv --width 32 --height 32 --turn-limit 200 "python3 OneShipCollection.py oneShip" "python3 OneShipCollection.py sent"
./halite --replay-directory replays/ -vvv --width 32 --height 32 --turn-limit 200 "python3 OneShipCollection.py oneShip"
