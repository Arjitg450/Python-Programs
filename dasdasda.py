from nltk.corpus import wordnet
import time
import pyperclip
import subprocess

old_word=""
while(True):
    synonyms=[]
    time.sleep(2)
    new_word=pyperclip.paste()
    if(new_word!=old_word):
        print(pyperclip.paste())
        
        define=wordnet.synsets(new_word)
        
        for i in define:
            for j in i.lemmas():
                synonyms=synonyms+[j.name()]
        
        counter=1
        definitions=""
        for i in define:
            message=str(counter)+'. '+i.definition()+'\n'
            definitions=definitions+'\n'+message
            counter=counter+1
            print(definitions)
        
        synonyms=set(synonyms)
        synonyms=', '.join(synonyms)
        
        script='\ndisplay dialog "Word meanings are - \n'+definitions+'\n\nSynonyms - \n\n'+synonyms+'" ¬\nwith title "'+new_word+'" ¬\nwith icon caution ¬\nbuttons {"OK"}\n'
        subprocess.call("osascript -e '{}'".format(script), shell=True)
        
        old_word=pyperclip.paste()
