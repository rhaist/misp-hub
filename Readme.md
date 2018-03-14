# MISP Hub [![Build Status](https://travis-ci.org/rhaist/misp-hub.svg?branch=master)](https://travis-ci.org/rhaist/misp-hub)

**Work In Progress - This is nowhere near production grade. Do not use for anything important yet.**

MISP hub is a currently under development syncing server compatible with the
MISP event exchange format and sync protocols. The idea is to create a hub for
syncing with different MISP instances and sharing groups based on python3 and
the Django framework to be easily extensible in the future with Django apps.


## Development Roadmap

- [ ] implement the current MISP 2.x data model [1] complete using Django apps
- [ ] implement the MISP permission model
- [ ] implement a clean json API fo the data model
- [ ] implement the MISP syncing protocols to be compatible with MISP 2.x servers
- [ ] implement a proper test suite with a as complete as possible code coverage

[1] https://raw.githubusercontent.com/MISP/misp-rfc/master/misp-core-format/raw.md.txt

## Development Ideas up for discussion

* Usage of Django Q for background tasks to be somewhat independent of task
brokers (https://django-q.readthedocs.io)
* Usage of the well tested django-restframework to build the API(s) with the
underlying Django permission model (http://www.django-rest-framework.org/)
* Usage of django-guardian (integrated with django-restframework) to port the
permission model (https://django-guardian.readthedocs.io/en/stable/)

## License

This software is licensed under [BSD-3 clause](https://opensource.org/licenses/BSD-3-Clause)

Copyright (C) 2017, Robert Haist

For more information, [the list of authors and contributors](AUTHORS) is available.
