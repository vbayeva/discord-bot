where_to_put = {
    "plastik": "zółty pojemnik",
    "metal": "zółty pojemnik",
    "papier": "niebieski pojemnik"
}

colors_from_item = {
    "plastik": "yellow",
    "metal": "yellow",
    "papier": "blue"
}

def get_where_to_put_item(item) -> str:
    if item in where_to_put:
        return where_to_put[item]
    else: 
        return "Nawet my nie wiemy gdzie to dać"
    
