from front import Front
"""This module is the entry point of this application. It basically create a ``Front`` object, and display the IU finally.  
"""


def __init__():
    """This function is the first step to launch the application in the intended way. Just run this file by running the 
    
    ```bash
    python app.py 
    ```
    command fo instance.
    """
    print("hello world")
    app = Front()
    app.render()

    app.show_viewport()
    app.start_dearpygui()
    app.destroy_context()


__init__()