data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["start"],
                "db_names": ["recovery_date"],
                "tests": ["not_null"],
                "datatype": "date",
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
        "extra_cols": [
            {"name": "time", "value": 0}
        ],
    },
]
