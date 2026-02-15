# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    customer_id = fields.Many2one('res.partner', string='Cliente')

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    antecedentes_servicio = fields.Text(string='3. Antecedentes del servicio')
    hallazgos = fields.Text(string='4. Hallazgos')
    accion_correctiva = fields.Text(string='5. Acción Correctiva')
    recomendaciones = fields.Text(string='6. Recomendaciones')
    
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehículo a reparar')

    # Campos de cliente en modo lectura
    partner_email = fields.Char(string='Correo', compute='_compute_partner_info', readonly=True)
    partner_street = fields.Char(string='Dirección', compute='_compute_partner_info', readonly=True)
    partner_phone = fields.Char(string='Teléfono', compute='_compute_partner_info', readonly=True)

    # Campos de vehículo en modo lectura
    vehicle_brand = fields.Char(string='Marca', compute='_compute_vehicle_info', readonly=True)
    vehicle_vin = fields.Char(string='Número de Chassis', compute='_compute_vehicle_info', readonly=True)
    vehicle_plate = fields.Char(string='Placa', compute='_compute_vehicle_info', readonly=True)

    @api.depends('partner_id')
    def _compute_partner_info(self):
        for record in self:
            if record.partner_id:
                record.partner_email = record.partner_id.email
                record.partner_street = record.partner_id.street
                record.partner_phone = record.partner_id.phone
            else:
                record.partner_email = False
                record.partner_street = False
                record.partner_phone = False

    @api.depends('vehicle_id')
    def _compute_vehicle_info(self):
        for record in self:
            if record.vehicle_id:
                record.vehicle_brand = record.vehicle_id.brand_id.name if record.vehicle_id.brand_id else ''
                record.vehicle_vin = record.vehicle_id.vin_sn
                record.vehicle_plate = record.vehicle_id.license_plate
            else:
                record.vehicle_brand = False
                record.vehicle_vin = False
                record.vehicle_plate = False

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            return {'domain': {'vehicle_id': [('customer_id', '=', self.partner_id.id)]}}
        return {'domain': {'vehicle_id': []}}

