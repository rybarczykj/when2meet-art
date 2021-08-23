# when2meet-art

www.when2meet.com is a popular web-based tool used to collaboratively schedule meetings. This tool takes advantage of the way when2meet presents results, a multi-shaded green gridlike calendar, to make fun pixel art on real schedules.


![mike and homer](https://i.imgur.com/XryMC38.png)

**Set up:**

[This is for personal reference. I don't expect people to use this.]

- Fork this repo
- Be sure Google Chrome installed, as the script opens and operates on a google chrome window instance
- You'll also need the latest version of [chromedriver](https://chromedriver.chromium.org/) to allow out script to control chrome

**Use:**
- Choose the image you want rendered and add it to cloned repository
- Go to when2meet.com and create an event. 
	- the days:hours ratio of the event should roughly match the length:height ratio of the image (squares are easiest). 
	- Be sure the days you select are consecutive 
- Run the tools from the command line and follow the prompts
- Don't move the mouse while it works. The script mocks human behavior and therefore requires you not to move the screen.

Gif of the tool in action:

![Gif of the tool in action](https://media.giphy.com/media/ZZScL3dNZOi3EZrogb/giphy.gif)
