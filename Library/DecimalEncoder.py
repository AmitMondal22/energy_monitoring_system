from decimal import Decimal
import json
from datetime import date, timedelta

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, timedelta):
            return str(o)
        return super().default(o)




# class DecimalEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, Decimal):
#             return str(o)
#         return super(DecimalEncoder, self).default(o)
    