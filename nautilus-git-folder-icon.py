#!/usr/bin/python2

"""
Show git icon on folders that contain git repos. Indicate whether they have
some uncommited modifications.
"""
import subprocess
import os.path

from gi.repository import Nautilus, GObject


def new_update_status(self, item, path, status):
    is_git_repo = os.path.exists(os.path.join(path, '.git'))
    if is_git_repo:
        return
    import rabbitvcs.ui
    if status.summary in rabbitvcs.ui.STATUS_EMBLEMS:
        item.add_emblem(rabbitvcs.ui.STATUS_EMBLEMS[status.summary])


try:
    from RabbitVCS import RabbitVCS
    RabbitVCS.update_status = new_update_status
except:
    pass


class GitFolderIconExtension(GObject.GObject, Nautilus.InfoProvider):
    def update_file_info(self, item):
        if not item.is_directory():
            return
        path = item.get_location().get_path()
        is_git_repo = os.path.exists(os.path.join(path, '.git'))
        if not is_git_repo:
            return
        dirty = subprocess.check_output(
            'git status --porcelain 2>/dev/null | egrep "^(M| M)" | wc -l',
            shell=True, cwd=path,
        )
        dirty = bool(int(dirty.strip()))
        if dirty:
            item.add_emblem('git-repo-dirty')
        else:
            item.add_emblem('git-repo')
