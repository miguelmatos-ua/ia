# Redes semanticas
# -- Exemplo
# 
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2018
# 2018/10/22
#


from semantic_network import *

a = Association('socrates', 'professor', 'filosofia')
s = Subtype('homem', 'mamifero')
m = Member('socrates', 'homem')

da = Declaration('descartes', a)
ds = Declaration('darwin', s)
dm = Declaration('descartes', m)

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin', Association('mamifero', 'mamar', 'sim')))
z.insert(Declaration('darwin', Association('homem', 'gosta', 'carne')))

# novas declaracoes

z.insert(Declaration('darwin', Subtype('mamifero', 'vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles', 'homem')))

b = Association('socrates', 'professor', 'matematica')
z.insert(Declaration('descartes', b))
z.insert(Declaration('simao', b))
z.insert(Declaration('simoes', b))

z.insert(Declaration('descartes', Member('platao', 'homem')))

e = Association('platao', 'professor', 'filosofia')
z.insert(Declaration('descartes', e))
z.insert(Declaration('simao', e))

z.insert(Declaration('descartes', Association('mamifero', 'altura', 1.2)))
z.insert(Declaration('descartes', Association('homem', 'altura', 1.75)))
z.insert(Declaration('simao', Association('homem', 'altura', 1.85)))
z.insert(Declaration('darwin', Association('homem', 'altura', 1.75)))

z.insert(Declaration('descartes', Association('socrates', 'peso', 80)))
z.insert(Declaration('darwin', Association('socrates', 'peso', 75)))
z.insert(Declaration('darwin', Association('platao', 'peso', 75)))

z.insert(Declaration('damasio', Association('filosofo', 'gosta', 'filosofia')))
z.insert(Declaration('damasio', Member('socrates', 'filosofo')))

# Extra - descomentar as restantes declaracoes para o exercicio II.2.16

# z.insert(Declaration('descartes', AssocNum('socrates','pulsacao',51)))
# z.insert(Declaration('darwin', AssocNum('socrates','pulsacao',61)))
# z.insert(Declaration('darwin', AssocNum('platao','pulsacao',65)))

# z.insert(Declaration('descartes',AssocNum('homem','temperatura',36.8)))
# z.insert(Declaration('simao',AssocNum('homem','temperatura',37.0)))
# z.insert(Declaration('darwin',AssocNum('homem','temperatura',37.1)))
# z.insert(Declaration('descartes',AssocNum('mamifero','temperatura',39.0)))

# z.insert(Declaration('simao',Association('homem','gosta','carne')))
# z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
# z.insert(Declaration('simao',Association('homem','gosta','peixe')))
# z.insert(Declaration('simao',Association('homem','gosta','couves')))

# z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
# z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
# z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))

print("Ex1:", z.list_associations())
print("\nEx2:", z.list_objects())
print("\nEx3:", z.list_users())
print("\nEx4:", z.list_types())
print("\nEx5: %s ('socrates')" % z.list_local_associations("socrates"))
print("\nEx6: {} ('descartes')".format(z.list_relations("descartes")))
print("\nEx7: {} ('descartes')".format(z.associations("descartes")))
print("\nEx8: {} ('socrates')".format(z.list_local_user("socrates")))
print("\nEx9: {} ('vertebrado', 'socrates')".format(z.predecessor("vertebrado", "socrates")))
print("Ex9: {} ('vertebrado', 'filosofo')".format(z.predecessor("vertebrado", "filosofo")))
print("\nEx10: {} ('vertebrado', 'socrates')".format(z.predecessor_path("vertebrado", "socrates")))
print("\nEx11 a): {} ('socrates', 'altura')".format(z.query("socrates", "altura")))
z.show_query_result()
print("\nEx11 b): {} ('homem', 'mamar')".format(z.query2("homem", "mamar")))
z.show_query_result()
print("\nEx11 b): {} ('homem')".format(z.query2("homem")))
z.show_query_result()
print("\nEx12: {} ('socrates', 'altura')".format(z.query_cancel('socrates', 'altura')))
z.show_query_result()
print("\nEx13: {} ('mamifero', 'altura')".format(z.query_down('mamifero', 'altura')))
z.show_query_result()
