def move(roll):
    global score #get global variables
    global batter
    global runners
    global balls
    global strikes
    global outs
    global inning

    global DISPLAYSURF
    global gamerect

    fontObj = pygame.font.Font('freesansbold.ttf', 18)
    
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
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
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
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif runners == 211:
            runners = 121
        elif runners == 121:
            runners = 112
        elif runners == 112:
            #print('No valid base to steal, next roll...')
            textSurfaceObj = fontObj.render('No valid base to steal, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif runners == 221:
            runners = 122
        elif runners == 122:
           #print('No valid base to steal, next roll...')
            textSurfaceObj = fontObj.render('No valid base to steal, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif runners == 212:
            runners = 122
        elif runners == 222:
            #print('No valid base to steal, next roll...')
            textSurfaceObj = fontObj.render('No valid base to steal, next roll...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
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
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            outs += 1
            strikes = 0
            balls = 0

    if balls >= 4:
            #print('Ball 4, take your base...')
            textSurfaceObj = fontObj.render('Ball 4, take your base...', True, BLACK)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
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
                    textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            elif batter == 0:
                if score[1] > score[0]:
                    #print('Game Over!')
                    #print('Home: ' + str(score[0]) + '  /  Away: ' + str(score[1]))
                    #print('Away Team Wins!')
                    #quit();
                    textSurfaceObj = fontObj.render('Game Over', True, BLACK)
                    textRectObj = textSurfaceObj.get_rect()
                    textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
                    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        #print('3 Outs, change sides...')
        textSurfaceObj = fontObj.render('3 Outs, Change Sides', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (gamerect.centerx, gamerect.bottom - 50)
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