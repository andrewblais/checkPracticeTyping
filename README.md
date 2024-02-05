# checkPracticeTyping

A [Tkinter](https://docs.python.org/3/library/tkinter.html) GUI which tests a users typing skill/speed and provides feedback.

Written with Python OOP approach, many methods which I've tried to break down into 
readable pieces.

The static folder contains lots and lots of lists of words for the typing test. I scoured
Project Gutenberg, Seinfeld scripts and other places for the data. This gave me a good
opportunity to practice my text-cleaning skills.

---

Future updates will include further separation of concerns and efficiency in the main class.

More words and phrases to be added to the word banks. Suggestions welcome!

---


### Documentation:

_Printed via `help(checkPracticeTyping) in `cpt_main.py`:_

```markdown
Help on class CheckPracticeTyping in module __main__:

class CheckPracticeTyping(builtins.object)
 |  CheckPracticeTyping(root, seconds: int = 60, gui_w: int = 480, gui_h: int = 640, move_x: int = 0, move_y: int = 0)
 |
 |  Class to create a GUI for testing and improving the user's typing speed.
 |
 |  This class uses Tkinter to build a user interface, imports data from `cts_data`,
 |  and provides a typing test for the user. It also calculates typing statistics like
 |  Words Per Minute (WPM) and word accuracy percentage.
 |
 |  Attributes:
 |      about_button (Button): Represents the 'About' button in the GUI.
 |      countdown_label (Label): Widget displaying the countdown during the typing test.
 |      counting_down (bool): Flag indicating whether the countdown is currently active.
 |      current_row (int): Current row in the GUI layout.
 |      entry_accuracy (float): Success rate calculated as the percentage of correct entries.
 |      exit_button (Button): Represents the 'Exit' button in the GUI.
 |      go_again_button (Button): Represents the 'Go again' button in the GUI.
 |      gui_w (int): Width of the GUI window.
 |      gui_h (int): Height of the GUI window.
 |      help_button (Button): Represents the 'Help' button in the GUI.
 |      move_x (int): X-coordinate for the initial window position.
 |      move_y (int): Y-coordinate for the initial window position.
 |      num_entries (int): Total number of entries during the typing test.
 |      root (Tk): The root Tkinter window for the applicatio
 |      seconds (int): Initial value for the countdown timer in seconds.
 |      test_text (Label): Widget displaying the text for the user to copy during the typing test.
 |      test_text_next (str): Randomly selected word for the next typing test.
 |      user_text_var (StringVar): Tkinter variable for tracking changes in the user_text widget.
 |      thumb (str): Default message for the thumb indicator.
 |      thumb_color (str): Default color for the thumb indicator.
 |      total_words (int): Total number of words in the typing test.
 |      title_label (Label): Widget displaying the title of the GUI.
 |      user_right (int): Number of correctly typed entries/sentences during the typing test.
 |      user_text (Entry): Widget where the user types during the typing test.
 |      user_text_feedback (Label): Widget displaying the thumb indicator for the typing test.
 |      user_wrong (int): Number of incorrectly typed entries during the typing test.
 |      word_accuracy (float): Percentage of correctly typed words in the typing test.
 |      words_feedback (list): List to store feedback for each word in the typing test.
 |      words_right (int): Number of correctly typed words during the typing text.
 |      wpm_str (str): User's typing Words Per Minute (WPM) stat.
 |      y_padding (int): Vertical padding value for the GUI layout.
 |
 |  Methods:
 |      about_popup(): 'About' button command, displays application information.
 |      _calculate_accuracy(): Calculates and displays typing accuracy percentages. Private method.
 |      color_mapping(): Determines the color of the countdown label text based on the second count.
 |      countdown_trigger(): Triggers a continuation of the countdown for the typing test.
 |      countdown_update(): Updates the countdown display during the typing test.
 |      _countdown_zero():  Resets attributes to their default state. Private method.
 |      _reset_widgets(): Resets various widgets to their initial state. Called by self.go_again(). Private method.
 |      _reset_instance_attributes(): Ensures instance attributes are reset. Called by self.go_again(). Private method.
 |      _trace_user_text_var(): Private method. Calls self.countdown_trigger() whenever self.user_text_var is assigned a new value. Called by self.go_again(). Private method.
 |      go_again(): Resets for a new typing round.
 |      help_popup(): 'Help' button command, displays help information.
 |      increment_row(): Increments the current row in the GUI layout.
 |      user_entry(event): Handles user's typing input and updates typing statistics.
 |      setup_gui(): Sets up the entire GUI for the typing test.
 |
 |  Methods defined here:
 |
 |  __init__(self, root, seconds: int = 60, gui_w: int = 480, gui_h: int = 640, move_x: int = 0, move_y: int = 0)
 |      Initialize `CheckPracticeTyping()` object.
 |
 |      Args:
 |          root (Tk): The root Tkinter window.
 |          seconds (int): Duration of the typing test in seconds. Default is 60.
 |          gui_w (int): Width of the GUI window. Default is 480.
 |          gui_h (int): Height of the GUI window. Default is 640.
 |          move_x (int): X-coordinate for the initial window position. Default is 0.
 |          move_y (int): Y-coordinate for the initial window position. Default is 0.
 |
 |  color_mapping(self)
 |      Determines the color of the countdown label text based on the second count.
 |
 |      This method iterates through the COLOR_MAP dictionary to find the color
 |      corresponding to the current number of seconds. It then updates the
 |      countdown label text color accordingly.
 |
 |  countdown_trigger(self)
 |      Triggers a continuation of the countdown for the typing test.
 |
 |      This method sets the counting_down flag to True, indicating that the
 |      countdown should continue. It then calls the countdown_update method.
 |
 |  countdown_update(self)
 |      Updates the countdown display during the typing test.
 |
 |      This method updates the countdown label's text and color based on the
 |      current value of the seconds attribute. It also handles the logic of
 |      decrementing the countdown and updating the GUI accordingly.
 |
 |  go_again(self)
 |      Resets for a new typing round.
 |
 |      This method resets the GUI and instance attributes for a new typing round.
 |      It's triggered by the 'Go again' button.
 |
 |  increment_row(self)
 |      Increments the current row in the GUI layout.
 |
 |      This method increments the current_row attribute, facilitating the correct
 |      placement of widgets in the GUI layout.
 |
 |  setup_gui(self)
 |      Sets up the entire GUI for the typing test.
 |
 |      This method configures and places all the widgets, buttons, and labels
 |      to create the Check/Practice Typing GUI.
 |
 |  user_entry(self, event)
 |      Handles user's typing input and updates typing statistics.
 |
 |      Args:
 |          event: The Tkinter event associated with the user's input.
 |
 |      This method handles the user's typing input, updates typing statistics,
 |      and triggers necessary actions based on the input event.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  about_popup()
 |      'About' button command, displays application information.
 |
 |  help_popup()
 |      'Help' button command, displays help information.
 |
 |      This static method displays help information in a popup when the 'Help' button
 |      is clicked.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
```

---

## Assignment for Angela Yu's Course:

### _I created this project in completing Day 86, Professional Portfolio Project - [GUI]:_

- _Assignment 5, "Typing Speed Test" from [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/):_

Here are the instructions for the assignment:

```
Assignment: Typing Speed Test

_A Tkinter GUI desktop application that tests your typing speed._

Assignment instructions

Using Tkinter and what you have learnt about building GUI applications with Python, build a
desktop app that assesses your typing speed. Give the user some sample text and detect how
many words they can type per minute.

The average typing speed is 40 words per minute. But with practice, you can speed up to 100
words per minute.

You can try out a web version here:

https://typing-speed-test.aoeu.eu/

If you have more time, you can build your typing speed test into a typing trainer, with high
scores and more text samples. You can design your program any way you want.
```

#### My reflections on the assignment:

The course asks:

```
This is a place to journal your experience of completing this project. This will help you
figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve
for the next project? What was your biggest learning from today? What would you do differently
if you were to tackle this project again?s
```

My answers:

Here's my projects repo's address: https://github.com/andrewblais/checkPracticeTyping

It was helpful having completed the Image Watermarking assigment prior to this, which really 
refreshed my memory on using Tkinter.

I set up the skeleton of the GUI and added/refined which widgets should appear after much trial and
error and after seeing what worked best for the simple interface I was trying to achieve.

I did a better job in this project of waiting to make sure the core functionality was operational before
adding bells and whistles and fine-tuning.

When my brain got too tired from figuring out some of the more advanced concepts to do with getting the functionality
beyond just the appearance to work, I enjoyed scouring the Internet for word lists I could use for my typing test's
data.

The hardest part was getting the functionality around checking the user's entries compared with the text they are
typing. Also, getting the timer countdown functionality was hard, too. I did a lot of work looking at Tkinter
documentaion, Stack Overflow/Geeks for Geeks/W3 and other resources, and ChatGPT 3.5 was very helpful when 
I got stuck and needed a tutor.

I did my best to refer to these references and not depend on them or copy anything, originality and creativity
are important to me and I strive to create a fun, unique project.

I also used PyInstaller to generate a standalone .exe for non-Python users. This was tricky, especially 
integrating with the (venv) and getting the Bash commands right.

I'm happy with the outcome, the simplicity of the GUI and ease-of-use.

Much refactoring is needed to simplify the main class methods and provide better error-handling, but I'm happy
for now and ready to submit my work.

What did I learn? I learned to take my time and approach big projects like this with simplicity and functionality
on a basic level in mind. I easily get ahead of myself with goals that might be too complex for the task at hand.
I did follow through on some of the more complex goals, but it took over a week to complete this assigment. I think
that's okay, though. 100 Days is probably more like 400 Days for me, as I'm a very slow and methodical learner.
I'm not in a rush, so I'm trying to give myself permission to go at my own pace and use the '100 Days' as a guide 
but not a rule.

Next project I may try to do a bit faster and make a bit simpler.

Thanks for the guidance and encouragement, Angela!!
