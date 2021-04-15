import arcade
from Sprites.Sun import Ball
from Sprites.Bird import Bird
from Sprites.man import Man
from Sprites.Sun import Ball
class MyGame(arcade.Window):

    def __init__(self):
       # self.bird = None
        self.keyPressed = False
        self.key = None
        self.modifiers = None
        self.man = None
        self.ball = None
        self.speedOfSprite = 0
        self.sprite = None
        super().__init__(1000, 700,"Sony Game",update_rate=0.008) 
    
    def run(self):
        arcade.run()

    def setup(self):
        ###load all sprites
        arcade.set_background_color(arcade.color.WHITE)
       # self.bird = Bird(500, 500, 180, 180, 0, 180, 5)
        self.man = Man(30, 100, 10, 2, 1, ":resources:images/animated_characters/female_person/femalePerson_idle.png" )
        self.ball = Ball(50, 700, 10, 0, -1, 2)
        self.spriteList = arcade.SpriteList()
        self.spriteList.append(self.man)        
        print ("setup called")
        
   
    def on_draw(self):
        arcade.start_render()
        #self.bird.draw()
        self.spriteList.draw()
        self.ball.draw()
        
    def on_key_press(self, symbol, modifiers):
        #print("on key press",str(symbol),str(modifiers))
        self.keyPressed = True
        self.key = symbol
        self.modifiers = modifiers
        if (self.key == 65363):
            self.man.changePosition(1)

        elif (self.key == 65361):
            self.man.changePosition(-1)
        return super().on_key_press(symbol, modifiers)
        
    def on_key_release(self, symbol, modifiers):
        #print("on key release called")
        self.man.changePosition(0)
        return super().on_key_release(symbol, modifiers)
             

    def startOver(self):
        self.setup()

    def update(self, delta_time): 

        self.spriteList.update()              
        if(self.ball.y <= self.man.center_y+20 and self.ball.y >= 0):
            if(self.ball.x>=self.man.center_x-3 and self.ball.x<=self.man.center_x+3): #reflect up
                self.ball.dy=self.ball.speed
                self.ball.dx=0
            elif(self.ball.x >= self.man.center_x+4 and self.ball.x<=self.man.center_x+25): #reflect right
                self.ball.dy = self.ball.speed
                self.ball.dx = self.ball.speed       
            elif(self.ball.x <= self.man.center_x-4 and self.ball.x >= self.man.center_x-25): #reflect left
                self.ball.dy = self.ball.speed
                self.ball.dx = -self.ball.speed
        if(self.ball.x <= 0):              # to make left wall reflective
            self.ball.dx = self.ball.speed     
        elif(self.ball.x >= 1000):              # to make right wall reflective
            self.ball.dx = -self.ball.speed
        elif(self.ball.y >= 700):              # to make top wall reflective
            self.ball.dy = -self.ball.speed
        elif(self.ball.y <= 0):
            print("Game Over")
            self.startOver()

        self.ball.move() 
        

            
        return super().update(delta_time)


def main():
    mygame = MyGame()
    mygame.setup()
    mygame.run()

if __name__ == "__main__": 
    main()
























