import os
import termcolor

def check():
    results=[]
    printed="1.1.5 Ensure noexec option set on /tmp partition: "
    print(printed,end='')
    one= False
    output = os.popen("mount | grep -E '\s/tmp\s' | grep -v noexec").read()
    if(output==""):
        one=True

    if(one):
        printed+="Success"
        results.append("1")
        print(termcolor.colored('Success', 'green'))
    else:
        printed += "Failed"
        results.append("0")
        print(termcolor.colored('Failed', 'red'))
    results.append(printed)
    return results
