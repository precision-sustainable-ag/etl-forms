from push_to_prod.push_to_prod import ProductionPusher
from parse_forms.parse_forms import FormParser
import traceback
import sys

try:
    fp = FormParser("local")
    pp = ProductionPusher("local")

    fp.parse_forms()
    pp.push_to_prod()

    fp.close_con()
    pp.close_cons()
except Exception:
    print("A general error ocurred \n")
    print(traceback.print_exc(file=sys.stdout))