# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [random.randrange(120.0, 240.0)/60.0, -random.randrange(60.0, 180.0)/60.0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [random.randrange(120, 240)/60, -random.randrange(60, 180)/60]
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

#helper function to update paddels
def p_update():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
    #paddles don't exit the canvas (top)
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel 
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel    

    if paddle1_pos + paddle1_vel >= HEIGHT - 29:
        paddle1_pos -= paddle1_vel
    if paddle2_pos + paddle2_vel >= HEIGHT - 29:
        paddle2_pos -= paddle2_vel    
    

def faster():    
    ball_vel[0] = (ball_vel[0] * 2)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS, hit1, hit2
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #ball reflection off top 
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    #ball reflection off left 
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
        
    
    #ball reflection of right
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS:
        ball_vel[0] = -ball_vel[0]
    
    #ball reflection of bottom
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
       
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "Yellow")
    
    #paddle is not gutter
    if ball_pos[1] >= (paddle1_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT):
        hit1 = True
    else:
        hit1 = False
    if ball_pos[1] >= (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT):
        hit2 = True
    else:
        hit2 = False 
        
    #hit gutter or not
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS) and hit1 == False:
        score2 += 1
        spawn_ball(False)
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS) and hit2 == False:
        score1 += 1
        spawn_ball(RIGHT)
        
    #increase acceleration by 10 percent
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        ball_vel[0] = (-ball_vel[0] * 1.1)

   

        
    
    
    # update paddle's vertical position, keep paddle on the screen
    p_update()
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")                                      
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Green")
                   
                    
    #draw scores
    canvas.draw_text(str(score1), (170, 50), 36, "Yellow")
    canvas.draw_text(str(score2), (400, 50), 36, "Yellow")
    

    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 100)
frame.add_button("Faster", faster, 100)


# start frame
new_game()
frame.start()

