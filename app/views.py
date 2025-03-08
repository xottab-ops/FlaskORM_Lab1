from flask import Blueprint, render_template
from app.services import (
    get_all_buildings,
    get_grouped_by_type,
    get_grouped_by_country,
    get_grouped_by_year,
    get_buildings_in_range
)

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    buildings_head, buildings_body = get_all_buildings()
    grouped_type_head, grouped_type_body = get_grouped_by_type()
    grouped_country_head, grouped_country_body = get_grouped_by_country()
    grouped_year_head, grouped_year_body = get_grouped_by_year()
    interval_head, interval_body = get_buildings_in_range(2000, 2018)

    return render_template(
        "index.html",
        buildings_head=buildings_head,
        buildings_body=buildings_body,
        grouped_type_head=grouped_type_head,
        grouped_type_body=grouped_type_body,
        grouped_country_head=grouped_country_head,
        grouped_country_body=grouped_country_body,
        grouped_year_head=grouped_year_head,
        grouped_year_body=grouped_year_body,
        interval_head=interval_head,
        interval_body=interval_body
    )