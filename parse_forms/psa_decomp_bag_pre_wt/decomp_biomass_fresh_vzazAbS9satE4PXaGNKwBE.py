data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_000/Scan_Decomp_Bag_Barcode_001_000"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_000/PreWeight_grams_001_000"],
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
        "completeness_errs": ["group_dg1mv45_000/Scan_Decomp_Bag_Barcode_001_000", "group_dg1mv45_000/PreWeight_grams_001_000"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_001/Scan_Decomp_Bag_Barcode_001_001"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_001/PreWeight_grams_001_001"],
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
        "completeness_errs": ["group_dg1mv45_001/Scan_Decomp_Bag_Barcode_001_001", "group_dg1mv45_001/PreWeight_grams_001_001"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_002/Scan_Decomp_Bag_Barcode_001_002"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_002/PreWeight_grams_001_002"],
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
        "completeness_errs": ["group_dg1mv45_002/Scan_Decomp_Bag_Barcode_001_002", "group_dg1mv45_002/PreWeight_grams_001_002"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt", "notes"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_003/Scan_Decomp_Bag_Barcode_001_003"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_003/PreWeight_grams_001_003"],
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
        "completeness_errs": ["group_dg1mv45_003/Scan_Decomp_Bag_Barcode_001_003", "group_dg1mv45_003/PreWeight_grams_001_003"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_004/Scan_Decomp_Bag_Barcode_001_004"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_004/PreWeight_grams_001_004"],
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
        "completeness_errs": ["group_dg1mv45_004/Scan_Decomp_Bag_Barcode_001_004", "group_dg1mv45_004/PreWeight_grams_001_004"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_005/Scan_Decomp_Bag_Barcode_001_005"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_005/PreWeight_grams_001_005"],
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
        "completeness_errs": ["group_dg1mv45_005/Scan_Decomp_Bag_Barcode_001_005", "group_dg1mv45_005/PreWeight_grams_001_005"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_006/Scan_Decomp_Bag_Barcode_001_006"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_006/PreWeight_grams_001_006"],
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
        "completeness_errs": ["group_dg1mv45_006/Scan_Decomp_Bag_Barcode_001_006", "group_dg1mv45_006/PreWeight_grams_001_006"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_007/Scan_Decomp_Bag_Barcode_001_007"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_007/PreWeight_grams_001_007"],
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
        "completeness_errs": ["group_dg1mv45_007/Scan_Decomp_Bag_Barcode_001_007", "group_dg1mv45_007/PreWeight_grams_001_007"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_008/Scan_Decomp_Bag_Barcode_001_008"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_008/PreWeight_grams_001_008"],
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
        "completeness_errs": ["group_dg1mv45_008/Scan_Decomp_Bag_Barcode_001_008", "group_dg1mv45_008/PreWeight_grams_001_008"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_009/Scan_Decomp_Bag_Barcode_001_009"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_009/PreWeight_grams_001_009"],
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
        "completeness_errs": ["group_dg1mv45_009/Scan_Decomp_Bag_Barcode_001_009", "group_dg1mv45_009/PreWeight_grams_001_009"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_010/Scan_Decomp_Bag_Barcode_001_010"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_010/PreWeight_grams_001_010"],
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
        "completeness_errs": ["group_dg1mv45_010/Scan_Decomp_Bag_Barcode_001_010", "group_dg1mv45_010/PreWeight_grams_001_010"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_011/Scan_Decomp_Bag_Barcode_001_011"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_011/PreWeight_grams_001_011"],
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
        "completeness_errs": ["group_dg1mv45_011/Scan_Decomp_Bag_Barcode_001_011", "group_dg1mv45_011/PreWeight_grams_001_011"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_012/Scan_Decomp_Bag_Barcode_001_012"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_012/PreWeight_grams_001_012"],
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
        "completeness_errs": ["group_dg1mv45_012/Scan_Decomp_Bag_Barcode_001_012", "group_dg1mv45_012/PreWeight_grams_001_012"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_013/Scan_Decomp_Bag_Barcode_001_013"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_013/PreWeight_grams_001_013"],
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
        "completeness_errs": ["group_dg1mv45_013/Scan_Decomp_Bag_Barcode_001_013", "group_dg1mv45_013/PreWeight_grams_001_013"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_014/Scan_Decomp_Bag_Barcode_001_014"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_014/PreWeight_grams_001_014"],
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
        "completeness_errs": ["group_dg1mv45_014/Scan_Decomp_Bag_Barcode_001_014", "group_dg1mv45_014/PreWeight_grams_001_014"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_015/Scan_Decomp_Bag_Barcode_001_015"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_015/PreWeight_grams_001_015"],
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
        "completeness_errs": ["group_dg1mv45_015/Scan_Decomp_Bag_Barcode_001_015", "group_dg1mv45_015/PreWeight_grams_001_015"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_016/Scan_Decomp_Bag_Barcode_001_016"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_016/PreWeight_grams_001_016"],
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
        "completeness_errs": ["group_dg1mv45_016/Scan_Decomp_Bag_Barcode_001_016", "group_dg1mv45_016/PreWeight_grams_001_016"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_017/Scan_Decomp_Bag_Barcode_001_017"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_017/PreWeight_grams_001_017"],
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
        "completeness_errs": ["group_dg1mv45_017/Scan_Decomp_Bag_Barcode_001_017", "group_dg1mv45_017/PreWeight_grams_001_017"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_018/Scan_Decomp_Bag_Barcode_001_018"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_018/PreWeight_grams_001_018"],
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
        "completeness_errs": ["group_dg1mv45_018/Scan_Decomp_Bag_Barcode_001_018", "group_dg1mv45_018/PreWeight_grams_001_018"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_019/Scan_Decomp_Bag_Barcode_001_019"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_019/PreWeight_grams_001_019"],
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
        "completeness_errs": ["group_dg1mv45_019/Scan_Decomp_Bag_Barcode_001_019", "group_dg1mv45_019/PreWeight_grams_001_019"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_020/Scan_Decomp_Bag_Barcode_001_020"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_020/PreWeight_grams_001_020"],
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
        "completeness_errs": ["group_dg1mv45_020/Scan_Decomp_Bag_Barcode_001_020", "group_dg1mv45_020/PreWeight_grams_001_020"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_021/Scan_Decomp_Bag_Barcode_001_021"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_021/PreWeight_grams_001_021"],
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
        "completeness_errs": ["group_dg1mv45_021/Scan_Decomp_Bag_Barcode_001_021", "group_dg1mv45_021/PreWeight_grams_001_021"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_022/Scan_Decomp_Bag_Barcode_001_022"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_022/PreWeight_grams_001_022"],
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
        "completeness_errs": ["group_dg1mv45_022/Scan_Decomp_Bag_Barcode_001_022", "group_dg1mv45_022/PreWeight_grams_001_022"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_dg1mv45_023/Scan_Decomp_Bag_Barcode_001_023"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_dg1mv45_023/PreWeight_grams_001_023"],
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
        "completeness_errs": ["group_dg1mv45_023/Scan_Decomp_Bag_Barcode_001_023", "group_dg1mv45_023/PreWeight_grams_001_023"],
        "completeness_err_message": "Barcode is malformed or missing empty bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "empty_bag_wt"]
    },
]
