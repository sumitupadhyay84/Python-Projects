import requests

def user_api():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json() # here convert all data into json formate and called the data. 
    
    if data["success"] and "data" in data:
        user_data = data["data"] # data ke under jo data hai called is user_data
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_name,country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        user_name,country = user_api()
        print(f"User_name:{user_name} \nCountry:{country}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()

output:

sumit@sumitupadhyay MINGW64 ~/OneDrive/Desktop/Explore-python
$ python -u "c:\Users\sumit\OneDrive\Desktop\Explore-python\Handling_Api\Freeapi.py"
user_name:greenpanda411 
Country:Serbia

sumit@sumitupadhyay MINGW64 ~/OneDrive/Desktop/Explore-python
$ python -u "c:\Users\sumit\OneDrive\Desktop\Explore-python\Handling_Api\Freeapi.py"
name 'user_name' is not defined

sumit@sumitupadhyay MINGW64 ~/OneDrive/Desktop/Explore-python
$ python -u "c:\Users\sumit\OneDrive\Desktop\Explore-python\Handling_Api\Freeapi.py"
User_name:heavybutterfly101 
Country:India

sumit@sumitupadhyay MINGW64 ~/OneDrive/Desktop/Explore-python
$ python -u "c:\Users\sumit\OneDrive\Desktop\Explore-python\Handling_Api\Freeapi.py"
User_name:lazypeacock856 
Country:United States

sumit@sumitupadhyay MINGW64 ~/OneDrive/Desktop/Explore-python
$ python -u "c:\Users\sumit\OneDrive\Desktop\Explore-python\Handling_Api\Freeapi.py"
User_name:lazypeacock856 
Country:United States

sumit@sumitupadhyay MINGW64 ~/OneDrive/Desktop/Explore-python
$ python -u "c:\Users\sumit\OneDrive\Desktop\Explore-python\Handling_Api\Freeapi.py"
User_name:greentiger702 
Country:Iran
