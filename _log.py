#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging as lg

def get_logger():
    logger = lg.getLogger('myquant')
    hdl = lg.StreamHandler()
    hdl.setFormatter(lg.Formatter('%(asctime)s %(levelname)s [%(filename)s:%(lineno)s] %(message)s',\
                    '%Y-%m-%d %H:%M:%S'))
    logger.setLevel(lg.DEBUG)
    logger.addHandler(hdl)
    return logger

logger = get_logger()

