# -*- coding: utf-8 -*-

import pytz
from datetime import datetime


def humanize_timesince(date):
    delta = datetime.now(pytz.utc) - date

    num_years = delta.days / 365
    if (num_years > 0):
        return u"%d 年前"%num_years

    num_weeks = delta.days / 7
    if (num_weeks > 0):
        return u"%d 周前"%num_weeks

    if (delta.days > 0):
        return u"%d 天前"%delta.days

    num_hours = delta.seconds / 3600
    if (num_hours > 0):
        return u"%d 小时前"%num_hours

    num_minutes = delta.seconds / 60
    if (num_minutes > 0):
        return u"%d 分钟前"%num_minutes

    return u"刚刚"