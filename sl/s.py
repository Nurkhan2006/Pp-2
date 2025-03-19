import pygame
import os

pygame.init()

songs_path = r"C:\Users\Hp\OneDrive\Рабочий стол\Pp-2\Lab7\songs"

def get_songs():
    return [f for f in os.listdir(songs_path) if f.endswith(".mp3")]

songs = get_songs()
print("tracks:", songs)

current_song = 0
pygame.mixer.init(frequency=44100, size=-16, channels=2)
pygame.mixer.music.load(os.path.join(songs_path, songs[current_song]))

paused = False

def play_music():
    global paused
    pygame.mixer.music.play()
    paused = False
    print(f"playing: {songs[current_song]}")

def next_song():
    global current_song, paused
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(songs_path, songs[current_song]))
    play_music()

def prev_song():
    global current_song, paused
    current_song = (current_song - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(songs_path, songs[current_song]))
    play_music()

def pause_or_next():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
        print("пауза")
    else:
        print("paused – next")
        next_song()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Player")

next_img = pygame.image.load(r'C:\Pp-2\Lab7\image\next.png')
pause_img = pygame.image.load(r'C:\Pp-2\Lab7\image\pause.png')
play_img = pygame.image.load(r'C:\Pp-2\Lab7\image\pause1.png')   
prev_img = pygame.image.load(r'C:\Pp-2\Lab7\image\prev.png')

button_size = (60, 60)
next_img = pygame.transform.scale(next_img, button_size)
pause_img = pygame.transform.scale(pause_img, button_size)
pause1_img = pygame.transform.scale(play_img, button_size)
prev_img = pygame.transform.scale(prev_img, button_size)

button_width, button_height = button_size

next_button_pos = (250, 75)
pause_button_pos = (150, 75)
prev_button_pos = (50, 75)

def draw_buttons():
    screen.fill((255, 255, 255))
    screen.blit(prev_img, prev_button_pos)

    if paused:
        screen.blit(pause1_img, pause_button_pos)
    else:
        screen.blit(pause_img, pause_button_pos)
    screen.blit(next_img, next_button_pos)
    pygame.display.update()

play_music()

running = True
while running:
    draw_buttons()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
        
            if next_button_pos[0] <= mouse_x <= next_button_pos[0] + button_width and \
               next_button_pos[1] <= mouse_y <= next_button_pos[1] + button_height:
                next_song()
            
            elif prev_button_pos[0] <= mouse_x <= prev_button_pos[0] + button_width and \
                 prev_button_pos[1] <= mouse_y <= prev_button_pos[1] + button_height:
                prev_song()
            
            elif pause_button_pos[0] <= mouse_x <= pause_button_pos[0] + button_width and \
                 pause_button_pos[1] <= mouse_y <= pause_button_pos[1] + button_height:
                pause_or_next()
                
    if not pygame.mixer.music.get_busy() and not paused:
        print("end – next")
        next_song()

pygame.quit()
