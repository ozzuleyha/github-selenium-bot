from selenium import webdriver
from githubUserInfo import username, password
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("http://github.com/login")
        self.browser.maximize_window()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login_field']")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()

    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".f4.link-gray-dark").text)


    def getFollowers(self):
        self.browser.get(f"https://github.com/{username}?tab=followers")
        time.sleep(2)
        self.loadFollowers()

        while True:
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()

                else:
                    break
            else:
                for link in links:
                    if link.text =="Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue
                    


github = Github(username, password)
# github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)