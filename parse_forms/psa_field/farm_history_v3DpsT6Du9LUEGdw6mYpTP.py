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
                "kobo_names": ["previous_crop"],
                "db_names": ["previous_cash_crop"],
                "multi_select": {
                    "corn": "Corn",
                    "soybean": "Soybeans",
                    "cotton": "Cotton",
                    "wheat": "Wheat",
                    "tobacco": "Tobacco",
                    "peanut": "Peanut",
                    "fallow": "Fallow",
                    "pasture": "Pasture",
                    "summer_cover_c": "Summer Cover Crop",
                    "hort": "Horticultural",
                    "other": "Other",
                },
            },
            {
                "kobo_names": ["previous_fert"],
                "db_names": ["total_n_previous_crop"],
            },
            {
                "kobo_names": ["cover_crop_plant_date"],
                "db_names": ["cc_planting_date"],
                "datatype": "date",
            },
            {
                "kobo_names": ["cover_crop_planting_method"],
                "db_names": ["cc_planting_method"],
                "multi_select": {
                    "drilled": "Drilled",
                    "broadcast": "Broadcast",
                    "aerial_seeded": "Aerial Seeding",
                    "other": "Other",
                },
            },
            {
                "kobo_names": ["litter_cover_crop"],
                "db_names": ["post_harvest_fertility"],
                "multi_select": {
                    "no": 0,
                    "yes": 1
                },
            },
            {
                "kobo_names": ["tillage_prior"],
                "db_names": ["cc_tillage"],
                "multi_select": {
                    "no": 0,
                    "yes": 1
                },
                "datatype": "int",
            },
            {
                "kobo_names": ["termination_method"],
                "db_names": ["cc_termination_method"],
                "multi_select": {
                    "herbicide": "Herbicide",
                    "mechanical": "Mechanical",
                    "combination_termination": "Herbicide + Mechanical",
                },
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
            "previous_cash_crop",
            "cc_planting_method",
            "cc_termination_method",
            "cc_planting_date",
            "total_n_previous_crop",
            "post_harvest_fertility",
            "cover_crop_tillage",
        ],
    }
]
