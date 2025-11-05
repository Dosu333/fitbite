MAIN_MENU = [
    {
        "id": "menu_001",
        "name": "Jollof Rice",
        "price": 1500,
        "ingredients": ["rice", "tomato sauce", "vegetables", "spices"],
        "in_stock": True,
        "required_sides_category": [],
    },
    {
        "id": "menu_002",
        "name": "Fried Rice",
        "price": 1300,
        "ingredients": ["rice", "vegetables", "soy sauce", "spices"],
        "in_stock": True,
        "required_sides_category": [],
    },
    {
        "id": "menu_003",
        "name": "Spaghetti Bolognese",
        "price": 1800,
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "cheese"],
        "in_stock": False,
        "required_sides_category": [],
    },
    {
        "id": "menu_004",
        "name": "Pounded Yam",
        "price": 1200,
        "ingredients": ["yam", "water"],
        "in_stock": True,
        "required_sides_category": [
            "soup",
        ],
    },
    {
        "id": "menu_005",
        "name": "Eba",
        "price": 1000,
        "ingredients": ["garri", "water"],
        "in_stock": True,
        "required_sides_category": [
            "soup",
        ],
    },
    {
        "id": "menu_006",
        "name": "Amala",
        "price": 1100,
        "ingredients": ["yam flour", "water"],
        "in_stock": False,
        "required_sides_category": [
            "soup",
        ],
    },
]

SOUPS = [
    {
        "id": "soup_001",
        "name": "Egusi Soup",
        "price": 800,
        "ingredients": ["egusi", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
    {
        "id": "soup_002",
        "name": "Ogbono Soup",
        "price": 900,
        "ingredients": ["ogbono seeds", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
    {
        "id": "soup_003",
        "name": "Okra Soup",
        "price": 700,
        "ingredients": ["okra", "vegetables", "meat", "spices"],
        "in_stock": False,
    },
    {
        "id": "soup_004",
        "name": "Efo riro",
        "price": 850,
        "ingredients": ["spinach", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
    {
        "id": "soup_005",
        "name": "Afang Soup",
        "price": 950,
        "ingredients": ["afang leaves", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
]

PROTEINS = [
    {
        "id": "prot_001",
        "name": "Grilled Chicken",
        "price": 1200,
        "ingredients": ["chicken", "spices"],
        "in_stock": True,
    },
    {
        "id": "prot_002",
        "name": "Fried Fish",
        "price": 1500,
        "ingredients": ["fish", "spices", "oil"],
        "in_stock": True,
    },
    {
        "id": "prot_003",
        "name": "Beef Steak",
        "price": 2000,
        "ingredients": ["beef", "spices"],
        "in_stock": False,
    },
]

DRINKS = [
    {
        "id": "drink_001",
        "name": "Coke",
        "price": 300,
        "ingredients": ["carbonated water", "sugar", "flavorings"],
        "in_stock": True,
    },
    {
        "id": "drink_002",
        "name": "Fanta",
        "price": 300,
        "ingredients": ["carbonated water", "sugar", "orange flavor"],
        "in_stock": True,
    },
    {
        "id": "drink_003",
        "name": "Sprite",
        "price": 300,
        "ingredients": ["carbonated water", "sugar", "lemon-lime flavor"],
        "in_stock": False,
    },
]

OTHER_SIDES = [
    {
        "id": "side_001",
        "name": "Plantains",
        "price": 500,
        "ingredients": ["plantains", "oil", "spices"],
        "in_stock": True,
    },
    {
        "id": "side_002",
        "name": "Salad",
        "price": 400,
        "ingredients": ["lettuce", "tomatoes", "cucumbers", "dressing"],
        "in_stock": True,
    },
]

FULL_MENU = {
    "main menu": MAIN_MENU,
    "soups": SOUPS,
    "proteins": PROTEINS,
    "drinks": DRINKS,
    "sides": OTHER_SIDES,
}
