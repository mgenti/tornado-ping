tornado-ping is a fast Tornado implementation of ICMP (ping) protocol.

Forked from https://github.com/stellarbit/aioping to use the Tornado event loop and work with Python 2.7

## Installation

tornado-ping requires Python 2.7.

Use pip to install it from the PyPI::

    $ pip install tornado-ping

Or use the latest version from the master (if you are brave enough)::

    $ pip install git+https://github.com/mgenti/tornado-ping

## Using tornado-ping

There are 2 ways to use the library.

First one is interactive, which sends results to standard Python logger.
Please make sure you are running this code under root, as only
root is allowed to send ICMP packets:

    import tornado_ping
    import logging
    import tornado

    logging.basicConfig(level=logging.INFO)     # or logging.DEBUG
    tornado.ioloop.IOLoop.instance().run_sync(lambda: verbose_ping('8.8.8.8'))

Alternatively, you can call a ping function, which returns a
ping delay in milliseconds or returns None in case of an error:

    import tornado_ping
    import tornado

    @gen.coroutine
    def do_ping(host):
        delay = yield ping(host)
        if delay:
            print "Ping response in %s ms" % (delay * 1000, )
        else:
            print "Timed out"


    tornado.ioloop.IOLoop.instance().run_sync(lambda: do_ping('8.8.8.8'))

## Methods

``ping(dest_addr, timeout=10, family=None)``

- ``dest_addr`` - destination address, IPv4, IPv6 or hostname
- ``timeout`` - timeout in seconds (default: ``10``)
- ``family`` - family of resolved address - ``socket.AddressFamily.AF_INET`` for IPv4, ``socket.AddressFamily.AF_INET6``
  for IPv6 or ``None`` if it doesn't matter (default: ``None``)

``verbose_ping(dest_addr, timeout=2, count=3, family=None)``

- ``dest_addr`` - destination address, IPv4, IPv6 or hostname
- ``timeout`` - timeout in seconds (default: ``2``)
- ``count`` - count of packets to send (default: ``3``)
- ``family`` - family of resolved address - ``socket.AddressFamily.AF_INET`` for IPv4, ``socket.AddressFamily.AF_INET6``
  for IPv6 or ``None`` if it doesn't matter (default: ``None``)

## Credits

- Original Version from Matthew Dixon Cowles:
  ftp://ftp.visi.com/users/mdc/ping.py

- Rewrite by Jens Diemer:
  http://www.python-forum.de/post-69122.html#69122

- Rewrite by Samuel Stauffer:
  https://github.com/samuel/python-ping

- Rewrite by Anton Belousov / Stellarbit LLC <anton@stellarbit.com>
  http://github.com/stellarbit/aioping
  
- Generous contributions from GitHub users:

  - https://github.com/JackSlateur
  - https://github.com/harriv
  - https://github.com/asantoni
  - https://github.com/eddebc
  - https://github.com/wise0wl
  - https://github.com/nARN
  - https://github.com/hergla
  - https://github.com/hanieljgoertz
  - https://github.com/Crypto-Spartan

- Tornado version by Mark Guagenti


## License

tornado-ping is licensed under GPLv2.
