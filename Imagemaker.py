import pyperclip

prompts = pyperclip.paste()

prompts = prompts.replace('<pre id="tiresult" style="font-size: 9px; background-color: #000000; font-weight: bold; padding: 4px 5px; --fs: 9px;">', "")
prompts = prompts.replace('</pre>', "")
prompts = prompts.replace('b style="color:', "color=")
prompts = prompts.replace('</b>', "</color>")
prompts = prompts.replace('"', "")

newprompt = ""

for i,v in enumerate(prompts.splitlines()):
    if i != 0:
        newprompt = newprompt+"\\n"+v
    else:
        newprompt = v

newprompt = "<size=2>"+newprompt+"</size>"

pyperclip.copy(newprompt)
print("Copied converted html code to clipboard")