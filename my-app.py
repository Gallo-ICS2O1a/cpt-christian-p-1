player_x = 0
player_y = 0
player_size = 50
score = 0
asteroids_pos_x = 0
asteroids_pos_y = 0
asteroids_speed_x = 0
asteroids_speed_y = 2
asteroids_size = 35


def setup():
    size(600, 600)
def draw():
    global player_x
    global player_y
    global player_size
    global score 
    global asteroids_pos_x
    global asteroids_pos_y
    global asteroids_speed_x
    global asteroids_speed_y
    global asteroids_size
    background(0)
    
    #Player ball
    fill(255, 255, 0)
    ellipse(player_x, player_y , 65, 65)
    
    #Player ball movement
    player_x = mouseX
    player_y = height - player_size/2

    #Asteroids falling
   
        
        