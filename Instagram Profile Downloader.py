# Programmer - python_scripts (Abhijith Warrier)

# Importing necessary packages
from tkinter import *
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import json, requests, urllib.request, tkinter as tk

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    urlLabel = Label(root, text="INSTAGRAM ID : ", background = "tan4")
    urlLabel.grid(row=0, column=0, padx=5, pady=5)

    root.urlEntry = Entry(root, width=30, textvariable=insta_id)
    root.urlEntry.grid(row=0, column=1,columnspan=2, pady=5)

    dwldBTN = Button(root, text="DOWNLOAD", command=i_Downloader, highlightbackground = "green")
    dwldBTN.grid(row=0, column=3, padx=5, pady=5)

    root.resultLabel = Label(root, textvariable=dwldtxt, background = "tan4")
    root.resultLabel.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
    root.resultLabel.config(font=("Courier", 25))

    root.previewLabel = Label(root, text="DP PREVIEW : ", background = "tan4")
    root.previewLabel.grid(row=3, column=0, padx=5, pady=5)

    root.dpLabel = Label(root, background = "tan4")
    root.dpLabel.grid(row=4, column=1, columnspan=2,padx=1, pady=1)

# Defining i_Downloader() to download the INSTAGRAM PROFILE PICTURE
def i_Downloader():
    # Storing the path where to download the instagram profile picture in download_path variable
    download_path = "YOUR DESTINATION PATH"
    # Fetching the user-input instagram id
    insta_username = insta_id.get()
    # Concatenating user-input instagram id with Instagram URL & storing complete URL in insta_url
    insta_url = "https://www.instagram.com/"+insta_username
    # Sending request to the insta_url URL & storing the response in insta_response
    insta_response =  requests.get(insta_url)
    # Specifying the desired format of the insta_Comments using html.parser
    # html.parser allows Python to read the components of the insta_Page
    soup = BeautifulSoup(insta_response.text, 'html.parser')
    # Finding <script> whose text matches with 'window._sharedData' using re.compile()
    script = soup.find('script', text=re.compile('window._sharedData'))
    # Splitting the text of <script>, 1 time at '=' and fetching the item at index 1
    # followed by removing the ';' from the string and storing the resulting string in page_json
    page_json = script.text.split(' = ', 1)[1].rstrip(';')
    # Parsing the above json page_json string using json_loads() and storing the resulting
    # dictionary in data variable which is a very long dictionary consisting of 19 items
    data = json.loads(page_json)
    # The profile_pic_url is present in value of key 'entry_data' which itself is a dictionary
    dp_url = data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    # Concatenating download_path with user-input username & .jpg extension & storing it as dp name
    dp_name = download_path+insta_username+'.jpg'
    # Download the profile_pic from dp_url and saving under 'dp_name':
    urllib.request.urlretrieve(dp_url, dp_name)
    # Opening the dp_name image using the open() method of the Image module
    dp_image = Image.open(dp_name)
    # Resizing the image using Image.resize()
    dp_image = dp_image.resize((200, 200), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    image = ImageTk.PhotoImage(dp_image)
    # Configuring the label and displaying the image
    root.dpLabel.config(image=image)
    root.dpLabel.photo = image
    # Displaying success message
    dwldtxt.set('DP DOWNLOADED SUCCESSFULLY')

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color disabling
# the  resizing property of the tkinter window
root.geometry("510x350")
root.title("i-DP DOWNLOADER")
root.config(background = "tan4")

# Creating tkinter variable
insta_id = StringVar()
dwldtxt = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
