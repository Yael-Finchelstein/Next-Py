import tkinter as tk
from tkinter.font import Font


def show_image():
    # Show the image label
    image_label.grid(row=2, column=0)


# Create the main window
root = tk.Tk()

# Set the window title
root.title("Window with Question")

# Create a label to display the question
question_label = tk.Label(root, text="What is my favorite song ?", foreground="purple", font=Font(size=16, family="Courier New"))
question_label.grid(row=0, column=0)

# Create a button
button = tk.Button(root, text="Show Answer", command=show_image, font=Font(size=10, family="Courier New"))
button.grid(row=1, column=0)

# Load the image
image = tk.PhotoImage(file=r"C:\yaelUser\fav-song.png")

# Create a label to display the image
image_label = tk.Label(root, image=image)

# Start the main event loop for the main window
root.mainloop()
