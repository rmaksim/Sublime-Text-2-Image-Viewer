# Image-Viewer

**v0.1.2**

---
## View image from CSS declaration, HTML <img> tag, and may be from something else :)

**Forum Thread**
http://www.sublimetext.com/forum/viewtopic.php?f=5&t=4514


### Example
**html:**

    <img src="img/image.png" />
                |
                ^ cursor

**css:**

    background: url(../img/image.png);
                            |
                            ^ cursor


Pressing the `super+i` opens the image viewer installed on your system by default.

**Now works only in Linux.**


### [image_viewer.sublime-settings](https://github.com/rmaksim/Sublime-Text-2-Image-Viewer/blob/master/image_viewer.sublime-settings)
    {
        "image_types": [".jpg", ".png", ".gif"]
    }


### Default (Linux).sublime-keymap
    [
        {"keys": ["super+i"],  "command": "image_viewer"}
    ]


### Copyright
**Copyright (c) 2012 Razumenko Maksim <razumenko.maksim@gmail.com>**

MIT License, see http://opensource.org/licenses/MIT
