while True:
    user_zip = input("please enter a zip code:")
    strip_zip = user_zip.strip()
    a = len(strip_zip)
    b = strip_zip.isdigit()
    if a == 5 and b:
       print("good zip")
       break
    else:
       print("invalid zip")    
