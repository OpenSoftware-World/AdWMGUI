#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
AdWMGUI Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
AdWMGUI All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/AdWMGUI
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/AdWMGUI """

import configparser

config = configparser.ConfigParser()
config.read("Settings/settings.ini")

userTheme = config['Theme']['userTheme']

userTheme_file = configparser.ConfigParser()
userTheme_file.read(f"Theme/{userTheme}_theme.ini")

window_bg = userTheme_file['ThemeContent']['window_bg']
button_bg = userTheme_file['ThemeContent']['button_bg']
button_fg = userTheme_file['ThemeContent']['button_fg']
button_active_bg = userTheme_file['ThemeContent']['button_active_bg']
button_active_fg = userTheme_file['ThemeContent']['button_active_fg']
label_bg = userTheme_file['ThemeContent']['label_bg']
label_fg = userTheme_file['ThemeContent']['label_fg']
entry_bg = userTheme_file['ThemeContent']['entry_bg']
entry_fg = userTheme_file['ThemeContent']['entry_fg']
entry_instert_bg = userTheme_file['ThemeContent']['entry_instert_bg']