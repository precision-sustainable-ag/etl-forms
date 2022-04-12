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
                "kobo_names": ["group_code_field_history/cover_crop_rate_total"],
                "db_names": ["total_rate"],
            },
            {
                "kobo_names": ["group_code_field_history/cover_crop_spp"],
                "value_separator": " ",
                "separate_into_multiple_rows": True,
                "db_names": ["cc_specie"],
                "multi_select": {
                    "alfalfa": "Alfalfa",
                    "barley": "Barley",
                    "berseem_clover": "Berseem Clover",
                    "canola__rape": "Rape/Canola",
                    "cereal_rye": "Cereal Rye",
                    "common_vetch": "Common Vetch",
                    "crimson_clover": "Crimson Clover",
                    "hairy_vetch": "Hairy Vetch",
                    "oats__black_oats": "Oats/Black Oats",
                    "other": "Other",
                    "other_brassica": "Other Brassica spp",
                    "other_clover_s": "Other Clover spp",
                    "other_grass_sp": "Other Grass spp",
                    "other_vetch_sp": "Other Vetch spp",
                    "radish": "Radish/Turnip",
                    "red_clover": "Red Clover",
                    "ryegrass": "Ryegrass",
                    "triticale": "Triticale",
                    "wheat": "Wheat",
                    "winter_pea": "Winter Peas",
                    "woolypod_vetch": "Woolypod Vetch",
                },
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
