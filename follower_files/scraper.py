import twint

tweets = []
c = twint.Config()

usernames = open('randomusers.csv', "r")
for name in usernames:
    c.Search = name
    c.Store_csv = True
    c.Output = "none"
    twint.run.Search(c)

