import json;
def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file) # json return the file in json list
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)
        
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']},Duration:{video['time']}")
    print("\n")
    print("*" * 70)
        
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    
def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to update: "))
    if 1<=index<=len(videos):
        name = input("Enter the video name ")
        time = input("Enter the video time ")
        videos[index-1] = {"name":name,"time":time} # index-1 means programmming using 0 indexing
        save_data_helper(videos)
    else:
        print("invalid index")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid video indexed selected")
    
def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add youtube videos")
        print("3. Update youtube videos details")
        print("4. Delete youtube videos")
        print("5. Exit the app")
        choice = input("Enter Your Choices: ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid videos")
                
if __name__ == "__main__":
    main()

output:

Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube videos
3. Update youtube videos details
4. Delete youtube videos
5. Exit the app
Enter Your Choices: 2
Enter video name: code with sumit
Enter video time: 15 hours

 Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube videos
3. Update youtube videos details
4. Delete youtube videos
5. Exit the app
Enter Your Choices: 1


**********************************************************************
1.code with sumit,Duration:15 hours


**********************************************************************

 Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube videos
3. Update youtube videos details
4. Delete youtube videos
5. Exit the app
Enter Your Choices: 2
Enter video name: code with akku
Enter video time: 16 hours

 Youtube Manager | choose an option
1. List all youtube videos
2. Add youtube videos
3. Update youtube videos details
4. Delete youtube videos
5. Exit the app
Enter Your Choices: 1


**********************************************************************
1.code with sumit,Duration:15 hours
2.code with akku,Duration:16 hours

**********************************************************************
