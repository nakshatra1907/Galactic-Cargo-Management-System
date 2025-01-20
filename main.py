# red max min
# yellow min max
# green max max
# blue min min


from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException

if __name__ == "__main__":

    gcms = GCMS()
    gcms.add_bin(4200, 100)
    gcms.add_bin(4300, 42)
    gcms.add_bin(4900, 74)
    gcms.add_bin(7967, 79)
    gcms.add_bin(1234, 55)
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    try:
        gcms.add_object(7000, 45, Color.RED)
    except:
        print("Error adding object 1")
    print(gcms.object_info(7000))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.add_object(7001, 37, Color.BLUE)
    except:
        print("Error adding object 2")
    print(gcms.object_info(7001))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    try:
        gcms.add_object(7002, 5, Color.RED)
    except:
        print("Error adding object 3")
    print(gcms.object_info(7002))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    try:
        gcms.add_object(7003, 37, Color.BLUE)
    except:
        print("Error adding object 4")
    print(gcms.object_info(7003))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    try:
        gcms.add_object(7004, 29, Color.RED)
    except:
        print("Error adding object 5")
    print(gcms.object_info(7004))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    try:
        gcms.add_object(7005, 19, Color.RED)
    except:
        print("Error adding object 5")
    print(gcms.object_info(7005))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.add_object(7006, 9, Color.RED)
    except:
        print("Error adding object 6")
    print(gcms.object_info(7006))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.delete_object(7006)
    except:
        print("Error deleting object 6")
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.add_object(7007, 19, Color.BLUE)
    except:
        print("Error adding object 7")
    print(gcms.object_info(7007))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    print(gcms.tree_caps.search(55).value.in_order())
    try:
        gcms.add_object(7008, 18, Color.GREEN)
    except:
        print("Error adding object 8")
    print(gcms.object_info(7008))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.add_object(7009, 4, Color.YELLOW)
    except:
        print("Error adding object 9")
    print(gcms.object_info(7009))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.add_object(7010, 15, Color.YELLOW)
    except:
        print("Error adding object 10")
    print(gcms.object_info(7010))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())

    try:
        gcms.add_object(7011, 36, Color.YELLOW)
    except:
        print("Error adding object 11")
    print(gcms.object_info(7011))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))
    print(gcms.tree_caps.in_order())
    try:
        gcms.add_object(7012, 30, Color.YELLOW)
    except:
        print("Error adding object 11")



    print(gcms.object_info(7012))
    print(gcms.bin_info(4200))
    print(gcms.bin_info(4300))
    print(gcms.bin_info(4900))
    print(gcms.bin_info(7967))
    print(gcms.bin_info(1234))