import requests as rq
from bs4 import * 
import os

print("""
                                  888                                         
888 88e   ,e e,   Y8b Y8Y  ,e e,  888  dP"Y      e88'888  e88 88e  888 888 8e 
888 888b d88 88b   Y8b Y  d88 88b 888 C88b      d888  '8 d888 888b 888 888 88b
888 888P 888   ,  e Y8b   888   , 888  Y88D d8b Y888   , Y888 888P 888 888 888
888 88"   "YeeP" d8b Y8b   "YeeP" 888 d,dP  Y8P  "88,e8'  "88 88"  888 888 888
888                                                                           
888                                 pexels Image Scraper
                                    
                                    Devloper:- Bhargav 
                                   
""")

try:
    
    print("pexels Image Scraper ")

    urla=input("Enter a Interest Images : ")

    url = "https://www.pexels.com/search/"+urla
    da = rq.get(url) 

    soup = BeautifulSoup(da.text, 'html.parser') 

    link = []

    img = soup.select('img[src^="https://images.pexels.com/photos"]')

    for im in img:
        link.append(im['src'])


    la=0;
    for i in link:
        la=la+1

    print("Maximum Number of Images Scrap This Profile : ",la)
    
    si=int(input("How Many Images Do You Want to Scrap ? : "))
    
    folder=input("Enter a Folder Name To Create Folder  And Store The Images : ")
    
    os.mkdir(folder)
    
    ffol=folder+"/"

    i=1

    if la>=si:
        for index,img_link in enumerate(link):
            if i<=si:
                img_data=rq.get(img_link).content
                imgname=urla+str(index+1)
                with open(ffol+imgname+'.jpg','wb+') as f:
                    f.write(img_data)
                print("Download Image "+imgname+",jpg")
                i=i+1
            else:
                f.close()
                break
        print("Images Download Successfully..")
    else:
        print("You can't scrap mor img.....")
    

except :
    print("Somting is not good.....")

