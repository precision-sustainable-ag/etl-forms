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
                "kobo_name": "termination_date",
                "db_names": ["cc_termination_date"],
                "datatype": "date",
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "all_cols": ["cc_termination_date"]    
    },
]