# when2meet-art

## How to use
For now, the only way to use this tool is from the command line, with a few small setup steps (some of which I hope to automate in the future):

**Setting up:**
- Clone this repository
- Install the requirements from requirements.txt
- You'll also need Google Chrome installed, as the script opens and operates on a google chrome window instance

**Using:**
- Choose the image you want rendered and add it to cloned repository
- Go to when2meet.com and create an event. 
	- the days:hours ratio of the event should roughly match the length:height ratio of the image (squares are easiest). 
	- Be sure the days you select are consecutive 
- From the command line, run `python when2meet.py` and follow the prompts

**Waiting:**
The program takes a few minutes to run, because selenium mimics user behavior so as to not overload the site / get blocked, but you can have the Chrome window run in the background. Just be careful not to click, hover, or change the window size as it might interfere with the script.

**Disclaiming:**
I don't really expect anybody to use this tool, but just in case I should say this project was made just for fun and is intended to be used as such. I didn't get permission from when2meet to make this tool, so if they find out about this I'm happy to take it down.

Finally, if you use the website a lot, consider making a donation to their paypal (link at the bottom of their website).




