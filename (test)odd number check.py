while True:
    user_input = input("Enter a number (or type ยกเลิก): ")

    if user_input.lower() == "ยกเลิก":
        print("ยกเลิกการทำงาน")
        break

    number = int(user_input)

    if number % 2 == 0:
        print("เป็นเลขคู่")
    else:
        print("เป็นเลขคี่")