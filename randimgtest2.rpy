init python:

    def showRandomAImage(subdir="."):
        directory = "/".join([config.gamedir.replace("\\", "/"), "accepted", subdir])
        modImageList = [ "/".join([directory, filename])
                        for filename in renpy.os.listdir(directory)
                            if filename.endswith((".webp", ".png", ".jpg")) ]


        selectedImage = renpy.random.choice(modImageList)
        renpy.show("randimg", what=Image( selectedImage ) )
        return selectedImage

    def showRandomRImage(subdir="."):
        directory = "/".join([config.gamedir.replace("\\", "/"), "rejected", subdir])
        modImageList = [ "/".join([directory, filename])
                        for filename in renpy.os.listdir(directory)
                            if filename.endswith((".webp", ".png", ".jpg")) ]


        selectedImage = renpy.random.choice(modImageList)
        renpy.show("randimg", what=Image( selectedImage ) )
        return selectedImage


label randimgtest2:
    $ imagecount  = 0
    $ randgamenbr = renpy.random.randint(0,1)
    if (randgamenbr == 0):
        $ imagecount += 1
        jump randimgaccept
    
    elif (randgamenbr == 1):
        $ imagecount += 1
        jump randimgreject

label randimgaccept:
    show expression showRandomAImage() at truecenter
    "accepted image"
    pause
    "You have seen [imagecount] images."
    if imagecount >= 10:
        scene black
        jump randimgtest2
    elif imagecount <= 10:
        scene black
        jump randimgend
    else:
        scene black
        jump start

label randimgreject:
    show expression showRandomRImage() at truecenter
    "rejected image"
    pause
    "You have seen [imagecount] images."
    if imagecount >= 10:
        scene black
        jump randimgtest2
    elif imagecount <= 10:
        scene black
        jump randimgend
    else:
        scene black
        jump start
    
label randimgend:
    "You saw [imagecount] images. Clearing."
    $ imagecount == 0
    scene black
    jump start

