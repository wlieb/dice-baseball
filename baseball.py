# dice baseball game
# by Will Liebhaber
# based on the game at http://baseballgames.dreamhosters.com/BbDiceHome.htm

import sys
from random import randint
import pygame
from pygame.locals import * 

batter = 1 # 0 for home, 1 for away
balls = 0 # number of balls in count
strikes = 0 # number of strikes in count
outs = 0 # number of outs
score = [0, 0] # home score, away score
runners = 111 # runners on 1st, 2nd, 3rd either 1 for no runner or 2 for runner on base
inning = 1 # 1st inning
dice = 2 #number of dice to roll
playres = ['','',''] #play result text

pygame.init()
  
def roll(numdice):  #roll the dice
    die = ''
    a = numdice #designed for possible game of 1, 2, or more dice

    while a >= 1:
        die = die + str(randint(1,6)) #randomly generate 1-6 and append to die
        a -= 1

    if die[1] < die[0]:
        die = die[1] + die[0]  # ensure that the result is always returned lowest number first
        
    return int(die)


def play(roll):  #get the resultant play
    global score #get global variables
    global batter
    global runners
    global balls
    global strikes
    global outs
    global inning

    move = ''
    result = ''
    error = ''

    if roll == 11:
        move = 'HOMERUN!'
        if runners == 111:
            score[batter] = score[batter] + 1
        elif runners == 222:
            score[batter] = score[batter] + 4
        elif runners == 212 or runners == 122 or runners == 221:
            score[batter] = score[batter] + 3
        else:
            score[batter] = score[batter] + 2
        balls = 0
        strikes = 0
        runners = 111

    elif roll == 12 or roll == 25 or roll == 36 or roll == 45:
        move = 'Strike!'
        strikes += 1

    elif roll == 13:
        if runners == 211 or runners == 221 or runners == 212 or runners == 122 or runners == 121 or runners == 112 or runners == 222:
            move = 'Double Play'
            outs += 2
            balls = 0
            strikes = 0

        if runners == 211:
            runners = 111
        elif runners == 221:
            runners = 112
        elif runners == 212 & outs < 3:
            runners = 111
            score[batter] += 1
        elif runners == 122 & outs < 3:
            runners = 111
            score[batter] += 1
        elif runners == 121:
            runners = 111
        elif runners == 112:
            runners = 111
        elif runners == 222 & outs < 3:
            runners = 112
            score[batter] += 1
        else:
            error = "No runners, 1 out only."
            outs += 1
            balls = 0
            strikes = 0

    elif roll == 14:
        move = 'Fly Out'
        outs += 1
        balls = 0
        strikes = 0

    elif roll == 15 or roll == 26 or roll == 34 or roll == 35 or roll == 46:
        move = 'Ball'
        balls += 1

    elif roll == 16:
        move = 'Stolen Base'
        if runners == 111:
            error = 'No runners on base, next roll...'
        elif runners == 211:
            runners = 121
        elif runners == 121:
            runners = 112
        elif runners == 112:
            error = 'No valid base to steal, next roll...'
        elif runners == 221:
            runners = 122
        elif runners == 122:
            error = 'No valid base to steal, next roll...'
        elif runners == 212:
            runners = 122
        elif runners == 222:
            error = 'No valid base to steal, next roll...'

    elif roll == 22:
        move = 'Triple'
        if runners == 111:
            runners = 112
        elif runners == 211:
            runners = 112
            score[batter] += 1
        elif runners == 121:
            runners = 112
            score[batter] += 1
        elif runners == 112:
            score[batter] += 1
        elif runners == 221:
            runners = 112
            score[batter] += 2
        elif runners == 122:
            runners = 112
            score[batter] += 2
        elif runners == 212:
            runners = 112
            score[batter] += 2
        elif runners == 222:
            runners = 112
            score[batter] += 3
        balls = 0
        strikes = 0

        #return 'TR'

    elif roll == 23 or roll == 56:
        #print('Groud Out')
        move = 'Ground Out'
        outs += 1
        balls = 0
        strikes = 0
        #return 'GO'

    elif roll == 24:
        #print('Foul Out')
        move = 'Foul Out'
        outs += 1
        balls = 0
        strikes = 0
        #return 'FO'

    elif roll == 33:
        #print('Double')
        move = 'Double'
        if runners == 111:
            runners = 121
        elif runners == 211:
            runners = 122
        elif runners == 121:
            score[batter] += 1
        elif runners == 112:
            runners = 121
            score[batter] += 1
        elif runners == 221:
            runners = 122
            score[batter] += 1
        elif runners == 122:
            runners = 121
            score[batter] += 2
        elif runners == 212:
            runners = 122
            score[batter] += 1
        elif runners == 222:
            runners = 122
            score[batter] += 2
        
        balls = 0
        strikes = 0

        #return 'DB'

    elif roll == 44:
        #print('Single')
        move = 'Single'

        if runners == 111:
            runners = 211
        elif runners == 211:
            runners = 221
        elif runners == 121:
            runners = 212
        elif runners == 112:
            runners = 211
            score[batter] += 1
        elif runners == 221:
            runners = 111
        elif runners == 122:
            runners = 212
            score[batter] += 1
        elif runners == 212:
            runners = 221
            score[batter] += 1
        elif runners == 222:
            runners = 222
            score[batter] += 1
        balls = 0
        strikes = 0
        #return 'SI'

    elif roll == 55:
        #print('Walk')
        move = 'Walk'

        if runners == 111:
            runners = 211
        elif runners == 211:
            runners = 221
        elif runners == 121:
            runners = 221
        elif runners == 112:
            runners = 212
        elif runners == 221:
            runners = 222
        elif runners == 122:
            runners = 222
        elif runners == 212:
            runners = 222
        elif runners == 222:
            runners = 222
            score[batter] += 1

        balls = 0
        strikes = 0
        #return 'WA'

    elif roll == 66:
        #print('Base on Error')
        move = 'Base on Error'

        if runners == 111:
            runners = 211
        elif runners == 211:
            runners = 221
        elif runners == 121:
            runners = 212
        elif runners == 112:
            runners = 211
            score[batter] += 1
        elif runners == 221:
            runners = 222
        elif runners == 122:
            runners = 212
            score[batter] += 1
        elif runners == 212:
            runners = 221
            score[batter] += 1
        elif runners == 222:
            runners = 222
            score[batter] += 1
        balls = 0
        strikes = 0
        #return 'ER'

        if strikes >= 3:
            result = 'Strike 3! You\'re Out!'
            outs += 1
            strikes = 0
            balls = 0

    if balls >= 4:
            #print('Ball 4, take your base...')
            result = 'Ball 4. Take your base.'
            if runners == 111:
                runners = 211
            elif runners == 211:
                runners = 221
            elif runners == 121:
                runners = 221
            elif runners == 112:
                runners = 212
            elif runners == 221:
                runners = 222
            elif runners == 122:
                runners = 222
            elif runners == 212:
                runners = 222
            elif runners == 222:
                runners = 222
                score[batter] += 1
            balls = 0
            strikes = 0

    if outs >= 3:
        if inning == 9:
            if batter == 1:
                if score[0] > score[1]:
                    #print('Game Over!')
                    #print('Home: ' + str(score[0]) + '  /  Away: ' + str(score[1]))
                    #print('Home Team Wins!')
                    #quit();
                    result = 'Game Over'
            elif batter == 0:
                if score[1] > score[0]:
                    #print('Game Over!')
                    #print('Home: ' + str(score[0]) + '  /  Away: ' + str(score[1]))
                    #print('Away Team Wins!')
                    #quit();
                    result = 'Game Over'

        #print('3 Outs, change sides...')
        result = '3 Outs, Change Sides'

        if batter == 1:
            batter -= 1
        else:
            batter += 1
            inning += 1
                
        outs = 0
        balls = 0
        strikes = 0
        runners = 111

    return move, result, error


def printboard(inn, bat, out, ball, strike, runner, score_home, score_away, move_text, result_text, error_text):
    #print('')
    
    #change required vairables to string
    inn = str(inn)
    out = str(out)
    ball = str(ball)
    strike = str(strike)
    runner = str(runner)
    score_home = str(score_home)
    score_away = str(score_away)

    #create surface
    DISPLAYSURF = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Dice Baseball')

    #set font (maybe change later)
    fontObj = pygame.font.Font('freesansbold.ttf', 18)

    #define rects
    backgroundrect = pygame.Rect(0, 0, 400, 400) #blue background
    gamerect = pygame.Rect(10, 10, 380, 380) #white game rectangle
    resRect = pygame.Rect(40, 200, 320, 60)

    #define colors (more than necessary)
    GREEN = pygame.Color(0, 255, 00)
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    BLUE = pygame.Color(0, 0, 255)
    RED = pygame.Color(255, 0, 0)
    YELLOW = pygame.Color(255, 255, 0)
    NAVY = pygame.Color(0, 0, 128)

    #display the background rects
    pygame.draw.rect(DISPLAYSURF, NAVY, backgroundrect)
    pygame.draw.rect(DISPLAYSURF, WHITE, gamerect)

    #draaw diamond with 30 px offset lower than centery
    pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx, gamerect.centery + 120), (gamerect.centerx + 90, gamerect.centery + 30), (gamerect.centerx, gamerect.centery - 60), (gamerect.centerx - 90, gamerect.centery + 30)), 5)
    pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx - 10, gamerect.centery + 130), (gamerect.centerx - 10, gamerect.centery + 120), (gamerect.centerx, gamerect.centery + 110), (gamerect.centerx + 10, gamerect.centery + 120), (gamerect.centerx + 10, gamerect.centery + 130)))
    pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
    pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx, gamerect.centery - 70), (gamerect.centerx - 10, gamerect.centery - 60), (gamerect.centerx, gamerect.centery - 50), (gamerect.centerx + 10, gamerect.centery - 60)))
    pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))

    #fill in bases
    pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 10, gamerect.centery + 130), (gamerect.centerx - 10, gamerect.centery + 120), (gamerect.centerx, gamerect.centery + 110), (gamerect.centerx + 10, gamerect.centery + 120), (gamerect.centerx + 10, gamerect.centery + 130)), 3)
    pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)), 3)
    pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx, gamerect.centery - 70), (gamerect.centerx - 10, gamerect.centery - 60), (gamerect.centerx, gamerect.centery - 50), (gamerect.centerx + 10, gamerect.centery - 60)), 3)
    pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)), 3)
    
    #draw the scoreboard
    textSurfaceObj = fontObj.render('Scoreboard', True, BLACK)
    
    #determin bottom or top of inning and print inninng number
    if bat == 1:
        innSurfaceObj = fontObj.render('Top of ' + inn, True, BLACK)
        innRectObj = innSurfaceObj.get_rect()
        innRectObj.center = (gamerect.left + 45, gamerect.top + 40)
    else:
        innSurfaceObj = fontObj.render('Bottom of ' + inn, True, BLACK)
        innRectObj = innSurfaceObj.get_rect()
        innRectObj.center = (gamerect.left + 63, gamerect.top + 40)
    
    #print score, outs, balls, strikes
    scoreSurfaceObj = fontObj.render('Home: ' + score_home + '  /  Away: ' + score_away, True, BLACK)
    outsSurfaceObj = fontObj.render('Outs: ' + out, True, BLACK)
    countSurfaceObj = fontObj.render('Balls: ' + ball + '  /  Strikes: ' + strike, True, BLACK)
    
    #display "Scoreboard"
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (gamerect.left + 63, gamerect.top + 20)
    
    #display "Home: x / Away: x"
    scoreRectObj = scoreSurfaceObj.get_rect()
    scoreRectObj.center = (gamerect.left + 95, gamerect.top + 60)
    
    #display "Outs: x"
    outsRectObj = outsSurfaceObj.get_rect()
    outsRectObj.center = (gamerect.left + 45, gamerect.top + 80)
    
    #display "Balls: x / Strikes: x"
    countRectObj = countSurfaceObj.get_rect()
    countRectObj.center = (gamerect.left + 101, gamerect.top + 100)

    #blit all objects to surface
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(innSurfaceObj, innRectObj)
    DISPLAYSURF.blit(scoreSurfaceObj, scoreRectObj)
    DISPLAYSURF.blit(outsSurfaceObj, outsRectObj)
    DISPLAYSURF.blit(countSurfaceObj, countRectObj)
    
    #display runner on 2nd
    if runners == 121 or runners == 122 or runners == 222 or runners ==221:
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx, gamerect.centery - 70), (gamerect.centerx - 10, gamerect.centery - 60), (gamerect.centerx, gamerect.centery - 50), (gamerect.centerx + 10, gamerect.centery - 60)))

    #clear 1st and second, runner on 2nd or  bases empty
    if runners == 121 or runners == 111:
        pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
        pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)), 3)
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)), 3)

    #display runners on 1st
    elif runners == 211 or runners == 221:
         pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
        
    #display runners on third
    elif runners == 112 or runners == 122:
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))
        
    #display runners on corners / 1st and 3rd
    elif runners == 212 or runners == 222:
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))
    
    #print error text (i.e. "No valid base to steal")
    if error_text == '':
        moveSurfaceObj = fontObj.render(move_text, True, BLACK)
        moveRectObj = moveSurfaceObj.get_rect()
        moveRectObj.center = (gamerect.centerx, gamerect.bottom - 30)
        DISPLAYSURF.blit(moveSurfaceObj, moveRectObj)
    else:
        #print move result with error text (i.e. "Stolen Base /n No runners on Base")
        moveSurfaceObj = fontObj.render(move_text, True, BLACK)
        moveRectObj = moveSurfaceObj.get_rect()
        moveRectObj.center = (gamerect.centerx, gamerect.bottom - 40)
        DISPLAYSURF.blit(moveSurfaceObj, moveRectObj)

        #display error text (i.e "No runners on base...")
        errorSurfaceObj = fontObj.render(error_text, True, BLACK)
        errorRectObj = errorSurfaceObj.get_rect()
        errorRectObj.center = (gamerect.centerx, gamerect.bottom - 20)
        DISPLAYSURF.blit(errorSurfaceObj, errorRectObj)

    if result_text != '':
        #print play result (i.e. "Change Sides, Game Over, Walk, ...")
        resSurfaceObj = fontObj.render(result_text, True, BLACK, WHITE)
        resRectObj = resSurfaceObj.get_rect()
        resRectObj.center = (gamerect.centerx, gamerect.centery + 30)
        pygame.draw.rect(DISPLAYSURF, WHITE, resRect)
        DISPLAYSURF.blit(resSurfaceObj, resRectObj)


printboard(inning, batter, outs, balls, strikes, runners, score[0], score[1], '', '', '')

#main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP and event.key == K_RETURN:
            playres = play(roll(dice))
            printboard(inning, batter, outs, balls, strikes, runners, score[0], score[1], playres[0], playres[1], playres[2])
    pygame.display.update() 