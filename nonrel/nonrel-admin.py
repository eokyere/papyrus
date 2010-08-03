"""
Native Django on App Engine

Updated: We've updated the installation instructions. 

You now also need djangotoolbox. 
Additionally, a simplified version of this post has been added to the 
documentation section of djangoappengine.

About a few months ago we started to port Django to support non-relational 
databases and to implement an App Engine database backend for this port. So 
far we ended up supporting basic Django functionality on App Engine. This 
post is intended to get you started using our port and to let you know what 
you can do and want you can't do with it at the moment. So let's start!

Installation

In order to use our port on App Engine you have to clone a few repositories first. 

These are the django-nonrel repository, djangoappengine and the django-testapp. 
So what are all these repos for? First in order to let you start a new Django 
project as fast as possible we created the django-testapp repo. 

It basically consists of a modified manage.py file to support the App Engine 
development 
server, and all corresponding settings in order to specify App Engine as the 
backend for Django. So the first step is to clone the django-testapp repo.

The djangoappengine repo contains all App Engine related backends for the 
non-relational Django port e.g. the email backend and the query backend for 
Django. So as the next step clone the djangoappengine and djangotoolbox packages
 and link them into the "common-apps" folder of the django-testapp checkout. 
 
 The django-nonrel repo is our modified Django port. It contains changes in 
 Django itself to support non-relational databases. Clone it and link the 
 repository's "django" folder into the "common-apps" folder. Your folder 
 structure should now look similar to this:

    * .../django-nonrel/django
    * .../djangoappengine
    * .../djangotoolbox
    * .../django-testapp
    * .../django-testapp/common-apps/djangoappengine -> ../../djangoappengine
    * .../django-testapp/common-apps/djangotoolbox -> ../../djangotoolbox
    * .../django-testapp/common-apps/django -> ../../django-nonrel/django

Now you should be able to create a new app in the testapp folder and use native Django models on App Engine. Try it!

"""

NONREL_HOME = '/Users/eokyere/Labs/django/nonrel'

if __name__ == "__main__":
    print 'hello, world!'
 
