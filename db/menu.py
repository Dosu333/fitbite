MAIN_MENU = [
    {
        "name": "Jollof Rice",
        "price": 1500,
        "ingredients": ["rice", "tomato sauce", "vegetables", "spices"],
        "in_stock": True,
        "required_sides_category": [],
    },
    {
        "name": "Fried Rice",
        "price": 1300,
        "ingredients": ["rice", "vegetables", "soy sauce", "spices"],
        "in_stock": True,
        "required_sides_category": [],
    },
    {
        "name": "Spaghetti Bolognese",
        "price": 1800,
        "ingredients": ["spaghetti", "ground beef", "tomato sauce", "cheese"],
        "in_stock": False,
        "required_sides_category": [],
    },
    {
        "name": "Pounded Yam",
        "price": 1200,
        "ingredients": ["yam", "water"],
        "in_stock": True,
        "required_sides_category": [
            "soup",
        ],
    },
    {
        "name": "Eba",
        "price": 1000,
        "ingredients": ["garri", "water"],
        "in_stock": True,
        "required_sides_category": [
            "soup",
        ],
    },
    {
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
        "name": "Egusi Soup",
        "price": 800,
        "ingredients": ["egusi", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
    {
        "name": "Ogbono Soup",
        "price": 900,
        "ingredients": ["ogbono seeds", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
    {
        "name": "Okra Soup",
        "price": 700,
        "ingredients": ["okra", "vegetables", "meat", "spices"],
        "in_stock": False,
    },
    {
        "name": "Efo riro",
        "price": 850,
        "ingredients": ["spinach", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
    {
        "name": "Afang Soup",
        "price": 950,
        "ingredients": ["afang leaves", "vegetables", "meat", "spices"],
        "in_stock": True,
    },
]

PROTEINS = [
    {
        "name": "Grilled Chicken",
        "price": 1200,
        "ingredients": ["chicken", "spices"],
        "in_stock": True,
    },
    {
        "name": "Fried Fish",
        "price": 1500,
        "ingredients": ["fish", "spices", "oil"],
        "in_stock": True,
    },
    {
        "name": "Beef Steak",
        "price": 2000,
        "ingredients": ["beef", "spices"],
        "in_stock": False,
    },
]

DRINKS = [
    {
        "name": "Coke",
        "price": 300,
        "ingredients": ["carbonated water", "sugar", "flavorings"],
        "in_stock": True,
    },
    {
        "name": "Fanta",
        "price": 300,
        "ingredients": ["carbonated water", "sugar", "orange flavor"],
        "in_stock": True,
    },
    {
        "name": "Sprite",
        "price": 300,
        "ingredients": ["carbonated water", "sugar", "lemon-lime flavor"],
        "in_stock": False,
    },
]

OTHER_SIDES = [
    {
        "name": "Plantains",
        "price": 500,
        "ingredients": ["plantains", "oil", "spices"],
        "in_stock": True,
    },
    {
        "name": "Salad",
        "price": 400,
        "ingredients": ["lettuce", "tomatoes", "cucumbers", "dressing"],
        "in_stock": True,
    },
]

FULL_MENU = {
    "main_menu": MAIN_MENU,
    "soups": SOUPS,
    "proteins": PROTEINS,
    "drinks": DRINKS,
    "other_sides": OTHER_SIDES,
}
