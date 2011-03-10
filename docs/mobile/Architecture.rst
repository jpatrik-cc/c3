=====================
 Mobile Architecture
=====================

Bottom Layer
============

The current mobile implementation is based on HTML5, CSS3 and
Javascript. To compile this into a native mobile application and have
the native capabilities available in javascript we are using
phonegap::

    http://www.phonegap.com/

To build different skeleton projects for different platforms check::

    http://www.phonegap.com/start

And to start using the native mobile capabilities through the
Javascript API check::

    http://docs.phonegap.com/


Top Layer
=========

To implement the interface and the classic mobile interactions (touch
events, lists, buttons, zoom, scrolling, forms, etc) we are using
Sencha Touch::

    http://www.sencha.com/products/touch/

The API documentation can be found at::

    http://dev.sencha.com/deploy/touch/docs/

To get started with Sencha Touch I would recommend taking a look at::

    http://www.sencha.com/learn/index.php?title=Main_Page 

File Structure
==============

To use phonegap with different platforms we need a directory for each
one of them. Each platform has a specific way of being compiled, but
they should all share a folder containing the html/css/js assets that
contain the cococloud implementation. 

The file structure within the `assets` folder is as follows::

    assets/www/              -> The HTML files 
    assets/www/js/           -> The Javascript files
    assets/www/stylesheet/   -> The Css files
    assets/www/static/       -> Any images or other static files that are necessary

Within the `assets/www/js/` folder, the main file to be included is::

    app.js

It should initialize the app, call any necessary external modules and
handle the application's flow. In the future, it would be good to have
a more complex and modularized javascript architecture.

Platform Specific
=================

Each platform should contain its own documentation file regarding the
specific details on how to work with them. Bellow are just some
general pointers that might be relevant without digging into the
details.

Android
-------

A basic android project is set up under::

    mobile/Android/
