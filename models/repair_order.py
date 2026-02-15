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

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            return {'domain': {'vehicle_id': [('customer_id', '=', self.partner_id.id)]}}
        return {'domain': {'vehicle_id': []}}

