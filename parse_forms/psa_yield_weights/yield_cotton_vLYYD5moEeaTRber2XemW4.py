data = [
    {
        "entry_to_iterate": "cotton_001",
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["cotton_001/barcode_cotton_001"],
                "db_names": ["code", "treatment", "subplot", "row"],
                "separator": "-",
                "indices": [1, 2, 3, 4],
                "tests": ["check_regex  Y-[A-Z0-9]{3}-[CB]-[12]-(R1|R2)$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["cotton_001/boll_wt_g_001"],
                "db_names": ["boll_wt"],
            },
            {
                "kobo_names": ["cotton_001/ginned_lint_wt_001"],
                "db_names": ["ginned_lint_wt"],
            },
            {
                "kobo_names": ["cotton_001/repeat_text_001_002"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "treatment", "subplot", "row", "boll_wt"],
        "completeness_errs": ["`group_ng29s00/barcode_corn` is malformed or missing cotton_001/boll_wt_g_001"],
        "all_cols": [
            "code",
            "boll_wt",
            "ginned_lint_wt",
        ],
    }
]
