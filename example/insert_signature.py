#-*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import datetime


class insertSignatureCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        date = datetime.datetime.now()
        dateStr = date.strftime("%Y-%m-%d %X")
        text_encode = """#-*- encoding: utf-8 -*-\n'''\n"""
        text_author = """\n\n@author: Srgzyq\n'''\n"""
        text = text_encode + 'Created on ' + dateStr + text_author

        for r in self.view.sel():
            str_r = self.view.substr(r)

            print 'str_r:', str_r

            if 'Created on' in str_r:
                if 'Updated on ' in str_r:
                    text = str_r[0:str_r.find(
                        'Updated on ')] + 'Updated on ' + dateStr + text_author
                else:
                    text = str_r.replace(
                        text_author, '\nUpdated on ' + dateStr + text_author)
            self.view.erase(edit, r)
            self.view.insert(edit, r.begin(), text)
