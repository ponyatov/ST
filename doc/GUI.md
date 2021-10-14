# #GUI (wxPython)
## There is a hard choice: native GUI or Web interface?
#ST

User interface selection is a big problem. Modern computer systems tend to cloud distribution, network services, and a web interface for users. In case we want to run locally, the choice is more problematic: the web is more flexible and gives mobile and remote access for free. Unfortunately, browsers become very fat, starts in dozens of second, eats a lot of memory, and require JS/HTML skills for development.

On the other side, we can focus on a more or less native GUI and fullscreen game-like applications. It will work run faster and lighter. Also, we can experiment with reimplementing the GUI of the scratch, change its design principles, try to build it with async message passing, or reactive.

If you want to share your work with some users, the native OS interface look and feel can be important for them. Thus, there are a set of mature portable libraries for Python which prove them usable for making complex multi-windowing interfaces. Maybe there will be the best choice: use native GUI for the ST system UI, and leave Web for external usage.
