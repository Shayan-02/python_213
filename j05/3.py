user1 = input("بین سنگ و کاغذ و قیچی انتخاب کنید: ")
user2 = input("بین سنگ و کاغذ و قیچی انتخاب کنید: ")

if user1 == "سنگ" or user1 == "کاغذ" or user1 == "قیچی":
    if user2 == "سنگ" or user2 == "کاغذ" or user2 == "قیچی":
        if user1 == user2:
            print("مساوی")
        elif user1 == "سنگ":
            if user2 == "کاغذ":
                print("یوزر 2 برنده شد")
            else:
            # elif user2 == "قیچی":
                print("یوزر 1 برنده شد")
        elif user1 == "کاغذ":
            if user2 == "قیچی":
                print("یوزر 2 برنده شد")
            elif user2 == "سنگ":
                print("یوزر 1 برنده شد")
        elif user1 == "قیچی":
            if user2 == "کاغذ":
                print("یوزر 2 برنده شد")
            elif user2 == "سنگ":
                print("یوزر 1 برنده شد")
    else:
        print("کاربر 2 اشتباه وارد کرده است")
else:
    print("کاربر 1 اشتباه وارد کرده است")
