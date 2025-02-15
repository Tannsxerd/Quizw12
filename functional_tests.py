
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.utils.timezone import now
import time
from mypoll.models import Question,Choice


class PollTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()  
        pubdate = now()
        q1 = Question.objects.create(question_text="คุณชอบสีอะไร?",pub_date = pubdate)
        Choice.objects.create(question=q1, choice_text="แดง", votes=0)
        Choice.objects.create(question=q1, choice_text="น้ำเงิน", votes=0)

    def test_poll_flow(self):
       
        #tanny find poll web
        self.browser.get(self.live_server_url + "")
        #title of web is poll
        self.assertEqual("mypoll",self.browser.title)

        time.sleep(2)

        #tanny find question
        question_links = self.browser.find_elements(By.CSS_SELECTOR, "ul li a")
        self.assertGreater(len(question_links), 0, "ไม่มีคำถามให้เลือก!")

        #tanny click question
        question_links[0].click()
        time.sleep(2)  # รอให้หน้าโหวตโหลด

        #tanny click choice  to vote
        self.assertIn("you are looking at question", self.browser.page_source)
        
        #bring to vote page 
        choices = self.browser.find_elements(By.NAME, "choice")
        self.assertGreater(len(choices), 0, "ไม่มีตัวเลือกให้โหวต")

        #click vote form
        choices[0].click()

        #submit vote form
        vote_button = self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
        #bring to result
        vote_button.click()
        
        time.sleep(2)  

        #tanny close web
        self.browser.quit()


