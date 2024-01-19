import datetime

# recorded on GMC500+, middle point start data and abrupt end,
# a few reference times, and some notes, 110 char long.
raw_history_with_notes1 = b"\x0c,5U\xaa\x05U\xaa\x00\x14\x07\x1a\x0c,6U\xaa\x00U\xaa\x00\x14\x07\x1a\x0c,6U\xaa\x01U\xaa\x00\x14\x07\x1a\x0c,7U\xaa\x02BX`][sYM[JSWXVBU\xaa\x00\x14\x07\x1a\r\x00\x1aU\xaa\x02U\xaa\x02\x05&5ABC?lpn\x80U\xaa\x00\x14\x07\x1a\r\x05&U\xaa\x02U\xaa\x02\x03ABCs\xa3t\x95\x95\x8fq\xa6"


raw_history_with_notes1_tidy = [
    (
        datetime.datetime(2020, 7, 26, 12, 45, 55),
        66,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 46, 55),
        88,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 47, 55),
        96,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 48, 55),
        93,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 49, 55),
        91,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 50, 55),
        115,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 51, 55),
        89,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 52, 55),
        77,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 53, 55),
        91,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 54, 55),
        74,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 55, 55),
        83,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 56, 55),
        87,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 57, 55),
        88,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 58, 55),
        86,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 12, 59, 55),
        66,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 12, 44, 55),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 1, 26),
        63,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 0, 26),
        "&5ABC",
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 2, 26),
        108,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 0, 26),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 3, 26),
        112,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 0, 26),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 4, 26),
        110,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 0, 26),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 5, 26),
        128,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 0, 26),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 6, 38),
        115,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        "ABC",
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 7, 38),
        163,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 8, 38),
        116,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 9, 38),
        149,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 10, 38),
        149,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 11, 38),
        143,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 12, 38),
        113,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
    (
        datetime.datetime(2020, 7, 26, 13, 13, 38),
        166,
        "CPM",
        "every minute",
        datetime.datetime(2020, 7, 26, 13, 5, 38),
        None,
    ),
]
