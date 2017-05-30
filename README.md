A simple baseball game based on "Dice Baseball"

Moves derived from the game at:
http://baseballgames.dreamhosters.com/BbDiceHome.htm

This version is very much a pitcher's duel and does not result in a lot of high scoring
under normal circumstances.

Simple randint() function generates two numbers between 1-6
The result is returned and the baseball move is derived from the result.

The entire diamond and all moves are drawn using pygame polygon/rect/text functions. This
makes the entire program a litle cumbersone as a lot of objects are manually spaced and 
the position is determined through repetitive testing/movement.

Future improvedments include changing to a graphics based diamond and scoreboard, animating
movement of runners/plays, adding each play as a modal that must be cleared to slow down
game play slightly.

## --- TODO --- ##

* Add movements / arrows to make moves more intuitive
* Slow down game play slightly by adding a dely for dice roll or movement (see above)
* Change to a graphical diamond/scoreboard


