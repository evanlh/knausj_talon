from talon import Context, Module, actions, imgui, settings, ui
from talon.mac import applescript

import os

ctx = Context()
ctx.matches = r"""
app: finder
"""

@ctx.action_class('user')
class UserActions:
    def file_manager_open_parent():
        actions.key('cmd-up')
    def file_manager_go_forward():
        actions.key('cmd-]')
    def file_manager_go_back():
        actions.key('cmd-[')
    def file_manager_current_path():
        if ui.active_window().title == "":
            return None # likely a modal window
        return applescript.run(r"""
            tell application id "com.apple.Finder"
                if not (exists (front window's target)) then return
                if front window's target's class is not in {disk, folder} then return
                return (front window's target as alias)'s POSIX path
            end tell
        """)

    def file_manager_terminal_here():
        if ui.active_window().title == "":
            return # likely a modal window
        applescript.run(r"""
            try
                tell application id "com.apple.Finder" to set theTarget to (front window's target as alias)
            on error -- fails with some windows, e.g. Preferences window
                return
            end try
            tell application id "com.apple.Terminal"
                activate
                open theTarget
            end tell
        """)

    def file_manager_show_properties():
        """Shows the properties for the file"""
        actions.key("cmd-i")

    def file_manager_open_directory(path: str):
        """opens the directory that's already visible in the view"""
        actions.key("cmd-shift-g")
        actions.sleep("50ms")
        actions.insert(path)
        actions.key("enter")

    def file_manager_select_directory(path: str):
        """selects the directory"""
        actions.insert(path)

    def file_manager_new_folder(name: str):
        """Creates a new folder in a gui filemanager or inserts the command to do so for terminals"""
        actions.key("cmd-shift-n")
        actions.sleep("500ms")
        actions.insert(name)

    def file_manager_open_file(path: str):
        """opens the file"""
        actions.key("esc")
        actions.insert(path)
        actions.key("cmd-o")

    def file_manager_select_file(path: str):
        """selects the file"""
        actions.key("esc")
        actions.insert(path)
