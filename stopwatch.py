# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
number_of_attempts = 0 
attempts = 0.0
correct = 0.0
current_number = 0
p_stop = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
t = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global current_number, n1, n2, n3, n4
    n1 = current_number // 600
    n2 = ((current_number // 100) % 6)
    n3 = ((current_number // 10) % 10)
    n4 = current_number % 10
    return str(n1) + ':' + str(n2) + str(n3) + '.' + str(n4)
    
    
    
    
    
#helper function to update score
def updater():
    global correct, attempts
    return str(correct) + ' ' + 'correct' + ' ' + '/' + ' '  + str(attempts) + ' ' + 'attempts'
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_h():
    timer1.start()
  
    
# handler to reset game    
def reset_h():
    global n1, n2, n3, n4, attempts, correct, current_number
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    attempts = 0.0
    correct = 0.0
    current_number = 0
    
#handler to stop game     
def stop_h():
    global attempts, correct, p_stop
    timer1.stop()
    if current_number != p_stop:
        attempts += 1
    if current_number % 10 == 0:
        correct += 1
    updater()    


        
        
            
# define event handler for timer with 0.1 sec interval
def stopwatch_ticker():
    global current_number
    current_number += 1
    return current_number

def calcpercentage():
    global attempts, correct
    if correct == 0:
        return "You are 0 percent correct"
    else:
        return 'You are' + ' ' + str((correct / attempts) * 100) + ' ' + 'percent correct.'
     
        


    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t), (100, 150), 50, "Yellow")
    canvas.draw_text(updater(), (0, 20), 20, "Red")
    canvas.draw_text(calcpercentage(), (0, 45), 20, "White")
    
# create frame
frame_stopwatch = simplegui.create_frame("The Stopwatch GAME!", 400, 400)


# register event handlers
timer1 = simplegui.create_timer(100, stopwatch_ticker)
frame_stopwatch.set_draw_handler(draw_handler)
start = frame_stopwatch.add_button("Start the Game", start_h, 50)
stop = frame_stopwatch.add_button("Stop the Game", stop_h, 50)
reset = frame_stopwatch.add_button("Reset the Game", reset_h, 50)
# start frame
frame_stopwatch.start()

# Please remember to review the grading rubric

