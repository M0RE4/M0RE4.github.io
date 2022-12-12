# Import the necessary modules
import time
import os

# Define the cat animation frames
cat_frames = [
    r"""
    /\_/\ 
   ( o.o )
    > ^ <
    """,
    r"""
    /\_/\ 
   ( o.O )
    > ^ <
    """,
    r"""
    /\_/\ 
   ( O.o )
    > ^ <
    """,
    r"""
    /\_/\ 
   ( O.O )
    > ^ <
    """
]

# Loop through the cat animation frames
while True:
    for frame in cat_frames:
        # Clear the screen
        os.system("cls" if os.name == "nt" else "clear")

        # Display the current frame
        print(frame)

        # Sleep for a short time
        time.sleep(0.5)