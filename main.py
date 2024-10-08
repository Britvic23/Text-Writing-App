import tkinter as tk
from tkinter import messagebox

class DangerousWritingApp:
    """
    A simple text editor that deletes all content if the user stops typing for 5 seconds.

    Attributes:
        root (tk.Tk): The root window for the application.
        text_area (tk.Text): The main text input area where users type.
        clear_time (int): Time in milliseconds before the text area is cleared (set to 5000ms or 5 seconds).
        timer (int): Stores the ID of the timer created by `after()` method.
        messagebox_open (bool): Flag to ensure only one messagebox is open at a time.
    """
    def __init__(self, root_win):
        """
        Initializes the DangerousWritingApp with a text area and binds keypress events to reset the timer.

        Args:
            root_win (tk.Tk): The root window of the application.
        """
        self.root = root_win
        self.root.title("Dangerous Writing App")
        self.root.geometry("600x400")

        self.explanation_label = tk.Label(self.root, text="Welcome to the Dangerous Writing App!\n"
                                                          "Keep typing! If you stop for 5 seconds, "
                                                          "you risk losing all your work!",
                                          font=("Arial", 12), fg="black", padx=10, pady=10)
        self.explanation_label.pack()

        self.text_area = tk.Text(self.root, font=("Arial", 12), wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        self.clear_time = 5000  # Time in milliseconds (5 seconds)
        self.timer = None  # Variable to store the timer ID
        self.messagebox_open = False  # Flag to track if a message box is already open

        # Bind the key press event to reset the timer every time a key is pressed
        self.text_area.bind("<KeyPress>", self.on_key_press)


    def on_key_press(self, event):
        """
        Handles the key press event to reset the timer.

        Args:
            event (tk.Event): The event object (though unused, it is needed to comply with the event handler signature).
        """
        if self.timer:
            # Cancel the previous timer if it's still running
            self.root.after_cancel(self.timer)
        # Start a new timer after each key press
        self.timer = self.root.after(self.clear_time, self.clear_text)


    def clear_text(self):
        """
        Clears the text if the user hasn't typed for the duration of `clear_time`.

        This function opens a message box to ask if the user wants to restart, and if they agree,
        the text is deleted.
        """
        if not self.messagebox_open:  # Ensures only one message box is opened at a time
            self.messagebox_open = True
            if messagebox.askyesno("Time's up!", "You stopped typing! Start over?"):
                self.text_area.delete('1.0', tk.END)
            self.messagebox_open = False  # Reset the flag after the messagebox closes


# Main execution
if __name__ == "__main__":
    """
    Initializes the tkinter root window and runs the DangerousWritingApp.
    """
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()