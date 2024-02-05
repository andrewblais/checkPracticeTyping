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
        entry_correct (int): Number of correctly typed entries/sentences during the typing test.
        words_correct (int): Number of correctly typed words during the typing text.
        countdown_label (Label): Widget displaying the countdown during the typing test.
        counting_down (bool): Flag indicating whether the countdown is currently active.
        current_row (int): Current row in the GUI layout.
        text_var (StringVar): Tkinter variable for tracking changes in the text entry widget.
        exit_button (Button): Represents the 'Exit' button in the GUI.
        entry_incorrect (int): Number of incorrectly typed entries during the typing test.
        go_again_button (Button): Represents the 'Go again' button in the GUI.
        gui_w (int): Width of the GUI window.
        gui_h (int): Height of the GUI window.
        help_button (Button): Represents the 'Help' button in the GUI.
        move_x (int): X-coordinate for the initial window position.
        move_y (int): Y-coordinate for the initial window position.
        read_text (Label): Widget displaying the text for the user to copy during the typing test.
        read_text_next (str): Randomly selected word for the next typing test.
        root (Tk): The root Tkinter window for the applicatio
        entry_percent (float): Success rate calculated as the percentage of correct entries.
        num_entries (int): Total number of entries during the typing test.
        seconds (int): Initial value for the countdown timer in seconds.
        thumb (str): Default message for the thumb indicator.
        thumb_color (str): Default color for the thumb indicator.
        total_words (int): Total number of words in the typing test.
        title_label (Label): Widget displaying the title of the GUI.
        type_text (Entry): Widget where the user types during the typing test.
        type_text_feedback (Label): Widget displaying the thumb indicator for the typing test.
        word_accuracy_percent (float): Percentage of correctly typed words in the typing test.
        words_feedback (list): List to store feedback for each word in the typing test.
        wpm_str (str): User's typing Words Per Minute (WPM) stat.
        y_padding (int): Vertical padding value for the GUI layout.

    Methods:
        about_popup(): 'About' button command, displays application information.
        color_mapping(): Determines the color of the countdown label text based on the second count.
        countdown_trigger(): Triggers a continuation of the countdown for the typing test.
        countdown_update(): Updates the countdown display during the typing test.
        _reset_widgets(): Resets various widgets to their initial state. Called by self.go_again().
        _reset_instance_attributes(): Ensures instance attributes are reset. Called by self.go_again().
        _trace_text_var(): Private method. Calls self.countdown_trigger() whenever self.text_var is assigned a new value. Called by self.go_again().
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
        Initialize `CheckPracticeTyping()` object with default values, sets up GUI.

        Args:
            root (Tk): The root Tkinter window.
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

        # Tkinter widget attributes (in order of appearance):
        self.title_label = None
        self.countdown_label = None
        self.read_text = None
        self.type_text = None
        self.type_text_feedback = None
        self.go_again_button = None
        self.help_button = None
        self.exit_button = None
        self.about_button = None

        # String attributes:
        self.text_var = StringVar()
        self.read_text_next = choice(long_sentences)

        # General tabulation attributes:
        self.counting_down = False
        self.num_entries = 0
        self.total_words = 0
        self.original_seconds = seconds  # Class param: defaults to 60
        self.seconds = self.original_seconds

        # User-tracking attributes:
        self.entry_correct = 0
        self.entry_incorrect = 0
        self.words_correct = 0
        self.entry_percent = 0
        self.word_accuracy_percent = 0
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

    def color_mapping(self):
        """
        Determines color of countdown label text based on second count.
        """
        for limit, color in COLOR_MAP.items():
            if self.seconds < limit:
                self.countdown_label.configure(fg=COLORS[color])
                break

    def countdown_trigger(self):
        """
        Triggers a continuation of the countdown for typing test.
        """
        if not self.counting_down:
            self.counting_down = True
            self.countdown_update()

    def countdown_update(self):
        """
        Updates the countdown display during the typing test.
        """
        if self.counting_down:
            self.go_again_button.configure(state="disabled", cursor="")

            # Specify color of countdown display:
            self.color_mapping()

            countdown_display = f"{self.seconds:02}"

            self.countdown_label.config(text=countdown_display)

            if self.seconds > 0:
                self.root.after(1000, self.countdown_update)
                self.seconds -= 1
            else:
                self.counting_down = False
                self.root.unbind("<Return>")  # Unbind <Return> key when countdown is 0
                self.go_again_button.configure(state="normal", cursor="exchange")
                self.countdown_label.config(text="--", fg="grey")
                self.read_text.configure(text="")
                self.type_text.delete(0, END)
                self.type_text.configure(state="disabled")
                self.wpm_str = f"{self.words_correct} words per minute."
                self.read_text.config(text=self.wpm_str, fg="dark green")
                if self.entry_correct == 0:
                    self.entry_percent = 0
                else:
                    self.entry_percent = round(
                        self.entry_correct / self.num_entries * 100)
                if self.words_correct == 0:
                    self.word_accuracy_percent = 0
                else:
                    self.word_accuracy_percent = round(
                        self.words_correct / self.total_words * 100)
                sentence_feedback = f"{self.word_accuracy_percent}% individual words correct.\n"
                sentence_feedback += f"{self.entry_percent}% total entries correct."
                self.type_text_feedback.config(text=sentence_feedback, fg="dark green")

    def _reset_widgets(self):
        """
        Private method.
        Resets various widgets to their initial state. Called by self.go_again().
        """
        self.countdown_label.config(text=f"{self.seconds:02}", fg="black")
        self.read_text.config(fg="black")
        self.type_text.configure(textvariable=self.text_var, state="normal")
        self.type_text_feedback.config(text=self.thumb, fg=self.thumb_color)
        self.type_text.focus_set()
        self.root.bind("<Return>", self.user_entry)

    def _reset_instance_attributes(self):
        """
        Private method.
        Ensures instance attributes are reset. Called by self.go_again().
        """
        self.read_text_next = choice(long_sentences)
        self.read_text.configure(text=self.read_text_next)
        self.seconds = self.original_seconds
        self.counting_down = False
        self.total_words = 0
        self.words_correct = 0
        self.num_entries = 0
        self.entry_correct = 0
        self.entry_incorrect = 0
        self.entry_percent = 0
        self.text_var = StringVar()
        self.word_accuracy_percent = 0
        self.words_feedback = list()
        self.wpm_str = ""
        self.thumb = "Type the phrase and hit 'Enter'"
        self.thumb_color = "black"

    def _trace_text_var(self):
        """
        Private method.
        Calls self.countdown_trigger() whenever self.text_var is assigned a new value.
        Called by self.go_again().
        """
        self.text_var.trace_add("write",
                                lambda name, index, mode: self.countdown_trigger())

    def go_again(self):
        """
        Resets for a new typing round.
        """
        self._reset_instance_attributes()
        self._reset_widgets()
        self._trace_text_var()

    @staticmethod
    def help_popup():
        """
        'Help' button command, displays help information.
        """
        messagebox.showinfo("CTS Help", help_text, icon="question")

    def increment_row(self):
        """
        Increments the current row in the GUI layout.
        """
        self.current_row += 1

    def user_entry(self, event):
        """
        Handles user's typing input and updates typing statistics.

        Args:
            event: The Tkinter event associated with user's input.
        """
        typed_text = self.type_text.get()
        self.type_text.delete(0, END)
        current_text = self.read_text.cget("text")
        current_text_split = current_text.split()
        typed_text_split = typed_text.split()
        self.total_words += len(current_text_split)

        for i in current_text_split:
            if i in typed_text_split:
                self.words_correct += 1

        if typed_text == current_text:
            self.entry_correct += 1
            self.thumb = "✔"
            self.thumb_color = COLORS["DARK_GREEN"]
        else:
            self.entry_incorrect += 1
            self.thumb = "✖"
            self.thumb_color = COLORS["RED4"]

        self.num_entries += 1

        if self.entry_correct == 0:
            self.entry_percent = 0
        else:
            self.entry_percent = f"{(self.entry_correct / self.num_entries * 100):.2f}"

        self.type_text_feedback.config(text=self.thumb, fg=self.thumb_color)

        # Length of entry based on time left:
        if self.seconds > 40:
            self.read_text_next = choice(long_sentences)
        elif self.seconds > 25:
            self.read_text_next = choice(short_sentences)
        elif self.seconds > 10:
            self.read_text_next = choice(words_two)
        else:
            self.read_text_next = choice(words_one)

        if self.counting_down:
            self.read_text.config(text=self.read_text_next)
        if event.keysym == "Return":
            self.countdown_trigger()

    def setup_gui(self):
        """
        Sets up the entire GUI for the typing test.
        """
        self.root.title("Check/Practice Typing")
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

        # Read text widget:
        self.read_text = Label(self.root,
                               width=50,
                               height=1,
                               padx=30,
                               pady=12,
                               text=self.read_text_next,
                               font=("Source Sans 3 Black", 28))
        self.read_text.grid(row=self.current_row,
                            column=0,
                            columnspan=3,
                            pady=(25, 0))

        # Increment row:
        self.increment_row()

        self.type_text = Entry(self.root,
                               width=50,
                               font=("Source Sans 3 Black", 28),
                               justify=CENTER,
                               textvariable=self.text_var)
        self.type_text.focus_set()
        self.type_text.grid(row=self.current_row,
                            column=0,
                            columnspan=3,
                            pady=(50, 0))
        self.text_var.trace_add("write",
                                lambda name, index, mode: self.countdown_trigger())
        self.root.bind("<Return>", self.user_entry)

        # Increment row:
        self.increment_row()

        # Type text feedback widget:
        self.type_text_feedback = Label(self.root,
                                        width=50,
                                        height=2,
                                        font=("Source Sans 3 Black", 12),
                                        fg=self.thumb_color,
                                        text=self.thumb,
                                        justify=CENTER)
        self.type_text_feedback.grid(row=self.current_row,
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


if __name__ == "__main__":
    window = Tk()
    watermark_gui = CheckPracticeTyping(window,
                                        seconds=60,
                                        gui_w=950,
                                        gui_h=650,
                                        move_x=100,
                                        move_y=0)
    window.mainloop()
