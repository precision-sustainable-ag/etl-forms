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
                "kobo_name": "start",
                "db_names": ["recovery_date"],
                "tests": ["not_null"],
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
        "extra_cols": [
            {"name": "time", "value": 0}
        ],
    },
]
