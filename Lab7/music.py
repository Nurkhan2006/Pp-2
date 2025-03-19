import pygame
import os

pygame.init()

songs_path = "C:\\Users\\Hp\\OneDrive\\Рабочий стол\\Pp-2\\Lab7\\songs"
songs = [f for f in os.listdir(songs_path) if f.endswith(".mp3")]
current_song = 0
pygame.mixer.init(frequency=44100, size=-16, channels=2)

pygame.mixer.music.load(os.path.join(songs_path, songs[current_song]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(os.path.join(songs_path, songs[current_song]))
    play_music()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    pygame.mixer.music.load(os.path.join(songs_path, songs[current_song]))
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()

pygame.quit()