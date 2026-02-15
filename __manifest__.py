{
    'name': 'Reporte de Reparación',
    'version': '1.0',
    'summary': 'Customizations for truck repair orders',
    'author': 'Gemini Expert',
    'depends': ['repair', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/repair_order_view.xml',
        'report/repair_report.xml',
        'report/repair_report_template.xml',
    ],
    'installable': True,
    'application': True,
}
