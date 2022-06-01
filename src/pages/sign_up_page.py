from seleniumpagefactory.Pagefactory import PageFactory


class SignUpPage(PageFactory):
   def __init__(self, driver):
       self.driver = driver

   locators = {
       'sign_in': ('ID', 'signin'),
       'username': ('CSS', '#username input'),
       'password': ('CSS', '#password input'),
       'log_in': ('ID', 'login-btn')
   }

   def click_on_signin(self):
        self.sign_in.click()
   
   def enter_username(self):
        self.username.set_text('demouser\n')
  
   def enter_password(self):
        self.password.set_text('testingisfun99\n')

   def click_on_login(self):
        self.log_in.click()
