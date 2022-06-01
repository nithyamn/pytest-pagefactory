from seleniumpagefactory.Pagefactory import PageFactory


class Homepage(PageFactory):
   def __init__(self, driver):
       self.driver = driver

   locators = {
      "user_name": ("CSS", ".username")
   }

   def get_username(self):
       retrieved_username = self.user_name.get_text()
       assert retrieved_username == "demouser"
