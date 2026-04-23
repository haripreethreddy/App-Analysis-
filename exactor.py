from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the WebDriver
driver = webdriver.Chrome()
app_id = "org.altruist.BajajExperia"
# Navigate to the app page on Google Play Store
app_url = f'https://play.google.com/store/apps/details?id={app_id}'  # Replace with the actual app URL
driver.get(app_url)

try:
    # Wait for the "See all reviews" button to be clickable
    see_all_reviews_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'See all reviews')]"))
    )
    
    # Click the button
    see_all_reviews_button.click()
    print("Successfully clicked 'See all reviews' button")
    time.sleep(3)

    # for scroll for 1 minute
    reviews_popup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".fysCi"))
    )
    end_time = time.time() + 60 
    scroll_amount = 10 * reviews_popup.size['height']  
    while time.time() < end_time:
     driver.execute_script("arguments[0].scrollTop += arguments[1];", reviews_popup, scroll_amount)
     time.sleep(0.1)  # Reduced sleep time for faster scrolling




    
        
    
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

    #name
   
    reviews_divs = soup.find('div', class_='VfPpkd-Sx9Kwc cC1eCc UDxLd PzCPDd HQdjr VfPpkd-Sx9Kwc-OWXEXe-FNFY6c')
    
    
    fsd = reviews_divs.find('div',class_='VfPpkd-wzTsW')
    sd = fsd.find('div',class_='VfPpkd-P5QLlc')
    jko = sd.find('div',class_='VfPpkd-cnG4Wd')
    dsa = jko.find('div')
    sa = dsa.find('div',class_='jgIq1')
    qda = sa.find('div',class_='fysCi Vk3ZVd')
    qedvds = qda.find('div',class_='odk6He')
    qqq = qedvds.find_all('div',class_='RHo1pe')
    
    with open(f'posts/reviews.txt','w', encoding='utf-8') as f:
     count = 0
     for q in qqq:
      

        count = count+1 
        rating = q.find('header')
        final_rating = rating.find('div',class_='Jx4nYe')
        rated = final_rating.find('div',class_='iXRFPc')
        aria_label = rated.get('aria-label').split()[1]
        dated_review = final_rating.find('span',class_='bp9Aid').text
     
        username = q.find('div',class_='YNR7H')
        fds = username.find('div',class_='gSGphe')
        realname = fds.find('div',class_='X5PpBb').text
       
        review = q.find('div',class_='h3YV2d').text

        founduseful = q.find('div',class_='AJTPZc')

        answered = q.find('div',class_='ocpBU')
       
      
        def neat_founduseful(founduseful):
           if(founduseful is None):
                 return '0'
           else:
                 return f"{founduseful.text.split()[0]}"
        def neat_answered(answered):
           if (answered == None):
              return f"No"
           else:
              return f"Yes"
        fs = neat_founduseful(founduseful)
        wer = neat_answered(answered)
        f.write(f"{realname}" + ']' + f"{aria_label}" + ']' + f"{review}" + ']' + f"{dated_review}" + ']' + f"{fs}" + ']' + f"{wer}\n")
    
    print(count)

    
    main= soup.find('c-wiz',class_='SSPGKf Czez9d')
    main_df = main.find('div')
    cp = main_df.find('div',class_='kFwPee')
    dsdfw = cp.find('div')
    hgf = dsdfw.find('div',class_='tU8Y5c')
    names = hgf.find('div',class_='P9KVBf')
    nsa = names.find('c-wiz')
    sd = nsa.find('div',class_='hnnXjf XcNflb J1Igtd')
    s = sd.find('div',class_='RhBWnf')
    rt = s.find('div',class_='Fd93Bb F5UCq p5VxAd')
    print(f"App Name:{rt.h1.text}")
    #rating 
    ratewq = nsa.find('div',class_='JU1wdd')
    opr = ratewq.find('div',class_='w7Iutd')
    casf = opr.find_all('div',class_='wVqUob')

    for p in casf:
        overall = p.find('div',class_='TT9eCd')
         
        total_reviews = p.find('div',class_='g1rdde')
        
        overed = p.find('div',class_='ClM7O')
        
        print(overall.text.strip())
        print(total_reviews.text)
        #print(overed.text)
 
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
