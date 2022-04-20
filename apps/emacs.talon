# activate this .talon file if the current app name is "Chrome"
# you can find app names by running ui.apps() in the REPL
app.name: Emacs
-
# key_wait increases the delay when pressing keys (milliseconds)
# this is useful if an app seems to jumble or drop keys
# settings():
#    key_wait = 4.0

# activate the global tag "browser"
# tag(): browser

# define some voice commands
win left: key(cmd-alt-left)
win up: key(cmd-alt-up)
win right: key(cmd-alt-right)
win down: key(cmd-alt-down)
win close:
    key(ctrl-x)
    key(0)

win split up:
       key(ctrl-x)
       key(2)
win split left:
       key(ctrl-x)
       key(3)

buffer back:
       key(ctrl-x)
       key(left)
buffer forward:
       key(ctrl-x)
       key(right)
buffer show|buffer open:
       key(ctrl-x)
       key(b)
buffer save:
       key(cmd-s)
buffer kill:
       key(ctrl-x)
       key(k)

slurp: key(ctrl-alt-.)
barf: key(ctrl-alt-,)

kill expression: key(ctrl-alt-k)

evil:
    key(ctrl-x)
    key(ctrl-e)
evil inline:
     key(ctrl-u)
     key(ctrl-x)
     key(ctrl-e)
#evil point:
#    key(ctrl-x)
#    key(ctrl-e)

delete word|kill word|kill word left: key(ctrl-backspace)
delete word right|kill word right: key(alt-d)
delete line|kill line: key(ctrl-k)

go word right|go right word: key(alt-f)
go word left|go left word: key(alt-b)
go paragraph left: key(ctrl-alt-b)
go paragraph right: key(ctrl-alt-f)

select: key(ctrl-space)
fix whitespace:
    key(alt-x)
    insert("fixup-whitespace")
comment: key(ctrl-;)