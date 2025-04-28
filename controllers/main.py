from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

class CustomerPortalExtended(CustomerPortal):
    
    def _prepare_portal_layout_values(self):
        values = super(CustomerPortalExtended, self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'date_of_birth': partner.date_of_birth,
            'place_of_birth': partner.place_of_birth,
            'gender': partner.gender,
            'school': partner.school,
            'exp': partner.exp,
        })
        return values
    
    def _get_optional_fields(self):
      """ This method is there so that we can override the optional fields """
      return [
          "street2", "zipcode", "state_id", "vat", "company_name",
          "mobile", "date_of_birth", "place_of_birth", "gender", "school", "exp"
      ]
