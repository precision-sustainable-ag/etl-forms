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
                "kobo_names": ["cc_termination_herbicide"],
                "value_separator": " ",
                "separate_into_multiple_rows": True,
                "db_names": ["chemical"],
                "multi_select": {
                    "2_4_d": "2 4-D",
                    "atrazine": "Atrazine",
                    "clopyralid": "Clopyralid",
                    "dicamba": "Dicamba",
                    "glufosinate_ammonium_liberty": "Glufosinate-ammonium/Liberty",
                    "glyphosate_roundup": "Glyphosate/Roundup",
                    "imazapyr": "Imazapyr",
                    "imazethapyr": "Imazethapyr/Pursuit",
                    "metolachlor": "Metolachlor/Bicep/Dual/etc.",
                    "na_salt_bentazon": "Na Salt of bentazon/ Basagran",
                    "gramoxone": "Paraquat/Gramoxone",
                    "pendimethalin": "Pendimethalin/Prowl",
                    "rimsulfuron": "Rimsulfuron/LeadOff",
                    "trifluralin": "Trifluralin/Treflan",
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
