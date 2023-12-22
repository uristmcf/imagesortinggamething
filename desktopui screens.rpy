screen desktopUI():

    imagemap:
        ground "lrlaptop.png"
        
    imagebutton:
        area (265, 67, 206, 199)
        idle "int1"
        hover "int2"
        action NullAction()
        #action jump("internetBrowse")
    
    imagebutton:
        area (263, 268, 203, 194)
        idle "game1"
        hover "game2"
        action NullAction()

    imagebutton:
        area (265, 468, 211, 204)
        idle "sm1"
        hover "sm2"
        #action NullAction()
        action [Jump("randimgtest2")]

    imagebutton:
        area (1532, 728, 121, 124)
        idle "pb"
        hover "rbdown"
        action NullAction()