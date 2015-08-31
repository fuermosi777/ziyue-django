# -*- coding: utf-8 -*-

import pytz
from datetime import datetime
import encrypter


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

def wrap_posts(post_instance):
    return [{
        'id': encrypter.encode(p.id),
        'title': p.title,
        'datetime': humanize_timesince(p.datetime),
        'source': p.source,
        'vendor': {
            'name': p.vendor.name,
            'avatar': p.vendor.avatar.url,
            'url': p.vendor.url,
        },
    } for p in post_instance]