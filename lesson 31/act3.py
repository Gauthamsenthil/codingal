#display capital,language,type for india and usa

class india:

    def capital(self):
        print("new delhi is the capital of india")

    def language(self):
        print("hindi is the national language of india")

    def type(self):
        print("india is a developing country")

class usa:

    def capital(self):
        print("washington dc is the capital of usa")

    def language(self):
        print("english is the national language of usa")

    def type(self):
        print("usa is a developed country")

#driver code
obj_ind = india()
obj_ind.capital()
obj_ind.language()
obj_ind.type()

obj_usa = usa()
obj_usa.capital()
obj_usa.language()
obj_usa.type()