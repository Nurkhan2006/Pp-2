import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))        
pygame.display.set_caption("Mickey Clock")

clock_png = pygame.image.load(r"C:\Users\Hp\OneDrive\Рабочий стол\Pp-2\Lab7\image\clock.png")
left_hand = pygame.image.load(r"C:\Users\Hp\OneDrive\Рабочий стол\Pp-2\Lab7\image\left_hand.png")
right_hand = pygame.image.load(r"C:\Users\Hp\OneDrive\Рабочий стол\Pp-2\Lab7\image\right_hand.png")

clock_rect = clock_png.get_rect(center=(250, 250))

running = True
print("Clock size:", clock_png.get_size())
print("Left hand size:", left_hand.get_size())
print("Right hand size:", right_hand.get_size())

while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_png, clock_rect)

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    rotated_minute = pygame.transform.rotate(right_hand, minute_angle)
    rotated_second = pygame.transform.rotate(left_hand, second_angle)

    min_rect = rotated_minute.get_rect(center=clock_rect.center)
    sec_rect = rotated_second.get_rect(center=clock_rect.center)
    
    screen.blit(rotated_minute, min_rect)
    screen.blit(rotated_second, sec_rect)
   


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()
