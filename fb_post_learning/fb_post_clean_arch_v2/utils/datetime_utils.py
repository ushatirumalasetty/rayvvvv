def get_datetime_as_string(date):
    from fb_post_clean_arch_v2.constants.config import DATE_TIME_FORMAT
    date = date.strftime(DATE_TIME_FORMAT)
    return date
