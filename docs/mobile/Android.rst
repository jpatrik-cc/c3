For now, just get the files in eclipse to point to the git repo






Someday will be able to do it without eclipse.. if you find out
how.. fill the docs below.

=============================
 Installing a virtual device
=============================

<How to install the virtual device>

==============================
 Running the android emulator
==============================

To run the android emulator just run::

       emulator -avd Android2.3 -scale 0.7

where -avd is the name of the virtual device and -scale is the factor
by which the graphics should be scaled

==========================================
 Installing the application on the device
==========================================

To install the application in the device you will need to have adb
available. It can be found on::

    <android-sdk>/platform-tools/

so add that to your path.

Once adb is installed you can add the application to the device by
doing::

     ... Dunno.. fuck it.. just use eclipse   
