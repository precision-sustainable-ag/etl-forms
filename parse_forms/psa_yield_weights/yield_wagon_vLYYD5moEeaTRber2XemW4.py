data = [
    {
        "entry_to_iterate": "weigh_wagon_group",
        "ignore_empty_forms": True,
        "top_level_cols": [
            {
                "key": "group_000/code",
                "db_name": "code"
            }
        ],
        "cols_from_form": [
            {
                "kobo_names": ["weigh_wagon_group/trt_select"],
                "db_names": ["treatment"],
                "multi_select": {
                    "cover": "C",
                    "bare": "B",
                },
            },
            {
                "kobo_names": ["weigh_wagon_group/rep_select"],
                "db_names": ["subplot"],
                "multi_select": {
                    "rep1": 1,
                    "rep2": 2,
                },
            },
            {
                "kobo_names": ["weigh_wagon_group/wagon_area_ft2"],
                "db_names": ["wagon_area_ft2"],
            },
            {
                "kobo_names": ["weigh_wagon_group/bushel_acre"],
                "db_names": ["bushels_acre"],
            },
            {
                "kobo_names": ["weigh_wagon_group/wagon_weight"],
                "db_names": ["wagon_weight_lbs"],
            },
            {
                "kobo_names": ["weigh_wagon_group/wagon_moisture"],
                "db_names": ["moisture_pct"],
            },
            {
                "kobo_names": ["weigh_wagon_group/repeat_text"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "treatment", "subplot"],
        "completeness_errs": ["Missing group_000/code, weigh_wagon_group/trt_select, or weigh_wagon_group/rep_select"],
        "all_cols": [
            "treatment",
            "subplot",
            "wagon_area_ft2",
            "wagon_weight_lbs",
            "bushels_acre",
            "moisture_pct",
        ],
    }
]
