# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

https://github.com/gygabor/zerda-exam-python/blob/master/third%20(1).png

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

The simpliest way if you use the standard Graphical User Interface (GUI) of python. It's the tkinter framework. You need import the tkinter modules (e.g. from tkinter import * ). After that you shoud create a TK() object. 

For drawing the Tk object should contain a canvas. Create a canvas widget. You have to add the size of the canvas. You have a lot of options to design the canvas (e.g. you can add background color with the "fill" argument). 

Now you create a rectangle with the "create_rectangle" canvas widget. You have to add the top left, and the bottom, right corners of the rectangle (x0, y0, x1, y1). You can add more options to design the rectangle (e.g. background color: fill, color of the line of rectangle: outline) for sure.
At the end, you have to close the tkinter root object with the mainloop block.

Example:

from tkinter import *

root = Tk()
canvas = Canvas(root, width = 300, height = 300, fill = black')
canvas.pack()
square = canvas.create_rectangle(100, 100, 155, 155, outline = 'white')

root.mainloop()


### What does V stand for in MVC? [2p]
#### Your answer:

V means View it handles every displays, output to the user. The View represents the visualization of the informations what the  Model contains but it gets the datas from the Controller. It doesn't have direct connection with the Model. The Controller pull the datas from the Modell and send them to the View. Actually the View is the user interface.
