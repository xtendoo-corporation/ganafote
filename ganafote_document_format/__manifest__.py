{
    "name": "Document Format Gañafote",
    "summary": """Formatos de documentos para Gañafote""",
<<<<<<< HEAD
    "version": "16.0.1.0.0",
    "description": """Formatos de documentos para Gañafote""",
    "author": "Daniel Dominguez, Camilo Prado",
=======
    "version": "15.0.1.0.0",
    "description": """Formatos de documentos para Gañafote""",
    "author": "Daniel Dominguez",
>>>>>>> 365abd87e9efac0223152faaaf4d1149b386d5be
    "company": "Xtendoo",
    "website": "https://github.com/OCA/edi",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "mail",
        "account",
    ],
    "data": [
        "data/quotation_to_factory_email_template.xml",
        "data/quotation_draft_template.xml",
        "data/quotation_confirmation_by_email_template.xml",
        "data/quotation_delivered_by_email_template.xml",
        "data/quotation_send_by_email_template.xml",
        "data/invoice_email_template.xml",
        "data/invoice_confirmation_email_template.xml",
        "views/email_template.xml",
        "views/external_layout_bold.xml",
        "views/report_sale_order.xml",
        "views/report_invoice.xml",
    ],
    "installable": True,
    "auto_install": False,
}
