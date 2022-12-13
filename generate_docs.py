from   RumblePy import RumbleBot
import inspect

with open ("example.py", 'r')  as stream_example:
    example = "## Example: \r\n```py\r\n" + stream_example.read() + "\r\n```"

with open ("README.md", 'w+')  as stream_readme:
    stream_readme.write(f"""
# RumblePy
*Unofficial Python wrapper for automating a Rumble account (Rumble.com).*
* This is a work in progress, and is primitive at best.
* RumblePy is a self-botting framework and acts as a user-account, not to be confused with the functionality of Rumble.com's [Official Admin/Editor API](https://help.rumble.com/).
* In no way am I affiliated with Rumble.com.
* This is not intended for public use and I am not responsible for any damage caused by the use of this software.
* This is not a political project, I simply enjoy reverse engineering social media apps and Rumble has been a very easy platform to do so.

{example}
            """)

r = RumbleBot()

# iterate over function variables
with open ("README.md", 'a') as stream_append:
    
    stream_append.write("\r\n## Methods:\r\n")
    method_docs = []
    
    for func in dir(r):
    
        if "__" not in func and "method" in str(type(getattr(r, func))):
            f = getattr(r, func)
            print(f)
            
            doc = getattr(getattr(r, func), "__doc__")
            if type(getattr(r, func)) != dict and type(getattr(r, func)) != None and doc is not None:
                try:
                    source = inspect.getsource(getattr(r, func))
                except:
                    continue
                
                definition = "???"
                for line in source.splitlines():
                    if "def" in line:
                        definition = line.split("def ")[1].split(":")[0]
                        break
                        
                method_docs.append(f"""
#### *[`RumbleBot.{definition}`](#{func})*
> {doc}""")
                
    for func in dir(r.feeds):
        
            if "__" not in func and "method" in str(type(getattr(r.feeds, func))):
                f = getattr(r.feeds, func)
                print(f)
                
                doc = getattr(getattr(r.feeds, func), "__doc__")
                if type(getattr(r.feeds, func)) != dict and type(getattr(r.feeds, func)) != None and doc is not None:
                    try:
                        source = inspect.getsource(getattr(r.feeds, func))
                    except:
                        continue
                    
                    definition = "???"
                    for line in source.splitlines():
                        if "def" in line:
                            definition = line.split("def ")[1].split(":")[0]
                            break
                            
                    method_docs.append(f"""
#### *[`RumbleBot.feeds.{definition}`](#{func})*
> {doc}""")

    for func in dir(r.search):
        
        if "__" not in func and "method" in str(type(getattr(r.search, func))):
            f = getattr(r.search, func)
            print(f)
            
            doc = getattr(getattr(r.search, func), "__doc__")
            if type(getattr(r.search, func)) != dict and type(getattr(r.search, func)) != None and doc is not None:
                try:
                    source = inspect.getsource(getattr(r.search, func))
                except:
                    continue
                
                definition = "???"
                for line in source.splitlines():
                    if "def" in line:
                        definition = line.split("def ")[1].split(":")[0]
                        break
                        
                method_docs.append(f"""
#### *[`RumbleBot.search.{definition}`](#{func})*
> {doc}""")
                                
    # Ensure array item with substring "RumbleBot.login" is first item in array
    for item in method_docs:
        if "RumbleBot.login" in item:
            method_docs.insert(0, method_docs.pop(method_docs.index(item)))
                
    stream_append.write("\r".join(method_docs))
    
# overwrite "RumblePy/__init__.py" with updated version
with open ("RumblePy/__init__.py", 'r') as stream_init:
    init = stream_init.read()
    
version = init.split("__version__ = \"")[1].split("\"")[0]
version_string = f"__version__ = \"{version}\""
with open ("__version__", 'r') as stream_version:
    new_version = stream_version.read()
    new_version_string = f"__version__ = \"{new_version}\""
    init = init.replace(version_string, new_version_string)
    with open ("RumblePy/__init__.py", 'w+') as stream_init:stream_init.write(init)
    
with open ("todos.txt", 'r') as stream_todos:
    todos = stream_todos.read()
    
with open ("README.md", 'a') as stream_append:
    stream_append.write("\r\n## Project Goals:\r\n")
    for todo in todos.splitlines():
        if len(todo) > 0:
            stream_append.write(f"\r\n- [ ] {todo[0].upper() + todo[1:]}")
    


        

