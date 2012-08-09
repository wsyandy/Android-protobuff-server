Android-protobuff-server
========================

Python package and mainfile to handle the messages sent using https://github.com/FedeCamposeco/Android-protobuff UDP protobuff transfer. It is a small Tkinter-based UI that lets the user remotely (over TCP) grab images from the phone and then receives the protobuff message, decodes it and converts the jpeg image to opencv mat (and displays it). The package and mainfile require Tkinter, PIL ImageTk, PIL Image, opencv-python (>2.4)  and numpy packages. The ports used for the TCP/UDP connection are currentlty hardcoded into the mainfile and the IP is obtained using a working internet connection.

Two main GUI applications are available: ServerIO and ServerI. ServerIO will require a TCP connection from the phone and will control the image grabbing via this link. ServerI will only display the UDP output from the phone (ServerIO will also display this).