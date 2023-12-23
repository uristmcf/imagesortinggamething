init python:

    def showRandomAImage(subdir="."):
        directory = "/".join([config.gamedir.replace("\\", "/"), "accepted", subdir])
        modImageList = [ "/".join([directory, filename])
                        for filename in renpy.os.listdir(directory)
                            if filename.endswith((".webp", ".png", ".jpg")) ]


        selectedImage = renpy.random.choice(modImageList)
        #renpy.show("randimg", what=Image( selectedImage ) )
        return selectedImage

    def showRandomRImage(subdir="."):
        directory = "/".join([config.gamedir.replace("\\", "/"), "rejected", subdir])
        modImageList = [ "/".join([directory, filename])
                        for filename in renpy.os.listdir(directory)
                            if filename.endswith((".webp", ".png", ".jpg")) ]


        selectedImage = renpy.random.choice(modImageList)
        #renpy.show("randimg", what=Image( selectedImage ) )
        return selectedImage


default imagecount = 0
default gamepoints = 0
default acceptimage = 0
default rejectimage = 0

label randimgtest2:
    scene black

    if imagecount >= 10:
        jump randimgend
    $ imagecount  += 1
    
    jump expression renpy.random.choice([ 'randimgaccept', 'randimgreject' ])

label randimgaccept:
    show expression showRandomAImage() at truecenter as sortingimage
    $ acceptimage = 1
    #"accepted image\n{w=0.5}{nw}"
    #extend "You have seen [imagecount] images."
    call screen gamescreen

label randimgaccept2:
    hide sortingimage
    $ acceptimage = 0
    jump randimgtest2

label randimgreject:
    show expression showRandomRImage() at truecenter as tsortingimage
    $ rejectimage = 1
    #"rejected image\n{w=0.5}{nw}"
    #extend "You have seen [imagecount] images."
    call screen gamescreen

label randimgreject2:
    hide sortingimage
    $ rejectimage = 0
    jump randimgtest2
    
label randimgend:
    "You saw [imagecount] images. You have [gamepoints] points. Clearing."
    $ gamepoints = 0
    $ imagecount = 0
    scene black
    jump start

