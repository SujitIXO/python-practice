import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. {vid['name']}, Duration: {vid['time']}")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video name: ")
    videos.append({'name': name, 'time': time})
    data_helper(videos)

def update_video(videos):
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name")
        time = input("Enter the video duration")
        videos[index-1] = {'name': name, 'time': time}
        data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        data_helper(videos)
    else:
        print("Invalid video index selected")

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtubr videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        # print(videos)

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
                print("Invalid Choice")

if __name__ == "__main__":
    main()
