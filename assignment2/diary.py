try:
    with open('diart.txt','a') as file:
        while True:
            info_user_day = input("What happened today?")
            if info_user_day.lower()== "done for now":
                file.write(f"{info_user_day}\n")
except Exception as e:
    print(f"An error occured: {e}")