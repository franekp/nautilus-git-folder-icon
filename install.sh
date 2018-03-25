#!/bin/bash

cp ./nautilus-git-folder-icon.py /usr/share/nautilus-python/extensions/
cp ./emblem-*.svg /usr/share/icons/hicolor/scalable/emblems/
gtk-update-icon-cache /usr/share/icons/hicolor/
