#!/usr/bin/env python3

import pronto

ont = pronto.Ontology('go.owl')

term_obj = ont['GO:0006355']
term_name = term_obj.name


print(term_obj)
print(term_name)





