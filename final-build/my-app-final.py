player_x = 0
player_y = 0
player_size = 50
score = 0
asteroids_pos_x = 0
asteroids_pos_x1 = 100
asteroids_pos_x2 = 200
asteroids_pos_x3 = 300
asteroids_pos_y = 0
asteroids_pos_y1 = 0
asteroids_pos_y2 = 0
asteroids_pos_y3 = 0
asteroids_speed_x = 0
asteroids_speed_y = 2.5
asteroids_size = 35
speed = 2
laser_y = 600
laser_size = 25
Text = "YOU WIN"
BONUS = "BONUS"
Instructions = "ASTEROIDS ARE FALLING IT IS YOUR JOB TO DESTROY 50 OF THEM"
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
    global speed
    global laser_y
    global laser_size
    global asteroids_pos_x1
    global asteroids_pos_y1
    global asteroids_pos_x2
    global asteroids_pos_y2
    global asteroids_pos_x3
    global asteroids_pos_y3
    global Text
    global Instructions
    global BONUS
    background(0)
    # Instructions
    if score == 0:
        asteroids_speed_y = 1
        speed = 0.5
        fill(0, 255, 0)
        textSize(15)
        textAlign(CENTER)
        text(Instructions, 300, 300)
    else:
        asteroids_speed_y = 2.5
        speed = 2
    # Player ball
    fill(255, 255, 0)
    ellipse(player_x, player_y, 65, 65)
    # Player ball movement
    player_x = mouseX
    player_y = height - player_size / 2
    # Asteroids
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
    lasers = [PVector(mouseX), PVector(mouseX), PVector(mouseX), PVector(mouseX)]
    for laser in lasers:
        fill(255, 255, 0)
        ellipse(mouseX, laser_y, 10, 25)
    for laser in lasers:
        laser_y -= speed
    if laser_y <= 0:
        laser_y = 600
    # Asteroid - player collision
    radius_asteroids = asteroids_size / 2
    radius_player = player_size / 2
    a = asteroids_pos_x - player_x
    b = asteroids_pos_y - player_y
    distance = sqrt(a ** 2 + b ** 2)
    if distance <= radius_asteroids + radius_player:
        score = 0
        asteroids_pos_y = 0
        asteroids_pos_x = random(0, width)
    # Collision
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
    # Game Over
    if asteroids_pos_y == 600:
        score = 0
    # If score = 5
    if score >= 5:
        # Asteroids
        noStroke()
        fill(200)
        ellipse(asteroids_pos_x1, asteroids_pos_y1, asteroids_size, asteroids_size)
        # Respawn
        asteroids_pos_y1 += asteroids_speed_y
        # Collision PLAYER - ASTEROID
        radius_asteroids = asteroids_size / 2
        radius_player = player_size / 2
        a = asteroids_pos_x1 - player_x
        b = asteroids_pos_y1 - player_y
        distance = sqrt(a ** 2 + b ** 2)
        if distance <= radius_asteroids + radius_player:
            score = 0
            asteroids_pos_y1 = 0
            asteroids_pos_x1 = random(0, width)
        # COLLISION ASTEROID-LASER
        radius_asteroids = asteroids_size / 2
        radius_laser = laser_size / 2
        a = asteroids_pos_x1 - mouseX
        b = asteroids_pos_y1 - laser_y
        distance = sqrt(a ** 2 + b ** 2)
        if distance <= radius_asteroids + radius_laser:
            score += 1
            asteroids_pos_y1 = 0
            asteroids_pos_x1 = random(0, width)
            laser_y = 600
        # Asteroids Respawn
        if asteroids_pos_y1 > height:
            asteroids_pos_y1 = 0
            asteroids_pos_x1 = random(0, width)
    # If score = 25
    if score >= 25:
        # Asteroids
        noStroke()
        fill(200)
        ellipse(asteroids_pos_x2, asteroids_pos_y2, asteroids_size, asteroids_size)
        # Respawn
        asteroids_pos_y2 += asteroids_speed_y
        # Collision PLAYER - ASTEROID
        radius_asteroids = asteroids_size / 2
        radius_player = player_size / 2
        a = asteroids_pos_x2 - player_x
        b = asteroids_pos_y2 - player_y
        distance = sqrt(a ** 2 + b ** 2)
        if distance <= radius_asteroids + radius_player:
            score = 0
            asteroids_pos_y2 = 0
            asteroids_pos_x2 = random(0, width)
        # COLLISION ASTEROID-LASER
        radius_asteroids = asteroids_size / 2
        radius_laser = laser_size / 2
        a = asteroids_pos_x2 - mouseX
        b = asteroids_pos_y2 - laser_y
        distance = sqrt(a ** 2 + b ** 2)
        if distance <= radius_asteroids + radius_laser:
            score += 1
            asteroids_pos_y2 = 0
            asteroids_pos_x2 = random(0, width)
            laser_y = 600
        # Asteroids Respawn
        if asteroids_pos_y2 > height:
            asteroids_pos_y2 = 0
            asteroids_pos_x2 = random(0, width)
    # If score = 40
    # Asteroids
    if score >= 40:
        noStroke()
        fill(200)
        ellipse(asteroids_pos_x3, asteroids_pos_y3, asteroids_size, asteroids_size)
        # Respawn
        asteroids_pos_y3 += asteroids_speed_y
        # Collision PLAYER - ASTEROID
        radius_asteroids = asteroids_size / 2
        radius_player = player_size / 2
        a = asteroids_pos_x3 - player_x
        b = asteroids_pos_y3 - player_y
        distance = sqrt(a ** 2 + b ** 2)
        if distance <= radius_asteroids + radius_player:
            score = 0
            asteroids_pos_y3 = 0
            asteroids_pos_x3 = random(0, width)
        # COLLISION ASTEROID-LASER
        radius_asteroids = asteroids_size / 2
        radius_laser = laser_size / 2
        a = asteroids_pos_x3 - mouseX
        b = asteroids_pos_y3 - laser_y
        distance = sqrt(a ** 2 + b ** 2)
        if distance <= radius_asteroids + radius_laser:
            score += 1
            asteroids_pos_y3 = 0
            asteroids_pos_x3 = random(0, width)
            laser_y = 600
        # Asteroids Respawn
        if asteroids_pos_y3 > height:
            asteroids_pos_y3 = 0
            asteroids_pos_x3 = random(0, width)
        # YOU WIN
        if score == 50:
            asteroids_pos_y == 600
            fill(255)
            textSize(50)
            textAlign(CENTER)
            text(Text, 300, 300)
        if score == 51:
            fill(255)
            textSize(75)
            textAlign(CENTER)
            text(BONUS, 300, 300)

