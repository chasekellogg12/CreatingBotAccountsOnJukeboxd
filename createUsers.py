from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver


# every user needs to:
    # open the website at /create-user
    # create an account
    # wait for then click create-post
    # wait for then click selectTrackButton 
    # wait for then enter 'songName' into searchSongField
    # click 'searchButton'
    # wait for then click 'selection1'
    # wait for then click 'star' + 'rating' (concatinate)
    # enter 'postText' into postTextInput
    # click 'postButton'
    # wait for then click 'logoutButton'

users = [
    {"username": "vinyllover", "name": "Vinny L.", "postSubject": "Life on Mars", "postRating": "star5", "postText": "Bowie's masterpiece. Gets me every time."},
    {"username": "dancer42", "name": "Ella Swing", "postSubject": "Uptown Funk", "postRating": "star4", "postText": "Perfect for a weekend dance-off!"},
    {"username": "emo_revival", "name": "Chris Black", "postSubject": "Welcome to the Black Parade", "postRating": "star5", "postText": "Takes me back to the good old days."},
    {"username": "pop_princess", "name": "Katie Sparkle", "postSubject": "Shake It Off", "postRating": "star4", "postText": "Super catchy and empowering."},
    {"username": "alt_rock_guru", "name": "Jesse Reed", "postSubject": "Smells Like Teen Spirit", "postRating": "star2", "postText": "Overrated and overplayed."},
    {"username": "metalhead666", "name": "Lars Inferno", "postSubject": "Enter Sandman", "postRating": "star5", "postText": "Metallica rules! This is the anthem."},
    {"username": "folkie", "name": "Joni Mitch", "postSubject": "Big Yellow Taxi", "postRating": "star5", "postText": "Folk music at its best."},
    {"username": "rapgodfan", "name": "Miles Poetic", "postSubject": "Sicko Mode", "postRating": "star3", "postText": "Not bad, but Travis Scott has better tracks."},
    {"username": "jazzcat", "name": "Mona Blue", "postSubject": "Take Five", "postRating": "star5", "postText": "A jazz standard. Always refreshing."},
    {"username": "tranceaddict", "name": "Trisha Beat", "postSubject": "Adagio For Strings", "postRating": "star4", "postText": "Epic track, a trance classic."},
    {"username": "groovy67", "name": "Donna Summer", "postSubject": "September", "postRating": "star5", "postText": "Never gets old! Earth, Wind & Fire forever!"},
    {"username": "punkrocker", "name": "Sid Vicious", "postSubject": "Anarchy in the UK", "postRating": "star4", "postText": "Punk isn't dead!"},
    {"username": "kpopfanatic", "name": "Kim Lee", "postSubject": "Dynamite", "postRating": "star5", "postText": "BTS can do no wrong. Love this!"},
    {"username": "bluesman", "name": "Robert J.", "postSubject": "Crossroad", "postRating": "star1", "postText": "Just couldn't get into this one."},
    {"username": "indiekid", "name": "Zoe Indie", "postSubject": "Somebody That I Used To Know", "postRating": "star5", "postText": "Indie pop at its finest."},
    {"username": "discodiva", "name": "Gloria Shimmer", "postSubject": "Stayin' Alive", "postRating": "star3", "postText": "Good but overplayed."},
    # ADD MORE USERS HERE
]

for user in users:
    # Open the website
    driver = webdriver.Chrome()
    driver.get("https://jukeboxd-frontend.vercel.app/create-user")

    # CREATE AN ACCOUNT
    name_field = driver.find_element(By.ID, "nameFieldId")  # Use the actual ID or XPATH
    name_field.send_keys(user["name"]) # PARAM1

    email_field = driver.find_element(By.ID, "emailFieldId")  # Use the actual ID or XPATH
    email_field.send_keys(user["username"] + "@gmail.com")

    username_field = driver.find_element(By.ID, "usernameFieldId")  # Use the actual ID or XPATH
    username_field.send_keys(user["username"])

    password1_field = driver.find_element(By.ID, "password1FieldId")  # Use the actual ID or XPATH
    password1_field.send_keys("bbbbbbbb")

    password2_field = driver.find_element(By.ID, "password2FieldId")  # Use the actual ID or XPATH
    password2_field.send_keys("bbbbbbbb")

    # Click the 'Submit' button
    submit_button = driver.find_element(By.ID, "submitButtonId")  # Use the actual ID or XPATH
    submit_button.click()

    # WAIT FOR THEN CLICK create-post
    wait = WebDriverWait(driver, 3)  # Wait for a maximum of 10 seconds
    create_post_button = wait.until(EC.presence_of_element_located((By.ID, "createPostButtonId")))
    create_post_button.click()

    # wait for then click selectTrackButton 
    select_track_button = wait.until(EC.presence_of_element_located((By.ID, "selectTrackButton")))
    select_track_button.click()

    # wait for then enter 'songName' into searchSongField
    searchSongField = wait.until(EC.presence_of_element_located((By.ID, "searchSongField")))
    searchSongField.send_keys(user["postSubject"]) # PARAMETER

    # click 'searchButton'
    searchButton = driver.find_element(By.ID, "searchButton")
    searchButton.click()

    # wait for then click 'selection1'
    selection1 = wait.until(EC.presence_of_element_located((By.ID, "selection1")))
    selection1.click()

    # wait for then click 'star' + 'rating' (concatinate)
    postRating = wait.until(EC.presence_of_element_located((By.ID, user["postRating"])))
    postRating.click()

    # enter 'postText' into postTextInput
    postTextInput = driver.find_element(By.ID, "postTextInput")
    postTextInput.send_keys(user["postText"]) # PARAMETER

    # click 'postButton'
    postButton = driver.find_element(By.ID, "postButton")
    postButton.click()

    postNumber1 = wait.until(EC.presence_of_element_located((By.ID, "postNumber1")))

    # wait for then click 'logoutButton'
    logoutButton = driver.find_element(By.ID, "logoutButton")
    logoutButton.click()

    # Close the browser
    driver.close()
