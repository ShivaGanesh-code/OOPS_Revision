class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedIn = ''
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like to proceed
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        
        if user_input == '1':
            self.signup()
        elif user_input =='2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.send_msg()
        else:
            exit()


    def signup(self):
        email = input("enter your email here")
        password = input("setup your password here")
        self.username = email
        self.password = password
        print('You have signed up successfully')
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input('enter your email/username here -> ')
            pwd = input('enter your password here-> ')
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!!")
                self.loggedIn = True
            else:
                print("Please input correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedIn == True:
            txt = input("enter your message here-> ")
            print(f"following content has been posted-> {txt}")
        else:
            print("You need to signin first to post something.")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedIn == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the message...")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first")
        print("\n")
        self.menu()

obj = chatbook()
