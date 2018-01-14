player_x = 0
player_y = 0
player_size = 50
score = 0
asteroids_pos_x = 0
asteroids_pos_y = 0
asteroids_speed_x = 0
asteroids_speed_y = 2
asteroids_size = 35
y = 0
speed = 1
laser_y = 600
laser_size = 25

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
    global y
    global speed
    global laser_y
    global laser_size
    
    background(0)

    # Player ball
    fill(255, 255, 0)
    ellipse(player_x, player_y, 65, 65)

    # Player ball movement
    player_x = mouseX
    player_y = height - player_size / 2

    # Asteroid
    noStroke()
    fill(200)
    ellipse(asteroids_pos_x, asteroids_pos_y, asteroids_size, asteroids_size)

    # Asteroids falling
    asteroids_pos_y += asteroids_speed_y

    # Collision between asteroids and player ball
    radius_asteroids = asteroids_size / 2
    radius_player = player_size / 2
    a = asteroids_pos_x - player_x
    b = asteroids_pos_y - player_y
    distance = sqrt(a ** 2 + b ** 2)
    if distance <= radius_asteroids + radius_player:
        score = 0
        asteroids_pos_y = 0
        asteroids_pos_x = random(0, width)

    # Score
    fill(255)
    textSize(50)
    textAlign(LEFT)
    text(score, 20, 55)

    # Asteroids Respawn
    if asteroids_pos_y > height:
        asteroids_pos_y = 0
        asteroids_pos_x = random(0, width)
        
    # Shooting lasers
    lasers = [PVector(mouseX),PVector(mouseX), PVector(mouseX), PVector(mouseX)]
    for laser in lasers:
        fill(255, 255, 0)
        ellipse(mouseX, laser_y, 10, 25)
    for laser in lasers:
        laser_y -= speed
    if laser_y <= 0:
        laser_y = 600
        
    # radius_asteroids = asteroids_size / 2
    # radius_player = player_size / 2
    # a = asteroids_pos_x - player_x
    # b = asteroids_pos_y - player_y
    # distance = sqrt(a ** 2 + b ** 2)
    # if distance <= radius_asteroids + radius_player:
    #     score = 0
    #     asteroids_pos_y = 0
    #     asteroids_pos_x = random(0, width)
    #Collision
    radius_asteroids = asteroids_size / 2
    radius_laser = laser_size / 2
    a = asteroids_pos_x - mouseX
    b = asteroids_pos_y - laser_y
    distance = sqrt(a ** 2 + b ** 2)
    if distance <= radius_asteroids + radius_laser:
        score += 1
        asteroids_pos_y = 0
        asteroids_pos_x = random(0, width)
        laser_y = 600
    
    
    #Game Over
    if asteroids_pos_y == 600:
        score = 0
    #     fill(0, 255, 0)
    #     textSize(100)
    #     textAlign(CENTER)
    #     text("GAME OVER", 50, 75)    
        
