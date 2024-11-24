name_file = input("File name: ").lower().strip()

if ".gif" in name_file:
    print("image/gif")

elif ".jpg" in name_file:
    print("image/jpeg")

elif ".jpeg" in name_file:
    print("image/jpeg")

elif ".png" in name_file:
    print("image/png")

elif ".pdf" in name_file:
    print("application/pdf")

elif ".txt" in name_file:
    print("text/plain")

elif ".zip" in name_file:
    print("application/zip")

else:
    print("application/octet-stream")
