from ..psa_gps import psa_gps_vFTrkLn3MMbs9wCLEBBh4s as psa_gps

from ..psa_water_sensor_install import wsensor_install_vuiiHRr2MJSGzFwSncyLP9 as wsensor_install_vuiiHRr2MJSGzFwSncyLP9
from ..psa_water_sensor_install import wsensor_install_vCK5tppVaNkkfWMhtddxEb as wsensor_install_vCK5tppVaNkkfWMhtddxEb

from ..psa_decomp_bag_pre_wt import decomp_biomass_fresh_vQnB8sJFc8JEhYJqXiYQRy as decomp_biomass_fresh_vQnB8sJFc8JEhYJqXiYQRy
from ..psa_decomp_bag_pre_wt import decomp_biomass_fresh_vZvVu9PdqRHLeeJGbGha3z as decomp_biomass_fresh_vZvVu9PdqRHLeeJGbGha3z
from ..psa_decomp_bag_pre_wt import decomp_biomass_fresh_vgaKFRKRg54E2Z7fvayCxf as decomp_biomass_fresh_vgaKFRKRg54E2Z7fvayCxf
from ..psa_decomp_bag_pre_wt import decomp_biomass_fresh_vzazAbS9satE4PXaGNKwBE as decomp_biomass_fresh_vzazAbS9satE4PXaGNKwBE 

from ..psa_bag_dry_wt import decomp_biomass_dry_vDqdEsDav5K6hSRHrgYJmM as decomp_biomass_dry_vDqdEsDav5K6hSRHrgYJmM
from ..psa_bag_dry_wt import decomp_biomass_dry_vusvAjv42DfdfjKkFWm6H3 as decomp_biomass_dry_vusvAjv42DfdfjKkFWm6H3

from ..psa_bag_collect import decomp_biomass_dry_v94kLXWMrZ8fZRpCFzSn4e as decomp_biomass_dry_v94kLXWMrZ8fZRpCFzSn4e
from ..psa_bag_collect import decomp_biomass_dry_v5LVmcbGVhR3C3fkW9ZhHG as decomp_biomass_dry_v5LVmcbGVhR3C3fkW9ZhHG

from ..psa_biomass_decomp_bag import biomass_in_field_vEchkcAone8S7y4eYhgru4 as biomass_in_field_vEchkcAone8S7y4eYhgru4
from ..psa_biomass_decomp_bag import biomass_in_field_vyYD9Bt3WSjzKorvPhLvLh as biomass_in_field_vyYD9Bt3WSjzKorvPhLvLh
from ..psa_biomass_decomp_bag import biomass_in_field_vcrycicDgojagKK5b7hTAP as biomass_in_field_vcrycicDgojagKK5b7hTAP
from ..psa_biomass_decomp_bag import biomass_in_field_va4wrosaFh5fN8rUZnKZHz as biomass_in_field_va4wrosaFh5fN8rUZnKZHz
from ..psa_biomass_decomp_bag import biomass_in_field_vLamBBuk4isVXD6ZxyNzjs as biomass_in_field_vLamBBuk4isVXD6ZxyNzjs

from ..psa_biomass_decomp_bag import decomp_biomass_fresh_vEchkcAone8S7y4eYhgru4 as decomp_biomass_fresh_vEchkcAone8S7y4eYhgru4
from ..psa_biomass_decomp_bag import decomp_biomass_fresh_vyYD9Bt3WSjzKorvPhLvLh as decomp_biomass_fresh_vyYD9Bt3WSjzKorvPhLvLh
from ..psa_biomass_decomp_bag import decomp_biomass_fresh_vcrycicDgojagKK5b7hTAP as decomp_biomass_fresh_vcrycicDgojagKK5b7hTAP
from ..psa_biomass_decomp_bag import decomp_biomass_fresh_va4wrosaFh5fN8rUZnKZHz as decomp_biomass_fresh_va4wrosaFh5fN8rUZnKZHz
from ..psa_biomass_decomp_bag import decomp_biomass_fresh_vLamBBuk4isVXD6ZxyNzjs as decomp_biomass_fresh_vLamBBuk4isVXD6ZxyNzjs

asset_names = {
    "psa gps": [
        {   
            "table_name": "gps_corners__gps",
            "table_keys": {
                "vFTrkLn3MMbs9wCLEBBh4s": psa_gps.data,
            },
        },
    ],

    "psa water sensor install": [
        {   
            "table_name": "wsensor_install__water_sensor_install",
            "table_keys": {
                "vuiiHRr2MJSGzFwSncyLP9": wsensor_install_vuiiHRr2MJSGzFwSncyLP9.data,
                "vCK5tppVaNkkfWMhtddxEb": wsensor_install_vCK5tppVaNkkfWMhtddxEb.data,
            },
        },
    ],

    "psa decomp bag pre wt": [
        {   
            "table_name": "decomp_biomass_fresh__decomp_bag_pre_wt",
            "table_keys": {
                "vQnB8sJFc8JEhYJqXiYQRy": decomp_biomass_fresh_vQnB8sJFc8JEhYJqXiYQRy.data,
                "vZvVu9PdqRHLeeJGbGha3z": decomp_biomass_fresh_vZvVu9PdqRHLeeJGbGha3z.data,
                "vgaKFRKRg54E2Z7fvayCxf": decomp_biomass_fresh_vgaKFRKRg54E2Z7fvayCxf.data,
                "vzazAbS9satE4PXaGNKwBE": decomp_biomass_fresh_vzazAbS9satE4PXaGNKwBE.data,                
            },
        },
    ],

    "psa decomp bag dry wt": [
        {   
            "table_name": "decomp_biomass_dry__decomp_bag_dry_wt",
            "table_keys": {
                "vDqdEsDav5K6hSRHrgYJmM": decomp_biomass_dry_vDqdEsDav5K6hSRHrgYJmM.data,
                "vusvAjv42DfdfjKkFWm6H3": decomp_biomass_dry_vusvAjv42DfdfjKkFWm6H3.data,
            },
        },
    ],

    "psa decomp bag collect": [
        {   
            "table_name": "decomp_biomass_dry__decomp_bag_collect",
            "table_keys": {
                "v94kLXWMrZ8fZRpCFzSn4e": decomp_biomass_dry_v94kLXWMrZ8fZRpCFzSn4e.data,
                "v5LVmcbGVhR3C3fkW9ZhHG": decomp_biomass_dry_v5LVmcbGVhR3C3fkW9ZhHG.data,
            },
        },
    ],

    "psa biomass decomp bag": [
        {   
            "table_name": "biomass_in_field__biomass_decomp_bag",
            "table_keys": {
                "vEchkcAone8S7y4eYhgru4": biomass_in_field_vEchkcAone8S7y4eYhgru4.data,
                "vyYD9Bt3WSjzKorvPhLvLh": biomass_in_field_vyYD9Bt3WSjzKorvPhLvLh.data,
                "vcrycicDgojagKK5b7hTAP": biomass_in_field_vcrycicDgojagKK5b7hTAP.data,
                "va4wrosaFh5fN8rUZnKZHz": biomass_in_field_va4wrosaFh5fN8rUZnKZHz.data,
                "vLamBBuk4isVXD6ZxyNzjs": biomass_in_field_vLamBBuk4isVXD6ZxyNzjs.data,
            },
        },
        {   
            "table_name": "decomp_biomass_fresh__biomass_decomp_bag",
            "table_keys": {
                "vEchkcAone8S7y4eYhgru4": decomp_biomass_fresh_vEchkcAone8S7y4eYhgru4.data,
                "vyYD9Bt3WSjzKorvPhLvLh": decomp_biomass_fresh_vyYD9Bt3WSjzKorvPhLvLh.data,
                "vcrycicDgojagKK5b7hTAP": decomp_biomass_fresh_vcrycicDgojagKK5b7hTAP.data,
                "va4wrosaFh5fN8rUZnKZHz": decomp_biomass_fresh_va4wrosaFh5fN8rUZnKZHz.data,
                "vLamBBuk4isVXD6ZxyNzjs": decomp_biomass_fresh_vLamBBuk4isVXD6ZxyNzjs.data,
            },
        },
    ],
}