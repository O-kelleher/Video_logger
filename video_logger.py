file = open('video_logger.txt', 'w')
number_of_videos = int(input("Enter number of videos: "))
for i in range(number_of_videos):
    video_time = str(input("Enter time of video in seconds: "))
    if video_time.isnumeric():
        str1 = video_time
        file.write(str1 + '\n')
    else:
        print("Video time must be a whole number")
        video_time = str(input("Enter time of video in seconds: "))
        str1 = video_time
        file.write(str1 + '\n')
file.close()
