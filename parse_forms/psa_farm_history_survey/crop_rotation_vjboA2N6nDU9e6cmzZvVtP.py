data = [
    {
        "entry_to_iterate": "group_code_field_history",
        "cols_from_form": [
            {
                "kobo_names": ["group_code_field_history/code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_code_field_history/code_crop_rotation"],
                "value_separator": " ",
                "separate_into_multiple_rows": True,
                "db_names": ["crop"],
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
        "all_cols": [
            "code",
            "cc_specie",
        ],
    }
]
