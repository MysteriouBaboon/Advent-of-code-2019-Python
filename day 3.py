first_wire = [0, 0]
second_wire = [0, 0]
step_1 = 0
step_2 = 0


def check_number_of_steps1(value1, value2, step):
    if value1 == 1524:
        if value2 == 6491:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")



    if value1 == 3060:
        if value2 == 6518:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")

    elif value1 == 2660:
        if value2 == 7207:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")

    elif value1 == 2591:
        if value2 == 7655:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")

    elif value1 == 2377:
        if value2 == 7371:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")

    elif value1 == 1619:
        if value2 == 6769:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")

        elif value2 == 6788:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")

        elif value2 == 7028:
            print(step)
            print(str(value1 + value2))
            print("Wire 1")




def check_number_of_steps2(value1, value2,step):
    if value1 == 1524:
        if value2 == 6491:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

    elif value1 == 3060:
        if value2 == 6518:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

    elif value1 == 2660:
        if value2 == 7207:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

    elif value1 == 2591:
        if value2 == 7655:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

    elif value1 == 2377:
        if value2 == 7371:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

    elif value1 == 1619:
        if value2 == 6769:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

        elif value2 == 6788:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")

        elif value2 == 7028:
            print(step)
            print(str(value1 + value2))
            print("Wire 2")



def u(wire, value):
    global step_1
    global step_2
    for p in range(0, value):
        x = wire[-2] + 1
        wire.append(x)
        wire.append(wire[-2])
        if wire == first_wire:
            step_1 += 1
            check_number_of_steps1(wire[-2], wire[-1], step_1)

        if wire == second_wire:
            step_2 += 1
            check_number_of_steps2(wire[-2], wire[-1], step_2)



def l(wire, value):
    global step_1
    global step_2
    for p in range(0, value):
        y = wire[-1] - 1
        wire.append(wire[-2])
        wire.append(y)
        if wire == first_wire:
            step_1 += 1
            check_number_of_steps1(wire[-2], wire[-1],step_1)

        if wire == second_wire:
            step_2 += 1
            check_number_of_steps2(wire[-2], wire[-1], step_2)



def r(wire, value):
    global step_1
    global step_2
    for p in range(0, value):
        y = wire[-1] + 1
        wire.append(wire[-2])
        wire.append(y)
        if wire == first_wire:
            step_1 += 1
            check_number_of_steps1(wire[-2], wire[-1],step_1)

        if wire == second_wire:
            step_2 += 1
            check_number_of_steps2(wire[-2], wire[-1], step_2)



def d(wire, value):
    global step_1
    global step_2
    for p in range(0, value):
        x = wire[-2] - 1
        wire.append(x)
        wire.append(wire[-2])
        if wire == first_wire:
            step_1 += 1
            check_number_of_steps1(wire[-2], wire[-1],step_1)

        if wire == second_wire:
            step_2 += 1
            check_number_of_steps2(wire[-2], wire[-1], step_2)



first_wire_coordinates = [r(first_wire, 999), d(first_wire, 467),l(first_wire, 84),d(first_wire, 619),l(first_wire, 49),u(first_wire, 380),r(first_wire, 287),u(first_wire, 80),r(first_wire, 744),d(first_wire, 642),l(first_wire, 340),u(first_wire, 738),r(first_wire, 959),u(first_wire, 710),r(first_wire, 882),u(first_wire, 861),l(first_wire, 130),d(first_wire, 354),l(first_wire, 579),d(first_wire, 586),r(first_wire, 798),d(first_wire, 735),l(first_wire, 661),d(first_wire, 453),l(first_wire, 828),u(first_wire, 953),r(first_wire, 604),d(first_wire, 834),r(first_wire, 921),d(first_wire, 348),r(first_wire, 620),u(first_wire, 775),r(first_wire, 364),u(first_wire, 552),l(first_wire, 221),u(first_wire, 119),r(first_wire, 590),u(first_wire, 29),l(first_wire, 267),d(first_wire, 745),l(first_wire, 128),u(first_wire, 468),l(first_wire, 978),d(first_wire, 717),r(first_wire, 883),d(first_wire, 227),r(first_wire, 691),d(first_wire, 330),l(first_wire, 33),u(first_wire, 520),l(first_wire, 862),d(first_wire, 132),r(first_wire, 99),u(first_wire, 400),l(first_wire, 455),u(first_wire, 737),l(first_wire, 603),u(first_wire, 220),l(first_wire, 689),u(first_wire, 131),r(first_wire, 158),d(first_wire, 674),r(first_wire, 617),d(first_wire, 287),r(first_wire, 422),u(first_wire, 734),l(first_wire, 73),u(first_wire, 327),l(first_wire, 525),d(first_wire, 245),r(first_wire, 849),d(first_wire, 692),r(first_wire, 114),u(first_wire, 136),r(first_wire, 762),d(first_wire, 5),r(first_wire, 329),u(first_wire, 429),l(first_wire, 849),u(first_wire, 748),r(first_wire, 816),u(first_wire, 556),r(first_wire, 614),d(first_wire, 412),r(first_wire, 416),d(first_wire, 306),r(first_wire, 307),u(first_wire, 826),r(first_wire, 880),u(first_wire, 936),l(first_wire, 164),u(first_wire, 984),l(first_wire, 689),d(first_wire, 934),r(first_wire, 790),d(first_wire, 14),r(first_wire, 561),d(first_wire, 736),l(first_wire, 3),d(first_wire, 442),r(first_wire, 301),d(first_wire, 520),l(first_wire, 451),u(first_wire, 76),r(first_wire, 844),d(first_wire, 307),l(first_wire, 144),d(first_wire, 800),l(first_wire, 462),d(first_wire, 138),r(first_wire, 956),u(first_wire, 225),l(first_wire, 393),d(first_wire, 186),l(first_wire, 924),d(first_wire, 445),l(first_wire, 86),d(first_wire, 640),l(first_wire, 920),d(first_wire, 877),l(first_wire, 197),u(first_wire, 191),l(first_wire, 371),d(first_wire, 701),r(first_wire, 826),d(first_wire, 282),r(first_wire, 856),d(first_wire, 412),l(first_wire, 788),d(first_wire, 417),r(first_wire, 69),d(first_wire, 678),r(first_wire, 978),d(first_wire, 268),l(first_wire, 268),u(first_wire, 112),l(first_wire, 69),u(first_wire, 164),l(first_wire, 748),u(first_wire, 191),r(first_wire, 227),d(first_wire, 227),r(first_wire, 59),u(first_wire, 749),r(first_wire, 134),u(first_wire, 779),r(first_wire, 865),u(first_wire, 247),r(first_wire, 55),d(first_wire, 567),r(first_wire, 821),u(first_wire, 799),r(first_wire, 937),d(first_wire, 942),l(first_wire, 445),d(first_wire, 571),r(first_wire, 685),d(first_wire, 111),r(first_wire, 107),d(first_wire, 769),r(first_wire, 269),d(first_wire, 968),r(first_wire, 102),u(first_wire, 335),r(first_wire, 538),u(first_wire, 125),l(first_wire, 725),d(first_wire, 654),r(first_wire, 451),d(first_wire, 242),r(first_wire, 777),u(first_wire, 813),r(first_wire, 799),d(first_wire, 786),l(first_wire, 804),u(first_wire, 313),l(first_wire, 322),u(first_wire, 771),r(first_wire, 219),u(first_wire, 316),l(first_wire, 973),u(first_wire, 963),r(first_wire, 84),d(first_wire, 289),r(first_wire, 825),d(first_wire, 299),l(first_wire, 425),d(first_wire, 49),r(first_wire, 995),d(first_wire, 486),r(first_wire, 550),d(first_wire, 789),r(first_wire, 735),d(first_wire, 501),r(first_wire, 966),u(first_wire, 955),r(first_wire, 432),u(first_wire, 635),l(first_wire, 353),d(first_wire, 600),r(first_wire, 675),d(first_wire, 236),r(first_wire, 864),u(first_wire, 322),r(first_wire, 719),d(first_wire, 418),l(first_wire, 877),u(first_wire, 833),r(first_wire, 839),d(first_wire, 634),l(first_wire, 533),d(first_wire, 438),l(first_wire, 734),u(first_wire, 130),l(first_wire, 578),u(first_wire, 498),l(first_wire, 984),d(first_wire, 413),l(first_wire, 615),u(first_wire, 40),l(first_wire, 699),u(first_wire, 656),l(first_wire, 653),u(first_wire, 419),r(first_wire, 856),u(first_wire, 882),r(first_wire, 30),d(first_wire, 266),r(first_wire, 386),d(first_wire, 692),l(first_wire, 210),u(first_wire, 802),l(first_wire, 390),u(first_wire, 753),l(first_wire, 406),u(first_wire, 338),r(first_wire, 743),d(first_wire, 320),l(first_wire, 125),u(first_wire, 204),r(first_wire, 391),u(first_wire, 537),r(first_wire, 887),d(first_wire, 194),l(first_wire, 302),u(first_wire, 400),r(first_wire, 510),u(first_wire, 92),l(first_wire, 310),d(first_wire, 382),r(first_wire, 597),u(first_wire, 498),r(first_wire, 851),d(first_wire, 357),l(first_wire, 568),u(first_wire, 800),r(first_wire, 918),d(first_wire, 106),r(first_wire, 673),d(first_wire, 735),l(first_wire, 86),d(first_wire, 67),r(first_wire, 398),d(first_wire, 677),r(first_wire, 355),d(first_wire, 501),l(first_wire, 909),d(first_wire, 133),r(first_wire, 729),d(first_wire, 293),l(first_wire, 498),u(first_wire, 222),r(first_wire, 832),u(first_wire, 671),r(first_wire, 751),u(first_wire, 36),r(first_wire, 422),u(first_wire, 840),l(first_wire, 636),d(first_wire, 476),l(first_wire, 292),d(first_wire, 105),l(first_wire, 239),u(first_wire, 199),r(first_wire, 669),u(first_wire, 736),l(first_wire, 345),d(first_wire, 911),l(first_wire, 277),u(first_wire, 452),l(first_wire, 979),d(first_wire, 153),r(first_wire, 882),u(first_wire, 604),r(first_wire, 602),u(first_wire, 495),l(first_wire, 311),u(first_wire, 453),l(first_wire, 215),d(first_wire, 713),r(first_wire, 873)]
second_wire_coordinates = [l(second_wire, 996),u(second_wire, 773),l(second_wire, 865),d(second_wire, 472),l(second_wire, 988),d(second_wire, 570),l(second_wire, 388),u(second_wire, 458),l(second_wire, 87),u(second_wire, 885),l(second_wire, 115),u(second_wire, 55),r(second_wire, 75),u(second_wire, 582),r(second_wire, 695),u(second_wire, 883),r(second_wire, 83),u(second_wire, 285),r(second_wire, 96),d(second_wire, 244),l(second_wire, 647),d(second_wire, 359),r(second_wire, 136),u(second_wire, 107),r(second_wire, 912),u(second_wire, 871),l(second_wire, 844),u(second_wire, 395),l(second_wire, 63),u(second_wire, 899),l(second_wire, 205),d(second_wire, 137),r(second_wire, 549),u(second_wire, 221),l(second_wire, 859),d(second_wire, 429),l(second_wire, 809),u(second_wire, 127),r(second_wire, 304),u(second_wire, 679),l(second_wire, 511),u(second_wire, 144),r(second_wire, 926),u(second_wire, 95),l(second_wire, 805),u(second_wire, 811),r(second_wire, 42),d(second_wire, 248),l(second_wire, 546),d(second_wire, 644),l(second_wire, 551),d(second_wire, 897),r(second_wire, 368),d(second_wire, 391),l(second_wire, 224),u(second_wire, 164),l(second_wire, 490),d(second_wire, 991),l(second_wire, 146),d(second_wire, 615),r(second_wire, 536),u(second_wire, 247),r(second_wire, 10),u(second_wire, 998),l(second_wire, 957),d(second_wire, 233),r(second_wire, 706),d(second_wire, 926),r(second_wire, 760),u(second_wire, 438),r(second_wire, 270),d(second_wire, 983),r(second_wire, 134),u(second_wire, 738),l(second_wire, 262),u(second_wire, 301),l(second_wire, 480),d(second_wire, 635),l(second_wire, 702),d(second_wire, 715),r(second_wire, 479),u(second_wire, 500),r(second_wire, 19),d(second_wire, 291),r(second_wire, 368),u(second_wire, 203),r(second_wire, 305),d(second_wire, 999),r(second_wire, 106),u(second_wire, 355),l(second_wire, 683),d(second_wire, 298),r(second_wire, 90),u(second_wire, 968),l(second_wire, 254),d(second_wire, 936),r(second_wire, 89),u(second_wire, 496),r(second_wire, 253),u(second_wire, 688),r(second_wire, 99),u(second_wire, 637),l(second_wire, 783),d(second_wire, 451),r(second_wire, 673),d(second_wire, 762),r(second_wire, 997),d(second_wire, 50),l(second_wire, 488),u(second_wire, 551),l(second_wire, 871),u(second_wire, 388),r(second_wire, 949),d(second_wire, 371),r(second_wire, 584),d(second_wire, 908),l(second_wire, 880),u(second_wire, 523),r(second_wire, 557),u(second_wire, 436),r(second_wire, 520),u(second_wire, 587),l(second_wire, 56),u(second_wire, 18),r(second_wire, 397),u(second_wire, 541),r(second_wire, 660),d(second_wire, 444),r(second_wire, 51),u(second_wire, 187),r(second_wire, 221),u(second_wire, 902),r(second_wire, 726),u(second_wire, 303),r(second_wire, 97),d(second_wire, 817),r(second_wire, 185),d(second_wire, 218),l(second_wire, 240),d(second_wire, 67),l(second_wire, 259),u(second_wire, 334),r(second_wire, 821),u(second_wire, 629),r(second_wire, 21),d(second_wire, 970),r(second_wire, 282),u(second_wire, 155),r(second_wire, 555),d(second_wire, 678),l(second_wire, 99),d(second_wire, 570),r(second_wire, 863),d(second_wire, 405),r(second_wire, 941),u(second_wire, 584),l(second_wire, 303),d(second_wire, 109),l(second_wire, 871),u(second_wire, 180),r(second_wire, 595),d(second_wire, 226),l(second_wire, 670),d(second_wire, 943),l(second_wire, 127),u(second_wire, 647),r(second_wire, 452),d(second_wire, 570),r(second_wire, 75),d(second_wire, 284),r(second_wire, 414),u(second_wire, 404),r(second_wire, 515),u(second_wire, 993),r(second_wire, 408),u(second_wire, 488),r(second_wire, 890),d(second_wire, 318),l(second_wire, 415),u(second_wire, 969),r(second_wire, 769),d(second_wire, 976),l(second_wire, 732),u(second_wire, 1),r(second_wire, 489),u(second_wire, 655),r(second_wire, 930),u(second_wire, 638),r(second_wire, 649),d(second_wire, 254),r(second_wire, 161),u(second_wire, 287),l(second_wire, 659),d(second_wire, 26),l(second_wire, 477),d(second_wire, 821),l(second_wire, 124),u(second_wire, 538),r(second_wire, 17),d(second_wire, 711),l(second_wire, 203),u(second_wire, 888),r(second_wire, 904),u(second_wire, 648),l(second_wire, 908),d(second_wire, 65),l(second_wire, 215),u(second_wire, 283),r(second_wire, 698),u(second_wire, 28),r(second_wire, 72),u(second_wire, 214),r(second_wire, 499),d(second_wire, 89),r(second_wire, 489),d(second_wire, 58),r(second_wire, 949),d(second_wire, 91),l(second_wire, 710),u(second_wire, 960),l(second_wire, 755),d(second_wire, 402),l(second_wire, 27),d(second_wire, 873),r(second_wire, 61),u(second_wire, 607),r(second_wire, 57),d(second_wire, 548),r(second_wire, 369),u(second_wire, 622),l(second_wire, 244),u(second_wire, 19),r(second_wire, 61),d(second_wire, 606),r(second_wire, 928),d(second_wire, 968),r(second_wire, 10),d(second_wire, 988),r(second_wire, 816),u(second_wire, 500),r(second_wire, 915),d(second_wire, 400),r(second_wire, 546),d(second_wire, 283),l(second_wire, 627),d(second_wire, 919),l(second_wire, 259),u(second_wire, 337),r(second_wire, 374),u(second_wire, 795),l(second_wire, 355),d(second_wire, 989),l(second_wire, 224),d(second_wire, 77),l(second_wire, 872),u(second_wire, 901),r(second_wire, 476),u(second_wire, 765),l(second_wire, 320),u(second_wire, 768),l(second_wire, 937),d(second_wire, 437),r(second_wire, 141),d(second_wire, 822),l(second_wire, 326),d(second_wire, 324),l(second_wire, 498),u(second_wire, 994),l(second_wire, 518),d(second_wire, 857),r(second_wire, 973),d(second_wire, 681),l(second_wire, 710),d(second_wire, 590),l(second_wire, 879),u(second_wire, 499),r(second_wire, 488),d(second_wire, 151),l(second_wire, 242),u(second_wire, 988),l(second_wire, 944),u(second_wire, 683),l(second_wire, 24),u(second_wire, 491),r(second_wire, 823),d(second_wire, 246),r(second_wire, 872),d(second_wire, 654),r(second_wire, 28),u(second_wire, 581),l(second_wire, 142),u(second_wire, 31),r(second_wire, 435),d(second_wire, 686),l(second_wire, 147),d(second_wire, 102),r(second_wire, 952),d(second_wire, 607),l(second_wire, 959),d(second_wire, 929),l(second_wire, 46)]


first_wire_tuple = [(0, 0)]
second_wire_tuple = [(0, 0)]

i = 0

ii = 0
while i < len(first_wire):
            first_wire_tuple.append((first_wire[i], first_wire[i + 1]))
            i += 2
while ii < len(second_wire):
            second_wire_tuple.append((second_wire[ii], second_wire[ii + 1]))
            ii += 2


print("Ceci est la taille de ma liste" + str(len(first_wire)))
print("Ceci est la taille de mon tuple" + str(len(first_wire_tuple)))
print("Ceci est la taille de mon sorted" + str(len(sorted(set(first_wire_tuple).intersection(set(second_wire_tuple))))))
print("ceci sont les resultat les plus bas " + str(sorted(first_wire_tuple)))
print("Ceci sont mes resultat" + str((set(first_wire_tuple).intersection(set(second_wire_tuple)))))



