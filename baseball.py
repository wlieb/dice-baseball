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

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Dice Baseball')

GREEN = pygame.Color(0, 255, 00)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 0, 255)
RED = pygame.Color(255, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
NAVY = pygame.Color(0, 0, 128)

gamerect = pygame.Rect(10, 10, 380, 380)
pygame.draw.rect(DISPLAYSURF, WHITE, gamerect)

def get_initial_diamond():
    #draw diamond with bases
    global gamerect
    global DISPLAYSURF
    
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
    fontObj = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObj = fontObj.render('Scoreboard', True, BLACK)
    textSurfaceObj4 = fontObj.render('Top of 1', True, BLACK)
    textSurfaceObj1 = fontObj.render('Home: 0  /  Away: 0', True, BLACK)
    textSurfaceObj2 = fontObj.render('Outs: 0', True, BLACK)
    textSurfaceObj3 = fontObj.render('Balls: 0  /  Strikes: 0', True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (gamerect.left + 110, gamerect.top + 20)
    textRectObj4 = textSurfaceObj4.get_rect()
    textRectObj4.center = (gamerect.left + 85, gamerect.top + 40)    
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (gamerect.left + 95, gamerect.top + 60)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (gamerect.left + 45, gamerect.top + 80)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = (gamerect.left + 101, gamerect.top + 100)

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)
    DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
    DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)


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
    global DISPLAYSURF

    if roll == 11:
        #print('HOMRERUN!')
        textSurfaceObj = fontObj.render('HOMERUN!', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'HR'
    elif roll == 12 or roll == 25 or roll == 36 or roll == 45:
        #print('Strike')
        textSurfaceObj = fontObj.render('Strike', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'ST'
    elif roll == 13:
        #print('Double Play')
        textSurfaceObj = fontObj.render('Double Play', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'DP'
    elif roll == 14:
        #print('Fly Out')
        textSurfaceObj = fontObj.render('Fly Out', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'FL'
    elif roll == 15 or roll == 26 or roll == 34 or roll == 35 or roll == 46:
        #print('Ball')
        textSurfaceObj = fontObj.render('Ball', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'BA'
    elif roll == 16:
        #print('Stolen Base')
        textSurfaceObj = fontObj.render('Stolen Base', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'SB'
    elif roll == 22:
        #print('Triple')
        textSurfaceObj = fontObj.render('Triple', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'TR'
    elif roll == 23 or roll == 56:
        #print('Groud Out')
        textSurfaceObj = fontObj.render('Ground Out', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'GO'
    elif roll == 24:
        #print('Foul Out')
        textSurfaceObj = fontObj.render('Foul Out', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'FO'
    elif roll == 33:
        #print('Double')
        textSurfaceObj = fontObj.render('Double', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'DB'
    elif roll == 44:
        #print('Single')
        textSurfaceObj = fontObj.render('Single', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'SI'
    elif roll == 55:
        #print('Walk')
        textSurfaceObj = fontObj.render('Walk', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'WA'
    elif roll == 66:
        #print('Base on Error')
        textSurfaceObj = fontObj.render('Base on Error', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return 'ER'


def move(roll):
    global score #get global variables
    global batter
    global runners
    global balls
    global strikes
    global outs
    global inning
    global DISPLAYSURF
    
    #determine runner movement, scoring, and outs
    if roll == 'HR':
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
    elif roll == 'ST':
        strikes += 1
    elif roll == 'DP':
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
            #print('No runners on base, one out only...')
            textSurfaceObj = fontObj.render('No runners on base, one out only...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            outs -= 1
        
        
    elif roll == 'FL':
        outs += 1
        balls = 0
        strikes = 0
    elif roll == 'BA':
        balls += 1
    elif roll == 'SB':
        if runners == 111:
            #print('No runners on base, next roll...')
            textSurfaceObj = fontObj.render('No runners on base, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif runners == 211:
            runners = 121
        elif runners == 121:
            runners = 112
        elif runners == 112:
            #print('No valid base to steal, next roll...')
            textSurfaceObj = fontObj.render('No valid base to steal, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif runners == 221:
            runners = 122
        elif runners == 122:
           #print('No valid base to steal, next roll...')
            textSurfaceObj = fontObj.render('No valid base to steal, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif runners == 212:
            runners = 122
        elif runners == 222:
            #print('No valid base to steal, next roll...')
            textSurfaceObj = fontObj.render('No valid base to steal, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    elif roll == 'TR':
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
    elif roll == 'GO':
        outs += 1
        balls = 0
        strikes = 0
    elif roll == 'FO':
        outs += 1
        balls = 0
        strikes = 0
    elif roll == 'DB':
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
    elif roll == 'SI':
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
    elif roll == 'WA':
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
    elif roll == 'ER':
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

    if strikes >= 3:
            #print('Strike 3! You\'re Out!')
            textSurfaceObj = fontObj.render('Strike 3! You\'re Out!', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            outs += 1
            strikes = 0
            balls = 0

    if balls >= 4:
            #print('Ball 4, take your base...')
            textSurfaceObj = fontObj.render('Ball 4, take your base...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
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
                    textSurfaceObj = fontObj.render('Game Over', True, BLACK)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            elif batter == 0:
                if score[1] > score[0]:
                    #print('Game Over!')
                    #print('Home: ' + str(score[0]) + '  /  Away: ' + str(score[1]))
                    #print('Away Team Wins!')
                    #quit();
                    textSurfaceObj = fontObj.render('Game Over', True, BLACK)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        #print('3 Outs, change sides...')
        textSurfaceObj = fontObj.render('3 Outs, Change Sides', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 10)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if batter == 1:
            batter -= 1
        else:
            batter += 1
            inning += 1
                
        outs = 0
        balls = 0
        strikes = 0
        runners = 111
            

    #if batter == 1:
    #    print('Inning: Top of ' + str(inning))
    #else:
    #    print('Inning: Bottom of ' + str(inning))
    #print('Home: ' + str(score[0]) + '  /  Away: ' + str(score[1]))
    #print('Outs: ' + str(outs))
    #print('Balls: ' + str(balls) + '  /  Strikes: ' + str(strikes))

def printboard(inn, bat, out, ball, strike, score_home, score_away):
    #print('')
    global DISPLAYSURF
    inn = str(inn)
    bat = str(bat)
    out = str(out)
    ball = str(ball)
    strike = str(strike)
    score_home = str(score_home)
    score_away = str(score_away)

    gamerect = pygame.Rect(10, 10, 380, 380)
    pygame.draw.rect(DISPLAYSURF, WHITE, gamerect)

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
    fontObj = pygame.font.Font('freesansbold.ttf', 18)
    textSurfaceObj = fontObj.render('Scoreboard', True, BLACK)
    if bat == 1:
        textSurfaceObj4 = fontObj.render('Top of ' + inn, True, BLACK)
    else:
        textSurfaceObj4 = fontObj.render('Bottom of ' + inn, True, BLACK)

    textSurfaceObj1 = fontObj.render('Home: ' + score_home + '  /  Away: ' + score_away, True, BLACK)
    textSurfaceObj2 = fontObj.render('Outs: ' + out, True, BLACK)
    textSurfaceObj3 = fontObj.render('Balls: ' + ball + '  /  Strikes: ' + strike, True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (gamerect.left + 110, gamerect.top + 20)
    textRectObj4 = textSurfaceObj4.get_rect()
    textRectObj4.center = (gamerect.left + 85, gamerect.top + 40)    
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (gamerect.left + 95, gamerect.top + 60)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (gamerect.left + 45, gamerect.top + 80)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = (gamerect.left + 101, gamerect.top + 100)

    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(textSurfaceObj4, textRectObj4)
    DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
    DISPLAYSURF.blit(textSurfaceObj3, textRectObj3)

    if runners == 121 or runners == 122 or runners == 222 or runners ==221:
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx, gamerect.centery - 70), (gamerect.centerx - 10, gamerect.centery - 60), (gamerect.centerx, gamerect.centery - 50), (gamerect.centerx + 10, gamerect.centery - 60)))
    
    #    print('          X         ')
    #else:
    #    print('          O         ')
    #print('         / \\       ')
    #print('        /   \\      ')
    if runners == 121 or runners == 111:
    #    print('       O     O     ')
        pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
        pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)), 3)
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)), 3)

    elif runners == 211 or runners == 221:
         pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
        
    #    print('       O     X     ')
    elif runners == 112 or runners == 122:
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))
        
    #    print('       X     O     ')
    elif runners == 212 or runners == 222:
        pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx + 100, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 40), (gamerect.centerx + 80, gamerect.centery + 30), (gamerect.centerx + 90, gamerect.centery + 20)))
        pygame.draw.polygon(DISPLAYSURF, WHITE, ((gamerect.centerx - 100, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 40), (gamerect.centerx - 80, gamerect.centery + 30), (gamerect.centerx - 90, gamerect.centery + 20)))
        
    #    print('       X     X     ')
    #print('        \\   /      ')
    #print('         \\ /       ')
    #print('          O        ')

ra = ''

#while ra != 'no':   
#    ra = input('continue?')
#    b = roll(dice)
#    c = play(b)
#    move(c)
#    printboard()
get_initial_diamond()

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP and event.key == K_RETURN:
            move(play(roll(dice)))
            printboard(inning, batter, outs, balls, strikes, score[0], score[1])
    pygame.display.update() 