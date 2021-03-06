data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_000/barcode_bag_000"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_000/pre_bag_wt_grams_000"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_000/barcode_bag_000", "group_000/pre_bag_wt_grams_000"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_001/barcode_bag_001"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_001/pre_bag_wt_grams_001"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_001/barcode_bag_001", "group_001/pre_bag_wt_grams_001"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_002/barcode_bag_002"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_002/pre_bag_wt_grams_002"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_002/barcode_bag_002", "group_002/pre_bag_wt_grams_002"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt", "notes"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_003/barcode_bag_003"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_003/pre_bag_wt_grams_003"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_003/barcode_bag_003", "group_003/pre_bag_wt_grams_003"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_004/barcode_bag_004"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_004/pre_bag_wt_grams_004"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_004/barcode_bag_004", "group_004/pre_bag_wt_grams_004"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_005/barcode_bag_005"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_005/pre_bag_wt_grams_005"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_005/barcode_bag_005", "group_005/pre_bag_wt_grams_005"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_006/barcode_bag_006"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_006/pre_bag_wt_grams_006"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_006/barcode_bag_006", "group_006/pre_bag_wt_grams_006"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_007/barcode_bag_007"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_007/pre_bag_wt_grams_007"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_007/barcode_bag_007", "group_007/pre_bag_wt_grams_007"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_008/barcode_bag_008"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_008/pre_bag_wt_grams_008"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_008/barcode_bag_008", "group_008/pre_bag_wt_grams_008"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_009/barcode_bag_009"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_009/pre_bag_wt_grams_009"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_009/barcode_bag_009", "group_009/pre_bag_wt_grams_009"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_010/barcode_bag_010"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_010/pre_bag_wt_grams_010"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_010/barcode_bag_010", "group_010/pre_bag_wt_grams_010"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_011/barcode_bag_011"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_011/pre_bag_wt_grams_011"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_011/barcode_bag_011", "group_011/pre_bag_wt_grams_011"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_012/barcode_bag_012"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_012/pre_bag_wt_grams_012"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_012/barcode_bag_012", "group_012/pre_bag_wt_grams_012"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_013/barcode_bag_013"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_013/pre_bag_wt_grams_013"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_013/barcode_bag_013", "group_013/pre_bag_wt_grams_013"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_014/barcode_bag_014"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_014/pre_bag_wt_grams_014"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_014/barcode_bag_014", "group_014/barcode_bag_014"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_015/barcode_bag_015"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_015/pre_bag_wt_grams_015"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_015/barcode_bag_015", "group_015/pre_bag_wt_grams_015"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_016/barcode_bag_016"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_016/pre_bag_wt_grams_016"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_016/barcode_bag_016", "group_016/pre_bag_wt_grams_016"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_017/barcode_bag_017"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_017/pre_bag_wt_grams_017"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_017/barcode_bag_017", "group_017/pre_bag_wt_grams_017"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_018/barcode_bag_018"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_018/pre_bag_wt_grams_018"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_018/barcode_bag_018", "group_018/pre_bag_wt_grams_018"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_019/barcode_bag_019"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_019/pre_bag_wt_grams_019"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_019/barcode_bag_019", "group_019/pre_bag_wt_grams_019"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_020/barcode_bag_020"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_020/pre_bag_wt_grams_020"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_020/barcode_bag_020", "group_020/pre_bag_wt_grams_020"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_021/barcode_bag_021"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_021/pre_bag_wt_grams_021"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_021/barcode_bag_021", "group_021/pre_bag_wt_grams_021"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_022/barcode_bag_022"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_022/pre_bag_wt_grams_022"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_022/barcode_bag_022", "group_022/pre_bag_wt_grams_022"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_023/barcode_bag_023"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_023/pre_bag_wt_grams_023"],
                "db_names": ["empty_bag_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"],
        "completeness_errs": ["group_023/barcode_bag_023", "group_023/pre_bag_wt_grams_023"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
]
