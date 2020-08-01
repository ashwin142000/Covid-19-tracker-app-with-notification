import requests
import bs4
import tkinter as tk
from PIL import ImageTk, Image
import plyer
import time
import datetime
import threading


def get_corona_detail_of_india():
	url='https://www.mygov.in/covid-19'
	data=requests.get(url)
	bs = bs4.BeautifulSoup(data.text, 'html.parser')
	alldetails=""
	#info=bs.find("div",class_="information_row").find('div',class_='info_title').get_text()
	t_case=bs.find("div",class_="iblock_text").find('span',class_='icount').get_text()
	active_cases=bs.find("div",class_="iblock active-case").find('span',class_='icount').get_text()
	discharge=bs.find("div",class_="iblock discharge").find("span",class_="icount").get_text()
	deaths=bs.find("div",class_="iblock death_case").find("span",class_="icount").get_text()
	total_samples=bs.find("div",class_="testing_result").find("strong").get_text()
	sample_today=bs.find("div",class_="testing_sample").find("strong").get_text()
	alldetails +='Total Cases:'+t_case+'\n'+"Active Cases:"+active_cases+'\n'+"Deaths:"+deaths+'\n'+"Total Samples Tested:"+total_samples+'\n'+"Samples Tested Today:"+sample_today
	return alldetails


def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing..")
    mainLabel['text'] = newdata

def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            #app_icon='icon.ico'
        )
        time.sleep(300)

root = tk.Tk()
root.geometry("900x800")
root.iconphoto(False, tk.PhotoImage(file='E:\Project\Covidtacker\icon.ico'))
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background='white')
f = ("poppins", 25, "bold")
banner = ImageTk.PhotoImage(Image.open("E:\Project\Covidtacker\photo.jpeg"))
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f, bg='white')
mainLabel.pack()

reBtn = tk.Button(root, text="REFRESH", font=f, relief='solid', command=refresh)
reBtn.pack()

# create a new thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()