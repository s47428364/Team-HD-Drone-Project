import airsim
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

import keyboard

speed = 1  # Default speed

while True:
    if keyboard.is_pressed('up'):
        speed += 0.1  # Increase speed
    elif keyboard.is_pressed('down'):
        speed -= 0.1  # Decrease speed
    if keyboard.is_pressed('w'):
        client.moveByVelocityAsync(0, 1, 0, speed).join()  # Move forward
    elif keyboard.is_pressed('s'):
        client.moveByVelocityAsync(0, -1, 0, speed).join()  # Move backward
    elif keyboard.is_pressed('a'):
        client.moveByVelocityAsync(-1, 0, 0, speed).join()  # Move left
    elif keyboard.is_pressed('d'):
        client.moveByVelocityAsync(1, 0, 0, speed).join()  # Move right
    elif keyboard.is_pressed('space'):
        client.takeoffAsync().join()  # Take off
    elif keyboard.is_pressed('c'):
        client.landAsync().join()  # Land