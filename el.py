import os
import shutil


folder = input("Enter the folder path: ")

if not os.path.exists(folder):
    print("The specified folder does not exist.")
else:
    files = os.listdir(folder)

    image = 0
    documents = 0
    videos = 0
    other = 0

    for name in [
        "Images",
        "Documents",
        "Videos",
        "Other"
    ]:
        path = os.path.exists(os.path.join(folder, name))

        if not path:
            os.mkdir(os.path.join(folder, name))

    for file in files:
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1].lower()

            if extension in [".jpg", ".jpeg", ".png", ".gif"]:
                shutil.move(file_path, os.path.join(folder, "Images", file))
                image += 1
            elif extension in [".pdf", ".docx", ".txt"]:
                shutil.move(file_path, os.path.join(folder, "Documents", file))
                documents += 1
            elif extension in [".mp4", ".avi", ".mov"]:
                shutil.move(file_path, os.path.join(folder, "Videos", file))
                videos += 1
            else:
                shutil.move(file_path, os.path.join(folder, "Other", file))
                other += 1

                shutil.move(file_path, os.path.join(folder, "Other", file))
            



    