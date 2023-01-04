import json

cities = []
with open('cities.ndjson', 'r') as f:
    for line in f:
        try:
            cities.append(json.loads(line))
        except:
            print(line)
            
inc_city_att = [
    'Atlanta city',
    'Charleston city',
    'Columbus city',
    'Charlotte city',
    'Chicago city',
    'Detroit city',
    'Houston city',
    'Huntsville city',
    'Indianapolis city (balance)',
    'Jacksonville city',
    'Jackson city',
    'Kansas City city',
    'Little Rock city',
    'Los Angeles city',
    'Louisville city',
    'Nashville-Davidson metropolitan government (balance)',
    'Milwaukee city',
    'New Orleans city',
    'Oklahoma City city',
    'Wichita city',
]

inc_city_cl = [
    'Albuquerque city',
    'Billings city',
    'Boise City city',
    'Cheyenne city',
    'Denver city',
    'Des Moines city',
    'Fargo city',
    'Las Vegas city',
    'Minneapolis city',
    'Omaha city',
    'Phoenix city',
    'Portland city',
    'Salt Lake City city',
    'Seattle city',
    'Sioux Falls city'
]

inc_city_verizon = [
    'Baltimore city',
    'Boston city',
    'New York city',
    'Newark city',
    'Philadelphia city',
    'Providence city',
    'Virginia Beach city',
    'Washington city',
    'Wilmington city'
]

inc_city_el = [
    'Albuquerque city',
    'Atlanta city',
    'Billings city',
    'Boise City city',
    'Bridgeport city',
    'Charleston city',
    'Charlotte city',
    'Cheyenne city',
    'Chicago city',
    'Columbus city',
    'Denver city',
    'Des Moines city',
    'Detroit city',
    'Fargo city',
    'Houston city',
    'Huntsville city',
    'Indianapolis city (balance)',
    'Jacksonville city',
    'Kansas City city',
    'Las Vegas city',
    'Little Rock city',
    'Los Angeles city',
    'Louisville city',
    'Milwaukee city',
    'Nashville-Davidson metropolitan government (balance)',
    'New Orleans city',
    'Oklahoma City city',
    'Omaha city',
    'Phoenix city',
    'Portland city',
    'Salt Lake City city',
    'Seattle city',
    'Sioux Falls city',
    'Wichita city'
]

city2ap = {
    'Albuquerque': 'Albuquerque, N.M.',
    'Atlanta': 'Atlanta, Ga.',
    'Baltimore': 'Baltimore, Md.',
    'Billings': 'Billings, Mont.',
    'Boise': 'Boise, Idaho',
    'Boston': 'Boston, Mass.',
    'Charleston': 'Charleston, S.C.',
    'Charlotte': 'Charlotte, N.C.',
    'Cheyenne': 'Cheyenne, Wyo.',
    'Chicago': 'Chicago, Ill.',
    'Columbus': 'Columbus, Ohio',
    'Denver': 'Denver, Colo.',
    'Des Moines': 'Des Moines, Iowa',
    'Detroit': 'Detroit, Mich.',
    'Fargo': 'Fargo, N.D.',
    'Houston': 'Houston, Texas',
    'Huntsville': 'Huntsville, Ala.',
    'Indianapolis': 'Indianapolis, Ind.',
    'Jackson': 'Jackson, Miss.',
    'Jacksonville': 'Jacksonville, Fla.',
    'Kansas City': 'Kansas City, Mo.',
    'Las Vegas': 'Las Vegas, Nev.',
    'Little Rock': 'Little Rock, Ark.',
    'Los Angeles': 'Los Angeles, Calif.',
    'Louisville': 'Louisville, Ky.',
    'Milwaukee': 'Milwaukee, Wis.',
    'Minneapolis': 'Minneapolis, Minn.',
    'Nashville': 'Nashville, Tenn.',
    'New Orleans': 'New Orleans, La.',
    'New York City': 'New York, N.Y.',
    'Newark': 'Newark, N.J.',
    'Oklahoma City': 'Oklahoma City, Okla.',
    'Omaha': 'Omaha, Neb.',
    'Philadelphia': 'Philadelphia, Pa.',
    'Phoenix': 'Phoenix, Ariz.',
    'Portland': 'Portland, Ore.',
    'Providence': 'Providence, R.I.',
    'Salt Lake City': 'Salt Lake City, Utah',
    'Seattle': 'Seattle, Wash',
    'Sioux Falls': 'Sioux Falls, S.D.',
    'Virginia Beach': 'Virginia Beach, Va.',
    'Washington': 'Washington',
    'Wichita': 'Wichita, Kan.'
}

state2redlining = {
    'TX': ['redlining/TXHouston19XX.geojson'],
    'CA': ['redlining/CALosAngeles1939.geojson'],
    'LA': ['redlining/LANewOrleans1939.geojson'],
    'KS': ['redlining/KSWichita1937.geojson'],
    'IA': ['redlining/IADesMoines19XX.geojson'],
#     'OH': ['redlining/OHCleveland1939.geojson'],
    'OH': ['redlining/OHColumbus1936.geojson'],
    'WV': ['redlining/WVCharleston1938.geojson'],
    'AR': ['redlining/ARLittleRock19XX.geojson'],
    'AZ': ['redlining/AZPhoenix19XX.geojson'],
    'OR': ['redlining/ORPortland1937.geojson'],
    'PA': ['redlining/PAPhiladelphia1937.geojson'],
    'KY': ['redlining/KYLouisville1938.geojson'],
    'MD': ['redlining/MDBaltimore1937.geojson'],
    'WI': ['redlining/WIMilwaukeeCo1937.geojson'],
    'IN': ['redlining/INIndianapolis1937.geojson'],
    'NE': ['redlining/NEOmaha19XX.geojson'],
    'FL': ['redlining/FLJacksonville1937.geojson'],
    'MI': ['redlining/MIDetroit1939.geojson'],
    'IL': ['redlining/ILChicago1940.geojson'],
    'UT': ['redlining/UTSaltLakeCity19XX.geojson'],
    'MA': ['redlining/MABoston1938.geojson'],
    'GA': ['redlining/GAAtlanta1938.geojson'],
    'RI': ['redlining/RIProvidence19XX.geojson'],
    'NJ': ['redlining/NJEssexCo1939.geojson'],
    'CO': ['redlining/CODenver1938.geojson'],
    'MN': ['redlining/MNMinneapolis1937.geojson'],
    'WA': ['redlining/WASeattle1936.geojson'],
    'MO': ['redlining/MOGreaterKansasCity1939.geojson'],
    'MS': ['redlining/MSJackson19XX.geojson'],
    'NC': ['redlining/NCCharlotte1935.geojson'],
#     'TN': ['redlining/TNMemphis19XX.geojson'],
    'TN': ['redlining/TNNashville19XX.geojson'],
    'NY': [
        'redlining/NYBronx1938.geojson',
        'redlining/NYBrooklyn1938.geojson',
        'redlining/NYManhattan1937.geojson',
        'redlining/NYQueens1938.geojson',
        'redlining/NYStatenIsland1940.geojson',
    ],
}

# EarthLink
name2speed_el = {
    'Earthlink Internet 3Mx1M': 3,
    'EarthLink Internet 3M': 3,
    'EarthLink Internet 6M': 6,
    'Earthlink Internet 6Mx1M': 6,
    'EarthLink Internet 9Mx1M': 9,
    'EarthLink Internet 10M': 10,
    'Earthlink Internet 12Mx1M': 12,
    'EarthLink Internet 12M': 12,
    'EarthLink Internet 15M': 15,
    'EarthLink Internet 18M': 18,
    'Earthlink Internet 18Mx1.5M': 18,
    'Earthlink Internet 24Mx3M': 24,
    'EarthLink Internet 25Mx2M': 25,
    'EarthLink Internet 30M': 30,
    'EarthLink Internet 40M': 40,
    'Earthlink Internet 45Mx6M': 45,
    'EarthLink Internet 45Mx6M': 45,
    'EarthLink Internet 45M': 45,
    'EarthLink Internet 60M': 60,
    'EarthLink Internet 70Mx3M': 70,
    'Earthlink Internet 75Mx8M': 75,
    'EarthLink Internet 75Mx8M': 75,
    'EarthLink Internet 75M': 75,
    'EarthLink Internet 80M': 80,
    'EarthLink Internet 90Mx5M' : 90,
    'EarthLink Fiber 100M': 100,
    'EarthLink Internet 115Mx7M' : 115,
    'Earthlink Fiber 100Mx100M': 100,
    'EarthLink Fiber 200M': 200,
    'EarthLink Fiber 300Mx300M': 300,
    'Earthlink Fiber 300Mx300M': 300,
    'Earthlink Fiber 500Mx500M': 500,
    'EarthLink Fiber 700Mx700M': 700,
    'EarthLink Fiber 1G': 1000,
    'Earthlink Fiber 1Gx1G': 1000,
    'Earthlink Fiber 2Gx2G': 2000,
    'Earthlink Fiber 5Gx5G': 5000,
}

name2speed_el = {k.lower(): v for k,v in name2speed_el.items()}

speed_labels = {
    'No service' : "#5D5D5D", 
    'Slow (<25 Mbps)' : '#801930', 
    'Medium (25-99)' : '#a8596d', 
    'Fast (100-199)' : '#aebdcf', 
    "Blazing (≥200)": '#7b89a1'
}

income_labels = [
    'Low', 
    'Middle-Lower', 
    'Middle-Upper', 
    'Upper Income'
]

redlininggrade2name = {
    'A' : 'A - Best',
    'B' : 'B - Desirable',
    'C' : 'C - Declining',
    'D' : 'D - Hazardous',
}

race_labels = ['most white', 'more white', 'less white', 'least white']