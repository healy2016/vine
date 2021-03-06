###apt-get install / download & setup
*   mongodb
*   python-dev
*   memcached

   > Windows x64: check **http://www.couchbase.com/communities/q-and-a/memcached-x64-version-couchbase**

*   [elasticsearch](https://github.com/elasticsearch/elasticsearch)
   *   you may need to install java first

     > Check: **https://github.com/geekben/deployment/blob/master/java_on_ubuntu.md**
     
*   libgeoip-dev
*   xvfb
*   xserver-xephyr
*   pyqt4 
    * for ubuntu: apt-get install python-qt4; then you need to add your global python lib path by: export PYTHONPATH="/usr/lib/python2.7/dist-packages/"
    * for mac: install in virtualenv [guide](http://stackoverflow.com/questions/20528731/install-pyqt-and-other-python-modules-for-multiple-versions-in-mac-os-x-maverick)

###django-nonrel
  > Check **http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html** to install.

* django-nonrel
* djangotoolbox
* django-mongodb-engine


###pip install
* django-registration
* django-crispy-forms
* django-admin-bootstrapped
* django-haystack
* jieba
* Whoosh
* Pillow
* python-social-auth
* python-memcached
* django_akismet_comments
* django-simple-captcha
* elasticsearch (for ubuntu: pyelasticsearch)
* django-avatar
   * if can't work, see https://github.com/jezdez/django-avatar/issues/53
   * Change PIL to Pillow,  Change x86_64 to i386 if you are installing it to a 32-bit machine
   * if enccounter this error: _imaging.c:76:20: fatal error: Python.h: No such file or directory
     * "sudo apt-get build-dep python-imaging"
     * then you can upgrade Pillow
* pytz
* pygeoip
* dnspython
* pydkim
* pyvirtualdisplay

-----
###Items should run.
*   Run a mail server to use account authentication.
   * sendmail, smtp.gmail, etc. 
   * `python -m smtpd -n -c DebuggingServer localhost:1025`
   * postfix for ubuntu

    > Check: **https://help.ubuntu.com/12.04/serverguide/postfix.html**

*   Memcached server
   * Linux: if your memcached server don't run automatically, try `./memcached -d -m 2048 -l 10.0.0.40 -p 11211`
   * Windows: download and run the binary.

*  elasticsearch server
   * `cd <elasticsearch home>`
   * `bin/elasticsearch &`

    > Check: **https://github.com/elasticsearch/elasticsearch**

###Options for better performance
* gunicorn
* supervisor
* nginx

###search engine
* django-haystack
* **[Elasticsearch](http://www.elasticsearch.org/overview/elkdownloads/)**
