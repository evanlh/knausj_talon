from talon import Context, actions, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
app.bundle: com.sublimetext.4
"""

@ctx.action_class("edit")
class edit_actions:
	def jump_line(n: int):
		actions.key("ctrl-g")
		actions.insert(str(n))
		actions.key("enter")

@ctx.action_class("user")
class user_actions:
	def find(text: str):
		actions.key("cmd-f")
		actions.insert(text)

	def find_everywhere(text: str):
		actions.key("cmd-shift-f")
		actions.insert(text)

	def replace(text: str): 
		actions.key("cmd-alt-f")
		actions.insert(text)

	replace_everywhere = find_everywhere

	def select_previous_occurrence(text: str):
		actions.key("cmd-i")
		actions.insert(text)
		actions.key("shift-enter")

	def select_next_occurrence(text: str):
		actions.key("cmd-i")
		actions.insert(text)
		actions.key("enter")

@ctx.action_class("win")
class win_actions:
	def filename():
		title = actions.win.title()
		result = title.split(" — ")[0]
		return result if "." in result else ""

	def file_ext():
		return actions.win.filename().split(".")[-1]
