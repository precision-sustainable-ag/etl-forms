data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["Scan_a_barcode"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["Enter_a_date_and_time"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`Scan_a_barcode` is malformed"],
        # {'code': 'SRT', 'subplot': '2', 'subsample': 'A', 'time': '0', 'empty_bag_wt': '146.92', 'notes': None, 'submitted_by': 'al_psa'}
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["Scan_a_barcode_001"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["Enter_a_date_and_time"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`Scan_a_barcode_001` is malformed"],
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["Scan_a_barcode_002"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["Enter_a_date_and_time"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`Scan_a_barcode_002` is malformed"],
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["Scan_a_barcode_003"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["Enter_a_date_and_time"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`Scan_a_barcode_003` is malformed"],
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
]
