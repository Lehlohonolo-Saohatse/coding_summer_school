# -*- coding: utf-8 -*-
"""
This script wraps the pipeline logic into a main() function and includes a
 standard Python entry point with if __name__ == "__main__": so it can
 be run as a standalone script or imported as a module.
"""

import pipeline_functions as pf

def main():
    print(f"******pipeline started******")

    # Extract the data
    apps_data = pf.extract("apps_data.csv")
    reviews_data = pf.extract("review_data.csv")

    print(f"******extract done******")

    # Transform the data
    top_apps_data = pf.transform(
        apps=apps_data,
        reviews=reviews_data,
        category="FOOD_AND_DRINK",
        min_rating=4.0,
        min_reviews=1000
    )

    print(f"******transform done******")

    # Load the data
    pf.load(
        dataframe=top_apps_data,
        database_name="market_research",
        table_name="top_apps"
    )

    print(f"******load done******")

if __name__ == "__main__":
    main()
