# FixMyStreet Meta Categories

FixMyStreet uses different category names in different local authorities to match the internal descriptions used by the local authority. 

For analysis across areas, category names have to be combined. This repository contains lookups to combine into catgories at various levels of detail.

The SHEF categories were created by Elvis Nyanzu in 2018. 

* SHEF_A - 94 Categories
* SHEF_B - 29 Categories
* SHEF_C - 8 Categories

These are not stackable - e.g. some base categories that have the same SHEF_B might not have the same SHEF_C.  

The purpose of this repository is to allow these lookups to be updated as new FixMyStreet categories are created - and to reduce the work needed to create differently focused lookups. 

## C-level Category Groupings

* Road Safety & Defects - Relates to things like potholes, roadworks, street lights, road markings, gritting and other carriageway defects
* Environmental Health - Relates to dog fouling, blocked drains, spillages, dead animals and rubbish.
* Environmental Disruptions - Relates to overgrown trees and vegetation, dangerous buildings and structures, bus stop damage, utility cabinet damage and manhole covers.
* Incivilities - Relates to flyposting, graffiti and noise complaints.
* Access - Relates to obstructions to right of way for vehicles and pedestrians and footway defects.
* Abandoned Vehicles and Parking - Relates to untaxed vehicles, abandoned bicycles, abandoned cars and car-parking concerns.
* Public Spaces - Relates to parks, playing fields, landscapes and other open space concerns
* Other - Relates to things like protected trees, housing association concerns and council specific reports.
 
## C to B Category overlaps

As of Jan 2019

| C Category                   | B Category                   | Count  | %C    | % All |
|------------------------------|------------------------------|--------|-------|-------|
| Abandoned Vehicles & Parking | Abandoned Vehicles           | 44499  | 54.27 | 3.16  |
| Abandoned Vehicles & Parking | Parking                      | 37354  | 45.55 | 2.65  |
| Abandoned Vehicles & Parking | Other                        | 146    | 0.18  | 0.01  |
| Access                       | Right of Way                 | 19674  | 95.94 | 1.4   |
| Access                       | Public Toilets               | 832    | 4.06  | 0.06  |
| Environmental Disruptions    | Overgrown/Fallen Veg/Trees   | 50204  | 72.36 | 3.56  |
| Environmental Disruptions    | Street Furniture             | 8110   | 11.69 | 0.58  |
| Environmental Disruptions    | Bus Stops Damage             | 4163   | 6     | 0.3   |
| Environmental Disruptions    | Open Spaces/Parks            | 2144   | 3.09  | 0.15  |
| Environmental Disruptions    | Rubbish                      | 1343   | 1.94  | 0.1   |
| Environmental Disruptions    | Utility Works                | 1038   | 1.5   | 0.07  |
| Environmental Disruptions    | Bridge/Culvert Defects       | 748    | 1.08  | 0.05  |
| Environmental Disruptions    | Dangerous Building/Structure | 607    | 0.87  | 0.04  |
| Environmental Disruptions    | Fences                       | 319    | 0.46  | 0.02  |
| Environmental Disruptions    | Property Damage              | 309    | 0.45  | 0.02  |
| Environmental Disruptions    | Other                        | 255    | 0.37  | 0.02  |
| Environmental Disruptions    | Retaining Wall               | 137    | 0.2   | 0.01  |
| Environmental Health         | Rubbish                      | 302679 | 84.55 | 21.49 |
| Environmental Health         | Drainage                     | 26959  | 7.53  | 1.91  |
| Environmental Health         | Dog Fouling                  | 23768  | 6.64  | 1.69  |
| Environmental Health         | Environmental Health         | 4130   | 1.15  | 0.29  |
| Environmental Health         | Bin Replacement              | 443    | 0.12  | 0.03  |
| Incivilities                 | Incivilities                 | 32851  | 87.06 | 2.33  |
| Incivilities                 | Rubbish                      | 4884   | 12.94 | 0.35  |
| Other                        | Other                        | 81077  | 99.79 | 5.76  |
| Other                        | Floral Displays              | 169    | 0.21  | 0.01  |
| Public Space                 | Open Spaces/Parks            | 16890  | 99.99 | 1.2   |
| Public Space                 | Public Toilets               | 1      | 0.01  | 0     |
| Road Safety & Defects        | Road Surface Defects         | 342975 | 46.21 | 24.35 |
| Road Safety & Defects        | Street Lights                | 129301 | 17.42 | 9.18  |
| Road Safety & Defects        | Highways Enquiries           | 120088 | 16.18 | 8.53  |
| Road Safety & Defects        | Pavement /Footway Defects    | 92689  | 12.49 | 6.58  |
| Road Safety & Defects        | Road Safety                  | 55538  | 7.48  | 3.94  |
| Road Safety & Defects        | Grounds Maintenance          | 1014   | 0.14  | 0.07  |
| Road Safety & Defects        | Gritting                     | 653    | 0.09  | 0.05  |

## B to A Category overlaps 

As of Jan 2019

| B Category                   | A Category                   | Count  | %B    | % All |
|------------------------------|------------------------------|--------|-------|-------|
| Abandoned Vehicles           | Abandoned Vehicles           | 44499  | 100   | 3.16  |
| Bin Replacement              | Bin Repair/Replacement       | 327    | 73.81 | 0.02  |
| Bin Replacement              | Dog Litter Bin               | 116    | 26.19 | 0.01  |
| Bridge/Culvert Defects       | Bridge/Culvert Defects       | 748    | 100   | 0.05  |
| Bus Stops Damage             | Bus Stops Damage             | 4163   | 100   | 0.3   |
| Dangerous Building/Structure | Dangerous Building/Structure | 607    | 100   | 0.04  |
| Dog Fouling                  | Dog Fouling                  | 23768  | 100   | 1.69  |
| Drainage                     | Blocked Drains               | 17914  | 66.45 | 1.27  |
| Drainage                     | Manhole Covers               | 3206   | 11.89 | 0.23  |
| Drainage                     | Gullies                      | 2508   | 9.3   | 0.18  |
| Drainage                     | Flooding                     | 1677   | 6.22  | 0.12  |
| Drainage                     | Gully/Manhole Defects        | 1395   | 5.17  | 0.1   |
| Drainage                     | Highway Drainage             | 108    | 0.4   | 0.01  |
| Drainage                     | Manhole Defects              | 85     | 0.32  | 0.01  |
| Drainage                     | Grids and Drains             | 66     | 0.24  | 0     |
| Environmental Health         | Dead Animals                 | 4023   | 97.41 | 0.29  |
| Environmental Health         | Environmental Health         | 66     | 1.6   | 0     |
| Environmental Health         | Pest Control                 | 41     | 0.99  | 0     |
| Fences                       | Fences                       | 319    | 100   | 0.02  |
| Floral Displays              | Floral displays              | 169    | 100   | 0.01  |
| Gritting                     | Grit Bins                    | 213    | 32.62 | 0.02  |
| Gritting                     | Gritting                     | 205    | 31.39 | 0.01  |
| Gritting                     | Ice & Snow                   | 177    | 27.11 | 0.01  |
| Gritting                     | Salt Bins                    | 58     | 8.88  | 0     |
| Grounds Maintenance          | Road Works                   | 456    | 44.97 | 0.03  |
| Grounds Maintenance          | Roadworks                    | 388    | 38.26 | 0.03  |
| Grounds Maintenance          | Highway Condition            | 146    | 14.4  | 0.01  |
| Grounds Maintenance          | Grounds Maintenance          | 24     | 2.37  | 0     |
| Highways Enquiries           | Highway Condition            | 114395 | 95.26 | 8.12  |
| Highways Enquiries           | General Highways Enquiries   | 5693   | 4.74  | 0.4   |
| Incivilities                 | Graffiti                     | 31797  | 96.79 | 2.26  |
| Incivilities                 | Flyposting                   | 486    | 1.48  | 0.03  |
| Incivilities                 | Shopping Trolley             | 461    | 1.4   | 0.03  |
| Incivilities                 | Noise                        | 107    | 0.33  | 0.01  |
| Open Spaces/Parks            | Open Spaces/Parks            | 19025  | 99.95 | 1.35  |
| Open Spaces/Parks            | Fallen/Dangerous Trees       | 9      | 0.05  | 0     |
| Other                        | Other                        | 79246  | 97.26 | 5.63  |
| Other                        | Admin                        | 1380   | 1.69  | 0.1   |
| Other                        | Lewisham Homes               | 378    | 0.46  | 0.03  |
| Other                        | Broken Kerbs                 | 240    | 0.29  | 0.02  |
| Other                        | Untaxed Vehcile              | 146    | 0.18  | 0.01  |
| Other                        | To Let Signs                 | 32     | 0.04  | 0     |
| Other                        | Phoenix HA                   | 21     | 0.03  | 0     |
| Other                        | Demo                         | 18     | 0.02  | 0     |
| Other                        | C.C.T.V Faults               | 12     | 0.01  | 0     |
| Other                        | Broken Fire Hydrant          | 3      | 0     | 0     |
| Other                        | Lit Signs                    | 1      | 0     | 0     |
| Other                        | Protected Trees              | 1      | 0     | 0     |
| Overgrown/Fallen Veg/Trees   | Fallen/Dangerous Trees       | 24987  | 49.77 | 1.77  |
| Overgrown/Fallen Veg/Trees   | Overgrown Vegetation         | 14641  | 29.16 | 1.04  |
| Overgrown/Fallen Veg/Trees   | Grass/Weed Control           | 10576  | 21.07 | 0.75  |
| Parking                      | Parking                      | 37354  | 100   | 2.65  |
| Pavement /Footway Defects    | Pavement /Footway Defects    | 92673  | 99.98 | 6.58  |
| Pavement /Footway Defects    | Road Surface Defects         | 16     | 0.02  | 0     |
| Property Damage              | Property Damage              | 309    | 100   | 0.02  |
| Public Toilets               | Public Toilets               | 833    | 100   | 0.06  |
| Retaining Wall               | Retaining Wall               | 137    | 100   | 0.01  |
| Right of Way                 | Obstruction                  | 8646   | 43.95 | 0.61  |
| Right of Way                 | Right of Way                 | 5452   | 27.71 | 0.39  |
| Right of Way                 | Trees and Hedges RoW         | 2294   | 11.66 | 0.16  |
| Right of Way                 | Pavement /Footway Defects    | 1769   | 8.99  | 0.13  |
| Right of Way                 | Overgrown Vegetation         | 954    | 4.85  | 0.07  |
| Right of Way                 | Trees on RoW                 | 405    | 2.06  | 0.03  |
| Right of Way                 | Barriers/Bollards on RoW     | 100    | 0.51  | 0.01  |
| Right of Way                 | Countryside RoW              | 32     | 0.16  | 0     |
| Right of Way                 | Vehicle Access               | 10     | 0.05  | 0     |
| Right of Way                 | Gates/Stiles RoW             | 8      | 0.04  | 0     |
| Right of Way                 | Street Signs                 | 3      | 0.02  | 0     |
| Right of Way                 | Grass/Weed Control           | 1      | 0.01  | 0     |
| Road Safety                  | Street Signs                 | 35264  | 63.5  | 2.5   |
| Road Safety                  | Traffic Lights               | 15851  | 28.54 | 1.13  |
| Road Safety                  | Road Markings                | 4172   | 7.51  | 0.3   |
| Road Safety                  | Barriers/Bollards on RoW     | 147    | 0.26  | 0.01  |
| Road Safety                  | Road Safety                  | 49     | 0.09  | 0     |
| Road Safety                  | Skips                        | 28     | 0.05  | 0     |
| Road Safety                  | Sign or Marking              | 16     | 0.03  | 0     |
| Road Safety                  | Zebra Crossing               | 11     | 0.02  | 0     |
| Road Surface Defects         | Potholes                     | 302454 | 88.19 | 21.47 |
| Road Surface Defects         | Road Surface Defects         | 25986  | 7.58  | 1.84  |
| Road Surface Defects         | Road/Pavement Defects        | 11645  | 3.4   | 0.83  |
| Road Surface Defects         | Pavement /Footway Defects    | 2777   | 0.81  | 0.2   |
| Road Surface Defects         | Highway Condition            | 113    | 0.03  | 0.01  |
| Rubbish                      | Fly-tipping                  | 156101 | 50.53 | 11.08 |
| Rubbish                      | Street Cleaning              | 54867  | 17.76 | 3.9   |
| Rubbish                      | Rubbish                      | 40521  | 13.12 | 2.88  |
| Rubbish                      | Dumped Rubbish               | 30564  | 9.89  | 2.17  |
| Rubbish                      | Litter/Litter Bin            | 7339   | 2.38  | 0.52  |
| Rubbish                      | Flyposting                   | 4884   | 1.58  | 0.35  |
| Rubbish                      | Accumulated Litter           | 3942   | 1.28  | 0.28  |
| Rubbish                      | Garden Waste                 | 3034   | 0.98  | 0.22  |
| Rubbish                      | Debris/Spillage              | 1816   | 0.59  | 0.13  |
| Rubbish                      | Missed Bin Collection        | 1383   | 0.45  | 0.1   |
| Rubbish                      | Leafing                      | 1343   | 0.43  | 0.1   |
| Rubbish                      | Spillage on Road             | 996    | 0.32  | 0.07  |
| Rubbish                      | Recycling                    | 731    | 0.24  | 0.05  |
| Rubbish                      | Bin Collection               | 564    | 0.18  | 0.04  |
| Rubbish                      | Trip Hazard                  | 477    | 0.15  | 0.03  |
| Rubbish                      | Discarded Syringes           | 140    | 0.05  | 0.01  |
| Rubbish                      | Skips                        | 117    | 0.04  | 0.01  |
| Rubbish                      | Trade Waste                  | 87     | 0.03  | 0.01  |
| Street Furniture             | Street Name Plates           | 6906   | 85.15 | 0.49  |
| Street Furniture             | Street Furniture             | 1140   | 14.06 | 0.08  |
| Street Furniture             | Benches/Bicycle Racks        | 64     | 0.79  | 0     |
| Street Lights                | Street Lights                | 129310 | 100   | 9.18  |
| Utility Works                | Utility Works                | 1037   | 99.9  | 0.07  |
| Utility Works                | Trenches                     | 1      | 0.1   | 0     |
