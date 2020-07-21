# when2meet-art

www.when2meet.com is a popular web-based tool used to collaboratively schedule meetings. This tool takes advantage of the way when2meet presents results, a multi-shaded green gridlike calendar, to make fun pixel art on real schedules.


Gif of the tool in action:

![Gif of the tool in action](https://media.giphy.com/media/ZZScL3dNZOi3EZrogb/giphy.gif)



## How to use
For now, the only way to use this tool is from the command line, with a bit of setup steps (some of which I hope to automate in the future), but a lot of this is for personal reference. By the way I've only tried this on Mac. Not sure how/if it would work on Windows:

**Setting up:**
- Clone this repository
- Install the requirements from requirements.txt
- You'll need Google Chrome installed, as the script opens and operates on a google chrome window instance
- You'll also need the latest version of [chromedriver](https://chromedriver.chromium.org/) to allow out script to control chrome

**Using:**
- Choose the image you want rendered and add it to cloned repository
- Go to when2meet.com and create an event. 
	- the days:hours ratio of the event should roughly match the length:height ratio of the image (squares are easiest). 
	- Be sure the days you select are consecutive 
- From the command line, run `python when2meet.py` and follow the prompts

**Waiting:**
The program takes a few minutes to run, because selenium mimics user behavior so as to not overload the site / get blocked, but you can have the Chrome window run in the background. Just be careful not to click, hover, or change the window size as it might interfere with the script.

**Disclaiming:**
I don't really expect anybody to use this tool, but just in case I should say this project was made just for fun and is intended to be used as such. I didn't get permission from when2meet to do this, so if they find out about this I'm happy to take it down.

Finally, if you use the website a lot, consider making a donation to their paypal (link at the bottom of their website).
![mike and homer](https://i.imgur.com/XryMC38.png)





