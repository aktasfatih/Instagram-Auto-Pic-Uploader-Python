from InstagramAPI import InstagramAPI
import os
import datetime
import time
print()

files = None

ID = None
Pass = None

#In hours
WaitingTime = 4

def main():
    global ID
    global Pass
    files = getFiles()
    print("You have "+ str(len(files)) + " pictures to upload.")

    if not files:
        print("You have nothing to upload at the moment.")
        print("Waiting for new pictures.")
        waitForPics()

    if ID == None and Pass == None:
        ID = raw_input("Username: ")
        Pass = raw_input("Password: ")
        print("Logging in...")
        for i in range(3,-1, -1):
            time.sleep(1)
            print(i)
    else:
        print("Logging in as " + ID)

    api = InstagramAPI(ID, Pass)
    if (api.login()):
        print("Login succes!")
    else:
        print("Can't login!")
        return True

    print("Starting uploading")
    while True:
        print("Uploading: ")
        photo_path = './images/'+ files[-1]
        filename, file_extension = os.path.splitext(files[-1])
        caption = filename
        print()
        print("CAPTION: ")
        print(caption)

        api.uploadPhoto(photo_path, caption=caption)

        now = datetime.datetime.now()
        print("Uploaded last at: " + now.strftime("%H"))
        text_file = open("./lastUpdated.txt", "w")
        text_file.write(now.strftime("%H"))
        text_file.close()

        print("Next Upload is at: ")
        print((now.hour + WaitingTime) % 24)

        time.sleep(WaitingTime*60*60)
        if len(files) > 0 :
            del files[-1]

        if not files:
            waitForPics()

def waitForPics():
    print("Looking for files...")
    while True:
        files = getFiles()
        if len(files) > 0 :
            print("Found some files")
            break
        else:
            print("NOPE")
            time.sleep(1)

def getFiles():
    for root, dirs, files in os.walk("./images"):
        return files



main()
