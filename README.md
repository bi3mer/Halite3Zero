# Halite3Zero

## Starter Kit

### Halite III starter kit components
* MyBot.{extension}, a starter bot outline
* /hlt directory, which contains modifiable helper functions for your bot
* A Halite executable that enables local playtesting of your bot
* The scripts run_game.bat (Windows) and run_game.sh (MacOS, Linux)

### Testing your bot locally
* Run run_game.bat (Windows) and run_game.sh (MacOS, Linux) to run a game of Halite III. By default, these scripts run a game of your MyBot.py bot vs. itself.  You can modify the board size, map seed, and the opponents of test games using the CLI.

### CLI
The Halite executable comes with a command line interface (CLI). Run `$ ./halite --help` to see a full listing of available flags.

### Submitting your bot
* Zip your MyBot.{extension} file and /hlt directory together.
* Submit your zipped file here: https://halite.io/play-programming-challenge

### Compiling your bot on our game servers
* Your bot has `10 minutes` to install dependencies and compile on the game server.
* You can run custom commands to set up your bot by including an `install.sh` file alongside `MyBot.{ext}`. This file will be executed and should be a Bash shell script. You must include the shebang line at the top: `#!/bin/bash`.
  * For Python, you may install packages using pip, but you may not install to the global package directory. Instead, install packages as follows: `python3.6 -m pip install --system --target . numpy`
* Some languages don't use the `MyBot.{ext}` convention. Exceptions include:
  * Rust: a Cargo.toml in the root will be detected as Rust. Your bot will compile with `cargo rustc`.
  * Swift: a Package.swift in the root will be detected as Swift. Your bot will compile with `swift build`.
  * Haskell: You may upload a MyBot.hs, or you may upload a `stack.yaml`, in which case your bot will compile with `stack build`.
  * Elixir: Upload a mix.exs. Your bot will compile with `mix deps.get` followed by `mix escript.build`.
  * Clojure: Upload a project.clj. Your bot will compile with `lein uberjar`.
  * .NET: Upload a MyBot.csproj or MyBot.fsproj. Your bot will compile with `dotnet restore` followed with `dotnet build`.

## HLT Client

Download client from [here](https://halite.io/assets/downloads/Halite3Tools.zip). Install with `python setup.py install`.

### Sample Commands

Download replay files by date:

```shell
python -m hlt_client replay date -t YYYYMMDD -d [destination_folder] ## Date example: 20181022
```

Download replay files by user:

```shell
python -m hlt_client replay user -i [user_id] -l [maximum_number_of_files] -d [destination_folder]
```

Also note, we can download as JSON instead:

```shell
python -m hlt_client replay date -t YYYYMMDD -d [destination_folder] --decompress
```

### Top 20 Ids

1. teccles
2. TheDuck314
3. cowzow
4. reCurs3
5. adam
6. cdurbin
7. Rachol
8. mlomb
9. TonyK
10. ZanderShah
11. Kowys
12. zxqfl
13. FiodorG
14. abenner
15. SiestaGuru
16. kovi
17. Jaraz
18. siman
19. ColinWHart
20. csmyu

## Training Phases
### Phase 1: Random

We play random agents until 10k valid games are generated. A game is 50 turns where there is no more than three ships. A valid game is one where the agent has collected 4500 halite. Once we have our 10k games, we train our net on this first batch of games.

Map Sizes: 32, 40, 48, 56, 64

### Phase 2: Collector Bot (one ship)

We play 5k one player games with one ship that will go to the closest halite source, collect, and return for 50 turns. We train our net on this batch of games.

Map Sizes: 32
Player count: 1

### Phase 3: Collector Bot (two ships)

We play 5k one player games with two ships that will go to the closest halite source, collect, and return for 50 turns. We train our net on this batch of games.

Map Sizes: 32
Player count: 1

### Phase 4: Sentdex Bot

We play against [hand crafted bot](https://www.youtube.com/watch?v=aMjSJGtXdeg) till we win. We train every thousand games played till we can win eighty times out of a hundred.

Map Sizes: 32, 40, 48, 56, 64
Player Count: 2, 4

### Phase 5: Imitation Bots

We play against imitations of the top twenty players listed above till we can win 80 out of a hundred games against every bot. 

Map Sizes: 32, 40, 48, 56, 64
Player Count: 2, 4

### Phase 6: Self Play

We play against ourselves with self play dqn and make sure we have something that forces us to improve or not train at all. While we wait for more imitation bots to be prepared. Once they are, go back to phase 5 and repeat till end of competition.

Map Sizes: 32, 40, 48, 56, 64
Player Count: 2, 4

## TODO:

* Get engine from HingedEmu if possible and update to support it
* Update data structure saved to support convolutions
* Update net to use convolutions and suppor
* Create visualizer of new data structure to make sure it looks correct
* Update trainer.py to support min games played
* Update trainer.py to include new tqdm bar to show progress in games played
* Update training_bot.py to include option to set whether the GPU is used or not
* Update trainer.py to allow only two games to run the GPU at a time
* Update trainer.py to run as many games as there are cores on the CPU at a time
* Update trainer.py to set the games to not timeout after 2 seconds so we can run on the CPU without fear
* Update trainer.py to do something other than log average halite collected (won't be useful with new updates)
* Random player with one ship
* Collector bot one ship
* Collector bot two ships
* Sentdex bot
* Imitation player creation
* Self play dqn
* Saving results to file to see results as training occurs