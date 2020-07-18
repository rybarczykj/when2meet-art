from PIL import Image, ImageOps

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


# trial 1 link: https://www.when2meet.com/?9272145-cDii7
# trail 2 link: https://www.when2meet.com/?9273442-hcOva
# trail 3 link: (creeper, bottom right edge cases failed): https://www.when2meet.com/?9273446-RIuto
# trail 4 link: (creeper, a little better): https://www.when2meet.com/?9273483-fzWRD
# trial 5 link: Error on edge case of color = 255: https://www.when2meet.com/?9273666-vY7dW
# Modern day clint: https://www.when2meet.com/?9275454-pNGWD
# Hibiscus: https://www.when2meet.com/?9275516-sZ8wx
# 420 Blaze It https://www.when2meet.com/?9275544-zHRN6
# Ben (first use of half boxes) https://www.when2meet.com/?9281376-zkgqq
# Modern day clint 2: https://www.when2meet.com/?9281470-Yu8dh
# Ben 2 (first use of quarter boxs) https://www.when2meet.com/?9282530-ccmrE
# Simpsons https://www.when2meet.com/?9282752-kvaBP
# Clint 3: https://www.when2meet.com/?9304127-2J6AV
# Clint 4: https://www.when2meet.com/?9304196-26mgu




IMAGE = "gop.jpg"
PIXEL_COUNT = 8
BOT_COUNT = 8
link = "https://www.when2meet.com/?9305356-xoIcn"
startbot = 0 # Which bot to start at, useful because it crashes halfway through commonly

class user:
    def __init__(self,name, numberOfDays, verticalPrecision):
        self.name = name
        self.numCols = numberOfDays
        self.numRows = verticalPrecision * self.numCols
        
        # Array of tuples to visit. format: (row, col)
        self.arr = [] 

        # Grid, defaulted as 0's where 1's represent squares this bot will visit
        self.grid = [[0 for col in range(self.numCols)] for row in range(self.numRows)] 

    def willVisit(self, row, col):
        """ 
        Records that this bot will visit a certain square
        """
        self.grid[row][col] = 1
        self.arr.append((row,col))

    
    def logIn(self, url = link):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(2)

        enter_name = self.driver.find_element_by_id("name")
        enter_name.send_keys(self.name)

        submit = WebDriverWait(self.driver,30).until(EC.presence_of_element_located(
                 (By.XPATH,'//*[@id="SignIn"]/div/div/input')))
        sleep(2)
        self.driver.execute_script("arguments[0].click();", submit)
        sleep(2)
        


    def enterAvailability(self):
        clicker = ActionChains(self.driver)

        for row in range(self.numRows):
            self.fillARow(row)

        self.stall()


        self.driver.implicitly_wait(5)
        sleep(2)
        self.driver.quit()            

    

    def fillARow(self, row):
        sleep(.1)
        row_arr = self.grid[row]

        clicker = ActionChains(self.driver)


        # Move cursor to the first element so that we don't start off-screen from the last row
        first = self.driver.find_element_by_xpath("//div[@data-col='%s'][@data-row='%s']"%(0, row))
        clicker.move_to_element(first).perform()
        # first.click()


        for col in range(self.numCols):
            if row_arr[col] == 1:
                for i in range(1):
                    box = self.driver.find_element_by_xpath("//div[@data-col='%s'][@data-row='%s']"%(col, row+i))
                    box.click()


    def stall(self):
        """
        This method simply clicks the top left square 10 times

        To be called at the end of filling out a calender to prevent the last few elements from dissapearing 
        (was a common issue previously due to leaving too soon).
        """
        clicker = ActionChains(self.driver)
        for i in range(10):
            box = self.driver.find_element_by_xpath("//div[@data-col='%s'][@data-row='%s']"%(0, 0))
            try:
                box.click()
            except:
                clicker.move_to_element(box).perform()

class photomaker:

    def __init__(self, numberOfDays, numberOfVisitors, img = IMAGE, verticalPrecision = 4):
        """
        verticalPrecision:
            Since 1 hour x 1 day = 1 square on when2meet.com, but we also can break up availbility
            within incremements of 15 minutes, to make a square image we can actually have 
            more vertical pixels available then horizontal pixels
                4 => use 15 minute increments
                2 => use 30 minute increments
                1 => use 1 hour incremements
        
        """
        self.image = img
        # self.users = []
        self.width = numberOfDays
        self.height = self.width * verticalPrecision

        self.numVisitors = numberOfVisitors

        
        # self.numVisitors = BOT_COUNT
        
        self.users = [user(i,self.width, verticalPrecision) for i in range(self.numVisitors)]
        self.grid = self.gridify()


    def gridify(self):
        """
        Given an image, turns it into a 2D array which tells how many bots need to 
        visit each square.
        
        
        """
        height = self.height
        width = self.width

        img = Image.open(self.image)
        gray_img = ImageOps.grayscale(img)

        # Resize smoothly down to 24x24 pixels
        gray_resized_img = gray_img.resize((width, height),resample=Image.BILINEAR)

        # Save the image
        gray_resized_img.save('result.png')

        # Get array of every pixel's value
        arr = list(gray_resized_img.getdata())


        # Flip every value because 255 means white and 0 means black  
        # Explanation:
        #   If we had 255 bots, we would want 255 bots to visit a black square,
        #   but RGB has black = 0 and white = 255, so we flip it 
        for i in range(len(arr)):
            new = 255 - arr[i]
            arr[i] = new

        # Adjust the range to account for my smallest and biggest, so that we can
        # have full black color and full white color
        # Example:
        #   If smallest = 50 and biggest = 200
        #   50 --> 0
        #   200 --> 255

        smallest = min(arr)
        biggest = max(arr)
        for i in range(len(arr)):
            num = (arr[i] - smallest) * 255/(biggest-smallest)
            arr[i] = int(num)

        # Translate color down to my number of bins
        #
        # Example: 
        #   if i have 5 bots, then I will have 6 bins (including white), so
        #   255 --> 5
        #   0 --> 0

        binSize = 255 / (self.numVisitors + 1) # (plus 1 to include white)
        for i in range(len(arr)):
            if arr[i] == 255: # edge case which usually made it too big
                arr[i] = self.numVisitors
            else:
                arr[i] = int(arr[i] // binSize)
            
        
        # Convert long list to 2d array:

        grid = [[0 for x in range(width)] for y in range(height)] 
        i = 0
        for row in range(height):
            for col in range(width):
                grid[row][col] = arr[i]
                i+=1

        # Make a record of each user who will visit this square
        # Form: tuple: (column, row)    
        for row in range(height):
            for col in range(width):
                val = grid[row][col]
                if val == 0:
                    pass
                else:
                    for i in range(0, val):
                        self.users[i].willVisit(row,col)

        return grid



def main():
    maker = photomaker(PIXEL_COUNT, BOT_COUNT, IMAGE)
    for row in maker.grid:
        print(row)

    users = maker.users

    curbot = 0
    while curbot < maker.numVisitors:
        u = maker.users[curbot]
        try:
            u.logIn()
            u.enterAvailability()
            curbot += 1
        except Exception as e:
            print("exception:", e)


    
    # for i in range(startbot,len(users)):
    #     u = maker.users[i]
    #     u.logIn()
    #     u.enterAvailability()





if __name__ == "__main__":
    main()