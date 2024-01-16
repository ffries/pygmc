import datetime


# GET CMDS
#########################################################################################
gets_cmd_response_map = {
    b"<GETVER>>": b"GMC-500+Re 2.22",
    b"<GETSERIAL>>": b"00!W!W\xf6",
    b"<GETCPM>>": b"\x00\x00\x04\xba",
    b"<GETCPS>>": b"\x00\x00\x00\x13",
    b"<GETMAXCPS>>": b'\x00\x00\x00"',
    b"<GETCPMH>>": b"\x00\x00\x00\x05",
    b"<GETCPML>>": b"\x00\x00\x05\xdc",
    b"<GETGYRO>>": b"\xff\xf9\xff\x0e\x00%\xaa",
    b"<GETVOLT>>": b"4.0v\x00",
    b"<GETDATETIME>>": b"\x17\x0b\n\x12!\x04\xaa",
    b"<GETCFG>>": b"\x00\x00\x00\x00\x1f\x00\x00d\x00d?&ffu0CC\x00\x00\x00\x19@\x9b33\x00?\x00\x00\x00\x00\x02\x03\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x01\x00x\n\x05\xe1<\x00\n\xff\x00\x00\x00\n\x00\x01\n\x00d\x00?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00wangshaofei\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00log2.asp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00www.gmcmap.com\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00log2.asp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x03\x00@<\x02\x00\x00\x01\x00x\x00\xc8\x002\x00d\x05\x01\x01\xa2\xa1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x0b\n\x12!\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff",
}


gets_device_result_map = {
    "get_version": "GMC-500+Re 2.22",
    "get_serial": "303021572157f6",
    "get_cpm": 1210,
    "get_cps": 19,
    "get_max_cps": 34,
    "get_cpmh": 5,
    "get_cpml": 1500,
    "get_gyro": (-7, -242, 37),
    "get_voltage": 4.0,
    "get_datetime": datetime.datetime(2023, 11, 10, 18, 33, 4),
    "get_usv_h": 7.865,
    "get_config": {
        "Power": 0,
        "Alarm": 0,
        "Speaker": 0,
        "CalibrationCPM_0": 100,
        "CalibrationCPM_1": 30000,
        "CalibrationCPM_2": 25,
        "SaveDataType": 2,
        "MaxCPM": 1505,
        "Baudrate": 0,
        "BatteryType": 0,
        "ThresholdMode": 0,
        "ThresholdCPM": 100,
        "Calibration_uSv_0": 0.6499999761581421,
        "Calibration_uSv_1": 195.0,
        "Calibration_uSv_2": 4.849999904632568,
        "IdleTextState": 0,
        "AlarmValue_uSv": 0.5,
        "Threshold_uSv": 0.5,
    },
}


# SET & ACTION CMDS
#########################################################################################
actions_cmd_response_map = {
    # datetime.datetime(2024, 1, 8, 17, 54, 57, 662848)
    b"<SETDATETIME\x18\x01\x08\x1169>>": b"\xaa",
    b"<KEY0>>": b"",
    b"<REBOOT>>": b"",
    b"<POWEROFF>>": b"",
    b"<POWERON>>": b"",
    b"<HEARTBEAT1>>": b"\x00\x00\x00\x13",  # 19
    b"<HEARTBEAT0>>": b"",
}


# voluptuous schema would be nice here... but do we want the overhead/dependency?
actions_device_test_cases = [
    {
        "test_name": "set datetime",
        "method": "set_datetime",
        "args": (),
        "kwargs": {"datetime_": datetime.datetime(2024, 1, 8, 17, 54, 57, 662848)},
        "return": None,
        "expected_write": b"<SETDATETIME\x18\x01\x08\x1169>>",
        "expected_read": b"\xaa",
        "raises": None,
    },
    {
        "test_name": "send key",
        "method": "send_key",
        "args": (),
        "kwargs": {"key_number": 0},
        "return": None,
        "expected_write": b"<KEY0>>",
        "expected_read": b"",
        "raises": None,
    },
    {
        "test_name": "send bad key",
        "method": "send_key",
        "args": (),
        "kwargs": {"key_number": 4},
        "return": None,
        "expected_write": b"",
        "expected_read": b"",
        "raises": ValueError,
    },
    {
        "test_name": "reboot",
        "method": "reboot",
        "args": (),
        "kwargs": {},
        "return": None,
        "expected_write": b"<REBOOT>>",
        "expected_read": b"",
        "raises": None,
    },
    {
        "test_name": "power on",
        "method": "power_on",
        "args": (),
        "kwargs": {},
        "return": None,
        "expected_write": b"<POWERON>>",
        "expected_read": b"",
        "raises": None,
    },
    {
        "test_name": "power off",
        "method": "power_off",
        "args": (),
        "kwargs": {},
        "return": None,
        "expected_write": b"<POWEROFF>>",
        "expected_read": b"",
        "raises": None,
    },
    {
        "test_name": "heartbeat on",
        "method": "_heartbeat_on",
        "args": (),
        "kwargs": {},
        "return": None,
        "expected_write": b"<HEARTBEAT1>>",
        "expected_read": b"",
        "raises": None,
    },
    {
        "test_name": "heartbeat off",
        "method": "_heartbeat_off",
        "args": (),
        "kwargs": {},
        "return": None,
        "expected_write": b"<HEARTBEAT0>>",
        "expected_read": b"",
        "raises": None,
    },
    # TODO: investigate WTF!
    {
        "test_name": "heartbeat live WTFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
        "method": "heartbeat_live",
        "args": (),
        "kwargs": {"count": 1},
        "return": 19,
        "expected_write": b"<HEARTBEAT0>>",  # WTF! Why is this passing!
        "expected_read": b"",
        "raises": None,
    },
    {
        "test_name": "heartbeat live",
        "method": "heartbeat_live",
        "args": (),
        "kwargs": {"count": 1},
        "return": 19,
        "expected_write": b"<HEARTBEAT1>>",
        "expected_read": b"",
        "raises": None,
    },
    # Same as heartbeat_live, just prints instead
    # TODO: add print check
    {
        "test_name": "heartbeat live print",
        "method": "heartbeat_live_print",
        "args": (),
        "kwargs": {"count": 1},
        "return": None,
        "expected_write": b"<HEARTBEAT1>>",
        "expected_read": b"",
        "raises": None,
    },
]
