# Presence app guide
Documentation for using the PresenceApp discord presence template.

### Steps in order:
- Creating an application on the discord developer portal
- Uploading the required images onto the developer portal
- Getting the id of the application
- Downloading the template
- Filling out the python template

### Step 1: _Creating an application_
To create an application, we will have to go to [the discord developer portal](https://discord.com/developers) and create a new application by clicking `New Aplication`!
_Notice: The name of the application will be the title of your presence, but you can change this name any time!_
![Alt](https://cdn.discordapp.com/attachments/1036012959983476838/1061703687661178931/image.png)
![Alt](https://cdn.discordapp.com/attachments/1036012959983476838/1061703897208590386/image.png)

### Step 2: Adding the images
Actually, having a visualization needs some preparation, so get your images ready! First go to the `Rich Presence` tab and click on `Art Assets`. After that, scroll down and click on `Add Image`. Now select your images and name them.
_Notice: Name the pictures with short and simple titles, because the name cant be changed later!_
![Alt](https://cdn.discordapp.com/attachments/1036012959983476838/1061707451315011676/image.png)
![Alt](https://cdn.discordapp.com/attachments/1036012959983476838/1061707645775515698/image.png)

### Step 3: Getting the ID of the app
The next step on our journey to having a rich presence is getting the ID, which is essential for this to work. Getting the ID is quite simple: Click on `General information` and locate the `Application ID` section. 
![Alt](https://cdn.discordapp.com/attachments/1036012959983476838/1062067326775730256/image.png)

### Step 4: Downloading the template
To make this easier, we will clone the repository using [git](https://git-scm.com/downloads). In your command prompt window (or python shell) write:
_Notice: locate your desired install location using `cd folder` or starting the command prompt in that location_
```
git clone https://github.com/LarssJakobsons/Discord-rich-presence-python
```
After it has created the folder in your desired install location, run the following command in the downloaded folder (shell or cmd)
```
pip install -r requirements.txt
```
Everything you need in this template should be installed, and you should be ready to go without any extra installs.

### Step 5: Filling out the template
We've finally got to the juice and bones of this tutorial! Filling out the template goes as following: After locating the `presenceapp.py` file, fill out the according values.
```
client_id = your app id

start = the start of your presence (if left without end, will show as "elapsed")
end = the "remaining" time of your presence (will show as "<time> remaining"). 
You can input when you want this ending time to be (in seconds)

large_image = the name that you gave in the developer portal of the image you want to show up as the main image of your presence.
large_text = text that shows upon hovering above the large image.
small_image = the name that you gave in the developer portal of the image you want to show up as the small icon image of your presence.
small_text = text that shows upon hovering above the small image.

details = the text that shows below the main title of your presence.
state = the text that shows below the details value of your presence.
start = the start time of your presence (shows below the presence state)
end = the "end" of your presence (replaces start if not 'None')

buttons = the buttons that appear at the bottom of your presence. For them to have an effect upon clicking input the 
label of the button in the "label" section, and the url the clicker will be sent to in the "url" section. 
If you want 1 or None buttons, comment/delete them. You can have up to 2 buttons in your presence.
```
If you have any questions feel free to ask me on my [discord server](https://discord.gg/TReMEyBQsh).
Feel free to experiment with this and learn something new in python!

> Written with [StackEdit](https://stackedit.io/). Go check them out :)