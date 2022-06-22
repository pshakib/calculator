
import pygame


BACKGROUND_COLOR = (41,41,43)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (88,89,91)
GREEN = (162,175,119)
ORANGE = (241,90,43)
BLUE = (65,162,197)
LIGHT_GRAY = (108,109,111)
LIGHT_ORANGE = (255,110,63)
LIGHT_BLUE = (85,182,217)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 420
window  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SHAKIB'S CALCULATOR")

class Button(object):
    def __init__(self,x,y,width,height,text,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.Font(None,40)
        self.text = self.font.render(text,True,WHITE)
        self.bg_color = color

    def draw(self,screen):
        pygame.draw.rect(screen,self.bg_color,self.rect)
        width = self.text.get_width()
        height = self.text.get_height()
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        screen.blit(self.text,(posX,posY))

    def isPressed(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
            
    def change_bg_color(self,color):
        self.bg_color = color


class Calculator(object):
    def __init__(self):
        self.btn_substraction = Button(245,150,60,40,"-",BLUE)
        self.btn_addition = Button(245,210,60,40,"+",BLUE)
        self.btn_multiplication = Button(245,270,60,40,"x",BLUE)
        self.btn_division = Button(245,330,60,40,"/",BLUE)
        self.btn_equal = Button(170,330,60,40,"=",ORANGE)
        
        self.prevVal = 0
        self.newVal = 0
        self.operator = ""
        self.resultVal = 0
         
        self.calculator_input = Calculator_input()
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
            self.calculator_input.event_handler(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_equal.isPressed():
                    self.calculate()
                    self.btn_equal.change_bg_color(LIGHT_ORANGE)
                                
                elif self.btn_addition.isPressed():
                    self.addition()
                    self.btn_addition.change_bg_color(LIGHT_BLUE)

                elif self.btn_substraction.isPressed():
                    self.substraction()
                    self.btn_substraction.change_bg_color(LIGHT_BLUE)
                    
                elif self.btn_multiplication.isPressed():
                    self.multiplication()
                    self.btn_multiplication.change_bg_color(LIGHT_BLUE)
                    
                elif self.btn_division.isPressed():
                    self.division()
                    self.btn_division.change_bg_color(LIGHT_BLUE)
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                self.btn_equal.change_bg_color(ORANGE)
                self.btn_addition.change_bg_color(BLUE)
                self.btn_substraction.change_bg_color(BLUE)
                self.btn_multiplication.change_bg_color(BLUE)
                self.btn_division.change_bg_color(BLUE)
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    self.addition()
                    self.btn_addition.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_KP_MINUS:
                    self.substraction()
                    self.btn_substraction.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_KP_MULTIPLY:
                    self.multiplication()
                    self.btn_multiplication.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_KP_DIVIDE:
                    self.division()
                    self.btn_division.change_bg_color(LIGHT_BLUE)
                    
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.calculate()
                    self.btn_equal.change_bg_color(LIGHT_ORANGE)
                
                elif event.key == pygame.K_ESCAPE:
                    self.calculator_input.set_value("0")
                    self.resultVal = 0
                    self.newVal = 0
                    self.prevVal = 0
                    self.operator = ""
                    
            elif event.type == pygame.KEYUP:
                self.btn_equal.change_bg_color(ORANGE)
                self.btn_addition.change_bg_color(BLUE)
                self.btn_substraction.change_bg_color(BLUE)
                self.btn_multiplication.change_bg_color(BLUE)
                self.btn_division.change_bg_color(BLUE)
                    
        return False
        
    
    def addition(self):
        self.prevVal = self.newVal
        self.operator = "+"
        self.calculator_input.set_value(str(self.newVal))
        
    def substraction(self):
        self.prevVal = self.newVal
        self.operator = "-"
        self.calculator_input.set_value(str(self.newVal))
        
    def multiplication(self):
        self.prevVal = self.newVal
        self.operator = "*"
        self.calculator_input.set_value(str(self.newVal))
        
    def division(self):
        self.prevVal = self.newVal
        self.operator = "/"
        self.calculator_input.set_value(str(self.newVal))
        
    def calculate(self):
        if self.operator == "+":
            self.resultVal = self.prevVal + self.newVal
            self.calculator_input.set_value(str(self.resultVal))
            self.newVal = self.resultVal
        elif self.operator == "-":
            self.resultVal = self.prevVal - self.newVal
            self.calculator_input.set_value(str(self.resultVal))
            self.newVal = self.resultVal
        elif self.operator == "*":
            self.resultVal = self.prevVal * self.newVal
            self.calculator_input.set_value(str(self.resultVal))
            self.newVal = self.resultVal
        elif self.operator == "/":
            try:
                self.resultVal = self.prevVal / self.newVal
                self.calculator_input.set_value(str(self.resultVal))
                self.newVal = self.resultVal
            except ZeroDivisionError:
                self.calculator_input.set_value("Math error")
                self.resultVal = 0
                self.newVal = 0
                self.prevVal = 0
                
        self.operator = ""
    
    def run_logic(self):
        if self.calculator_input.key_pressed:
            self.newVal = self.calculator_input.get_value()
            self.calculator_input.key_pressed = False
        
    def display_frame(self,screen):
        screen.fill(BACKGROUND_COLOR)

        self.btn_substraction.draw(screen)
        self.btn_addition.draw(screen)
        self.btn_multiplication.draw(screen)
        self.btn_division.draw(screen)
        self.btn_equal.draw(screen)
        self.calculator_input.draw(screen)
        
        pygame.display.flip()


class Calculator_input(object):
    def __init__(self):
        self.font = pygame.font.SysFont('Comic Sans MS', 35)
        self.text = self.font.render("0",True,BLACK)
        self.value = "0"
        self.btn0 = Button(20,330,60,40,"0",GRAY)
        self.btn1 = Button(20,270,60,40,"1",GRAY)
        self.btn2 = Button(95,270,60,40,"2",GRAY)
        self.btn3 = Button(170,270,60,40,"3",GRAY) 
        self.btn4 = Button(20,210,60,40,"4",GRAY)
        self.btn5 = Button(95,210,60,40,"5",GRAY)
        self.btn6 = Button(170,210,60,40,"6",GRAY)
        self.btn7 = Button(20,150,60,40,"7",GRAY)
        self.btn8 = Button(95,150,60,40,"8",GRAY)
        self.btn9 = Button(170,150,60,40,"9",GRAY)
        self.btn_point = Button(95,330,60,40,".",GRAY) 
        self.new_entry = True
        self.key_pressed = False

    def event_handler(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.btn0.isPressed():
                self.append_value("0")
                self.btn0.change_bg_color(LIGHT_GRAY)
            elif self.btn1.isPressed():
                self.append_value("1")
                self.btn1.change_bg_color(LIGHT_GRAY)
            elif self.btn2.isPressed():
                self.append_value("2")
                self.btn2.change_bg_color(LIGHT_GRAY)
            elif self.btn3.isPressed():
                self.append_value("3")
                self.btn3.change_bg_color(LIGHT_GRAY)
            elif self.btn4.isPressed():
                self.append_value("4")
                self.btn4.change_bg_color(LIGHT_GRAY)
            elif self.btn5.isPressed():
                self.append_value("5")
                self.btn5.change_bg_color(LIGHT_GRAY)
            elif self.btn6.isPressed():
                self.append_value("6")
                self.btn6.change_bg_color(LIGHT_GRAY)
            elif self.btn7.isPressed():
                self.append_value("7")
                self.btn7.change_bg_color(LIGHT_GRAY)
            elif self.btn8.isPressed():
                self.append_value("8")
                self.btn8.change_bg_color(LIGHT_GRAY)
            elif self.btn9.isPressed():
                self.append_value("9")
                self.btn9.change_bg_color(LIGHT_GRAY)
            elif self.btn_point.isPressed():
                self.append_point()
                self.btn_point.change_bg_color(LIGHT_GRAY)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.btn0.change_bg_color(GRAY)
            self.btn1.change_bg_color(GRAY)
            self.btn2.change_bg_color(GRAY)
            self.btn3.change_bg_color(GRAY)
            self.btn4.change_bg_color(GRAY)
            self.btn5.change_bg_color(GRAY)
            self.btn6.change_bg_color(GRAY)
            self.btn7.change_bg_color(GRAY)
            self.btn8.change_bg_color(GRAY)
            self.btn9.change_bg_color(GRAY)
            self.btn_point.change_bg_color(GRAY)
                
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                self.append_value("0")
                self.btn0.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                self.append_value("1")
                self.btn1.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                self.append_value("2")
                self.btn2.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                self.append_value("3")
                self.btn3.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                self.append_value("4")
                self.btn4.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                self.append_value("5")
                self.btn5.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                self.append_value("6")
                self.btn6.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                self.append_value("7")
                self.btn7.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                self.append_value("8")
                self.btn8.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                self.append_value("9")
                self.btn9.change_bg_color(LIGHT_GRAY)
            elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                self.append_point()
                self.btn_point.change_bg_color(LIGHT_GRAY)
                
                
        elif event.type == pygame.KEYUP:
            self.btn0.change_bg_color(GRAY)
            self.btn1.change_bg_color(GRAY)
            self.btn2.change_bg_color(GRAY)
            self.btn3.change_bg_color(GRAY)
            self.btn4.change_bg_color(GRAY)
            self.btn5.change_bg_color(GRAY)
            self.btn6.change_bg_color(GRAY)
            self.btn7.change_bg_color(GRAY)
            self.btn8.change_bg_color(GRAY)
            self.btn9.change_bg_color(GRAY)
            self.btn_point.change_bg_color(GRAY)
                
    def get_value(self):
        return float(self.value)
            
    def append_value(self,new_value):
        if self.text.get_width() < 260:
            if self.value == "0" or self.new_entry:
                self.value = new_value
                self.new_entry = False
            else:
                self.value += new_value
                
            self.text = self.font.render(self.value,True,BLACK)
            self.key_pressed = True
            
    def append_point(self):
        
        if self.new_entry:
            self.value = "0."
            self.text = self.font.render(self.value,True,BLACK)
            self.new_entry = False
        
        elif not "." in self.value:
            self.value += "."
            self.text = self.font.render(self.value,True,BLACK)
            
    def set_value(self,value):
        if value[-2:] == ".0":
            self.value = value[:-2]
        else:
            self.value = value
        self.new_entry = True
        self.text = self.font.render(self.value,True,BLACK)
        
    def draw(self,screen):
        posX = SCREEN_WIDTH - self.text.get_width() - 35
        pygame.draw.rect(screen,GREEN,pygame.Rect(20,20,280,95))
        screen.blit(self.text,(posX,40))
        self.btn0.draw(screen)
        self.btn1.draw(screen)
        self.btn2.draw(screen)
        self.btn3.draw(screen)
        self.btn4.draw(screen)
        self.btn5.draw(screen)
        self.btn6.draw(screen)
        self.btn7.draw(screen)
        self.btn8.draw(screen)
        self.btn9.draw(screen)
        self.btn_point.draw(screen)



def main():
    pygame.init()
    done = False
    clock = pygame.time.Clock()
    calculator = Calculator()
    
    while not done:
        done = calculator.process_events()
        calculator.run_logic()
        calculator.display_frame(window)
        clock.tick(30)
    
    pygame.quit()

if __name__ == '__main__':
    main()