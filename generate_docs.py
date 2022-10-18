from os import listdir
from rumble_bot import RumbleBot
import inspect

with open ("example.py", 'r')  as stream_example:
    example = "## Example: \r\n```py\r\n" + stream_example.read() + "\r\n```"

with open ("README.md", 'w+')  as stream_readme:
    stream_readme.write(f"""
# RumbleBot
*Unofficial Python wrapper for automating a Rumble account (Rumble.com).*
* This proof-of-concept is a work in progress, and is primitive at best.
* In no way am I affiliated with Rumble.com.
* This is not intended for public use and I am not responsible for any damage caused by this software.

{example}
            """)

r = RumbleBot()

# iterate over function variables
with open ("README.md", 'a') as stream_append:
    
    stream_append.write("\r\n## Methods:\r\n")
    method_docs = []
    for func in dir(r):
        if "__" not in func:
            doc = inspect.getdoc(getattr(r, func))
            if doc:
                source = inspect.getsource(getattr(r, func))
                definition = "???"
                for line in source.splitlines():
                    if "def" in line:
                        definition = line.split("def ")[1].split(":")[0]
                        break
                        
                method_docs.append(f"""
#### *[`RumbleBot.{definition}`](#{func})*
> {doc}""")
                
    # Ensure array item with substring "RumbleBot.login" is first item in array
    for item in method_docs:
        if "RumbleBot.login" in item:
            method_docs.insert(0, method_docs.pop(method_docs.index(item)))
                
    stream_append.write("\r".join(method_docs))
        


        

