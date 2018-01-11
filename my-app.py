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
laser1 = PVector (300, 300, 10)
laser2 = PVector (200, 150, 25)
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
    global laser1
    global laser2
    
    background(0)

    # Player ball
    fill(255, 255, 0)
    ellipse(player_x, player_y, 65, 65)

    # Player ball movement
    player_x = mouseX
    player_y = height - player_size / 2

    # Asteroid
    noStroke()
    fill(255, 255, 0)
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
    lasers = [laser1, laser2]
    for laser in lasers:
        fill(255, 0, 0)
        ellipse(300, 300, 50, 50)
    #Game Over
    # if asteroids_pos_y == 0:
    #     fill(0, 255, 0)
    #     textSize(100)
    #     textAlign(CENTER)
    #     text(score, 20, 55)
        
