import pygame
from time import sleep as slp

pygame.init()
pygame.display.set_caption("PASSWORD CHECKER")

WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60
SCREEN_FONT = pygame.font.SysFont('Comic sans MS',30)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

screen_window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

user_text = ''

input_rect = pygame.Rect(25, 675, 750, 100)
input_rect_color = (100,230,100)

class textBox():

    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.text_font = pygame.font.SysFont('Comic Sans MS', 18)

    def draw_textbox(self):
        img = self.text_font.render(self.text, True, WHITE)
        pygame.draw.rect(screen_window, (50, 200, 50), self.rect)
        text_rect = img.get_rect(center=self.rect.center)
        screen_window.blit(img, text_rect)

def draw(window, textboxes):
    global user_text, input_rect, input_rect_color

    window.fill(BLACK)

    if type(textboxes) is list or type(textboxes) is tuple:
        for textbox in textboxes:
            textbox.draw_textbox()
    else:
        textboxes.draw_textbox()

    pygame.draw.rect(screen_window, input_rect_color, input_rect)
    text_surface = SCREEN_FONT.render(user_text, True, WHITE)
    screen_window.blit(text_surface, (input_rect.x, input_rect.y+(input_rect.height*.25)))
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()

    pygame.display.update()

def checkPassword(password):
    if checkPassLength(password)


def checkPassLength(password):
    if len(password) > 8:
        return True
    else:
        return False



def main(window):
    global user_text, input_rect, input_rect_color

    clock = pygame.time.Clock()

    run = True
    while run:

        clock.tick(FPS)
        condition1 = textBox(110,25,650,75, text="Length")

        if len(user_text) > 8:
            condition1.text = "Password has good length"
        else:
            condition1.text = "Password has bad length"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text= user_text[:-1]
                else:
                    user_text += event.unicode

        draw(window,condition1)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(screen_window)