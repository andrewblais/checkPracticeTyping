# Import Python libraries:
from random import choice
from tkinter import *
from tkinter import messagebox

# Import data from `static` directory:
from static.cpt_config import about_text, help_text, COLOR_MAP, COLORS
from static.cpt_long_sentences import long_sentences
from static.cpt_short_sentences import short_sentences
from static.cpt_words_one import words_one
from static.cpt_words_two import words_two


class CheckPracticeTyping:
    """
    Class to create a GUI for testing and improving the user's typing speed.

    This class uses Tkinter to build a user interface, imports data from `cts_data`,
    and provides a typing test for the user. It also calculates typing statistics like
    Words Per Minute (WPM) and word accuracy percentage.

    Attributes:
        about_button (Button): Represents the 'About' button in the GUI.
        countdown_label (Label): Widget displaying the countdown during the typing test.
        counting_down (bool): Flag indicating whether the countdown is currently active.
        current_row (int): Current row in the GUI layout.
        entry_accuracy (float): Success rate calculated as the percentage of correct entries.
        exit_button (Button): Represents the 'Exit' button in the GUI.
        go_again_button (Button): Represents the 'Go again' button in the GUI.
        gui_w (int): Width of the GUI window.
        gui_h (int): Height of the GUI window.
        help_button (Button): Represents the 'Help' button in the GUI.
        move_x (int): X-coordinate for the initial window position.
        move_y (int): Y-coordinate for the initial window position.
        num_entries (int): Total number of entries during the typing test.
        root (Tk): The root Tkinter window for the applicatio
        seconds (int): Initial value for the countdown timer in seconds.
        test_text (Label): Widget displaying the text for the user to copy during the typing test.
        test_text_next (str): Randomly selected word for the next typing test.
        user_text_var (StringVar): Tkinter variable for tracking changes in the user_text widget.
        thumb (str): Default message for the thumb indicator.
        thumb_color (str): Default color for the thumb indicator.
        total_words (int): Total number of words in the typing test.
        title_label (Label): Widget displaying the title of the GUI.
        user_right (int): Number of correctly typed entries/sentences during the typing test.
        user_text (Entry): Widget where the user types during the typing test.
        user_text_feedback (Label): Widget displaying the thumb indicator for the typing test.
        user_wrong (int): Number of incorrectly typed entries during the typing test.
        word_accuracy (float): Percentage of correctly typed words in the typing test.
        words_feedback (list): List to store feedback for each word in the typing test.
        words_right (int): Number of correctly typed words during the typing text.
        wpm_str (str): User's typing Words Per Minute (WPM) stat.
        y_padding (int): Vertical padding value for the GUI layout.

    Methods:
        about_popup(): 'About' button command, displays application information.
        _calculate_accuracy(): Calculates and displays typing accuracy percentages. Private method.
        color_mapping(): Determines the color of the countdown label text based on the second count.
        countdown_trigger(): Triggers a continuation of the countdown for the typing test.
        countdown_update(): Updates the countdown display during the typing test.
        _countdown_zero():  Resets attributes to their default state. Private method.
        _reset_widgets(): Resets various widgets to their initial state. Called by self.go_again(). Private method.
        _reset_instance_attributes(): Ensures instance attributes are reset. Called by self.go_again(). Private method.
        _trace_user_text_var(): Private method. Calls self.countdown_trigger() whenever self.user_text_var is assigned a new value. Called by self.go_again(). Private method.
        go_again(): Resets for a new typing round.
        help_popup(): 'Help' button command, displays help information.
        increment_row(): Increments the current row in the GUI layout.
        user_entry(event): Handles user's typing input and updates typing statistics.
        setup_gui(): Sets up the entire GUI for the typing test.
    """

    def __init__(self,
                 root,
                 seconds: int = 60,
                 gui_w: int = 480,
                 gui_h: int = 640,
                 move_x: int = 0,
                 move_y: int = 0):
        """
        Initialize `CheckPracticeTyping()` object.

        Args:
            root (Tk): The root Tkinter window.
            seconds (int): Duration of the typing test in seconds. Default is 60.
            gui_w (int): Width of the GUI window. Default is 480.
            gui_h (int): Height of the GUI window. Default is 640.
            move_x (int): X-coordinate for the initial window position. Default is 0.
            move_y (int): Y-coordinate for the initial window position. Default is 0.
        """

        # Tkinter main window attributes:
        self.root = root  # Class param - required
        self.gui_w = gui_w  # Class param: defaults to 480
        self.gui_h = gui_h  # Class param: defaults to 640
        self.move_x = move_x  # Class param: defaults to 0
        self.move_y = move_y  # Class param: defaults to 0
        self.y_padding = 75
        self.current_row = 0

        # Tkinter widget attributes (in order of display):
        # Row 1:
        self.title_label = None
        # Row 2:
        self.countdown_label = None
        # Row 3:
        self.test_text = None
        # Row 4:
        self.user_text = None
        # Row 5:
        self.user_text_feedback = None
        # Row 6:
        self.go_again_button = None
        # Row 7:
        self.help_button = None
        self.exit_button = None
        self.about_button = None

        # String attributes:
        self.user_text_var = StringVar()
        self.test_text_next = choice(long_sentences)

        # General tabulation attributes:
        self.counting_down = False
        self.num_entries = 0
        self.total_words = 0
        self.original_seconds = seconds  # Class param: defaults to 60
        self.seconds = self.original_seconds

        # User-tracking attributes:
        self.user_right = 0
        self.user_wrong = 0
        self.words_right = 0
        self.entry_accuracy = 0
        self.word_accuracy = 0
        self.words_feedback = list()
        self.wpm_str = ""
        self.thumb = "Type the phrase and hit 'Enter'"
        self.thumb_color = "black"

        # Automatically instantiate the GUI:
        self.setup_gui()

    @staticmethod
    def about_popup():
        """
        'About' button command, displays application information.
        """
        messagebox.showinfo("About Check/Practice Typing", about_text, icon="info")

    def _calculate_accuracy(self):
        """
        Private method.
        Calculates and displays typing accuracy percentages.

        This method sets the values of various attributes based on the user's
        accuracy. Called by the countdown_update method.
        """
        if self.user_right == 0:
            self.entry_accuracy = 0
        else:
            entry_accuracy = round(self.user_right / self.num_entries * 100)
            self.entry_accuracy = entry_accuracy
        if self.words_right == 0:
            self.word_accuracy = 0
        else:
            word_accuracy = round(self.words_right / self.total_words * 100)
            self.word_accuracy = word_accuracy

    def color_mapping(self):
        """
        Determines the color of the countdown label text based on the second count.

        This method iterates through the COLOR_MAP dictionary to find the color
        corresponding to the current number of seconds. It then updates the
        countdown label text color accordingly.
        """
        for limit, color in COLOR_MAP.items():
            if self.seconds < limit:
                self.countdown_label.configure(fg=COLORS[color])
                break

    def countdown_trigger(self):
        """
        Triggers a continuation of the countdown for the typing test.

        This method sets the counting_down flag to True, indicating that the
        countdown should continue. It then calls the countdown_update method.
        """
        if not self.counting_down:
            self.counting_down = True
            self.countdown_update()

    def countdown_update(self):
        """
        Updates the countdown display during the typing test.

        This method updates the countdown label's text and color based on the
        current value of the seconds attribute. It also handles the logic of
        decrementing the countdown and updating the GUI accordingly.
        """
        if self.counting_down:
            self.go_again_button.configure(state="disabled", cursor="")

            # Specify color of countdown display:
            self.color_mapping()

            # Redefine countdown display digits:
            countdown_display = f"{self.seconds:02}"

            # Refresh `self.countdown_label`:
            self.countdown_label.config(text=countdown_display)

            # Continue countdown if seconds is 1 or greater:
            if self.seconds > 0:
                # Run `self.countdown_update()` every second:
                self.root.after(1000, self.countdown_update)
                # Subtract 1 from `self.seconds` every second:
                self.seconds -= 1
            # Countdown has reached 0:
            else:
                self._countdown_zero()

                # Calculate and display Words Per Minute (WPM) statistics:
                self.wpm_str = f"{self.words_right} words per minute."
                self.test_text.config(text=self.wpm_str, fg="dark green")

                # Calculate and display typing accuracy percentages:
                self._calculate_accuracy()

                # Display feedback on individual word accuracy and total entry correctness:
                sentence_feedback = f"{self.word_accuracy}% individual words correct.\n"
                sentence_feedback += f"{self.entry_accuracy}% total entries correct."
                self.user_text_feedback.config(text=sentence_feedback, fg="dark green")

    def _countdown_zero(self):
        """
        Private method.
        Resets attributes to their default state.

        This method is responsible for resetting the state of various instance
        attributes to their default state so the user can take the test again.
        It's called by the countdown_update method.
        """
        self.counting_down = False
        self.root.unbind("<Return>")  # Unbind <Return> key when countdown is 0
        self.go_again_button.configure(state="normal", cursor="exchange")
        self.countdown_label.config(text="--", fg="grey")
        self.test_text.configure(text="")
        self.user_text.delete(0, END)
        self.user_text.configure(state="disabled")

    def _reset_widgets(self):
        """
        Private method.
        Resets various widgets to their initial state. Called by self.go_again().

        This method is responsible for resetting the state of various widgets to
        their initial conditions for a new typing round. It's called by the go_again
        method.
        """
        # Reset countdown label to initial state
        self.countdown_label.config(text=f"{self.seconds:02}", fg="black")

        # Reset `test_text` label to default color
        self.test_text.config(fg="black")

        # Enable the user_text Entry widget and set its text variable
        self.user_text.configure(textvariable=self.user_text_var, state="normal")

        # Reset thumb indicator text and color
        self.user_text_feedback.config(text=self.thumb, fg=self.thumb_color)

        # Set focus to the user_text Entry widget
        self.user_text.focus_set()

        # Bind the "Return" key to the user_entry method
        self.root.bind("<Return>", self.user_entry)

    def _reset_instance_attributes(self):
        """
        Private method.
        Ensures instance attributes are reset. Called by self.go_again().

        This method resets the instance attributes to their initial values for a new
        typing round. It's called by the go_again method.
        """
        # Select a new random sentence for the user to type
        self.test_text_next = choice(long_sentences)
        self.test_text.configure(text=self.test_text_next)

        # Reset countdown timer and related flags
        self.seconds = self.original_seconds
        self.counting_down = False

        # Reset typing statistics
        self.total_words = 0
        self.words_right = 0
        self.num_entries = 0
        self.user_right = 0
        self.user_wrong = 0
        self.entry_accuracy = 0

        # Reset text variable for user input
        self.user_text_var = StringVar()

        # Reset word accuracy and feedback attributes
        self.word_accuracy = 0
        self.words_feedback = list()

        # Reset display attributes
        self.wpm_str = ""
        self.thumb = "Type the phrase and hit 'Enter'"
        self.thumb_color = "black"

    def _trace_user_text_var(self):
        """
        Private method.
        Calls self.countdown_trigger() whenever self.user_text_var is assigned a new value.
        Called by self.go_again().

        This method uses Tkinter's trace method to call countdown_trigger whenever
        self.user_text_var is assigned a new value. It's called by the go_again method.
        """
        # Set up a trace on self.user_text_var to trigger self.countdown_trigger on write
        self.user_text_var.trace_add("write",
                                     lambda name, index, mode: self.countdown_trigger())

    def go_again(self):
        """
        Resets for a new typing round.

        This method resets the GUI and instance attributes for a new typing round.
        It's triggered by the 'Go again' button.
        """
        # Reset instance attributes for a new typing round
        self._reset_instance_attributes()

        # Reset various widgets to their initial state
        self._reset_widgets()

        # Set up trace on self.user_text_var to trigger countdown on text change
        self._trace_user_text_var()

    @staticmethod
    def help_popup():
        """
        'Help' button command, displays help information.

        This static method displays help information in a popup when the 'Help' button
        is clicked.
        """
        # Show a popup with help information
        messagebox.showinfo("Check/Practice Typing Help", help_text, icon="question")

    def increment_row(self):
        """
        Increments the current row in the GUI layout.

        This method increments the current_row attribute, facilitating the correct
        placement of widgets in the GUI layout.
        """
        # Increment the current row for proper widget placement
        self.current_row += 1

    def user_entry(self, event):
        """
        Handles user's typing input and updates typing statistics.

        Args:
            event: The Tkinter event associated with the user's input.

        This method handles the user's typing input, updates typing statistics,
        and triggers necessary actions based on the input event.
        """
        # Get the text typed by the user and clear the input field
        typed_text = self.user_text.get()
        self.user_text.delete(0, END)

        # Get the current text that the user is supposed to type
        current_text = self.test_text.cget("text")

        # Split the current text into individual words
        current_text_split = current_text.split()

        # Split the typed text into individual words
        typed_text_split = typed_text.split()

        # Update total word count based on the current text
        self.total_words += len(current_text_split)

        # Check how many words the user typed correctly
        for i in current_text_split:
            if i in typed_text_split:
                self.words_right += 1

        # Check if the entire typed text matches the current text
        if typed_text == current_text:
            self.user_right += 1
            self.thumb = "✔"
            self.thumb_color = COLORS["DARK_GREEN"]
        else:
            self.user_wrong += 1
            self.thumb = "✖"
            self.thumb_color = COLORS["RED4"]

        # Increment the total number of entries
        self.num_entries += 1

        # Calculate entry correctness percentage
        if self.user_right == 0:
            self.entry_accuracy = 0
        else:
            self.entry_accuracy = f"{(self.user_right / self.num_entries * 100):.2f}"

        # Update the thumb indicator based on correctness
        self.user_text_feedback.config(text=self.thumb, fg=self.thumb_color)

        # Choose the next text for the user to type based on the remaining time
        if self.seconds > 40:
            self.test_text_next = choice(long_sentences)
        elif self.seconds > 25:
            self.test_text_next = choice(short_sentences)
        elif self.seconds > 10:
            self.test_text_next = choice(words_two)
        else:
            self.test_text_next = choice(words_one)

        # Update the displayed text for the next typing round
        if self.counting_down:
            self.test_text.config(text=self.test_text_next)

        # If the "Return" key was pressed, trigger the countdown
        if event.keysym == "Return":
            self.countdown_trigger()

    def setup_gui(self):
        """
        Sets up the entire GUI for the typing test.

        This method configures and places all the widgets, buttons, and labels
        to create the Check/Practice Typing GUI.
        """
        self.root.title("Check/Practice Typing")

        # App favicon, comment out when creating .exe with PyInstaller:
        self.root.iconbitmap("static/icon.ico")

        self.root.geometry(f"{self.gui_w}x{self.gui_h}+{self.move_x}+{self.move_y}")
        self.root.minsize(self.gui_w, self.gui_h)
        self.root.maxsize(self.gui_w, self.gui_h)
        self.root.config(padx=45, pady=20)
        for i in range(3):
            self.root.columnconfigure(i, weight=1)

        # Title label widget:
        self.title_label = Label(self.root,
                                 text="CHECK/PRACTICE TYPING",
                                 font=("Source Sans 3 Black", 16))
        self.title_label.grid(row=self.current_row,
                              column=0,
                              columnspan=3,
                              pady=(0, 0))

        # Increment row:
        self.increment_row()

        # Countdown label widget:
        self.countdown_label = Label(self.root,
                                     text=f"{self.seconds}",
                                     font=("Source Sans 3 Black", 48))
        self.countdown_label.grid(row=self.current_row,
                                  column=0,
                                  columnspan=3,
                                  pady=(35, 0))

        # Increment row:
        self.increment_row()

        # Test text widget:
        self.test_text = Label(self.root,
                               width=50,
                               height=1,
                               padx=30,
                               pady=12,
                               text=self.test_text_next,
                               font=("Source Sans 3 Black", 28))
        self.test_text.grid(row=self.current_row,
                            column=0,
                            columnspan=3,
                            pady=(25, 0))

        # Increment row:
        self.increment_row()

        # User text widget:
        self.user_text = Entry(self.root,
                               width=50,
                               font=("Source Sans 3 Black", 28),
                               justify=CENTER,
                               textvariable=self.user_text_var)
        self.user_text.focus_set()
        self.user_text.grid(row=self.current_row,
                            column=0,
                            columnspan=3,
                            pady=(50, 0))
        self.user_text_var.trace_add("write",
                                     lambda name, index, mode: self.countdown_trigger())
        self.root.bind("<Return>", self.user_entry)

        # Increment row:
        self.increment_row()

        # User text feedback widget:
        self.user_text_feedback = Label(self.root,
                                        width=50,
                                        height=2,
                                        font=("Source Sans 3 Black", 12),
                                        fg=self.thumb_color,
                                        text=self.thumb,
                                        justify=CENTER)
        self.user_text_feedback.grid(row=self.current_row,
                                     column=0,
                                     columnspan=3,
                                     pady=(25, 0))

        # Increment row:
        self.increment_row()

        # Go again button widget:
        self.go_again_button = Button(self.root,
                                      text="Go again",
                                      cursor="exchange",
                                      width=8,
                                      height=1,
                                      command=self.go_again)
        self.go_again_button.grid(row=self.current_row,
                                  column=0,
                                  columnspan=3,
                                  padx=(0, 0),
                                  pady=(10, 0))
        # Increment row:
        self.increment_row()

        # Help button widget:
        self.help_button = Button(self.root,
                                  text="Help",
                                  cursor="question_arrow",
                                  width=8,
                                  height=1,
                                  command=self.help_popup)
        self.help_button.grid(row=self.current_row,
                              column=0,
                              padx=(0, 0),
                              pady=(65, 0))

        # Exit button widget:
        self.exit_button = Button(self.root,
                                  text="Exit",
                                  cursor="trek",
                                  width=8,
                                  height=1,
                                  command=self.root.quit)
        self.exit_button.grid(row=self.current_row,
                              column=1,
                              pady=(65, 0))

        # About button widget:
        self.about_button = Button(self.root,
                                   text="About",
                                   width=8,
                                   height=1,
                                   command=self.about_popup)
        self.about_button.grid(row=self.current_row,
                               column=2,
                               padx=(0, 0),
                               pady=(65, 0))


# Create an instance of `CheckPracticeTyping()` and ENJOY!:
if __name__ == "__main__":
    window = Tk()
    watermark_gui = CheckPracticeTyping(window,
                                        seconds=60,
                                        gui_w=950,
                                        gui_h=650,
                                        move_x=100,
                                        move_y=0)
    window.mainloop()

