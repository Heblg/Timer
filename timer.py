from time import sleep

medida = str(input("enter the time measurement ( hours-h | minutes-m | seconds-s ): ")).lower().strip()
t,sec = int(input("time: ")),60

if medida == "s":
    while t != 0:
        print("{} seconds".format(t))
        t -= 1
        sleep(1)

if medida == "m":
    a = t * 60
    while a != 0:
        a -= 1
        t -= 1/60
        print("{} minutes and {:.0f} seconds".format(t.__trunc__(), sec))
        sec -= 1
        if sec == 0:
            sec = 60
        sleep(1)

if medida == "h":
    min = 60
    a = t * 3600
    while a != 0:
        a -= 1
        t -= 1/3600
        min -= 1/60
        print("{} hours, {} minutes and {:.0f} seconds".format(t.__trunc__(), min.__trunc__(), sec))
        sec -= 1
        if min == 0:
            min = 60
        if sec == 0:
            sec = 60
        sleep(1)
