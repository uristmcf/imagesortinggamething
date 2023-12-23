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


default imagecount = 0

label randimgtest2:
    $ imagecount  += 1
    jump expression renpy.random.choice([ 'randimgaccept', 'randimgreject' ])

label randimgaccept:
    show expression showRandomAImage() at truecenter
    "accepted image"
    pause
    "You have seen [imagecount] images."
    if imagecount <= 10:
        scene black
        jump randimgtest2
    elif imagecount >= 10:
        scene black
        jump randimgend

label randimgreject:
    show expression showRandomRImage() at truecenter
    "rejected image"
    pause
    "You have seen [imagecount] images."
    if imagecount <= 10:
        scene black
        jump randimgtest2
    elif imagecount >= 10:
        scene black
        jump randimgend
    
label randimgend:
    "You saw [imagecount] images. Clearing."
    $ imagecount = 0
    scene black
    jump start

