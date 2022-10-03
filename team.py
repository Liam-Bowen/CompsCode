import pygame, sys
from pygame.locals import *

pygame.init()

pygame.font.init()

W, H = 1000, 700
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 100, 255]
light_blue = [0, 200, 255]
teal = [0, 255, 255]

# creates screen
screen.fill(white)
pygame.display.flip()

pygame.display.set_caption('My Team')

# Creates banner at top of page
pygame.draw.polygon(screen, light_blue, ((0, 0), (1000, 0), (1000, 100), (0, 100)))
pygame.draw.line(screen, black, (0, 100), (1000, 100), width=5)

# drawing background color for icons

# creates the font for the page
font = pygame.font.Font('freesansbold.ttf', 50)

# creates the My Team header
name = font.render('My Team', True, black)
nameRect = name.get_rect()
nameRect.center = (115, 50)
screen.blit(name, nameRect)

# Roster title
# pygame.draw.polygon(screen, light_blue, ((0, 103), (94, 103), (94, 139), (0, 139)))
# font = pygame.font.Font('freesansbold.ttf', 25)
# roster = font.render('Roster', True, black)
# rosterRect = roster.get_rect()
# rosterRect.center = (47, 125)
# screen.blit(roster, rosterRect)

# batter & pitcher & bench titles
pygame.draw.polygon(screen, teal, ((0, 103), (1000, 103), (1000, 139), (0, 139)))
pygame.draw.polygon(screen, teal, ((0, 366), (1000, 366), (1000, 404), (0, 404)))
pygame.draw.polygon(screen, teal, ((0, 611), (1000, 611), (1000, 649), (0, 649)))
font = pygame.font.Font('freesansbold.ttf', 25)
# pygame.draw.polygon(screen, teal, ((0, 141), (94, 141), (94, 159), (0, 159)))
# pygame.draw.polygon(screen, teal, ((0, 341), (94, 341), (94, 359), (0, 359)))
# pygame.draw.polygon(screen, teal, ((0, 501), (94, 501), (94, 519), (0, 519)))
# font = pygame.font.Font('freesansbold.ttf', 18)
batter = font.render('Batter', True, black)
batterRect = batter.get_rect()
batterRect.center = (45, 120)
screen.blit(batter, batterRect)

pitcher = font.render('Pitcher', True, black)
pitcherRect = pitcher.get_rect()
pitcherRect.center = (45, 385)
screen.blit(pitcher, pitcherRect)

# bench = font.render('Bench', True, black)
# benchRect = bench.get_rect()
# benchRect.center = (40, 530)
# screen.blit(bench, benchRect)

injured = font.render('Injured List', True, black)
injuredRect = injured.get_rect()
injuredRect.center = (70, 630)
screen.blit(injured, injuredRect)

# List of positions

font = pygame.font.Font('freesansbold.ttf', 16)

# catcher
catcher = font.render('C', True, black)
catcherRect = catcher.get_rect()
catcherRect.center = (47, 155)
screen.blit(catcher, catcherRect)

# first base
first = font.render('1B', True, black)
firstRect = first.get_rect()
firstRect.center = (47, 175)
screen.blit(first, firstRect)

# second base
second = font.render('2B', True, black)
secondRect = second.get_rect()
secondRect.center = (47, 195)
screen.blit(second, secondRect)

# third base
third = font.render('3B', True, black)
thirdRect = third.get_rect()
thirdRect.center = (47, 215)
screen.blit(third, thirdRect)

# shortstop
short = font.render('SS', True, black)
shortRect = short.get_rect()
shortRect.center = (47, 235)
screen.blit(short, shortRect)

# left field
left = font.render('LF', True, black)
leftRect = left.get_rect()
leftRect.center = (47, 255)
screen.blit(left, leftRect)

# center field
center = font.render('CF', True, black)
centerRect = center.get_rect()
centerRect.center = (47, 275)
screen.blit(center, centerRect)

# right field
right = font.render('RF', True, black)
rightRect = right.get_rect()
rightRect.center = (47, 295)
screen.blit(right, rightRect)

# designated hitter
dh = font.render('DH', True, black)
dhRect = dh.get_rect()
dhRect.center = (47, 315)
screen.blit(dh, dhRect)

# pitcher 1
p1 = font.render('P', True, black)
p1Rect = p1.get_rect()
p1Rect.center = (47, 420)
screen.blit(p1, p1Rect)

# pitcher 2
p2 = font.render('P', True, black)
p2Rect = p2.get_rect()
p2Rect.center = (47, 440)
screen.blit(p2, p2Rect)

# pitcher 3
p3 = font.render('P', True, black)
p3Rect = p3.get_rect()
p3Rect.center = (47, 460)
screen.blit(p3, p3Rect)

# pitcher 4
p4 = font.render('P', True, black)
p4Rect = p4.get_rect()
p4Rect.center = (47, 480)
screen.blit(p4, p4Rect)

# pitcher 5
p5 = font.render('P', True, black)
p5Rect = p5.get_rect()
p5Rect.center = (47, 500)
screen.blit(p5, p5Rect)

# pitcher 6
p6 = font.render('P', True, black)
p6Rect = p6.get_rect()
p6Rect.center = (47, 520)
screen.blit(p6, p6Rect)

# pitcher 7
p7 = font.render('P', True, black)
p7Rect = p7.get_rect()
p7Rect.center = (47, 540)
screen.blit(p7, p7Rect)

# bench 1
b1 = font.render('BE', True, black)
b1Rect = b1.get_rect()
b1Rect.center = (47, 335)
screen.blit(b1, b1Rect)

# bench 2
b2 = font.render('BE', True, black)
b2Rect = b2.get_rect()
b2Rect.center = (47, 355)
screen.blit(b2, b2Rect)

# bench 3
b3 = font.render('BE', True, black)
b3Rect = b3.get_rect()
b3Rect.center = (47, 560)
screen.blit(b3, b3Rect)

# bench 4
b4 = font.render('BE', True, black)
b4Rect = b4.get_rect()
b4Rect.center = (47, 580)
screen.blit(b4, b4Rect)

# bench 5
b5 = font.render('BE', True, black)
b5Rect = b5.get_rect()
b5Rect.center = (47, 600)
screen.blit(b5, b5Rect)

# injured 1
i1 = font.render('IR', True, black)
i1Rect = i1.get_rect()
i1Rect.center = (47, 665)
screen.blit(i1, i1Rect)

# injured 2
i2 = font.render('IR', True, black)
i2Rect = i2.get_rect()
i2Rect.center = (47, 685)
screen.blit(i2, i2Rect)

# player names


# stats to track

# player name
name = font.render('Name', True, black)
nameRect = name.get_rect()
nameRect.center = (135, 120)
screen.blit(name, nameRect)
pygame.draw.line(screen, black, (180, 100), (180, 610), width=3)

nameRect.center = (135, 385)
screen.blit(name, nameRect)

# At bats
ab = font.render('AB', True, black)
abRect = ab.get_rect()
abRect.center = (250, 120)
screen.blit(ab, abRect)

# Innings Pitched
ip = font.render('IP', True, black)
ipRect = ip.get_rect()
ipRect.center = (250, 385)
screen.blit(ip, ipRect)

pygame.draw.line(screen, black, (225, 100), (225, 610), width=3)

# Games
games = font.render('G', True, black)
gamesRect = games.get_rect()
gamesRect.center = (200, 120)
screen.blit(games, gamesRect)

gamesRect.center = (200, 385)
screen.blit(games, gamesRect)

pygame.draw.line(screen, black, (275, 100), (275, 610), width=3)

# Hits
hits = font.render('H', True, black)
hitsRect = hits.get_rect()
hitsRect.center = (300, 120)
screen.blit(hits, hitsRect)

# Wins
w = font.render('W', True, black)
wRect = w.get_rect()
wRect.center = (300, 385)
screen.blit(w, wRect)

pygame.draw.line(screen, black, (325, 100), (325, 610), width=3)

# Total Bases
tb = font.render('TB', True, black)
tbRect = tb.get_rect()
tbRect.center = (350, 120)
screen.blit(tb, tbRect)

# Losses
loss = font.render('L', True, black)
lRect = loss.get_rect()
lRect.center = (350, 385)
screen.blit(loss, lRect)

pygame.draw.line(screen, black, (375, 100), (375, 610), width=3)

# Runs
runs = font.render('R', True, black)
runsRect = runs.get_rect()
runsRect.center = (400, 120)
screen.blit(runs, runsRect)

# Saves
save = font.render('SV', True, black)
saveRect = save.get_rect()
saveRect.center = (400, 385)
screen.blit(save, saveRect)

pygame.draw.line(screen, black, (425, 100), (425, 610), width=3)

# Home runs
hr = font.render('HR', True, black)
hrRect = hr.get_rect()
hrRect.center = (450, 120)
screen.blit(hr, hrRect)

hrRect.center = (700, 385)
screen.blit(hr, hrRect)

# Blown Saves
bs = font.render('BS', True, black)
bsRect = bs.get_rect()
bsRect.center = (450, 385)
screen.blit(bs, bsRect)

pygame.draw.line(screen, black, (475, 100), (475, 610), width=3)

# Runs batted in
rbi = font.render('RBI', True, black)
rbiRect = rbi.get_rect()
rbiRect.center = (500, 120)
screen.blit(rbi, rbiRect)

# Holds
hold = font.render('H', True, black)
hRect = hold.get_rect()
hRect.center = (500, 385)
screen.blit(hold, hRect)

pygame.draw.line(screen, black, (525, 100), (525, 610), width=3)

# Walks
walk = font.render('BB', True, black)
walkRect = walk.get_rect()
walkRect.center = (550, 120)
screen.blit(walk, walkRect)

walkRect.center = (600, 385)
screen.blit(walk, walkRect)

pygame.draw.line(screen, black, (575, 100), (575, 610), width=3)

# Strikeouts
strike = font.render('K', True, black)
strikeRect = strike.get_rect()
strikeRect.center = (600, 120)
screen.blit(strike, strikeRect)

strikeRect.center = (550, 385)
screen.blit(strike, strikeRect)

pygame.draw.line(screen, black, (625, 100), (625, 610), width=3)

# Stolen bases
sb = font.render('SB', True, black)
sbRect = sb.get_rect()
sbRect.center = (650, 120)
screen.blit(sb, sbRect)

# Earned Runs
er = font.render('ER', True, black)
erRect = er.get_rect()
erRect.center = (650, 385)
screen.blit(er, erRect)

pygame.draw.line(screen, black, (675, 100), (675, 610), width=3)

# Caught stealing
cs = font.render('CS', True, black)
csRect = cs.get_rect()
csRect.center = (700, 120)
screen.blit(cs, csRect)

pygame.draw.line(screen, black, (725, 100), (725, 610), width=3)

# hit by pitch
hbp = font.render('HBP', True, black)
hbpRect = hbp.get_rect()
hbpRect.center = (750, 120)
screen.blit(hbp, hbpRect)

hbpRect.center = (850, 385)
screen.blit(hbp, hbpRect)

# complete games
cg = font.render('CG', True, black)
cgRect = cg.get_rect()
cgRect.center = (750, 385)
screen.blit(cg, cgRect)

pygame.draw.line(screen, black, (775, 100), (775, 610), width=3)

# shutouts
sho = font.render('SHO', True, black)
shoRect = sho.get_rect()
shoRect.center = (800, 385)
screen.blit(sho, shoRect)

# sacrifice flies
sf = font.render('SF', True, black)
sfRect = sf.get_rect()
sfRect.center = (800, 120)
screen.blit(sf, sfRect)

pygame.draw.line(screen, black, (825, 100), (825, 610), width=3)

# exit velocity 100+
ex = font.render('100+', True, black)
exRect = ex.get_rect()
exRect.center = (850, 120)
screen.blit(ex, exRect)

pygame.draw.line(screen, black, (875, 100), (875, 610), width=3)


# home run 450+ ft
hrd = font.render('450+', True, black)
hrdRect = hrd.get_rect()
hrdRect.center = (900, 120)
screen.blit(hrd, hrdRect)

# wild pitch
wp = font.render('WP', True, black)
wpRect = wp.get_rect()
wpRect.center = (900, 385)
screen.blit(wp, wpRect)

pygame.draw.line(screen, black, (925, 100), (925, 610), width=3)

# total points
tp = font.render('TP', True, black)
tpRect = tp.get_rect()
tpRect.center = (950, 120)
screen.blit(tp, tpRect)

tpRect.center = (950, 385)
screen.blit(tp, tpRect)

# vertical lines
pygame.draw.line(screen, black, (95, 100), (95, 610), width=3)

# horizontal lines
pygame.draw.line(screen, black, (0, 140), (1000, 140), width=3)
pygame.draw.line(screen, black, (0, 365), (1000, 365), width=3)
pygame.draw.line(screen, black, (0, 405), (1000, 405), width=3)
pygame.draw.line(screen, black, (0, 610), (1000, 610), width=3)
pygame.draw.line(screen, black, (0, 650), (1000, 650), width=3)

# buttons
players = font.render('Players', True, black)

width = screen.get_width()
height = screen.get_height()

red = [255, 100, 0]


while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()

    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, red, [width/2, height/2, 140, 40])
    else:
        pygame.draw.rect(screen, red, [width/2, height/2, 140, 40])

    screen.blit(players, (width/2+50, height/2))
    pygame.display.update()

pygame.display.update()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
