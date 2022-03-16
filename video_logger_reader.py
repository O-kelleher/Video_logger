clip_number = 0
file = open('video_logger.txt', 'r')
with open('video_logger.txt', 'r'):
    total_run_time = file.read()
    total_run_time_ints = [int(x) for x in total_run_time.split()]
    print("The total run time of this commercial is", sum(total_run_time_ints), "seconds")
file.seek(0)
for x in file:
    clip_number = clip_number + 1
    print("Video", clip_number, "run time is", x, "seconds")
file.close()
