import pywhatkit as ps
txt = '''Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:
- web development (server-side),
- software development,
- mathematics,
- system scripting.'''

ps.text_to_handwriting(txt,"Make_Handwritten_Assignment.py",[0,0,135])
print("End")