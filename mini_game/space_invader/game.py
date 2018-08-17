from create_game import *
import os

#move left and right
def move_left(player, speed):
    x = player.xcor()
    x -= speed
    x = max(-280, x)
    player.setx(x)

def move_right(player, speed):
    x = player.xcor()
    x += speed
    x = min(280, x)
    player.setx(x)

def fire_bullet(player, bullet, speed):
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay audio/laser.wav&")
        bulletstate = "fire"
        x, y = player.xcor(), player.ycor()
        bullet.setposition(x, y+10)
        bullet.showturtle()

#check if an invader is hit
def isCollided(bullet, invader):
    bx, by = bullet.xcor(), bullet.ycor()
    ix, iy = invader.xcor(), invader.ycor()
    return ((bx-ix)**2 + (by-iy)**2) <= 15**2

def score_update(score, s):
    score.clear()
    score.write(f"Score: {s}", False, align="left", font=("Arial", 14, "normal"))

###############################################


if __name__ == "__main__":
    screen()
    draw_border()
    score = draw_score()
    player = create_player()
    invaders = create_invaders(5)
    bullet = create_bullet()
    playerspeed, invaderspeed, bulletspeed = 15, 2, 20
    bulletstate = "ready"
    points = 0
    #helper
    def ml():
        move_left(player, playerspeed)
    def mr():
        move_right(player, playerspeed)
    def fire():
        fire_bullet(player, bullet, bulletspeed)

    turtle.listen()
    turtle.onkey(ml, "Left")
    turtle.onkey(mr, "Right")
    turtle.onkey(fire, "space")

    game = False

    while not game:

        #move invaders
        for invader in invaders:
            x = invader.xcor()
            x += invaderspeed
            invader.setx(x)

            if abs(invader.xcor()) > 280:
                invaderspeed *= -1
                for i in invaders:
                    i.sety(i.ycor()-40)

        bullet.sety(bullet.ycor()+bulletspeed)

        #check whether bullet reach top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        #check if bullet hits invader
        for i in invaders:
            if isCollided(bullet, i):
                os.system("afplay audio/explosion.wav&")
                i.setposition(random.randint(-275, 275), random.randint(150, 250))
                points+=10
                score_update(score, points)
            if isCollided(player, i) or i.ycor() < -280 :
                os.system("afplay audio/explosion.wav&")
                game = True
                break

    print(f'GAMEOVER FINAL SCORE: {points}')
