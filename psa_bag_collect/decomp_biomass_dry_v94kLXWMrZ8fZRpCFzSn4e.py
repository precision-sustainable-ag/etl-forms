data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "barcode_bag_000",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0,1,2,3],
                "tests": ["check_reqex ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "decomp_bag_collect_date",
                "db_names": ["recovery_date"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "recovery_date"],   
        # {'code': 'SRT', 'subplot': '2', 'subsample': 'A', 'time': '0', 'empty_bag_wt': '146.92', 'notes': None, 'submitted_by': 'al_psa'} 
        "all_cols": ["code", "subplot", "subsample", "time", "recovery_date"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "barcode_bag_001",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0,1,2,3],
                "tests": ["check_reqex ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "decomp_bag_collect_date",
                "db_names": ["recovery_date"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "recovery_date"],    
        "all_cols": ["code", "subplot", "subsample", "time", "recovery_date"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "barcode_bag_002",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0,1,2,3],
                "tests": ["check_reqex ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "decomp_bag_collect_date",
                "db_names": ["recovery_date"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "recovery_date"],    
        "all_cols": ["code", "subplot", "subsample", "time", "recovery_date"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "barcode_bag_003",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0,1,2,3],
                "tests": ["check_reqex ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "decomp_bag_collect_date",
                "db_names": ["recovery_date"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "recovery_date"],    
        "all_cols": ["code", "subplot", "subsample", "time", "recovery_date"]
    },
]