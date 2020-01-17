import os
import schedule
import shutil
import time

def job1():
    source_folder = r'C:\Users\User\Desktop\Bye'
    destination_folder = 'C:\Users\User\Desktop\Cheese'

    for src_dir, dirs, files in os.walk(source_folder):
        dst_dir = src_dir.replace(source_folder, destination_folder, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.copy(src_file, dst_dir)

schedule.every().day.at("20:00").do(job1)

while True:
    schedule.run_pending()
    time.sleep(100000000000000000000000000000000000000000000000)

def job2():
    print("I'm working...")

schedule.every(10).minutes.do(job2)
schedule.every().hour.do(job2)
schedule.every().day.at("10:30").do(job2)
schedule.every(5).to(10).minutes.do(job2)
schedule.every().monday.do(job2)
schedule.every().wednesday.at("13:15").do(job2)
schedule.every().minute.at(":17").do(job2)

while True:
        schedule.run_pending()
        time.sleep(1000000000000000000000000000000000)
