# Copyright (C) 2025 whitevamp
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import Dict, Tuple

# Master dictionary of common aspect ratios and their associated resolutions
# This acts as the authoritative source for resolution definitions.
# This dictionary can be updated by the scanner's merging functions.
COMMON_RESOLUTIONS_DEFINITIONS: Dict[str, Dict[str, Tuple[int, int]]] = {
    '9:21': {
        'UW-FHD Portrait': (1080, 2560),
        'UW-QHD Portrait': (1440, 3440),
    },
    '9:16': {
        'FHD Portrait': (1080, 1920),
        'Custom Portrait (1152x2048)': (1152, 2048),
        'QHD Portrait': (1440, 2560),
        '4K Portrait': (2160, 3840),
    },
    '1469:2560': {
        'Custom Portrait': (1469, 2560),
    },
    '151:262': {
        'Custom Portrait': (1208, 2096),
    },
    '1479:2560': {
        'Custom Portrait': (1479, 2560),
    },
    '3:5': {
        'Custom Portrait (720x1200)': (720, 1200),
        'Custom Portrait': (1680, 2800),
        'Custom Portrait (1800x3000)': (1800, 3000),
    },
    '53:88': {
        'Custom Portrait': (1696, 2816),
    },
    '160:263': {
        'Common Portrait (160:263)': (1280, 2104),
    },
    '1573:2560': {
        'Custom Portrait': (1573, 2560),
    },
    '5:8': {
        'Extra Small Portrait': (250, 400),
        'Small Portrait': (400, 640),
        'Common AI Gen Portrait': (800, 1280),
        'Medium Portrait': (1000, 1600),
        'Large Portrait': (1250, 2000),
        'Custom Portrait (1280x2048)': (1280, 2048),
        'Extra Large Portrait': (1500, 2400),
        'Super Large Portrait': (2000, 3200),
    },
    '10:16': {
        'WXGA Portrait': (800, 1280),
        'WUXGA Portrait': (1200, 1920),
    },
    '201:308': {
        'Custom Portrait': (1608, 2464),
    },
    '55:84': {
        'Custom Portrait': (880, 1344),
    },
    '2:3': {
        'Custom Portrait (512x768)': (512, 768),
        'Custom Portrait (564x846)': (564, 846),
        'Custom Portrait (600x900)': (600, 900),
        'Custom Portrait (640x960)': (640, 960),
        'Custom Portrait (658x987)': (658, 987),
        'Custom Portrait (700x1050)': (700, 1050),
        'Custom Portrait (720x1080)': (720, 1080),
        'Custom Portrait (750x1125)': (750, 1125),
        'Custom Portrait (768x1152)': (768, 1152),
        'Custom Portrait (800x1200)': (800, 1200),
        'Custom Portrait (816x1224)': (816, 1224),
        'Custom Portrait (850x1275)': (850, 1275),
        'Custom Portrait (896x1344)': (896, 1344),
        'Custom Portrait (960x1440)': (960, 1440),
        'Custom Portrait (968x1452)': (968, 1452),
        'Custom Portrait (980x1470)': (980, 1470),
        'Common AI Gen Portrait': (1024, 1536),
        'Custom Portrait (1072x1608)': (1072, 1608),
        'Custom Portrait (1080x1620)': (1080, 1620),
        'Custom Portrait (1152x1728)': (1152, 1728),
        'Custom Portrait (1200x1800)': (1200, 1800),
        'Custom Portrait (1280x1920)': (1280, 1920),
        'Custom Portrait (1328x1992)': (1328, 1992),
        'Custom Portrait (1440x2160)': (1440, 2160),
        'Medium Portrait': (1504, 2256),
        'Custom Portrait (1536x2304)': (1536, 2304),
        'Custom Portrait (1600x2400)': (1600, 2400),
        'Custom Portrait (1664x2496)': (1664, 2496),
        'Custom Portrait (1700x2550)': (1700, 2550),
        'Custom Portrait (1792x2688)': (1792, 2688),
        'Custom Portrait (1920x2880)': (1920, 2880),
        'Custom Portrait (2048x3072)': (2048, 3072),
    },
    '13:19': {
        'Extra Small Portrait': (208, 304),
        'Small Portrait': (416, 608),
        'Common AI Gen Portrait': (832, 1216),
        'Medium Portrait': (1040, 1520),
        'Custom Portrait (1248x1824)': (1248, 1824),
        'Large Portrait': (1300, 1900),
        'Extra Large Portrait': (1560, 2280),
        'Custom Portrait (1664x2432)': (1664, 2432),
        'Super Large Portrait': (1820, 2660),
        'Ultra Large Portrait': (2080, 3040),
    },
    '832:1193': {
        'Custom Portrait': (832, 1193),
    },
    '7:10': {
        'Custom Portrait (448x640)': (448, 640),
        'Custom Portrait (896x1280)': (896, 1280),
        'Custom Portrait (1008x1440)': (1008, 1440),
        'Custom Portrait (1050x1500)': (1050, 1500),
        'Custom Portrait': (1400, 2000),
    },
    '1280:1811': {
        'Custom Portrait': (1280, 1811),
    },
    '850:1169': {
        'Custom Portrait': (850, 1169),
    },
    '187:250': {
        'Custom Portrait': (1496, 2000),
    },
    '3:4': {
        'Custom Portrait (165x220)': (165, 220),
        'VGA Portrait': (480, 640),
        'Custom Portrait (576x768)': (576, 768),
        'Custom Portrait (600x800)': (600, 800),
        'Custom Portrait (675x900)': (675, 900),
        'Custom Portrait (720x960)': (720, 960),
        'Custom Portrait (750x1000)': (750, 1000),
        'XGA Portrait': (768, 1024),
        'Custom Portrait (900x1200)': (900, 1200),
        'Custom Portrait (960x1280)': (960, 1280),
        'Custom Portrait (1056x1408)': (1056, 1408),
        'Custom Portrait (1125x1500)': (1125, 1500),
        'XGA+ Portrait': (1152, 1536),
        'UXGA Portrait': (1200, 1600),
        'UXGA+ Portrait': (1536, 2048),
        'Custom Portrait (1620x2160)': (1620, 2160),
        'Custom Portrait (1728x2304)': (1728, 2304),
        'Custom Portrait (1800x2400)': (1800, 2400),
        'QHD-Equivalent Portrait': (1920, 2560),
        'Custom Portrait (1992x2656)': (1992, 2656),
    },
    '199:256': {
        'Custom Portrait': (995, 1280),
    },
    '64:81': {
        'Custom Portrait': (1024, 1296),
    },
    '19:24': {
        'Custom Portrait': (1216, 1536),
    },
    '55:69': {
        'Custom Portrait': (165, 207),
    },
    '4:5': {
        'Custom Portrait (700x875)': (700, 875),
        'Custom Portrait (900x1125)': (900, 1125),
        'Medium 4:5 Portrait': (1024, 1280),
        'Custom Portrait (1200x1500)': (1200, 1500),
        'Desktop Portrait': (1280, 1600),
        'Custom Portrait (1536x1920)': (1536, 1920),
        'Large 4:5 Portrait': (2048, 2560),
    },
    '71:86': {
        'Custom Portrait': (1136, 1376),
    },
    '64:75': {
        'Custom Portrait': (1024, 1200),
        'Custom Portrait (1280x1500)': (1280, 1500),
    },
    '47:53': {
        'Custom Portrait': (1504, 1696),
    },
    '1:1': {
        'Custom Landscape (165x165)': (165, 165),
        'Custom Landscape (320x320)': (320, 320),
        'Common AI Gen Square': (512, 512),
        'Custom Landscape (600x600)': (600, 600),
        'Instagram': (640, 640),
        'Custom Landscape (650x650)': (650, 650),
        'Custom Landscape (700x700)': (700, 700),
        'Custom Landscape (716x716)': (716, 716),
        'Custom Landscape (720x720)': (720, 720),
        'Custom Landscape (750x750)': (750, 750),
        'Custom Landscape (768x768)': (768, 768),
        'Custom Landscape (800x800)': (800, 800),
        'Custom Landscape (838x838)': (838, 838),
        'Custom Landscape (850x850)': (850, 850),
        'Custom Landscape (857x857)': (857, 857),
        'Custom Landscape (911x911)': (911, 911),
        'Custom Landscape (980x980)': (980, 980),
        'Custom Landscape (993x993)': (993, 993),
        'Custom Landscape (1000x1000)': (1000, 1000),
        'Custom Landscape (1024x1024)': (1024, 1024),
        'Custom Landscape (1076x1076)': (1076, 1076),
        'Square': (1080, 1080),
        'Custom Landscape (1101x1101)': (1101, 1101),
        'Custom Landscape (1152x1152)': (1152, 1152),
        'Custom Landscape (1181x1181)': (1181, 1181),
        'Custom Landscape (1200x1200)': (1200, 1200),
        'Custom Landscape (1238x1238)': (1238, 1238),
        'Custom Landscape (1269x1269)': (1269, 1269),
        'Custom Landscape (1280x1280)': (1280, 1280),
        'Custom Landscape (1285x1285)': (1285, 1285),
        'Custom Landscape (1408x1408)': (1408, 1408),
        'Custom Landscape (1424x1424)': (1424, 1424),
        'Custom Landscape (1440x1440)': (1440, 1440),
        'Custom Landscape (1536x1536)': (1536, 1536),
        'Custom Landscape (1608x1608)': (1608, 1608),
        'Custom Landscape (1638x1638)': (1638, 1638),
        'Custom Landscape (1664x1664)': (1664, 1664),
        'Custom Landscape (1728x1728)': (1728, 1728),
        'Custom Landscape (1843x1843)': (1843, 1843),
        'Custom Landscape (1920x1920)': (1920, 1920),
        'Custom Landscape (2000x2000)': (2000, 2000),
        'Custom Landscape (2001x2001)': (2001, 2001),
        'Custom Landscape (2032x2032)': (2032, 2032),
        'Higher Res Square': (2048, 2048),
    },
    '5:4': {
        'Custom Landscape (800x640)': (800, 640),
        'Custom Landscape (850x680)': (850, 680),
        'Custom Landscape (1120x896)': (1120, 896),
        'Custom Landscape (1200x960)': (1200, 960),
        'SXGA': (1280, 1024),
    },
    '4:3': {
        'Custom Landscape (320x240)': (320, 240),
        'Custom Landscape (560x420)': (560, 420),
        'Custom Landscape (600x450)': (600, 450),
        'Custom Landscape (620x465)': (620, 465),
        'VGA': (640, 480),
        'SVGA': (800, 600),
        'Custom Landscape (900x675)': (900, 675),
        'Custom Landscape (1000x750)': (1000, 750),
        'XGA': (1024, 768),
        'Custom Landscape (1200x900)': (1200, 900),
        'Custom Landscape (1280x960)': (1280, 960),
        'SXGA+': (1400, 1050),
        'UXGA': (1600, 1200),
        'QXGA': (2048, 1536),
    },
    '1645:1152': {
        'Custom Landscape': (1645, 1152),
    },
    '730:499': {
        'Custom Landscape': (730, 499),
    },
    '3:2': {
        'Custom Landscape (768x512)': (768, 512),
        'Custom Landscape (900x600)': (900, 600),
        'Custom Landscape (1095x730)': (1095, 730),
        'Custom Landscape (1536x1024)': (1536, 1024),
        'Custom Landscape (1920x1280)': (1920, 1280),
        'Surface Laptop': (2256, 1504),
        'Surface Pro': (2736, 1824),
    },
    '16:10': {
        'WXGA': (1280, 800),
        'WXGA+': (1440, 900),
        'WSXGA+': (1680, 1050),
        'WUXGA': (1920, 1200),
    },
    '5:3': {
        'Common Laptop': (1280, 768),
        'HD-Ready': (1360, 768),
    },
    '16:9': {
        'Custom Landscape (1024x576)': (1024, 576),
        '720p': (1280, 720),
        '1080p': (1920, 1080),
        '1440p': (2560, 1440),
        '4K UHD': (3840, 2160),
        '8K UHD': (7680, 4320),
    },
    '21:9': {
        'UW-FHD': (2560, 1080),
        'UW-QHD': (3440, 1440),
        'UW-4K': (5120, 2160),
    },
    '2.35:1': {
        'Cinema FHD': (1920, 817),
        'Cinema 4K': (4096, 1746),
    },
    '2.39:1': {
        'Cinema FHD': (1920, 803),
        'Cinema 4K': (4096, 1716),
    },
    '32:9': {
        'Super Ultrawide FHD': (3840, 1080),
        'Super Ultrawide QHD': (5120, 1440),
        'Super Ultrawide 4K': (7680, 2160),
    },
    ##ADDED
        '1:57': {
        'Custom Portrait': (1024, 58368),
    },
    '1:9': {
        'Custom Portrait': (1024, 9216),
    },
    '500:2447': {
        'Custom Portrait': (1000, 4894),
    },
    '4:15': {
        'Custom Portrait': (320, 1200),
    },
    '167:600': {
        'Custom Portrait': (334, 1200),
    },
    '191:600': {
        'Custom Portrait': (382, 1200),
    },
    '256:787': {
        'Custom Portrait': (1280, 3935),
    },
    '200:613': {
        'Custom Portrait': (400, 1226),
    },
    '536:1619': {
        'Custom Portrait': (536, 1619),
    },
    '1:3': {
        'Custom Portrait': (1280, 3840),
    },
    '403:1200': {
        'Custom Portrait': (403, 1200),
    },
    '27:80': {
        'Custom Portrait': (405, 1200),
    },
    '552:1619': {
        'Custom Portrait': (552, 1619),
    },
    '1135:3264': {
        'Custom Portrait': (1135, 3264),
    },
    '545:1518': {
        'Custom Portrait': (545, 1518),
    },
    '568:1539': {
        'Custom Portrait': (568, 1539),
    },
    '37:100': {
        'Custom Portrait': (444, 1200),
    },
    '189:500': {
        'Custom Portrait': (378, 1000),
    },
    '59:150': {
        'Custom Portrait': (472, 1200),
    },
    '2:5': {
        'Custom Portrait': (480, 1200),
    },
    '491:1200': {
        'Custom Portrait': (491, 1200),
    },
    '46:111': {
        'Custom Portrait': (736, 1776),
    },
    '167:400': {
        'Custom Portrait': (501, 1200),
    },
    '1280:3059': {
        'Custom Portrait': (1280, 3059),
    },
    '96:229': {
        'Custom Portrait': (768, 1832),
    },
    '517:1200': {
        'Custom Portrait': (517, 1200),
    },
    '527:1200': {
        'Custom Portrait': (527, 1200),
    },
    '640:1417': {
        'Custom Portrait': (1280, 2834),
    },
    '5:11': {
        'Custom Portrait': (1280, 2816),
    },
    '137:300': {
        'Custom Portrait': (548, 1200),
    },
    '195:422': {
        'Custom Portrait': (1170, 2532),
    },
    '596:1287': {
        'Custom Portrait': (596, 1287),
    },
    '7:15': {
        'Custom Portrait': (560, 1200),
    },
    '187:400': {
        'Custom Portrait': (561, 1200),
    },
    '281:600': {
        'Custom Portrait': (562, 1200),
    },
    '309:655': {
        'Custom Portrait': (1236, 2620),
    },
    '1280:2683': {
        'Custom Portrait': (1280, 2683),
    },
    '1280:2679': {
        'Custom Portrait': (1280, 2679),
    },
    '287:600': {
        'Custom Portrait': (574, 1200),
    },
    '1280:2639': {
        'Custom Portrait': (1280, 2639),
    },
    '37:75': {
        'Custom Portrait': (592, 1200),
    },
    '1000:2023': {
        'Custom Portrait': (1000, 2023),
    },
    '1280:2577': {
        'Custom Portrait': (1280, 2577),
    },
    '89:179': {
        'Custom Portrait': (712, 1432),
    },
    '100:201': {
        'Custom Portrait': (1000, 2010),
    },
    '1:2': {
        'Custom Portrait': (1000, 2000),
    },
    '867:1720': {
        'Custom Portrait': (867, 1720),
    },
    '627:1237': {
        'Custom Portrait': (627, 1237),
    },
    '1280:2523': {
        'Custom Portrait': (1280, 2523),
    },
    '100:197': {
        'Custom Portrait': (1200, 2364),
    },
    '32:63': {
        'Custom Portrait': (736, 1449),
    },
    '127:250': {
        'Custom Portrait': (762, 1500),
    },
    '1280:2519': {
        'Custom Portrait': (1280, 2519),
    },
    '736:1437': {
        'Custom Portrait': (736, 1437),
    },
    '256:497': {
        'Custom Portrait': (1280, 2485),
    },
    '40:77': {
        'Custom Portrait': (1280, 2464),
    },
    '13:25': {
        'Custom Portrait': (1144, 2200),
    },
    '115:221': {
        'Custom Portrait': (1840, 3536),
    },
    '640:1223': {
        'Custom Portrait': (1280, 2446),
    },
    '1189:2272': {
        'Custom Portrait': (1189, 2272),
    },
    '157:300': {
        'Custom Portrait': (471, 900),
    },
    '1280:2433': {
        'Custom Portrait': (1280, 2433),
    },
    '585:1111': {
        'Custom Portrait': (1170, 2222),
    },
    '17:32': {
        'Custom Portrait': (544, 1024),
    },
    '320:601': {
        'Custom Portrait': (1280, 2404),
    },
    '8:15': {
        'Custom Portrait': (800, 1500),
    },
    '1073:2000': {
        'Custom Portrait': (1073, 2000),
    },
    '320:593': {
        'Custom Portrait': (1280, 2372),
    },
    '128:237': {
        'Custom Portrait': (1280, 2370),
    },
    '1280:2367': {
        'Custom Portrait': (1280, 2367),
    },
    '800:1477': {
        'Custom Portrait': (800, 1477),
    },
    '107:197': {
        'Custom Portrait': (642, 1182),
    },
    '87:160': {
        'Custom Portrait': (870, 1600),
    },
    '640:1177': {
        'Custom Portrait': (1280, 2354),
    },
    '821:1506': {
        'Custom Portrait': (821, 1506),
    },
    '6:11': {
        'Custom Portrait': (1080, 1980),
    },
    '640:1173': {
        'Custom Portrait': (1280, 2346),
    },
    '64:117': {
        'Custom Portrait': (1280, 2340),
    },
    '173:316': {
        'Custom Portrait': (1384, 2528),
    },
    '701:1280': {
        'Custom Portrait': (1402, 2560),
    },
    '320:583': {
        'Custom Portrait': (1280, 2332),
    },
    '11:20': {
        'Custom Portrait': (1056, 1920),
    },
    '1409:2560': {
        'Custom Portrait': (1409, 2560),
    },
    '1280:2309': {
        'Custom Portrait': (1280, 2309),
    },
    '137:247': {
        'Custom Portrait': (548, 988),
    },
    '71:128': {
        'Custom Portrait': (1136, 2048),
    },
    '1421:2560': {
        'Custom Portrait': (1421, 2560),
    },
    '1280:2303': {
        'Custom Portrait': (1280, 2303),
    },
    '1280:2299': {
        'Custom Portrait': (1280, 2299),
    },
    '39:70': {
        'Custom Portrait': (1248, 2240),
    },
    '67:120': {
        'Custom Portrait': (1072, 1920),
    },
    '19:34': {
        'Custom Portrait': (760, 1360),
    },
    '253:452': {
        'Custom Portrait': (759, 1356),
    },
    '93:166': {
        'Custom Portrait': (1488, 2656),
    },
    '143:255': {
        'Custom Portrait': (1144, 2040),
    },
    '359:640': {
        'Custom Portrait': (1436, 2560),
    },
    '32:57': {
        'Custom Portrait': (1024, 1824),
    },
    '600:1067': {
        'Custom Portrait': (1200, 2134),
    },
    '320:569': {
        'Custom Portrait': (1280, 2276),
    },
    '305:542': {
        'Custom Portrait': (1220, 2168),
    },
    '300:533': {
        'Custom Portrait': (300, 533),
    },
    '58:103': {
        'Custom Portrait': (1102, 1957),
    },
    '1280:2273': {
        'Custom Portrait': (1280, 2273),
    },
    '721:1280': {
        'Custom Portrait': (1442, 2560),
    },
    '661:1173': {
        'Custom Portrait': (661, 1173),
    },
    '1139:2021': {
        'Custom Portrait': (1139, 2021),
    },
    '31:55': {
        'Custom Portrait': (1984, 3520),
    },
    '1443:2560': {
        'Custom Portrait': (1443, 2560),
    },
    '219:388': {
        'Custom Portrait': (438, 776),
    },
    '496:877': {
        'Custom Portrait': (992, 1754),
    },
    '1280:2261': {
        'Custom Portrait': (1280, 2261),
    },
    '64:113': {
        'Custom Portrait': (1280, 2260),
    },
    '98:173': {
        'Custom Portrait': (1176, 2076),
    },
    '1280:2259': {
        'Custom Portrait': (1280, 2259),
    },
    '17:30': {
        'Custom Portrait': (1088, 1920),
    },
    '363:640': {
        'Custom Portrait': (1452, 2560),
    },
    '256:451': {
        'Custom Portrait': (1280, 2255),
    },
    '320:563': {
        'Custom Portrait': (1280, 2252),
    },
    '91:160': {
        'Custom Portrait': (1456, 2560),
    },
    '128:225': {
        'Custom Portrait': (2048, 3600),
    },
    '1280:2241': {
        'Custom Portrait': (1280, 2241),
    },
    '4:7': {
        'Custom Portrait': (1536, 2688),
    },
    '1463:2560': {
        'Custom Portrait': (1463, 2560),
    },
    '1280:2239': {
        'Custom Portrait': (1280, 2239),
    },
    '943:1648': {
        'Custom Portrait': (943, 1648),
    },
    '256:447': {
        'Custom Portrait': (1280, 2235),
    },
    '1467:2560': {
        'Custom Portrait': (1467, 2560),
    },
    '1280:2231': {
        'Custom Portrait': (1280, 2231),
    },
    '35:61': {
        'Custom Portrait': (1680, 2928),
    },
    '576:1003': {
        'Custom Portrait': (1152, 2006),
    },
    '1280:2227': {
        'Custom Portrait': (1280, 2227),
    },
    '883:1536': {
        'Custom Portrait': (883, 1536),
    },
    '640:1113': {
        'Custom Portrait': (1280, 2226),
    },
    '369:640': {
        'Custom Portrait': (1476, 2560),
    },
    '739:1280': {
        'Custom Portrait': (1478, 2560),
    },
    '1280:2217': {
        'Custom Portrait': (1280, 2217),
    },
    '256:443': {
        'Custom Portrait': (1280, 2215),
    },
    '289:500': {
        'Custom Portrait': (578, 1000),
    },
    '37:64': {
        'Custom Portrait': (1332, 2304),
    },
    '889:1536': {
        'Custom Portrait': (889, 1536),
    },
    '1280:2211': {
        'Custom Portrait': (1280, 2211),
    },
    '128:221': {
        'Custom Portrait': (1280, 2210),
    },
    '40:69': {
        'Custom Portrait': (1280, 2208),
    },
    '297:512': {
        'Custom Portrait': (1485, 2560),
    },
    '640:1101': {
        'Custom Portrait': (1280, 2202),
    },
    '163:280': {
        'Custom Portrait': (1304, 2240),
    },
    '900:1543': {
        'Custom Portrait': (900, 1543),
    },
    '7:12': {
        'Custom Portrait': (980, 1680),
    },
    '80:137': {
        'Custom Portrait': (800, 1370),
    },
    '128:219': {
        'Custom Portrait': (1280, 2190),
    },
    '320:547': {
        'Custom Portrait': (1280, 2188),
    },
    '103:176': {
        'Custom Portrait': (1648, 2816),
    },
    '557:950': {
        'Custom Portrait': (1114, 1900),
    },
    '1201:2048': {
        'Custom Portrait': (1201, 2048),
    },
    '104:177': {
        'Custom Portrait': (1664, 2832),
    },
    '1280:2177': {
        'Custom Portrait': (1280, 2177),
    },
    '10:17': {
        'Custom Portrait': (1000, 1700),
    },
    '1280:2173': {
        'Custom Portrait': (1280, 2173),
    },
    '1280:2171': {
        'Custom Portrait': (1280, 2171),
    },
    '1511:2560': {
        'Custom Portrait': (1511, 2560),
    },
    '160:271': {
        'Custom Portrait': (1280, 2168),
    },
    '1280:2167': {
        'Custom Portrait': (1280, 2167),
    },
    '94:159': {
        'Custom Portrait': (1504, 2544),
    },
    '256:433': {
        'Custom Portrait': (1280, 2165),
    },
    '1280:2163': {
        'Custom Portrait': (1280, 2163),
    },
    '237:400': {
        'Custom Portrait': (711, 1200),
    },
    '19:32': {
        'Custom Portrait': (608, 1024),
    },
    '1523:2560': {
        'Custom Portrait': (1523, 2560),
    },
    '47:79': {
        'Custom Portrait': (1504, 2528),
    },
    '131:220': {
        'Custom Portrait': (786, 1320),
    },
    '763:1280': {
        'Custom Portrait': (1526, 2560),
    },
    '105:176': {
        'Custom Portrait': (1680, 2816),
    },
    '256:429': {
        'Custom Portrait': (1280, 2145),
    },
    '52:87': {
        'Custom Portrait': (1664, 2784),
    },
    '1225:2048': {
        'Custom Portrait': (1225, 2048),
    },
    '640:1069': {
        'Custom Portrait': (1280, 2138),
    },
    '1533:2560': {
        'Custom Portrait': (1533, 2560),
    },
    '1280:2137': {
        'Custom Portrait': (1280, 2137),
    },
    '640:1067': {
        'Custom Portrait': (1280, 2134),
    },
    '3:5': {
        'Custom Portrait': (720, 1200),
    },
    '1280:2133': {
        'Custom Portrait': (1280, 2133),
    },
    '104:173': {
        'Custom Portrait': (1664, 2768),
    },
    '80:133': {
        'Custom Portrait': (1200, 1995),
    },
    '1541:2560': {
        'Custom Portrait': (1541, 2560),
    },
    '256:425': {
        'Custom Portrait': (1280, 2125),
    },
    '50:83': {
        'Custom Portrait': (1000, 1660),
    },
    '32:53': {
        'Custom Portrait': (1280, 2120),
    },
    '93:154': {
        'Custom Portrait': (1488, 2464),
    },
    '1280:2119': {
        'Custom Portrait': (1280, 2119),
    },
    '95:157': {
        'Custom Portrait': (1520, 2512),
    },
    '1553:2560': {
        'Custom Portrait': (1553, 2560),
    },
    '1280:2109': {
        'Custom Portrait': (1280, 2109),
    },
    '48:79': {
        'Custom Portrait': (1200, 1975),
    },
    '256:421': {
        'Custom Portrait': (1280, 2105),
    },
    '870:1429': {
        'Custom Portrait': (870, 1429),
    },
    '64:105': {
        'Custom Portrait': (512, 840),
    },
    '469:768': {
        'Custom Portrait': (938, 1536),
    },
    '80:131': {
        'Custom Portrait': (1280, 2096),
    },
    '30:49': {
        'Custom Portrait': (720, 1176),
    },
    '49:80': {
        'Custom Portrait': (735, 1200),
    },
    '160:261': {
        'Custom Portrait': (1280, 2088),
    },
    '141:230': {
        'Custom Portrait': (987, 1610),
    },
    '640:1043': {
        'Custom Portrait': (1280, 2086),
    },
    '1280:2081': {
        'Custom Portrait': (1280, 2081),
    },
    '640:1039': {
        'Custom Portrait': (1280, 2078),
    },
    '1280:2077': {
        'Custom Portrait': (1280, 2077),
    },
    '320:519': {
        'Custom Portrait': (1280, 2076),
    },
    '1280:2073': {
        'Custom Portrait': (1280, 2073),
    },
    '247:400': {
        'Custom Portrait': (494, 800),
    },
    '160:259': {
        'Custom Portrait': (1280, 2072),
    },
    '1280:2071': {
        'Custom Portrait': (1280, 2071),
    },
    '633:1024': {
        'Custom Portrait': (1266, 2048),
    },
    '317:512': {
        'Custom Portrait': (1585, 2560),
    },
    '1280:2063': {
        'Custom Portrait': (1280, 2063),
    },
    '640:1031': {
        'Custom Portrait': (1280, 2062),
    },
    '621:1000': {
        'Custom Portrait': (1242, 2000),
    },
    '1280:2059': {
        'Custom Portrait': (1280, 2059),
    },
    '640:1029': {
        'Custom Portrait': (1280, 2058),
    },
    '399:640': {
        'Custom Portrait': (798, 1280),
    },
    '639:1024': {
        'Custom Portrait': (639, 1024),
    },
    '1280:2049': {
        'Custom Portrait': (1280, 2049),
    },
    '5:8': {
        'Custom Portrait': (1280, 2048),
    },
    '256:409': {
        'Custom Portrait': (1280, 2045),
    },
    '783:1250': {
        'Custom Portrait': (783, 1250),
    },
    '516:823': {
        'Custom Portrait': (1032, 1646),
    },
    '550:877': {
        'Custom Portrait': (550, 877),
    },
    '32:51': {
        'Custom Portrait': (1280, 2040),
    },
    '457:727': {
        'Custom Portrait': (457, 727),
    },
    '320:509': {
        'Custom Portrait': (1280, 2036),
    },
    '640:1017': {
        'Custom Portrait': (1280, 2034),
    },
    '1280:2033': {
        'Custom Portrait': (1280, 2033),
    },
    '896:1423': {
        'Custom Portrait': (896, 1423),
    },
    '63:100': {
        'Custom Portrait': (630, 1000),
    },
    '1280:2023': {
        'Custom Portrait': (1280, 2023),
    },
    '81:128': {
        'Custom Portrait': (1620, 2560),
    },
    '240:379': {
        'Custom Portrait': (1200, 1895),
    },
    '1280:2021': {
        'Custom Portrait': (1280, 2021),
    },
    '640:1009': {
        'Custom Portrait': (1280, 2018),
    },
    '40:63': {
        'Custom Portrait': (1280, 2016),
    },
    '1280:2013': {
        'Custom Portrait': (1280, 2013),
    },
    '278:437': {
        'Custom Portrait': (834, 1311),
    },
    '292:459': {
        'Custom Portrait': (876, 1377),
    },
    '1280:2011': {
        'Custom Portrait': (1280, 2011),
    },
    '1273:2000': {
        'Custom Portrait': (1273, 2000),
    },
    '163:256': {
        'Custom Portrait': (1630, 2560),
    },
    '128:201': {
        'Custom Portrait': (1280, 2010),
    },
    '1280:2009': {
        'Custom Portrait': (1280, 2009),
    },
    '160:251': {
        'Custom Portrait': (1280, 2008),
    },
    '653:1024': {
        'Custom Portrait': (1306, 2048),
    },
    '1000:1567': {
        'Custom Portrait': (1000, 1567),
    },
    '613:960': {
        'Custom Portrait': (1226, 1920),
    },
    '1280:2003': {
        'Custom Portrait': (1280, 2003),
    },
    '640:1001': {
        'Custom Portrait': (1280, 2002),
    },
    '655:1024': {
        'Custom Portrait': (1310, 2048),
    },
    '16:25': {
        'Custom Portrait': (768, 1200),
    },
    '411:640': {
        'Custom Portrait': (1644, 2560),
    },
    '70:109': {
        'Custom Portrait': (700, 1090),
    },
    '160:249': {
        'Custom Portrait': (1280, 1992),
    },
    '1280:1991': {
        'Custom Portrait': (1280, 1991),
    },
    '1280:1989': {
        'Custom Portrait': (1280, 1989),
    },
    '65:101': {
        'Custom Portrait': (1040, 1616),
    },
    '700:1087': {
        'Custom Portrait': (700, 1087),
    },
    '256:397': {
        'Custom Portrait': (1280, 1985),
    },
    '640:991': {
        'Custom Portrait': (1280, 1982),
    },
    '560:867': {
        'Custom Portrait': (1120, 1734),
    },
    '1280:1981': {
        'Custom Portrait': (1280, 1981),
    },
    '497:768': {
        'Custom Portrait': (1491, 2304),
    },
    '1280:1977': {
        'Custom Portrait': (1280, 1977),
    },
    '406:627': {
        'Custom Portrait': (1218, 1881),
    },
    '160:247': {
        'Custom Portrait': (1280, 1976),
    },
    '425:656': {
        'Custom Portrait': (850, 1312),
    },
    '1036:1599': {
        'Custom Portrait': (1036, 1599),
    },
    '1280:1973': {
        'Custom Portrait': (1280, 1973),
    },
    '1280:1971': {
        'Custom Portrait': (1280, 1971),
    },
    '1600:2463': {
        'Custom Portrait': (1600, 2463),
    },
    '1280:1967': {
        'Custom Portrait': (1280, 1967),
    },
    '640:983': {
        'Custom Portrait': (1280, 1966),
    },
    '256:393': {
        'Custom Portrait': (1280, 1965),
    },
    '320:491': {
        'Custom Portrait': (1280, 1964),
    },
    '163:250': {
        'Custom Portrait': (815, 1250),
    },
    '979:1500': {
        'Custom Portrait': (979, 1500),
    },
    '1280:1961': {
        'Custom Portrait': (1280, 1961),
    },
    '209:320': {
        'Custom Portrait': (1672, 2560),
    },
    '523:800': {
        'Custom Portrait': (523, 800),
    },
    '17:26': {
        'Custom Portrait': (952, 1456),
    },
    '1280:1951': {
        'Custom Portrait': (1280, 1951),
    },
    '21:32': {
        'Custom Portrait': (672, 1024),
    },
    '193:294': {
        'Custom Portrait': (1158, 1764),
    },
    '1280:1949': {
        'Custom Portrait': (1280, 1949),
    },
    '320:487': {
        'Custom Portrait': (1280, 1948),
    },
    '263:400': {
        'Custom Portrait': (789, 1200),
    },
    '1243:1890': {
        'Custom Portrait': (1243, 1890),
    },
    '171:260': {
        'Custom Portrait': (1368, 2080),
    },
    '25:38': {
        'Custom Portrait': (1000, 1520),
    },
    '1621:2463': {
        'Custom Portrait': (1621, 2463),
    },
    '160:243': {
        'Custom Portrait': (1280, 1944),
    },
    '600:911': {
        'Custom Portrait': (1200, 1822),
    },
    '1280:1943': {
        'Custom Portrait': (1280, 1943),
    },
    '118:179': {
        'Custom Portrait': (944, 1432),
    },
    '1280:1941': {
        'Custom Portrait': (1280, 1941),
    },
    '80:121': {
        'Custom Portrait': (1280, 1936),
    },
    '853:1290': {
        'Custom Portrait': (853, 1290),
    },
    '127:192': {
        'Custom Portrait': (508, 768),
    },
    '640:967': {
        'Custom Portrait': (1280, 1934),
    },
    '339:512': {
        'Custom Portrait': (678, 1024),
    },
    '104:157': {
        'Custom Portrait': (832, 1256),
    },
    '320:483': {
        'Custom Portrait': (1280, 1932),
    },
    '108:163': {
        'Custom Portrait': (864, 1304),
    },
    '57:86': {
        'Custom Portrait': (912, 1376),
    },
    '800:1207': {
        'Custom Portrait': (800, 1207),
    },
    '1280:1931': {
        'Custom Portrait': (1280, 1931),
    },
    '73:110': {
        'Custom Portrait': (730, 1100),
    },
    '1699:2560': {
        'Custom Portrait': (1699, 2560),
    },
    '152:229': {
        'Custom Portrait': (1216, 1832),
    },
    '85:128': {
        'Custom Portrait': (1360, 2048),
    },
    '1280:1927': {
        'Custom Portrait': (1280, 1927),
    },
    '833:1254': {
        'Custom Portrait': (833, 1254),
    },
    '640:963': {
        'Custom Portrait': (1280, 1926),
    },
    '107:161': {
        'Custom Portrait': (1712, 2576),
    },
    '121:182': {
        'Custom Portrait': (968, 1456),
    },
    '851:1280': {
        'Custom Portrait': (1702, 2560),
    },
    '123:185': {
        'Custom Portrait': (984, 1480),
    },
    '256:385': {
        'Custom Portrait': (1280, 1925),
    },
    '133:200': {
        'Custom Portrait': (665, 1000),
    },
    '153:230': {
        'Custom Portrait': (1224, 1840),
    },
    '1703:2560': {
        'Custom Portrait': (1703, 2560),
    },
    '165:248': {
        'Custom Portrait': (165, 248),
    },
    '169:254': {
        'Custom Portrait': (1352, 2032),
    },
    '213:320': {
        'Custom Portrait': (1704, 2560),
    },
    '1280:1923': {
        'Custom Portrait': (1280, 1923),
    },
    '947:1422': {
        'Custom Portrait': (947, 1422),
    },
    '533:800': {
        'Custom Portrait': (533, 800),
    },
    '851:1277': {
        'Custom Portrait': (1702, 2554),
    },
    '1365:2048': {
        'Custom Portrait': (1365, 2048),
    },
    '2:3': {
        'Custom Portrait': (800, 1200),
    },
    '1843:2764': {
        'Custom Portrait': (1843, 2764),
    },
    '1707:2560': {
        'Custom Portrait': (1707, 2560),
    },
    '683:1024': {
        'Custom Portrait': (683, 1024),
    },
    '667:1000': {
        'Custom Portrait': (667, 1000),
    },
    '1280:1919': {
        'Custom Portrait': (1280, 1919),
    },
    '612:917': {
        'Custom Portrait': (612, 917),
    },
    '211:316': {
        'Custom Portrait': (1688, 2528),
    },
    '827:1238': {
        'Custom Portrait': (827, 1238),
    },
    '163:244': {
        'Custom Portrait': (1304, 1952),
    },
    '139:208': {
        'Custom Portrait': (1112, 1664),
    },
    '115:172': {
        'Custom Portrait': (920, 1376),
    },
    '414:619': {
        'Custom Portrait': (1656, 2476),
    },
    '97:145': {
        'Custom Portrait': (776, 1160),
    },
    '1713:2560': {
        'Custom Portrait': (1713, 2560),
    },
    '87:130': {
        'Custom Portrait': (1392, 2080),
    },
    '75:112': {
        'Custom Portrait': (1200, 1792),
    },
    '1000:1493': {
        'Custom Portrait': (2000, 2986),
    },
    '67:100': {
        'Custom Portrait': (670, 1000),
    },
    '128:191': {
        'Custom Portrait': (1280, 1910),
    },
    '175:261': {
        'Custom Portrait': (1400, 2088),
    },
    '1280:1909': {
        'Custom Portrait': (1280, 1909),
    },
    '503:750': {
        'Custom Portrait': (1006, 1500),
    },
    '1477:2202': {
        'Custom Portrait': (1477, 2202),
    },
    '100:149': {
        'Custom Portrait': (800, 1192),
    },
    '1280:1907': {
        'Custom Portrait': (1280, 1907),
    },
    '640:953': {
        'Custom Portrait': (1280, 1906),
    },
    '403:600': {
        'Custom Portrait': (806, 1200),
    },
    '80:119': {
        'Custom Portrait': (1280, 1904),
    },
    '39:58': {
        'Custom Portrait': (624, 928),
    },
    '1280:1903': {
        'Custom Portrait': (1280, 1903),
    },
    '37:55': {
        'Custom Portrait': (1184, 1760),
    },
    '640:951': {
        'Custom Portrait': (1280, 1902),
    },
    '35:52': {
        'Custom Portrait': (700, 1040),
    },
    '1280:1901': {
        'Custom Portrait': (1280, 1901),
    },
    '200:297': {
        'Custom Portrait': (1000, 1485),
    },
    '828:1229': {
        'Custom Portrait': (828, 1229),
    },
    '700:1039': {
        'Custom Portrait': (700, 1039),
    },
    '345:512': {
        'Custom Portrait': (1725, 2560),
    },
    '768:1139': {
        'Custom Portrait': (1536, 2278),
    },
    '640:949': {
        'Custom Portrait': (1280, 1898),
    },
    '1280:1897': {
        'Custom Portrait': (1280, 1897),
    },
    '160:237': {
        'Custom Portrait': (1280, 1896),
    },
    '256:379': {
        'Custom Portrait': (1280, 1895),
    },
    '1181:1748': {
        'Custom Portrait': (1181, 1748),
    },
    '25:37': {
        'Custom Portrait': (1600, 2368),
    },
    '640:947': {
        'Custom Portrait': (1280, 1894),
    },
    '1217:1800': {
        'Custom Portrait': (1217, 1800),
    },
    '165:244': {
        'Custom Portrait': (825, 1220),
    },
    '1352:1999': {
        'Custom Portrait': (1352, 1999),
    },
    '320:473': {
        'Custom Portrait': (1280, 1892),
    },
    '500:739': {
        'Custom Portrait': (1000, 1478),
    },
    '203:300': {
        'Custom Portrait': (609, 900),
    },
    '677:1000': {
        'Custom Portrait': (677, 1000),
    },
    '65:96': {
        'Custom Portrait': (1040, 1536),
    },
    '1126:1663': {
        'Custom Portrait': (1126, 1663),
    },
    '128:189': {
        'Custom Portrait': (1280, 1890),
    },
    '1280:1889': {
        'Custom Portrait': (1280, 1889),
    },
    '407:600': {
        'Custom Portrait': (814, 1200),
    },
    '640:943': {
        'Custom Portrait': (1280, 1886),
    },
    '320:471': {
        'Custom Portrait': (1280, 1884),
    },
    '1280:1883': {
        'Custom Portrait': (1280, 1883),
    },
    '632:929': {
        'Custom Portrait': (632, 929),
    },
    '1280:1881': {
        'Custom Portrait': (1280, 1881),
    },
    '32:47': {
        'Custom Portrait': (1024, 1504),
    },
    '1743:2560': {
        'Custom Portrait': (1743, 2560),
    },
    '1280:1877': {
        'Custom Portrait': (1280, 1877),
    },
    '2000:2931': {
        'Custom Portrait': (2000, 2931),
    },
    '437:640': {
        'Custom Portrait': (874, 1280),
    },
    '1093:1600': {
        'Custom Portrait': (1093, 1600),
    },
    '831:1216': {
        'Custom Portrait': (831, 1216),
    },
    '749:1096': {
        'Custom Portrait': (749, 1096),
    },
    '1280:1873': {
        'Custom Portrait': (1280, 1873),
    },
    '80:117': {
        'Custom Portrait': (1280, 1872),
    },
    '1751:2560': {
        'Custom Portrait': (1751, 2560),
    },
    '288:421': {
        'Custom Portrait': (1440, 2105),
    },
    '1280:1871': {
        'Custom Portrait': (1280, 1871),
    },
    '13:19': {
        'Custom Portrait': (1664, 2432),
    },
    '1472:2151': {
        'Custom Portrait': (1472, 2151),
    },
    '800:1169': {
        'Custom Portrait': (1600, 2338),
    },
    '219:320': {
        'Custom Portrait': (1752, 2560),
    },
    '128:187': {
        'Custom Portrait': (1280, 1870),
    },
    '137:200': {
        'Custom Portrait': (822, 1200),
    },
    '535:781': {
        'Custom Portrait': (1070, 1562),
    },
    '1280:1867': {
        'Custom Portrait': (1280, 1867),
    },
    '24:35': {
        'Custom Portrait': (960, 1400),
    },
    '1024:1493': {
        'Custom Portrait': (1024, 1493),
    },
    '640:933': {
        'Custom Portrait': (1280, 1866),
    },
    '256:373': {
        'Custom Portrait': (1280, 1865),
    },
    '160:233': {
        'Custom Portrait': (1280, 1864),
    },
    '687:1000': {
        'Custom Portrait': (687, 1000),
    },
    '11:16': {
        'Custom Portrait': (385, 560),
    },
    '350:509': {
        'Custom Portrait': (700, 1018),
    },
    '86:125': {
        'Custom Portrait': (688, 1000),
    },
    '42:61': {
        'Custom Portrait': (1344, 1952),
    },
    '640:929': {
        'Custom Portrait': (1280, 1858),
    },
    '144:209': {
        'Custom Portrait': (720, 1045),
    },
    '512:743': {
        'Custom Portrait': (512, 743),
    },
    '397:576': {
        'Custom Portrait': (1588, 2304),
    },
    '1280:1857': {
        'Custom Portrait': (1280, 1857),
    },
    '850:1233': {
        'Custom Portrait': (850, 1233),
    },
    '1081:1568': {
        'Custom Portrait': (1081, 1568),
    },
    '704:1021': {
        'Custom Portrait': (1408, 2042),
    },
    '864:1253': {
        'Custom Portrait': (1728, 2506),
    },
    '602:873': {
        'Custom Portrait': (1204, 1746),
    },
    '20:29': {
        'Custom Portrait': (1280, 1856),
    },
    '1449:2101': {
        'Custom Portrait': (1449, 2101),
    },
    '958:1389': {
        'Custom Portrait': (958, 1389),
    },
    '425:616': {
        'Custom Portrait': (850, 1232),
    },
    '1413:2048': {
        'Custom Portrait': (1413, 2048),
    },
    '701:1016': {
        'Custom Portrait': (1402, 2032),
    },
    '69:100': {
        'Custom Portrait': (828, 1200),
    },
    '265:384': {
        'Custom Portrait': (1060, 1536),
    },
    '205:297': {
        'Custom Portrait': (410, 594),
    },
    '640:927': {
        'Custom Portrait': (1280, 1854),
    },
    '221:320': {
        'Custom Portrait': (1768, 2560),
    },
    '259:375': {
        'Custom Portrait': (1036, 1500),
    },
    '1360:1969': {
        'Custom Portrait': (1360, 1969),
    },
    '829:1200': {
        'Custom Portrait': (829, 1200),
    },
    '38:55': {
        'Custom Portrait': (1140, 1650),
    },
    '320:463': {
        'Custom Portrait': (1280, 1852),
    },
    '177:256': {
        'Custom Portrait': (1770, 2560),
    },
    '1280:1851': {
        'Custom Portrait': (1280, 1851),
    },
    '200:289': {
        'Custom Portrait': (600, 867),
    },
    '1280:1849': {
        'Custom Portrait': (1280, 1849),
    },
    '9:13': {
        'Custom Portrait': (1728, 2496),
    },
    '1200:1733': {
        'Custom Portrait': (1200, 1733),
    },
    '1063:1535': {
        'Custom Portrait': (1063, 1535),
    },
    '250:361': {
        'Custom Portrait': (500, 722),
    },
    '160:231': {
        'Custom Portrait': (1280, 1848),
    },
    '850:1227': {
        'Custom Portrait': (850, 1227),
    },
    '1280:1847': {
        'Custom Portrait': (1280, 1847),
    },
    '61:88': {
        'Custom Portrait': (1464, 2112),
    },
    '839:1210': {
        'Custom Portrait': (839, 1210),
    },
    '256:369': {
        'Custom Portrait': (1280, 1845),
    },
    '833:1200': {
        'Custom Portrait': (833, 1200),
    },
    '1102:1587': {
        'Custom Portrait': (1102, 1587),
    },
    '1280:1843': {
        'Custom Portrait': (1280, 1843),
    },
    '640:921': {
        'Custom Portrait': (1280, 1842),
    },
    '16:23': {
        'Custom Portrait': (1280, 1840),
    },
    '1280:1839': {
        'Custom Portrait': (1280, 1839),
    },
    '557:800': {
        'Custom Portrait': (557, 800),
    },
    '640:919': {
        'Custom Portrait': (1280, 1838),
    },
    '225:323': {
        'Custom Portrait': (900, 1292),
    },
    '209:300': {
        'Custom Portrait': (1045, 1500),
    },
    '1280:1837': {
        'Custom Portrait': (1280, 1837),
    },
    '320:459': {
        'Custom Portrait': (1280, 1836),
    },
    '500:717': {
        'Custom Portrait': (500, 717),
    },
    '256:367': {
        'Custom Portrait': (1280, 1835),
    },
    '30:43': {
        'Custom Portrait': (1200, 1720),
    },
    '425:609': {
        'Custom Portrait': (850, 1218),
    },
    '1800:2579': {
        'Custom Portrait': (1800, 2579),
    },
    '1280:1833': {
        'Custom Portrait': (1280, 1833),
    },
    '160:229': {
        'Custom Portrait': (1280, 1832),
    },
    '1789:2560': {
        'Custom Portrait': (1789, 2560),
    },
    '1280:1831': {
        'Custom Portrait': (1280, 1831),
    },
    '100:143': {
        'Custom Portrait': (500, 715),
    },
    '1399:2000': {
        'Custom Portrait': (1399, 2000),
    },
    '1280:1829': {
        'Custom Portrait': (1280, 1829),
    },
    '7:10': {
        'Custom Portrait': (448, 640),
    },
    '717:1024': {
        'Custom Portrait': (1434, 2048),
    },
    '320:457': {
        'Custom Portrait': (1280, 1828),
    },
    '1535:2192': {
        'Custom Portrait': (1535, 2192),
    },
    '145:207': {
        'Custom Portrait': (1160, 1656),
    },
    '239:341': {
        'Custom Portrait': (717, 1023),
    },
    '68:97': {
        'Custom Portrait': (952, 1358),
    },
    '256:365': {
        'Custom Portrait': (256, 365),
    },
    '40:57': {
        'Custom Portrait': (1280, 1824),
    },
    '1280:1823': {
        'Custom Portrait': (1280, 1823),
    },
    '158:225': {
        'Custom Portrait': (632, 900),
    },
    '281:400': {
        'Custom Portrait': (1124, 1600),
    },
    '640:911': {
        'Custom Portrait': (1280, 1822),
    },
    '1799:2560': {
        'Custom Portrait': (1799, 2560),
    },
    '1280:1821': {
        'Custom Portrait': (1280, 1821),
    },
    '703:1000': {
        'Custom Portrait': (703, 1000),
    },
    '45:64': {
        'Custom Portrait': (720, 1024),
    },
    '211:300': {
        'Custom Portrait': (844, 1200),
    },
    '1071:1522': {
        'Custom Portrait': (1071, 1522),
    },
    '1280:1819': {
        'Custom Portrait': (1280, 1819),
    },
    '1247:1772': {
        'Custom Portrait': (1247, 1772),
    },
    '1000:1421': {
        'Custom Portrait': (1000, 1421),
    },
    '563:800': {
        'Custom Portrait': (1126, 1600),
    },
    '640:909': {
        'Custom Portrait': (1280, 1818),
    },
    '1040:1477': {
        'Custom Portrait': (1040, 1477),
    },
    '1280:1817': {
        'Custom Portrait': (1280, 1817),
    },
    '1057:1500': {
        'Custom Portrait': (1057, 1500),
    },
    '160:227': {
        'Custom Portrait': (1280, 1816),
    },
    '600:851': {
        'Custom Portrait': (600, 851),
    },
    '361:512': {
        'Custom Portrait': (1805, 2560),
    },
    '1440:2041': {
        'Custom Portrait': (1440, 2041),
    },
    '640:907': {
        'Custom Portrait': (1280, 1814),
    },
    '1062:1505': {
        'Custom Portrait': (1062, 1505),
    },
    '353:500': {
        'Custom Portrait': (706, 1000),
    },
    '1280:1813': {
        'Custom Portrait': (1280, 1813),
    },
    '723:1024': {
        'Custom Portrait': (723, 1024),
    },
    '113:160': {
        'Custom Portrait': (1017, 1440),
    },
    '320:453': {
        'Custom Portrait': (1280, 1812),
    },
    '450:637': {
        'Custom Portrait': (900, 1274),
    },
    '53:75': {
        'Custom Portrait': (848, 1200),
    },
    '200:283': {
        'Custom Portrait': (800, 1132),
    },
    '347:491': {
        'Custom Portrait': (694, 982),
    },
    '827:1170': {
        'Custom Portrait': (827, 1170),
    },
    '1131:1600': {
        'Custom Portrait': (1131, 1600),
    },
    '620:877': {
        'Custom Portrait': (1240, 1754),
    },
    '900:1273': {
        'Custom Portrait': (900, 1273),
    },
    '707:1000': {
        'Custom Portrait': (707, 1000),
    },
    '852:1205': {
        'Custom Portrait': (852, 1205),
    },
    '992:1403': {
        'Custom Portrait': (992, 1403),
    },
    '70:99': {
        'Custom Portrait': (700, 990),
    },
    '1200:1697': {
        'Custom Portrait': (1200, 1697),
    },
    '99:140': {
        'Custom Portrait': (990, 1400),
    },
    '425:601': {
        'Custom Portrait': (850, 1202),
    },
    '128:181': {
        'Custom Portrait': (1280, 1810),
    },
    '29:41': {
        'Custom Portrait': (580, 820),
    },
    '1061:1500': {
        'Custom Portrait': (1061, 1500),
    },
    '800:1131': {
        'Custom Portrait': (800, 1131),
    },
    '283:400': {
        'Custom Portrait': (1415, 2000),
    },
    '1280:1809': {
        'Custom Portrait': (1280, 1809),
    },
    '1024:1447': {
        'Custom Portrait': (1024, 1447),
    },
    '707:999': {
        'Custom Portrait': (707, 999),
    },
    '1000:1413': {
        'Custom Portrait': (1000, 1413),
    },
    '1189:1680': {
        'Custom Portrait': (1189, 1680),
    },
    '155:219': {
        'Custom Portrait': (620, 876),
    },
    '637:900': {
        'Custom Portrait': (637, 900),
    },
    '63:89': {
        'Custom Portrait': (630, 890),
    },
    '80:113': {
        'Custom Portrait': (800, 1130),
    },
    '177:250': {
        'Custom Portrait': (1062, 1500),
    },
    '725:1024': {
        'Custom Portrait': (725, 1024),
    },
    '114:161': {
        'Custom Portrait': (1254, 1771),
    },
    '376:531': {
        'Custom Portrait': (752, 1062),
    },
    '1133:1600': {
        'Custom Portrait': (1133, 1600),
    },
    '1075:1518': {
        'Custom Portrait': (1075, 1518),
    },
    '250:353': {
        'Custom Portrait': (1000, 1412),
    },
    '1280:1807': {
        'Custom Portrait': (1280, 1807),
    },
    '600:847': {
        'Custom Portrait': (600, 847),
    },
    '192:271': {
        'Custom Portrait': (768, 1084),
    },
    '688:971': {
        'Custom Portrait': (688, 971),
    },
    '800:1129': {
        'Custom Portrait': (800, 1129),
    },
    '256:361': {
        'Custom Portrait': (1280, 1805),
    },
    '227:320': {
        'Custom Portrait': (1135, 1600),
    },
    '310:437': {
        'Custom Portrait': (1240, 1748),
    },
    '1280:1803': {
        'Custom Portrait': (1280, 1803),
    },
    '404:569': {
        'Custom Portrait': (1616, 2276),
    },
    '125:176': {
        'Custom Portrait': (1000, 1408),
    },
    '640:901': {
        'Custom Portrait': (1280, 1802),
    },
    '606:853': {
        'Custom Portrait': (1212, 1706),
    },
    '1280:1801': {
        'Custom Portrait': (1280, 1801),
    },
    '853:1200': {
        'Custom Portrait': (853, 1200),
    },
    '32:45': {
        'Custom Portrait': (1280, 1800),
    },
    '293:412': {
        'Custom Portrait': (586, 824),
    },
    '1280:1799': {
        'Custom Portrait': (1280, 1799),
    },
    '89:125': {
        'Custom Portrait': (1068, 1500),
    },
    '240:337': {
        'Custom Portrait': (480, 674),
    },
    '57:80': {
        'Custom Portrait': (570, 800),
    },
    '62:87': {
        'Custom Portrait': (744, 1044),
    },
    '320:449': {
        'Custom Portrait': (1280, 1796),
    },
    '1000:1403': {
        'Custom Portrait': (1000, 1403),
    },
    '713:1000': {
        'Custom Portrait': (713, 1000),
    },
    '256:359': {
        'Custom Portrait': (1280, 1795),
    },
    '1141:1600': {
        'Custom Portrait': (1141, 1600),
    },
    '600:841': {
        'Custom Portrait': (1200, 1682),
    },
    '800:1121': {
        'Custom Portrait': (800, 1121),
    },
    '357:500': {
        'Custom Portrait': (357, 500),
    },
    '5:7': {
        'Custom Portrait': (1280, 1792),
    },
    '643:900': {
        'Custom Portrait': (643, 900),
    },
    '1280:1791': {
        'Custom Portrait': (1280, 1791),
    },
    '1000:1399': {
        'Custom Portrait': (1000, 1399),
    },
    '800:1119': {
        'Custom Portrait': (800, 1119),
    },
    '311:435': {
        'Custom Portrait': (1244, 1740),
    },
    '1066:1491': {
        'Custom Portrait': (1066, 1491),
    },
    '128:179': {
        'Custom Portrait': (1280, 1790),
    },
    '108:151': {
        'Custom Portrait': (648, 906),
    },
    '425:594': {
        'Custom Portrait': (850, 1188),
    },
    '350:489': {
        'Custom Portrait': (700, 978),
    },
    '227:317': {
        'Custom Portrait': (227, 317),
    },
    '48:67': {
        'Custom Portrait': (1200, 1675),
    },
    '448:625': {
        'Custom Portrait': (896, 1250),
    },
    '1200:1673': {
        'Custom Portrait': (1200, 1673),
    },
    '33:46': {
        'Custom Portrait': (1056, 1472),
    },
    '359:500': {
        'Custom Portrait': (718, 1000),
    },
    '640:891': {
        'Custom Portrait': (1280, 1782),
    },
    '686:955': {
        'Custom Portrait': (686, 955),
    },
    '1200:1669': {
        'Custom Portrait': (1200, 1669),
    },
    '64:89': {
        'Custom Portrait': (1280, 1780),
    },
    '1280:1779': {
        'Custom Portrait': (1280, 1779),
    },
    '18:25': {
        'Custom Portrait': (720, 1000),
    },
    '139:193': {
        'Custom Portrait': (1112, 1544),
    },
    '256:355': {
        'Custom Portrait': (1280, 1775),
    },
    '640:887': {
        'Custom Portrait': (1280, 1774),
    },
    '633:877': {
        'Custom Portrait': (633, 877),
    },
    '361:500': {
        'Custom Portrait': (722, 1000),
    },
    '13:18': {
        'Custom Portrait': (1144, 1584),
    },
    '1135:1569': {
        'Custom Portrait': (1135, 1569),
    },
    '199:275': {
        'Custom Portrait': (796, 1100),
    },
    '765:1057': {
        'Custom Portrait': (765, 1057),
    },
    '160:221': {
        'Custom Portrait': (1280, 1768),
    },
    '712:983': {
        'Custom Portrait': (712, 983),
    },
    '877:1210': {
        'Custom Portrait': (877, 1210),
    },
    '29:40': {
        'Custom Portrait': (406, 560),
    },
    '256:353': {
        'Custom Portrait': (1280, 1765),
    },
    '37:51': {
        'Custom Portrait': (629, 867),
    },
    '320:441': {
        'Custom Portrait': (1280, 1764),
    },
    '127:175': {
        'Custom Portrait': (1270, 1750),
    },
    '363:500': {
        'Custom Portrait': (726, 1000),
    },
    '1280:1763': {
        'Custom Portrait': (1280, 1763),
    },
    '640:881': {
        'Custom Portrait': (1280, 1762),
    },
    '93:128': {
        'Custom Portrait': (930, 1280),
    },
    '1280:1761': {
        'Custom Portrait': (1280, 1761),
    },
    '8:11': {
        'Custom Portrait': (1024, 1408),
    },
    '931:1280': {
        'Custom Portrait': (1862, 2560),
    },
    '1280:1759': {
        'Custom Portrait': (1280, 1759),
    },
    '139:191': {
        'Custom Portrait': (1112, 1528),
    },
    '640:879': {
        'Custom Portrait': (1280, 1758),
    },
    '59:81': {
        'Custom Portrait': (1416, 1944),
    },
    '1280:1757': {
        'Custom Portrait': (1280, 1757),
    },
    '320:439': {
        'Custom Portrait': (1280, 1756),
    },
    '256:351': {
        'Custom Portrait': (1280, 1755),
    },
    '467:640': {
        'Custom Portrait': (934, 1280),
    },
    '27:37': {
        'Custom Portrait': (864, 1184),
    },
    '1280:1753': {
        'Custom Portrait': (1280, 1753),
    },
    '65:89': {
        'Custom Portrait': (1040, 1424),
    },
    '160:219': {
        'Custom Portrait': (1280, 1752),
    },
    '850:1163': {
        'Custom Portrait': (850, 1163),
    },
    '1280:1751': {
        'Custom Portrait': (1280, 1751),
    },
    '128:175': {
        'Custom Portrait': (1024, 1400),
    },
    '800:1093': {
        'Custom Portrait': (800, 1093),
    },
    '137:187': {
        'Custom Portrait': (1096, 1496),
    },
    '1280:1747': {
        'Custom Portrait': (1280, 1747),
    },
    '225:307': {
        'Custom Portrait': (900, 1228),
    },
    '11:15': {
        'Custom Portrait': (1144, 1560),
    },
    '80:109': {
        'Custom Portrait': (1280, 1744),
    },
    '147:200': {
        'Custom Portrait': (1176, 1600),
    },
    '1000:1359': {
        'Custom Portrait': (1000, 1359),
    },
    '471:640': {
        'Custom Portrait': (1884, 2560),
    },
    '92:125': {
        'Custom Portrait': (736, 1000),
    },
    '640:869': {
        'Custom Portrait': (1280, 1738),
    },
    '14:19': {
        'Custom Portrait': (1400, 1900),
    },
    '1280:1737': {
        'Custom Portrait': (1280, 1737),
    },
    '369:500': {
        'Custom Portrait': (738, 1000),
    },
    '640:867': {
        'Custom Portrait': (1280, 1734),
    },
    '500:677': {
        'Custom Portrait': (1000, 1354),
    },
    '1280:1733': {
        'Custom Portrait': (1280, 1733),
    },
    '133:180': {
        'Custom Portrait': (665, 900),
    },
    '320:433': {
        'Custom Portrait': (1280, 1732),
    },
    '360:487': {
        'Custom Portrait': (720, 974),
    },
    '190:257': {
        'Custom Portrait': (1520, 2056),
    },
    '128:173': {
        'Custom Portrait': (1280, 1730),
    },
    '37:50': {
        'Custom Portrait': (888, 1200),
    },
    '1280:1729': {
        'Custom Portrait': (1280, 1729),
    },
    '20:27': {
        'Custom Portrait': (800, 1080),
    },
    '263:355': {
        'Custom Portrait': (789, 1065),
    },
    '1280:1727': {
        'Custom Portrait': (1280, 1727),
    },
    '949:1280': {
        'Custom Portrait': (1898, 2560),
    },
    '640:863': {
        'Custom Portrait': (1280, 1726),
    },
    '256:345': {
        'Custom Portrait': (1280, 1725),
    },
    '75:101': {
        'Custom Portrait': (1200, 1616),
    },
    '1280:1723': {
        'Custom Portrait': (1280, 1723),
    },
    '640:861': {
        'Custom Portrait': (1280, 1722),
    },
    '942:1267': {
        'Custom Portrait': (942, 1267),
    },
    '32:43': {
        'Custom Portrait': (800, 1075),
    },
    '521:700': {
        'Custom Portrait': (1042, 1400),
    },
    '149:200': {
        'Custom Portrait': (894, 1200),
    },
    '640:859': {
        'Custom Portrait': (1280, 1718),
    },
    '320:429': {
        'Custom Portrait': (1280, 1716),
    },
    '373:500': {
        'Custom Portrait': (746, 1000),
    },
    '97:130': {
        'Custom Portrait': (970, 1300),
    },
    '62:83': {
        'Custom Portrait': (992, 1328),
    },
    '827:1107': {
        'Custom Portrait': (827, 1107),
    },
    '65:87': {
        'Custom Portrait': (1040, 1392),
    },
    '600:803': {
        'Custom Portrait': (1200, 1606),
    },
    '1280:1713': {
        'Custom Portrait': (1280, 1713),
    },
    '234:313': {
        'Custom Portrait': (936, 1252),
    },
    '1280:1709': {
        'Custom Portrait': (1280, 1709),
    },
    '320:427': {
        'Custom Portrait': (1280, 1708),
    },
    '973:1298': {
        'Custom Portrait': (973, 1298),
    },
    '1013:1351': {
        'Custom Portrait': (1013, 1351),
    },
    '1280:1707': {
        'Custom Portrait': (1280, 1707),
    },
    '3:4': {
        'Custom Portrait': (165, 220),
    },
    '1126:1501': {
        'Custom Portrait': (1126, 1501),
    },
    '850:1133': {
        'Custom Portrait': (850, 1133),
    },
    '700:933': {
        'Custom Portrait': (700, 933),
    },
    '256:341': {
        'Custom Portrait': (1280, 1705),
    },
    '250:333': {
        'Custom Portrait': (500, 666),
    },
    '160:213': {
        'Custom Portrait': (1280, 1704),
    },
    '1280:1703': {
        'Custom Portrait': (1280, 1703),
    },
    '94:125': {
        'Custom Portrait': (752, 1000),
    },
    '489:650': {
        'Custom Portrait': (978, 1300),
    },
    '1280:1701': {
        'Custom Portrait': (1280, 1701),
    },
    '64:85': {
        'Custom Portrait': (1024, 1360),
    },
    '1280:1697': {
        'Custom Portrait': (1280, 1697),
    },
    '981:1300': {
        'Custom Portrait': (981, 1300),
    },
    '256:339': {
        'Custom Portrait': (1280, 1695),
    },
    '967:1280': {
        'Custom Portrait': (1934, 2560),
    },
    '320:423': {
        'Custom Portrait': (1280, 1692),
    },
    '1280:1691': {
        'Custom Portrait': (1280, 1691),
    },
    '757:1000': {
        'Custom Portrait': (757, 1000),
    },
    '128:169': {
        'Custom Portrait': (1280, 1690),
    },
    '25:33': {
        'Custom Portrait': (750, 990),
    },
    '1280:1689': {
        'Custom Portrait': (1280, 1689),
    },
    '160:211': {
        'Custom Portrait': (1280, 1688),
    },
    '256:337': {
        'Custom Portrait': (1280, 1685),
    },
    '250:329': {
        'Custom Portrait': (1000, 1316),
    },
    '2048:2695': {
        'Custom Portrait': (2048, 2695),
    },
    '19:25': {
        'Custom Portrait': (1216, 1600),
    },
    '320:421': {
        'Custom Portrait': (1280, 1684),
    },
    '640:841': {
        'Custom Portrait': (1280, 1682),
    },
    '195:256': {
        'Custom Portrait': (1950, 2560),
    },
    '16:21': {
        'Custom Portrait': (1280, 1680),
    },
    '1563:2048': {
        'Custom Portrait': (1563, 2048),
    },
    '1280:1677': {
        'Custom Portrait': (1280, 1677),
    },
    '49:64': {
        'Custom Portrait': (1960, 2560),
    },
    '1540:2011': {
        'Custom Portrait': (1540, 2011),
    },
    '1280:1671': {
        'Custom Portrait': (1280, 1671),
    },
    '721:941': {
        'Custom Portrait': (721, 941),
    },
    '613:800': {
        'Custom Portrait': (613, 800),
    },
    '1280:1669': {
        'Custom Portrait': (1280, 1669),
    },
    '307:400': {
        'Custom Portrait': (921, 1200),
    },
    '1280:1667': {
        'Custom Portrait': (1280, 1667),
    },
    '1997:2599': {
        'Custom Portrait': (1997, 2599),
    },
    '769:1000': {
        'Custom Portrait': (769, 1000),
    },
    '423:550': {
        'Custom Portrait': (846, 1100),
    },
    '10:13': {
        'Custom Portrait': (1280, 1664),
    },
    '577:750': {
        'Custom Portrait': (1154, 1500),
    },
    '1280:1663': {
        'Custom Portrait': (1280, 1663),
    },
    '77:100': {
        'Custom Portrait': (1155, 1500),
    },
    '640:831': {
        'Custom Portrait': (1280, 1662),
    },
    '37:48': {
        'Custom Portrait': (1480, 1920),
    },
    '64:83': {
        'Custom Portrait': (2048, 2656),
    },
    '987:1280': {
        'Custom Portrait': (1974, 2560),
    },
    '160:207': {
        'Custom Portrait': (1280, 1656),
    },
    '358:463': {
        'Custom Portrait': (716, 926),
    },
    '256:331': {
        'Custom Portrait': (1280, 1655),
    },
    '387:500': {
        'Custom Portrait': (1161, 1500),
    },
    '1280:1653': {
        'Custom Portrait': (1280, 1653),
    },
    '320:413': {
        'Custom Portrait': (1280, 1652),
    },
    '31:40': {
        'Custom Portrait': (775, 1000),
    },
    '1280:1651': {
        'Custom Portrait': (1280, 1651),
    },
    '128:165': {
        'Custom Portrait': (1024, 1320),
    },
    '933:1202': {
        'Custom Portrait': (933, 1202),
    },
    '80:103': {
        'Custom Portrait': (1280, 1648),
    },
    '640:823': {
        'Custom Portrait': (1280, 1646),
    },
    '1991:2560': {
        'Custom Portrait': (1991, 2560),
    },
    '7:9': {
        'Custom Portrait': (1008, 1296),
    },
    '256:329': {
        'Custom Portrait': (1280, 1645),
    },
    '320:411': {
        'Custom Portrait': (1280, 1644),
    },
    '779:1000': {
        'Custom Portrait': (779, 1000),
    },
    '1280:1643': {
        'Custom Portrait': (1280, 1643),
    },
    '60:77': {
        'Custom Portrait': (720, 924),
    },
    '640:821': {
        'Custom Portrait': (1280, 1642),
    },
    '32:41': {
        'Custom Portrait': (1280, 1640),
    },
    '25:32': {
        'Custom Portrait': (1200, 1536),
    },
    '256:327': {
        'Custom Portrait': (1280, 1635),
    },
    '40:51': {
        'Custom Portrait': (1280, 1632),
    },
    '157:200': {
        'Custom Portrait': (785, 1000),
    },
    '683:870': {
        'Custom Portrait': (683, 870),
    },
    '320:407': {
        'Custom Portrait': (1280, 1628),
    },
    '1280:1627': {
        'Custom Portrait': (1280, 1627),
    },
    '640:813': {
        'Custom Portrait': (1280, 1626),
    },
    '256:325': {
        'Custom Portrait': (1280, 1625),
    },
    '567:719': {
        'Custom Portrait': (567, 719),
    },
    '1280:1621': {
        'Custom Portrait': (1280, 1621),
    },
    '80:101': {
        'Custom Portrait': (1280, 1616),
    },
    '640:807': {
        'Custom Portrait': (1280, 1614),
    },
    '1280:1613': {
        'Custom Portrait': (1280, 1613),
    },
    '143:180': {
        'Custom Portrait': (715, 900),
    },
    '1280:1611': {
        'Custom Portrait': (1280, 1611),
    },
    '500:629': {
        'Custom Portrait': (1000, 1258),
    },
    '128:161': {
        'Custom Portrait': (1280, 1610),
    },
    '35:44': {
        'Custom Portrait': (1120, 1408),
    },
    '1280:1609': {
        'Custom Portrait': (1280, 1609),
    },
    '637:800': {
        'Custom Portrait': (1274, 1600),
    },
    '1280:1607': {
        'Custom Portrait': (1280, 1607),
    },
    '640:803': {
        'Custom Portrait': (1280, 1606),
    },
    '256:321': {
        'Custom Portrait': (1280, 1605),
    },
    '700:877': {
        'Custom Portrait': (700, 877),
    },
    '1280:1603': {
        'Custom Portrait': (1280, 1603),
    },
    '900:1127': {
        'Custom Portrait': (900, 1127),
    },
    '767:960': {
        'Custom Portrait': (1534, 1920),
    },
    '779:974': {
        'Custom Portrait': (779, 974),
    },
    '819:1024': {
        'Custom Portrait': (819, 1024),
    },
    '4:5': {
        'Custom Portrait': (1200, 1500),
    },
    '766:957': {
        'Custom Portrait': (766, 957),
    },
    '1280:1599': {
        'Custom Portrait': (1280, 1599),
    },
    '640:799': {
        'Custom Portrait': (1280, 1598),
    },
    '1280:1597': {
        'Custom Portrait': (1280, 1597),
    },
    '65:81': {
        'Custom Portrait': (1040, 1296),
    },
    '175:218': {
        'Custom Portrait': (1400, 1744),
    },
    '640:797': {
        'Custom Portrait': (1280, 1594),
    },
    '617:768': {
        'Custom Portrait': (1234, 1536),
    },
    '1280:1593': {
        'Custom Portrait': (1280, 1593),
    },
    '45:56': {
        'Custom Portrait': (1080, 1344),
    },
    '160:199': {
        'Custom Portrait': (1280, 1592),
    },
    '1280:1591': {
        'Custom Portrait': (1280, 1591),
    },
    '103:128': {
        'Custom Portrait': (824, 1024),
    },
    '128:159': {
        'Custom Portrait': (1280, 1590),
    },
    '320:397': {
        'Custom Portrait': (1280, 1588),
    },
    '1280:1587': {
        'Custom Portrait': (1280, 1587),
    },
    '80:99': {
        'Custom Portrait': (1280, 1584),
    },
    '1280:1581': {
        'Custom Portrait': (1280, 1581),
    },
    '1280:1577': {
        'Custom Portrait': (1280, 1577),
    },
    '256:315': {
        'Custom Portrait': (1280, 1575),
    },
    '640:787': {
        'Custom Portrait': (1280, 1574),
    },
    '320:393': {
        'Custom Portrait': (1280, 1572),
    },
    '1280:1571': {
        'Custom Portrait': (1280, 1571),
    },
    '1280:1569': {
        'Custom Portrait': (1280, 1569),
    },
    '40:49': {
        'Custom Portrait': (1280, 1568),
    },
    '1280:1567': {
        'Custom Portrait': (1280, 1567),
    },
    '640:783': {
        'Custom Portrait': (1280, 1566),
    },
    '112:137': {
        'Custom Portrait': (896, 1096),
    },
    '256:313': {
        'Custom Portrait': (1280, 1565),
    },
    '640:781': {
        'Custom Portrait': (1280, 1562),
    },
    '32:39': {
        'Custom Portrait': (1024, 1248),
    },
    '1280:1557': {
        'Custom Portrait': (1280, 1557),
    },
    '256:311': {
        'Custom Portrait': (1280, 1555),
    },
    '80:97': {
        'Custom Portrait': (1280, 1552),
    },
    '147:178': {
        'Custom Portrait': (1176, 1424),
    },
    '1280:1549': {
        'Custom Portrait': (1280, 1549),
    },
    '640:771': {
        'Custom Portrait': (1280, 1542),
    },
    '5:6': {
        'Custom Portrait': (750, 900),
    },
    '640:767': {
        'Custom Portrait': (1280, 1534),
    },
    '898:1075': {
        'Custom Portrait': (898, 1075),
    },
    '320:383': {
        'Custom Portrait': (1280, 1532),
    },
    '128:153': {
        'Custom Portrait': (1280, 1530),
    },
    '1280:1521': {
        'Custom Portrait': (1280, 1521),
    },
    '16:19': {
        'Custom Portrait': (1280, 1520),
    },
    '1399:1661': {
        'Custom Portrait': (1399, 1661),
    },
    '1280:1519': {
        'Custom Portrait': (1280, 1519),
    },
    '1280:1517': {
        'Custom Portrait': (1280, 1517),
    },
    '256:303': {
        'Custom Portrait': (1280, 1515),
    },
    '169:200': {
        'Custom Portrait': (845, 1000),
    },
    '640:757': {
        'Custom Portrait': (1280, 1514),
    },
    '1280:1511': {
        'Custom Portrait': (1280, 1511),
    },
    '320:377': {
        'Custom Portrait': (1280, 1508),
    },
    '1280:1507': {
        'Custom Portrait': (1280, 1507),
    },
    '17:20': {
        'Custom Portrait': (1088, 1280),
    },
    '256:301': {
        'Custom Portrait': (1280, 1505),
    },
    '40:47': {
        'Custom Portrait': (1280, 1504),
    },
    '1280:1503': {
        'Custom Portrait': (1280, 1503),
    },
    '640:751': {
        'Custom Portrait': (1280, 1502),
    },
    '1280:1501': {
        'Custom Portrait': (1280, 1501),
    },
    '64:75': {
        'Custom Portrait': (1280, 1500),
    },
    '1280:1499': {
        'Custom Portrait': (1280, 1499),
    },
    '640:749': {
        'Custom Portrait': (1280, 1498),
    },
    '160:187': {
        'Custom Portrait': (1280, 1496),
    },
    '6:7': {
        'Custom Portrait': (672, 784),
    },
    '1280:1493': {
        'Custom Portrait': (1280, 1493),
    },
    '1280:1491': {
        'Custom Portrait': (1280, 1491),
    },
    '128:149': {
        'Custom Portrait': (1280, 1490),
    },
    '116:135': {
        'Custom Portrait': (928, 1080),
    },
    '1280:1489': {
        'Custom Portrait': (1280, 1489),
    },
    '619:720': {
        'Custom Portrait': (1238, 1440),
    },
    '80:93': {
        'Custom Portrait': (1280, 1488),
    },
    '1280:1487': {
        'Custom Portrait': (1280, 1487),
    },
    '640:743': {
        'Custom Portrait': (1280, 1486),
    },
    '83:96': {
        'Custom Portrait': (664, 768),
    },
    '32:37': {
        'Custom Portrait': (1280, 1480),
    },
    '1280:1479': {
        'Custom Portrait': (1280, 1479),
    },
    '320:369': {
        'Custom Portrait': (1280, 1476),
    },
    '256:295': {
        'Custom Portrait': (1280, 1475),
    },
    '640:737': {
        'Custom Portrait': (1280, 1474),
    },
    '1280:1473': {
        'Custom Portrait': (1280, 1473),
    },
    '271:311': {
        'Custom Portrait': (813, 933),
    },
    '813:932': {
        'Custom Portrait': (813, 932),
    },
    '640:733': {
        'Custom Portrait': (1280, 1466),
    },
    '256:293': {
        'Custom Portrait': (1280, 1465),
    },
    '1280:1463': {
        'Custom Portrait': (1280, 1463),
    },
    '1280:1457': {
        'Custom Portrait': (1280, 1457),
    },
    '80:91': {
        'Custom Portrait': (1280, 1456),
    },
    '563:640': {
        'Custom Portrait': (1126, 1280),
    },
    '256:291': {
        'Custom Portrait': (1280, 1455),
    },
    '1280:1453': {
        'Custom Portrait': (1280, 1453),
    },
    '320:363': {
        'Custom Portrait': (1280, 1452),
    },
    '256:289': {
        'Custom Portrait': (1280, 1445),
    },
    '889:1000': {
        'Custom Portrait': (889, 1000),
    },
    '1280:1439': {
        'Custom Portrait': (1280, 1439),
    },
    '640:717': {
        'Custom Portrait': (1280, 1434),
    },
    '860:963': {
        'Custom Portrait': (860, 963),
    },
    '229:256': {
        'Custom Portrait': (1145, 1280),
    },
    '1280:1429': {
        'Custom Portrait': (1280, 1429),
    },
    '745:831': {
        'Custom Portrait': (745, 831),
    },
    '1280:1427': {
        'Custom Portrait': (1280, 1427),
    },
    '1280:1423': {
        'Custom Portrait': (1280, 1423),
    },
    '9:10': {
        'Custom Portrait': (900, 1000),
    },
    '640:711': {
        'Custom Portrait': (1280, 1422),
    },
    '425:472': {
        'Custom Portrait': (850, 944),
    },
    '160:177': {
        'Custom Portrait': (1280, 1416),
    },
    '1280:1413': {
        'Custom Portrait': (1280, 1413),
    },
    '1280:1409': {
        'Custom Portrait': (1280, 1409),
    },
    '499:549': {
        'Custom Portrait': (499, 549),
    },
    '10:11': {
        'Custom Portrait': (1280, 1408),
    },
    '1280:1403': {
        'Custom Portrait': (1280, 1403),
    },
    '1607:1761': {
        'Custom Portrait': (1607, 1761),
    },
    '1280:1401': {
        'Custom Portrait': (1280, 1401),
    },
    '32:35': {
        'Custom Portrait': (1280, 1400),
    },
    '640:699': {
        'Custom Portrait': (1280, 1398),
    },
    '640:697': {
        'Custom Portrait': (1280, 1394),
    },
    '1280:1391': {
        'Custom Portrait': (1280, 1391),
    },
    '553:600': {
        'Custom Portrait': (1106, 1200),
    },
    '640:691': {
        'Custom Portrait': (1280, 1382),
    },
    '1280:1381': {
        'Custom Portrait': (1280, 1381),
    },
    '64:69': {
        'Custom Portrait': (1280, 1380),
    },
    '256:275': {
        'Custom Portrait': (1280, 1375),
    },
    '800:859': {
        'Custom Portrait': (800, 859),
    },
    '256:273': {
        'Custom Portrait': (1280, 1365),
    },
    '320:341': {
        'Custom Portrait': (1280, 1364),
    },
    '1280:1363': {
        'Custom Portrait': (1280, 1363),
    },
    '640:681': {
        'Custom Portrait': (1280, 1362),
    },
    '850:903': {
        'Custom Portrait': (850, 903),
    },
    '35:37': {
        'Custom Portrait': (700, 740),
    },
    '1280:1353': {
        'Custom Portrait': (1280, 1353),
    },
    '675:709': {
        'Custom Portrait': (675, 709),
    },
    '20:21': {
        'Custom Portrait': (1280, 1344),
    },
    '767:800': {
        'Custom Portrait': (767, 800),
    },
    '256:267': {
        'Custom Portrait': (1280, 1335),
    },
    '1280:1331': {
        'Custom Portrait': (1280, 1331),
    },
    '1280:1329': {
        'Custom Portrait': (1280, 1329),
    },
    '80:83': {
        'Custom Portrait': (1280, 1328),
    },
    '256:265': {
        'Custom Portrait': (1280, 1325),
    },
    '1280:1323': {
        'Custom Portrait': (1280, 1323),
    },
    '547:565': {
        'Custom Portrait': (1094, 1130),
    },
    '640:659': {
        'Custom Portrait': (1280, 1318),
    },
    '777:800': {
        'Custom Portrait': (777, 800),
    },
    '1280:1317': {
        'Custom Portrait': (1280, 1317),
    },
    '320:329': {
        'Custom Portrait': (1280, 1316),
    },
    '1280:1311': {
        'Custom Portrait': (1280, 1311),
    },
    '128:131': {
        'Custom Portrait': (1280, 1310),
    },
    '256:261': {
        'Custom Portrait': (1280, 1305),
    },
    '1280:1303': {
        'Custom Portrait': (1280, 1303),
    },
    '1280:1299': {
        'Custom Portrait': (1280, 1299),
    },
    '1280:1297': {
        'Custom Portrait': (1280, 1297),
    },
    '1280:1293': {
        'Custom Portrait': (1280, 1293),
    },
    '1280:1291': {
        'Custom Portrait': (1280, 1291),
    },
    '128:129': {
        'Custom Portrait': (1280, 1290),
    },
    '160:161': {
        'Custom Portrait': (1280, 1288),
    },
    '179:180': {
        'Custom Portrait': (895, 900),
    },
    '1167:1172': {
        'Custom Portrait': (1167, 1172),
    },
    '1:1': {
        'Custom Landscape': (2000, 2000),
    },
    '640:639': {
        'Custom Landscape': (1280, 1278),
    },
    '320:319': {
        'Custom Landscape': (1280, 1276),
    },
    '1280:1273': {
        'Custom Landscape': (1280, 1273),
    },
    '128:127': {
        'Custom Landscape': (1280, 1270),
    },
    '1000:991': {
        'Custom Landscape': (1000, 991),
    },
    '320:317': {
        'Custom Landscape': (1280, 1268),
    },
    '1280:1267': {
        'Custom Landscape': (1280, 1267),
    },
    '640:633': {
        'Custom Landscape': (1280, 1266),
    },
    '78:77': {
        'Custom Landscape': (1248, 1232),
    },
    '1280:1263': {
        'Custom Landscape': (1280, 1263),
    },
    '360:353': {
        'Custom Landscape': (720, 706),
    },
    '1280:1247': {
        'Custom Landscape': (1280, 1247),
    },
    '320:311': {
        'Custom Landscape': (1280, 1244),
    },
    '384:373': {
        'Custom Landscape': (1536, 1492),
    },
    '640:621': {
        'Custom Landscape': (1280, 1242),
    },
    '640:619': {
        'Custom Landscape': (1280, 1238),
    },
    '320:309': {
        'Custom Landscape': (1280, 1236),
    },
    '640:617': {
        'Custom Landscape': (1280, 1234),
    },
    '1280:1233': {
        'Custom Landscape': (1280, 1233),
    },
    '80:77': {
        'Custom Landscape': (1280, 1232),
    },
    '448:431': {
        'Custom Landscape': (1344, 1293),
    },
    '1280:1229': {
        'Custom Landscape': (1280, 1229),
    },
    '640:613': {
        'Custom Landscape': (1280, 1226),
    },
    '1149:1100': {
        'Custom Landscape': (1149, 1100),
    },
    '256:245': {
        'Custom Landscape': (1280, 1225),
    },
    '160:153': {
        'Custom Landscape': (1280, 1224),
    },
    '65:62': {
        'Custom Landscape': (910, 868),
    },
    '1280:1219': {
        'Custom Landscape': (1280, 1219),
    },
    '640:609': {
        'Custom Landscape': (1280, 1218),
    },
    '20:19': {
        'Custom Landscape': (1280, 1216),
    },
    '1280:1213': {
        'Custom Landscape': (1280, 1213),
    },
    '160:151': {
        'Custom Landscape': (1280, 1208),
    },
    '1000:943': {
        'Custom Landscape': (1000, 943),
    },
    '640:603': {
        'Custom Landscape': (1280, 1206),
    },
    '800:753': {
        'Custom Landscape': (800, 753),
    },
    '320:301': {
        'Custom Landscape': (1280, 1204),
    },
    '218:205': {
        'Custom Landscape': (1744, 1640),
    },
    '1280:1203': {
        'Custom Landscape': (1280, 1203),
    },
    '1280:1201': {
        'Custom Landscape': (1280, 1201),
    },
    '81:76': {
        'Custom Landscape': (810, 760),
    },
    '16:15': {
        'Custom Landscape': (1280, 1200),
    },
    '1280:1199': {
        'Custom Landscape': (1280, 1199),
    },
    '640:597': {
        'Custom Landscape': (1280, 1194),
    },
    '1280:1189': {
        'Custom Landscape': (1280, 1189),
    },
    '320:297': {
        'Custom Landscape': (1280, 1188),
    },
    '1280:1187': {
        'Custom Landscape': (1280, 1187),
    },
    '640:593': {
        'Custom Landscape': (1280, 1186),
    },
    '40:37': {
        'Custom Landscape': (1280, 1184),
    },
    '64:59': {
        'Custom Landscape': (1280, 1180),
    },
    '431:397': {
        'Custom Landscape': (862, 794),
    },
    '151:139': {
        'Custom Landscape': (755, 695),
    },
    '1280:1177': {
        'Custom Landscape': (1280, 1177),
    },
    '320:293': {
        'Custom Landscape': (1280, 1172),
    },
    '80:73': {
        'Custom Landscape': (1280, 1168),
    },
    '125:114': {
        'Custom Landscape': (1000, 912),
    },
    '1280:1161': {
        'Custom Landscape': (1280, 1161),
    },
    '1280:1159': {
        'Custom Landscape': (1280, 1159),
    },
    '640:579': {
        'Custom Landscape': (1280, 1158),
    },
    '1280:1157': {
        'Custom Landscape': (1280, 1157),
    },
    '128:115': {
        'Custom Landscape': (1280, 1150),
    },
    '1280:1149': {
        'Custom Landscape': (1280, 1149),
    },
    '447:400': {
        'Custom Landscape': (894, 800),
    },
    '256:229': {
        'Custom Landscape': (1280, 1145),
    },
    '1119:1000': {
        'Custom Landscape': (1119, 1000),
    },
    '1280:1143': {
        'Custom Landscape': (1280, 1143),
    },
    '64:57': {
        'Custom Landscape': (1280, 1140),
    },
    '1280:1137': {
        'Custom Landscape': (1280, 1137),
    },
    '418:371': {
        'Custom Landscape': (836, 742),
    },
    '640:567': {
        'Custom Landscape': (1280, 1134),
    },
    '341:302': {
        'Custom Landscape': (1023, 906),
    },
    '1280:1131': {
        'Custom Landscape': (1280, 1131),
    },
    '17:15': {
        'Custom Landscape': (1088, 960),
    },
    '181:159': {
        'Custom Landscape': (724, 636),
    },
    '1280:1123': {
        'Custom Landscape': (1280, 1123),
    },
    '640:561': {
        'Custom Landscape': (1280, 1122),
    },
    '8:7': {
        'Custom Landscape': (1280, 1120),
    },
    '239:209': {
        'Custom Landscape': (956, 836),
    },
    '1024:895': {
        'Custom Landscape': (1024, 895),
    },
    '640:559': {
        'Custom Landscape': (1280, 1118),
    },
    '1280:1117': {
        'Custom Landscape': (1280, 1117),
    },
    '640:557': {
        'Custom Landscape': (1280, 1114),
    },
    '1280:1113': {
        'Custom Landscape': (1280, 1113),
    },
    '128:111': {
        'Custom Landscape': (1280, 1110),
    },
    '1280:1109': {
        'Custom Landscape': (1280, 1109),
    },
    '320:277': {
        'Custom Landscape': (1280, 1108),
    },
    '64:55': {
        'Custom Landscape': (1280, 1100),
    },
    '7:6': {
        'Custom Landscape': (1050, 900),
    },
    '1280:1097': {
        'Custom Landscape': (1280, 1097),
    },
    '256:219': {
        'Custom Landscape': (1280, 1095),
    },
    '640:547': {
        'Custom Landscape': (1280, 1094),
    },
    '320:273': {
        'Custom Landscape': (640, 546),
    },
    '128:109': {
        'Custom Landscape': (1280, 1090),
    },
    '153:130': {
        'Custom Landscape': (1224, 1040),
    },
    '1280:1087': {
        'Custom Landscape': (1280, 1087),
    },
    '85:72': {
        'Custom Landscape': (1190, 1008),
    },
    '1280:1081': {
        'Custom Landscape': (1280, 1081),
    },
    '32:27': {
        'Custom Landscape': (1280, 1080),
    },
    '640:539': {
        'Custom Landscape': (1280, 1078),
    },
    '513:431': {
        'Custom Landscape': (1026, 862),
    },
    '1280:1073': {
        'Custom Landscape': (1280, 1073),
    },
    '55:46': {
        'Custom Landscape': (1100, 920),
    },
    '1280:1069': {
        'Custom Landscape': (1280, 1069),
    },
    '320:267': {
        'Custom Landscape': (1280, 1068),
    },
    '6:5': {
        'Custom Landscape': (1200, 1000),
    },
    '425:354': {
        'Custom Landscape': (850, 708),
    },
    '640:533': {
        'Custom Landscape': (1280, 1066),
    },
    '160:133': {
        'Custom Landscape': (1280, 1064),
    },
    '1173:971': {
        'Custom Landscape': (1173, 971),
    },
    '155:128': {
        'Custom Landscape': (1240, 1024),
    },
    '1280:1057': {
        'Custom Landscape': (1280, 1057),
    },
    '40:33': {
        'Custom Landscape': (1280, 1056),
    },
    '378:311': {
        'Custom Landscape': (756, 622),
    },
    '320:263': {
        'Custom Landscape': (1280, 1052),
    },
    '1280:1051': {
        'Custom Landscape': (1280, 1051),
    },
    '50:41': {
        'Custom Landscape': (1050, 861),
    },
    '160:131': {
        'Custom Landscape': (1280, 1048),
    },
    '1280:1047': {
        'Custom Landscape': (1280, 1047),
    },
    '640:523': {
        'Custom Landscape': (1280, 1046),
    },
    '256:203': {
        'Custom Landscape': (1280, 1045),
    },
    '1280:1041': {
        'Custom Landscape': (1280, 1041),
    },
    '1280:1039': {
        'Custom Landscape': (1280, 1039),
    },
    '1280:1037': {
        'Custom Landscape': (1280, 1037),
    },
    '640:517': {
        'Custom Landscape': (1280, 1034),
    },
    '1280:1033': {
        'Custom Landscape': (1280, 1033),
    },
    '1280:1031': {
        'Custom Landscape': (1280, 1031),
    },
    '200:161': {
        'Custom Landscape': (1000, 805),
    },
    '1280:1029': {
        'Custom Landscape': (1280, 1029),
    },
    '269:216': {
        'Custom Landscape': (1076, 864),
    },
    '1280:1027': {
        'Custom Landscape': (1280, 1027),
    },
    '5:4': {
        'Custom Landscape': (800, 640),
    },
    '1024:819': {
        'Custom Landscape': (1024, 819),
    },
    '800:639': {
        'Custom Landscape': (800, 639),
    },
    '640:511': {
        'Custom Landscape': (1280, 1022),
    },
    '500:399': {
        'Custom Landscape': (1000, 798),
    },
    '1280:1021': {
        'Custom Landscape': (1280, 1021),
    },
    '400:319': {
        'Custom Landscape': (800, 638),
    },
    '64:51': {
        'Custom Landscape': (1280, 1020),
    },
    '1280:1017': {
        'Custom Landscape': (1280, 1017),
    },
    '256:203': {
        'Custom Landscape': (1280, 1015),
    },
    '640:507': {
        'Custom Landscape': (1280, 1014),
    },
    '1280:1013': {
        'Custom Landscape': (1280, 1013),
    },
    '1280:1011': {
        'Custom Landscape': (1280, 1011),
    },
    '80:63': {
        'Custom Landscape': (1280, 1008),
    },
    '320:251': {
        'Custom Landscape': (1280, 1004),
    },
    '88:69': {
        'Custom Landscape': (1408, 1104),
    },
    '653:512': {
        'Custom Landscape': (1306, 1024),
    },
    '32:25': {
        'Custom Landscape': (1280, 1000),
    },
    '640:499': {
        'Custom Landscape': (1280, 998),
    },
    '1280:997': {
        'Custom Landscape': (1280, 997),
    },
    '425:331': {
        'Custom Landscape': (850, 662),
    },
    '1024:797': {
        'Custom Landscape': (1024, 797),
    },
    '9:7': {
        'Custom Landscape': (1125, 875),
    },
    '1280:993': {
        'Custom Landscape': (1280, 993),
    },
    '75:58': {
        'Custom Landscape': (1200, 928),
    },
    '119:92': {
        'Custom Landscape': (1190, 920),
    },
    '1000:773': {
        'Custom Landscape': (1000, 773),
    },
    '1280:989': {
        'Custom Landscape': (1280, 989),
    },
    '320:247': {
        'Custom Landscape': (1280, 988),
    },
    '1280:987': {
        'Custom Landscape': (1280, 987),
    },
    '256:197': {
        'Custom Landscape': (1280, 985),
    },
    '1000:769': {
        'Custom Landscape': (1000, 769),
    },
    '160:123': {
        'Custom Landscape': (1280, 984),
    },
    '1280:983': {
        'Custom Landscape': (1280, 983),
    },
    '640:491': {
        'Custom Landscape': (1280, 982),
    },
    '1280:981': {
        'Custom Landscape': (1280, 981),
    },
    '64:49': {
        'Custom Landscape': (1280, 980),
    },
    '1280:977': {
        'Custom Landscape': (1280, 977),
    },
    '80:61': {
        'Custom Landscape': (1280, 976),
    },
    '21:16': {
        'Custom Landscape': (1260, 960),
    },
    '239:182': {
        'Custom Landscape': (717, 546),
    },
    '320:243': {
        'Custom Landscape': (1280, 972),
    },
    '416:315': {
        'Custom Landscape': (1248, 945),
    },
    '1280:969': {
        'Custom Landscape': (1280, 969),
    },
    '300:227': {
        'Custom Landscape': (1200, 908),
    },
    '160:121': {
        'Custom Landscape': (1280, 968),
    },
    '827:625': {
        'Custom Landscape': (827, 625),
    },
    '49:37': {
        'Custom Landscape': (637, 481),
    },
    '640:483': {
        'Custom Landscape': (1280, 966),
    },
    '256:193': {
        'Custom Landscape': (1280, 965),
    },
    '799:602': {
        'Custom Landscape': (799, 602),
    },
    '320:241': {
        'Custom Landscape': (1280, 964),
    },
    '400:301': {
        'Custom Landscape': (800, 602),
    },
    '1206:907': {
        'Custom Landscape': (1206, 907),
    },
    '640:481': {
        'Custom Landscape': (1280, 962),
    },
    '161:121': {
        'Custom Landscape': (644, 484),
    },
    '638:479': {
        'Custom Landscape': (638, 479),
    },
    '425:319': {
        'Custom Landscape': (850, 638),
    },
    '950:713': {
        'Custom Landscape': (950, 713),
    },
    '1278:959': {
        'Custom Landscape': (1278, 959),
    },
    '4:3': {
        'Custom Landscape': (1280, 960),
    },
    '1067:800': {
        'Custom Landscape': (1067, 800),
    },
    '799:599': {
        'Custom Landscape': (799, 599),
    },
    '695:521': {
        'Custom Landscape': (695, 521),
    },
    '850:637': {
        'Custom Landscape': (850, 637),
    },
    '399:299': {
        'Custom Landscape': (798, 598),
    },
    '640:479': {
        'Custom Landscape': (1280, 958),
    },
    '159:119': {
        'Custom Landscape': (795, 595),
    },
    '801:599': {
        'Custom Landscape': (801, 599),
    },
    '256:191': {
        'Custom Landscape': (1280, 955),
    },
    '206:153': {
        'Custom Landscape': (1236, 918),
    },
    '320:237': {
        'Custom Landscape': (1280, 948),
    },
    '585:433': {
        'Custom Landscape': (1170, 866),
    },
    '50:37': {
        'Custom Landscape': (700, 518),
    },
    '1173:868': {
        'Custom Landscape': (1173, 868),
    },
    '640:473': {
        'Custom Landscape': (1280, 946),
    },
    '80:59': {
        'Custom Landscape': (1280, 944),
    },
    '750:553': {
        'Custom Landscape': (750, 553),
    },
    '640:471': {
        'Custom Landscape': (1280, 942),
    },
    '1280:941': {
        'Custom Landscape': (1280, 941),
    },
    '599:440': {
        'Custom Landscape': (1198, 880),
    },
    '64:47': {
        'Custom Landscape': (1280, 940),
    },
    '1280:939': {
        'Custom Landscape': (1280, 939),
    },
    '850:623': {
        'Custom Landscape': (850, 623),
    },
    '640:469': {
        'Custom Landscape': (1280, 938),
    },
    '112:75': {
        'Custom Landscape': (896, 600),
    },
    '160:107': {
        'Custom Landscape': (1280, 856),
    },
    '425:284': {
        'Custom Landscape': (850, 568),
    },
    '256:171': {
        'Custom Landscape': (1280, 855),
    },
    '3:2': {
        'Custom Landscape': (900, 600),
    },
    '2611:1740': {
        'Custom Landscape': (2611, 1740),
    },
    '1280:853': {
        'Custom Landscape': (1280, 853),
    },
    '320:213': {
        'Custom Landscape': (1280, 852),
    },
    '1280:851': {
        'Custom Landscape': (1280, 851),
    },
    '80:53': {
        'Custom Landscape': (1280, 848),
    },
    '640:423': {
        'Custom Landscape': (1280, 846),
    },
    '1280:839': {
        'Custom Landscape': (1280, 839),
    },
    '640:419': {
        'Custom Landscape': (1280, 838),
    },
    '256:167': {
        'Custom Landscape': (1280, 835),
    },
    '1280:831': {
        'Custom Landscape': (1280, 831),
    },
    '160:103': {
        'Custom Landscape': (1280, 824),
    },
    '120:77': {
        'Custom Landscape': (960, 536),
    },
    '1280:817': {
        'Custom Landscape': (1280, 817),
    },
    '11:7': {
        'Custom Landscape': (1100, 700),
    },
    '1280:813': {
        'Custom Landscape': (1280, 813),
    },
    '128:81': {
        'Custom Landscape': (1280, 810),
    },
    '160:101': {
        'Custom Landscape': (1280, 808),
    },
    '640:403': {
        'Custom Landscape': (1280, 806),
    },
    '256:161': {
        'Custom Landscape': (1280, 805),
    },
    '1280:803': {
        'Custom Landscape': (1280, 803),
    },
    '1280:801': {
        'Custom Landscape': (1280, 801),
    },
    '8:5': {
        'Custom Landscape': (1200, 750),
    },
    '640:399': {
        'Custom Landscape': (1280, 798),
    },
    '1280:797': {
        'Custom Landscape': (1280, 797),
    },
    '320:199': {
        'Custom Landscape': (1280, 796),
    },
    '640:397': {
        'Custom Landscape': (1280, 794),
    },
    '128:79': {
        'Custom Landscape': (2048, 1264),
    },
    '1280:789': {
        'Custom Landscape': (1280, 789),
    },
    '1280:787': {
        'Custom Landscape': (1280, 787),
    },
    '256:157': {
        'Custom Landscape': (1280, 785),
    },
    '1280:783': {
        'Custom Landscape': (1280, 783),
    },
    '1200:733': {
        'Custom Landscape': (1200, 733),
    },
    '1280:781': {
        'Custom Landscape': (1280, 781),
    },
    '1280:779': {
        'Custom Landscape': (1280, 779),
    },
    '256:155': {
        'Custom Landscape': (1280, 775),
    },
    '1280:769': {
        'Custom Landscape': (1280, 769),
    },
    '1280:753': {
        'Custom Landscape': (1280, 753),
    },
    '80:47': {
        'Custom Landscape': (1280, 752),
    },
    '128:75': {
        'Custom Landscape': (1024, 600),
    },
    '137:80': {
        'Custom Landscape': (959, 560),
    },
    '1280:747': {
        'Custom Landscape': (1280, 747),
    },
    '256:149': {
        'Custom Landscape': (1280, 745),
    },
    '160:93': {
        'Custom Landscape': (1280, 744),
    },
    '1280:741': {
        'Custom Landscape': (1280, 741),
    },
    '1280:739': {
        'Custom Landscape': (1280, 739),
    },
    '1280:737': {
        'Custom Landscape': (1280, 737),
    },
    '128:73': {
        'Custom Landscape': (1280, 730),
    },
    '1280:727': {
        'Custom Landscape': (1280, 727),
    },
    '30:17': {
        'Custom Landscape': (1920, 1088),
    },
    '256:145': {
        'Custom Landscape': (1280, 725),
    },
    '113:64': {
        'Custom Landscape': (1356, 768),
    },
    '640:361': {
        'Custom Landscape': (1280, 722),
    },
    '16:9': {
        'Custom Landscape': (1024, 576),
    },
    '425:239': {
        'Custom Landscape': (850, 478),
    },
    '120:67': {
        'Custom Landscape': (960, 536),
    },
    '323:180': {
        'Custom Landscape': (1292, 720),
    },
    '160:89': {
        'Custom Landscape': (1280, 712),
    },
    '1280:709': {
        'Custom Landscape': (1280, 709),
    },
    '1280:707': {
        'Custom Landscape': (1280, 707),
    },
    '1280:701': {
        'Custom Landscape': (1280, 701),
    },
    '75:41': {
        'Custom Landscape': (1200, 656),
    },
    '2047:1095': {
        'Custom Landscape': (2047, 1095),
    },
    '1280:683': {
        'Custom Landscape': (1280, 683),
    },
    '859:458': {
        'Custom Landscape': (859, 458),
    },
    '256:135': {
        'Custom Landscape': (1280, 675),
    },
    '40:21': {
        'Custom Landscape': (1200, 630),
    },
    '256:131': {
        'Custom Landscape': (1280, 655),
    },
    '256:129': {
        'Custom Landscape': (1280, 645),
    },
    '1280:643': {
        'Custom Landscape': (1280, 643),
    },
    '1280:641': {
        'Custom Landscape': (1280, 641),
    },
    '1280:627': {
        'Custom Landscape': (1280, 627),
    },
    '640:311': {
        'Custom Landscape': (1280, 622),
    },
    '1280:617': {
        'Custom Landscape': (1280, 617),
    },
    '160:77': {
        'Custom Landscape': (1280, 616),
    },
    '640:307': {
        'Custom Landscape': (1280, 614),
    },
    '320:153': {
        'Custom Landscape': (1280, 612),
    },
    '40:19': {
        'Custom Landscape': (1280, 608),
    },
    '1280:587': {
        'Custom Landscape': (1280, 587),
    },
    '640:293': {
        'Custom Landscape': (1280, 586),
    },
    '64:29': {
        'Custom Landscape': (1280, 580),
    },
    '1280:579': {
        'Custom Landscape': (1280, 579),
    },
    '1280:577': {
        'Custom Landscape': (1280, 577),
    },
    '320:141': {
        'Custom Landscape': (1280, 564),
    },
    '1280:561': {
        'Custom Landscape': (1280, 561),
    },
    '1280:531': {
        'Custom Landscape': (1280, 531),
    },
    '256:105': {
        'Custom Landscape': (1280, 525),
    },
    '1280:509': {
        'Custom Landscape': (1280, 509),
    },
    '1280:487': {
        'Custom Landscape': (1280, 487),
    },
    '256:97': {
        'Custom Landscape': (1280, 485),
    },
    '256:95': {
        'Custom Landscape': (1280, 475),
    },
    '128:47': {
        'Custom Landscape': (1280, 470),
    },
    '320:117': {
        'Custom Landscape': (1280, 468),
    },
    '80:29': {
        'Custom Landscape': (1280, 464),
    },
    '1280:461': {
        'Custom Landscape': (1280, 461),
    },
    '160:53': {
        'Custom Landscape': (1280, 424),
    },
    '160:47': {
        'Custom Landscape': (1280, 376),
    },
    '1280:371': {
        'Custom Landscape': (1280, 371),
    },
    '256:65': {
        'Custom Landscape': (1280, 325),
    },
    '128:31': {
        'Custom Landscape': (1280, 310),
    },
    '320:61': {
        'Custom Landscape': (1280, 244),
    },
    ##END ADD
}
