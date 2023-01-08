"""
PresenceApp.py
Made by @Larss_J
To upload the images go to https://discord.com/developers/applications and upload them in the Rich Presence>Art assets tab.
Notice: The name of the rich presence is the name of the application.
If you have any questions feel free to ask me on my discord server: https://discord.gg/TReMEyBQsh
"""

# importing all the required modules
from pypresence import Presence
import time
import datetime
from datetime import timedelta

# setting the start time
start = datetime.datetime.now()
# setting the end time (this can be changed to your liking)
end = start + timedelta(days=0, hours=0, minutes=30, seconds=0)

# setting the client id
client_id = "<client id>"  # this can be obtained from the application id section from the discord developer portal

# connecting to discord and starting the presence
RPC = Presence(client_id)
RPC.connect()
print("Started.")

# keeping the presence alive and updating it every 3 minutes (this time can be changed)
while True:
    RPC.update(
        large_image="<large image name>",  # the name of the image you uploaded it as to the discord developer portal
        large_text="<text>",  # the text that appears when you hover over the large image
        small_image="<small image name>",  # the name of the image you uploaded it as to the discord developer portal
        small_text="<text>",  # the text that appears when you hover over the small image
        details="<text>",  # the text that appears under the main title of your presence
        state="<text>",  # the text that appears under the details
        start=start,  # the inputted start time (shows as "elapsed")
        end=None,  # the end time (shows as "remaining")
        # the buttons that appear under your presence (max 2 buttons)
        buttons=[
            {"label": "<Your label>", "url": "<url link>"},
            {"label": "<Your label>", "url": "<url link>"},
        ],
    )
    # wait time before next presence update (if this time is too slow/fast youre more than welcome to change this to your liking)
    time.sleep(180)
