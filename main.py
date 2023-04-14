import imgkit
import time
import os
import random
from instagrapi import Client
from decouple import config

from features import fetchFact
from features import fetchImage


while True:
    username = config("INSTA_USERNAME")#"facts1Fantastic1facts"#artisticwonders_234
    password = config("INSTA_PASSWORD")#"password.1"
    fact = fetchFact.fetchFact()
    image_theme_array = ["mystery", "color", "art","nature"]
    image_theme = image_theme_array[random.randint(0,2)]
    image = fetchImage.fetchImage(image_theme)


    if len(fact) < 90:
        textSize = "5"
    elif len(fact) < 120:
        textSize = "4"
    else:
        textSize = "3"

    with open("test.html", "r") as file:
        content = file.read()
        addedText_content = content.replace("test_url_to_replace", image)
        final_content = addedText_content.replace("random_fact_to_replace", fact)
        contentFinal = final_content.replace("fact_font_size",textSize)
        
    with open("output.html", "w") as file:
        file.write(contentFinal)




    input_html = "output.html"
    output_image = os.getcwd() + "/posts/"+str(time.time())+".jpg" 


    # Configure the options for imgkit
    options = {
        "format": "jpg",  # Change this to "jpg" for JPEG output
        "quality": 100,   # Quality value, 100 for maximum quality
    }


    imgkit.from_file(input_html, output_image, options=options)

    image_path = output_image
    caption = "😸hi guys new post has arrived 🛩️" + "\n🔗link to image: " + image 
    bot = Client()


    bot.login(username, password)

    # Upload and post the image
    try:
        media = bot.photo_upload(image_path, caption)
        bot.photo_configure(media,1200,1200, "😸hi guys new post has arrived 🛩️" + "\n🔗link to image: " + image)
    except:
        print("little error")
        pass
    print("😏done\n.......................................\n")
    print("🔄Starting a new cycle")
    time.sleep(3689*random.randint(1,4))
