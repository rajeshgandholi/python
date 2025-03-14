import re
# re.search("is", "How many is are there here?")

# re.search("view.$", "How is the view?")

re.search("mala*vika", "how is mal and vika?") #no search

re.search("mala*vika", "how is malvika?") # search success, * means "a" to be available 0 or many times

re.search("mala+vika", "how is malavika?") # search success, * means at lease "a" to be available once

re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')