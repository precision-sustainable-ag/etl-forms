# to run use 'python -m tests.test_parse_forms' from ./etl-forms


from push_to_prod.push_to_prod import ProductionPusher

from parse_forms.parse_forms import FormParser
import traceback
import sys

try:
    pp = ProductionPusher("local")

    pp.push_to_prod()

    pp.close_cons()
except Exception:
    print("A general error ocurred \n")
    print(traceback.print_exc(file=sys.stdout))
