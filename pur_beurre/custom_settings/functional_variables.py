""" Functionnal variable module
"""
# DESCRIPTION: OpenFoodFacts (OFF) API categories list endpoint.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "https://fr.openfoodfacts.org/categories.json".
# CUSTOM SETTINGS: To use the application with product references from
# another country than France, use the appropriate ISO-3166-1
# Alpha 2 code and replace it in the endpoint (e.g.
# "https://es.openfoodfacts.org/categories.json" for Spain).
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
CATEGORIES_ENDPOINT = "https://fr.openfoodfacts.org/categories.json"

# DESCRIPTION: OFF API products categories type used in the application.
# MANDATORY: Yes.
# DEFAULT SETTINGS: ["en:snacks", "en:desserts", "en:breads",
# "en:breakfast-cereals", "en:meals"].
# CUSTOM SETTINGS: Categories can be changed. Value to use can be found in
# "https://world.openfoodfacts.org/categories.json" in the
# category "tags" "id".
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
SELECTED_CATEGORIES = [
    "en:snacks", "en:desserts", "en:breads", "en:breakfast-cereals",
    "en:meals"
]

# DESCRIPTION: OFF API products research functionality endpoint.
# It returns the product research functionality per country.
# MANDATORY: Yes.
# DEFAULT SETTINGS: "https://fr.openfoodfacts.org/cgi/search.pl".
# CUSTOM SETTINGS: To use the application with product references from
# another country than France, use the appropriate ISO-3166-1
# Alpha 2 code and replace it in the endpoint (e.g.
# "https://es.openfoodfacts.org/cgi/search.pl").
# For more information, please check "https://documenter.getpostman.com/view/
# 8470508/SVtN3Wzy?version=latest#intro".
PRODUCTS_ENDPOINT = "https://fr.openfoodfacts.org/cgi/search.pl"

# DESCRIPTION: Amount of product to get from OFF API per product category.
# MANDATORY: Yes.
# DEFAULT SETTINGS: 1000.
# CUSTOM SETTINGS: Can be changed but should not exceed 2000 to avoid
# upload failure.
PRODUCTS_AMOUNT = 30
