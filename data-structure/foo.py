def open_box():
    global count
    count -= 1
    print("count:", count)
    if count == 0 :
        return
    open_box()
    print("The box is now open.",count)

count = 10
open_box()