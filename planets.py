from helpers import formatstr

planets = {
    "earth": {
        "name": "Earth",
        "ethiopic_name": "መሬት",
        "photo_file_id": "AgACAgQAAxkBAANfZh5SEvspcQABqRnYIftdnCDcZFUDAALQyjEbiMP5UEeD7HAlfFtkAQADAgADeQADNAQ",
        "description": """The beautiful blue planet we call home, Earth is the third planet from the Sun and the only known celestial body to support life. With its vast oceans and diverse landscapes, it's a wonder of the cosmos.""",
        "tags": ["home_sweet_home", "oasis_of_life"],
        "prompt": "Discover the wonders of our home planet! Click below to explore more about Earth."
    },
    "jupiter": {
        "name": "Jupiter",
        "ethiopic_name": "መሽተሪ",
        "photo_file_id": "AgACAgQAAxkBAANBZh5GeOcNfyrSgfN-nFcCPX-658kAArquMRu6zt1QrN6pQY-MAV4BAAMCAAN3AAM0BA",
        "description": """Jupiter, the giant of our solar system, is a mesmerizing gas giant with swirling clouds and a remarkable system of moons. It's the fifth planet from the Sun and a captivating sight through telescopes.""",
        "tags": ["king_of_planets", "moons_playground"],
        "prompt": "Ready to dive into the mysteries of Jupiter? Click below to unveil the secrets of the largest planet!"
    },
    "mars": {
        "name": "Mars",
        "ethiopic_name": "መሪህ",
        "photo_file_id": "AgACAgQAAxkBAANDZh5GymRC04t6WFkO8TL3BcqTUowAAiKwMRt_fCRRmvwVAAHsro-eAQADAgADdwADNAQ",
        "description": """Known as the 'Red Planet', Mars has fascinated humanity for centuries. With its rusty surface and potential for exploration, it's a frontier of human ambition and a potential future home for humanity.""",
        "tags": ["red_frontier", "humanitys_destiny"],
        "prompt": "Embark on an adventure to the Red Planet! Click below to explore the possibilities of Mars."
    },
    "mercury": {
        "name": "Mercury",
        "ethiopic_name": "ዐጣርድ",
        "photo_file_id": "AgACAgQAAxkBAANFZh5HGegHz_CP5Y3tFyA0X129qgkAAuywMRuwNYRRAAG6zSpu3WWKAQADAgADdwADNAQ",
        "description": """Mercury, the closest planet to the Sun, is a scorched world of extremes. With its barren, cratered surface, it's a testament to the harsh realities of space exploration.""",
        "tags": ["scorched_domain", "cratered_realm"],
        "prompt": "Discover the secrets of the closest planet to the Sun! Click below to uncover the mysteries of Mercury."
    },
    "neptune": {
        "name": "Neptune",
        "ethiopic_name": "ኔፕቱን",
        "photo_file_id": "AgACAgQAAxkBAANJZh5H_k6VWsGwcG-5r1fe5T7qSnEAAnavMRu1EIxRX6kYGH5yIYgBAAMCAAN3AAM0BA",
        "description": """Neptune, the distant ice giant, holds mysteries deep within its blue depths. As the eighth planet from the Sun, it's a symbol of the outer reaches of our solar system and the quest for understanding.""",
        "tags": ["blue_enigma", "cosmic_mystery"],
        "prompt": "Dive into the depths of Neptune's mysteries! Click below to embark on a cosmic journey."
    },
    "saturn": {
        "name": "Saturn",
        "ethiopic_name": "ዙሐል",
        "photo_file_id": "AgACAgQAAxkBAANPZh5IqxVs-w45kHdQ2lrpQau-pgUAAn-wMRtLXDRSFY1XK9_-ufYBAAMCAAN5AAM0BA",
        "description": """Saturn, adorned with its iconic rings, is a jewel of the night sky. As the sixth planet from the Sun, it's a symbol of cosmic beauty and the wonders of the universe.""",
        "tags": ["ringed_beauty", "cosmic_jewel"],
        "prompt": "Witness the splendor of Saturn's rings! Click below to explore the beauty of the ringed planet."
    },
    "sun": {
        "name": "Sun",
        "ethiopic_name": "ፀሀይ",
        "photo_file_id": "AgACAgQAAxkBAANTZh5KqH5z6CXUI30LMuXON0achPYAAgyyMRtDLdVSj5MEXUF1eeIBAAMCAAN3AAM0BA",
        "description": """The radiant star at the heart of our solar system, the Sun is a life-giving force that lights up the heavens. Its energy sustains all life on Earth and fuels the dynamic processes of our planet.""",
        "tags": ["stellar_powerhouse", "life_source"],
        "prompt": "Feel the warmth of the life-giving Sun. Click below to bask in its radiant glory!",
    },
    "uranus": {
        "name": "Uranus",
        "ethiopic_name": "ዩራኑስ",
        "photo_file_id": "AgACAgQAAxkBAANVZh5LOvCrJRPc6h0FOMVwhNRqg04AAruyMRtTSVxQoeWozHPCVwkBAAMCAAN3AAM0BA",
        "description": """Uranus, the enigmatic ice giant, spins on its side in the depths of space. With its unique tilt and icy composition, it's a world of intrigue and mystery waiting to be explored.""",
        "tags": ["mysterious_wanderer", "icy_odyssey"],
        "prompt": "Embark on an icy odyssey to the enigmatic world of Uranus. Click below to uncover its secrets!",
    },
    "venus": {
        "name": "Venus",
        "ethiopic_name": "ዝሁራ",
        "photo_file_id": "AgACAgQAAxkBAANbZh5L1f8nsHAq86MUaI_z5pHeV2UAAjWvMRte0NxSRfbyNCluWSQBAAMCAAN3AAM0BA",
        "description": """Venus, the shimmering jewel of the dawn and dusk, beckons with its ethereal beauty. As Earth's sister planet, it's a tantalizing glimpse into the potential diversity of worlds beyond our own.""",
        "tags": ["ethereal_gem", "sister_world"],
        "prompt": "Experience the ethereal beauty of Venus. Click below to explore this sister world of Earth!",
    }
}

caption_template = '''<b>{kwargs['name']}</b> | <code>{kwargs['ethiopic_name']}</code>

<b>{kwargs['description']}</b>

#{" #".join(kwargs['tags'])}

<i>{kwargs['prompt']}</i>'''

