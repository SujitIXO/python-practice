import os
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_DBNAME = os.getenv("MONGODB_DBNAME")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

client = MongoClient(f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.shuggbd.mongodb.net/{MONGODB_DBNAME}", tlsAllowInvalidCertificates = True)

db = client[MONGODB_DBNAME] #This is the Database
video_collection = db[MONGODB_COLLECTION] #Database collection


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video ['name']} and Time: {video['time']}")

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the updated video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id, name, time)
        elif choice == '5':
            break
        else:
            print("enter valid number")


if __name__ == "__main__":
    main()