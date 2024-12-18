import pygame
from time import sleep as slp
from os.path import join

#Initializing pygame and caption
pygame.init()
pygame.key.set_repeat(500,100)
pygame.display.set_caption("PASSWORD CHECKER")

# ----- CONSTANTS -----
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60
SCREEN_FONT = pygame.font.SysFont('Comic sans MS',30)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

GREEN_SHADE = (50, 168, 82)
GREEN_PASTEL = (132, 224, 157)

VALID_CHARS = "abcdefghijklmnopqrstuvxyz0123456789"

# SCREEN
screen_window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#GLOBAL VAIRABLES FOR MAIN()

user_text = ''
validation_text = "Is password Valid?"
hint_text = 'Hint:'

valid_imgs = ("wait.png", "yes.png", "no.png")
vi_num = 0

input_rect = pygame.Rect(25, 675, 750, 100)
input_rect_color = (100,230,100)

# ---------- CLASSES ----------

class textBox():

    def __init__(self, x, y, width, height, text,want_center=True):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.color = GREEN_SHADE
        self.want_center = want_center
        self.text_font = pygame.font.SysFont('Comic Sans MS', 18)

    def draw_textbox(self):
        """DRAWS TEXTBOX AND TEXT"""
        img = self.text_font.render(self.text, True, WHITE)
        pygame.draw.rect(screen_window, self.color, self.rect)

        #Text position
        if self.want_center: #Center Text
            text_rect = img.get_rect(center=self.rect.center)
        else:
            text_rect = self.rect #Left Text
        screen_window.blit(img, text_rect)

class imageBox():

    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(join('password_assets','validation_imgs',image))

    def draw_image(self):
        screen_window.blit(self.image, (self.x, self.y))

# DRAW FUNCTION FOR SCREEN

def draw(window, textboxes,images):
    """DRAWS ON SCREEN ELEMENTS"""
    global user_text, input_rect, input_rect_color

    window.fill(BLACK)

    # DRAW TEXTBOXES ON SCREEN
    if type(textboxes) is list or type(textboxes) is tuple:
        for textbox in textboxes:
            textbox.draw_textbox()
    else:
        textboxes.draw_textbox()

    # DRAW IMAGES ON SCREEN
    if type(images) is list or type(images) is tuple:
        for image in images:
            if not image == "":
                image.draw_image()
    else:
        if not images == "":
            images.draw_image()

    # INPUT RECTANGLE DRAWN
    pygame.draw.rect(screen_window, input_rect_color, input_rect)
    text_surface = SCREEN_FONT.render(user_text, True, WHITE)
    screen_window.blit(text_surface, (input_rect.x, input_rect.y+(input_rect.height*.25)))
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()

    pygame.display.update()

# PASSWORD FUNCTIONS

def check_digit_and_letters(password):
    """Makes sure that the password (or input string) has both numbers and letters only"""
    if password.isalpha(): #CHECKS IF ALL LETTERS
        return False
    elif password.isdigit(): #CHECKS IF ALL NUMBERS
        return False
    elif check_specials(password): # CHECKS FOR SPECIAL CHARS
        return False
    else:
        return True
    
def has_alpha(password):
    """MAKES SURE PASSWORD (or inputted string) has atleast a letter in it"""
    for char in password:
        if char.isalpha():
            return True
    return False
    
def has_digit(password):
    """MAKES SURE PASSWORD (or inputted string) has atleast a number in it"""
    for char in password:
        if char.isdigit():
            return True
    return False
    
def check_specials(password):
    """MAKES SURE PASSWORD (or inputted string) does not have any special characters in it"""
    for char in password:
        if char not in VALID_CHARS:
            return True
    return False

def check_first_five(password):
    """Checks if the first five characters of the password( or input string)
    has only letters in it"""
    if check_pass_length(password,4)  and password[:5].isalpha():
        return True
    else:
        return False

def check_last_three(password):
    """Checks if password (or input string) has only numbers in the last 3 characters"""
    if check_pass_length(password, 2) and password[-3:].isdigit():
        return True
    else:
        return False

def check_pass_length(password, l=8):
    """Makes sure password( or input string) is long enough to set length"""
    if len(password) > l:
        return True
    else:
        return False

def validate_password(password):
    """validates password input"""
    if check_digit_and_letters(password) and has_alpha(password) and has_digit(password) and check_first_five(password) and check_last_three(password) and check_pass_length(password, l=8):
        return True
    else:
        return False

# MAIN(WINDOW)
def main(window):
    #Global text and input box
    global user_text, input_rect, input_rect_color, validation_text, hint_text, valid_imgs, vi_num

    # defining clock for FPS
    clock = pygame.time.Clock()

    #Running game
    run = True
    while run:

        #Setting FPS
        clock.tick(FPS)

        # TEXTBOXES

        checkbox_img = valid_imgs[vi_num]

        prompt = textBox(25,25,750,75, text="Type a password and type \"Enter\" to check validation!")

        validation_box = textBox(100,110,675,75, text=validation_text)
        hint = textBox(25,635, 750, 25, text = hint_text, want_center=False)

        checkbox = imageBox(25,110,75,75,checkbox_img)

        #Checking for events happening in program
        for event in pygame.event.get():

            #QUIT EVENT
            if event.type == pygame.QUIT:
                run = False
                break
                
            if event.type == pygame.KEYDOWN: #CHECKS IF A KEY HAS BEEN PRESSED
                if event.key == pygame.K_BACKSPACE: # BACKSPACE function
                    user_text= user_text[:-1]
                elif event.key == pygame.K_RETURN: # PRESSING ENTER

                    if validate_password(user_text):
                        validation_text = "Password is Valid"
                        hint_text = "Hint: None needed"
                        vi_num = 1
                    else:
                        # HINT TEXTS
                        validation_text = "Password is invalid"
                        vi_num = 2
                        if not check_pass_length(user_text):
                            hint_text = "Hint: Password needs to be longer" #SHORT PASSWORD
                        else:
                            if not check_digit_and_letters(user_text):
                                if user_text.isalpha(): # PASSWORD ONLY ALPHA
                                    hint_text = "Hint: Password needs some numbers in it" # NEEDS NUMBERS
                                elif user_text.isdigit(): # PASSSWORD ONLY NUMS
                                    hint_text = "Hint: Password needs some letters in it" # PASSWORD NEEDS ALPHA
                                elif check_specials(user_text): # CHECK FOR SPECIAL CHARACTERS
                                    hint_text = "Hint: Password can not contain special characters, letters and numbers only" # HAS SPECIAL CHARACTERS
                            else:
                                if not check_first_five(user_text): #COND1: LETTERS ONLY: FIRST 5 CHARS
                                    hint_text = "Hint: first 5 characters need to be letters only"
                                else:
                                    if not check_last_three(user_text): #COND2: NUMS ONLY: LAST 3 CHARS
                                        hint_text = "Hint: Last 3 characters needs to be numbers only"
                                
                else:
                    user_text += event.unicode

        draw(window,[validation_box, prompt, hint], checkbox) # updates screen

    pygame.quit()
    quit()

#Running

if __name__ == "__main__":
    main(screen_window)