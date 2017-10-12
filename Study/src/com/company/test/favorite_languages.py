from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages["Suresh"]="python"
favorite_languages["Kumar"]="Java"
favorite_languages["Gupta"]="c"

for key in favorite_languages.keys():
    print(key+" like to use :"+favorite_languages[key].title())
    
lang = {}
lang["Suresh"]="python"
lang["Kumar"]="Java"
lang["Gupta"]="c"
lang["1"]="2"

for key in lang.keys():
    print(key+" like to use :"+lang[key])
