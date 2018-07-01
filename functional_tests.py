from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    time.sleep(7)
    self.browser.quit()
  
  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')

    check_button_create = self.browser.find_element_by_name('create')
    self.assertEqual(check_button_create.get_attribute('value'), 'Create Question')
    time.sleep(3)
  
    check_button_create.click()
    check_url_create= self.browser.current_url
    self.assertRegex(check_url_create, '/createpage')
 
    input_question = self.browser.find_element_by_id('question')
    input_choice1 = self.browser.find_element_by_id('choice1')
    input_choice2 = self.browser.find_element_by_id('choice2')
    input_choice3 = self.browser.find_element_by_id('choice3')
    input_answer = self.browser.find_element_by_id('answer')

    self.assertEqual(input_question.get_attribute('placeholder'),'Enter your question')
    input_question.send_keys('What is color of the sky?')
    time.sleep(2)
    self.assertEqual(input_choice1.get_attribute('placeholder'),'Enter your choice')
    input_choice1.send_keys('Blue')
    time.sleep(2)
    self.assertEqual(input_choice2.get_attribute('placeholder'),'Enter your choice')
    input_choice2.send_keys('Pink')
    time.sleep(2)
    self.assertEqual(input_choice3.get_attribute('placeholder'),'Enter your choice')
    input_choice3.send_keys('Green')
    time.sleep(2)
    self.assertEqual(input_answer.get_attribute('placeholder'),'Enter your answer')
    input_answer.send_keys('Blue')
    time.sleep(2)

    submit_button = self.browser.find_element_by_name('create_button')
    submit_button.click()
    time.sleep(2)

    find_text = self.browser.find_element_by_id('1')

    self.assertEqual(find_text.get_attribute('name'), 'What is color of the sky?')
    find_text.click()
    time.sleep(2)

    find_ans = self.browser.find_element_by_id('answer_q')
    find_ans.click()
    submit_button2 = self.browser.find_element_by_id('create_ans')
    submit_button2.click()
 
    check_url_results= self.browser.current_url
    self.assertRegex(check_url_results, '/keepresults/*')
    time.sleep(2)

    input_home = self.browser.find_element_by_id('back_home')
    input_home.click()
    check_url_results= self.browser.current_url
    self.assertRegex(check_url_results, '/')


    
    self.fail('Finish the test!')

if __name__ == '__main__':
   unittest.main(warnings='ignore')
