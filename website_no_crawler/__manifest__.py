# Copyright 2016 B-informed B.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Alter robots.txt disallow indexing",
    "summary": "Disables robots.txt for indexing by webcrawlers like Google",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "https://github.com/OCA/website",
    "author": "B-Informed B.V., Ooops, Odoo Community Association (OCA)",
    "category": "Website",
    "depends": ["website"],
    "data": ["data/data.xml", "views/disable_robots.xml"],
    "installable": True,
}
