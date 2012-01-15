'''
Image-Viewer v0.1.0

[
    {"keys": ["super+i"],  "command": "image_viewer"}
]

view from CSS:
    background: url(../img/image.png);
                            |
                            ^ cursor
view from HTML:
    <img src="img/image.png" />
                |
                ^ cursor

Copyright (c) 2012 Razumenko Maksim <razumenko.maksim@gmail.com>

MIT License, see http://opensource.org/licenses/MIT
'''

import sublime, sublime_plugin, re, os, desktop


class ImageViewerCommand(sublime_plugin.TextCommand):

    def run(self, edit):\

        settings = sublime.load_settings(__name__ + '.sublime-settings')
        image_types = settings.get("image_types", "[]")

        def is_image(file_name):
            '''Return True if file_name is image'''
            file_type = re.match('.*(\..*)$', file_name or "")
            file_type = file_type.group(1) if file_type else ""

            return file_type in image_types


        view = self.view
        file_name = view.file_name()

        if is_image(file_name):
            self.view_image(file_name)

        else:
            cur_pos   = view.sel()[0].a
            scope_reg = view.extract_scope(cur_pos)

            file_string = view.substr(scope_reg)
            with_quotes = re.match('^[\"\']{1}(.*)[\"\']{1}$', file_string)
            file_string = with_quotes.group(1) if with_quotes else file_string

            if is_image(file_string):
                dir_name  = re.match('(.*)(\/.*)$', view.file_name())
                dir_name  = dir_name.group(1) + "/" if dir_name else ""
                full_name = dir_name + file_string
                self.view_image(dir_name, file_string)

            else:
                sublime.error_message("Image-Viewer\n\nERROR: Image type is not recognized:\n\n" + file_string)


    def view_image(self, dir_name, file_name = ""):
        '''View image with default OS viewer'''

        full_name = dir_name + file_name

        if (os.path.isfile(full_name)):
            desktop.open(full_name)

        else:
            full_name2 = dir_name + "../" + file_name
            if (os.path.isfile(full_name2)):
                desktop.open(full_name2)
            else:
                sublime.error_message("Image-Viewer\n\nERROR: File not found:\n\n" + full_name)
