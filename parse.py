from parse_rest.connection import register
from parse_rest.datatypes import Object
register("lkHCX43bL8tqi0kpiICrOdXLlcx6yxDs3k9rUE5A", "uIE9zOF0dsbr5N9uPrtF2eBDiuGiIhuffvFsdaaA", master_key="ikropQhezf8HiYJKg0ZidOJ0Oa2I9RLRsdzP16Zt")
class EmergencyContacts(Object):
	pass

contact = EmergencyContacts(Name="david", Phone="+18000000000")
contact.save()
