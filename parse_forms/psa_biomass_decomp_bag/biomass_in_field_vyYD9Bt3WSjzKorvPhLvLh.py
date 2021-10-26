data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "fresh_wt_a1",
                "db_names": ["fresh_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "fresh_wt_b1",
                "db_names": ["fresh_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "bag_a1",
                "db_names": ["bag_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "bag_b1",
                "db_names": ["bag_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "sub1_legume",
                "db_names": ["legumes_40"],
                "tests": ["not_null"],
                "multi_select": {
                    "less_than_40_legume": 0,
                    "more_than_40_legume": 1
                },
            },
            {
                "kobo_name": "WONT BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 1}
        ],
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "fresh_wt_a2",
                "db_names": ["fresh_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "fresh_wt_b2",
                "db_names": ["fresh_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "bag_a2",
                "db_names": ["bag_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "bag_b2",
                "db_names": ["bag_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "sub2_legume",
                "db_names": ["legumes_40"],
                "tests": ["not_null"],
                "multi_select": {
                    "less_than_40_legume": 0,
                    "more_than_40_legume": 1
                },
            },
            {
                "kobo_name": "WONT BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 2}
        ],
    },
]