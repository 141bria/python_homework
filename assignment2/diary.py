import traceback
try:
    with open('diary.txt','a') as file:
        first_prompt = True
        while True:
            if first_prompt:
                info_user_day = input("What happened today? ")
                first_prompt = False
            else:
                info_user_day = input("What else? ")
            file.write(f"{info_user_day}\n")
            if info_user_day()== "done for now":
                break
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"An exception occured. {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")