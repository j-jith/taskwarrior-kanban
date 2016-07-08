# taskwarrior-kanban: Personal Kanban Board for Taskwarrior.

`tw-kanban.py` is a Python(3) script which provides a simple [personal
Kanban](http://lifehacker.com/productivity-101-how-to-use-personal-kanban-to-visuali-1687948640)
board for the task management tool [Taskwarrior](taskwarrior.org). It sorts your tasks into the
following three categories - **Not started**, **In progress**, and **Done**, and generates an
HTML+CSS file (I like to set this file as my browser homepage so that I'm always aware of my
progress).

**Not started** category contains tasks which are pending and have not been started yet. **In
progress** category contains tasks which are pending but have been started. And finally, **Done**
category contains the last 10 tasks which have been completed.

*This does not give you an interactive Kanban board. All changes have to be made through taskwarrior
and `tw-kanban.py` has to be run again to regenerate the board.*

## Prerequisites

- [Taskwarrior](http://taskwarrior.org/download/) (Tested on version 2.5.0)

- Python 3.0+

- Requires the **jinja2** package: `pip3 install jinja2`.

Feel free to request more features.
