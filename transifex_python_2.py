from transifex.native import init
from transifex.native import tx
from transifex.native.parsing import SourceString

# Inialize SDK
#init(token="PUBLIC-TOKEN", secret="SECRET", languages=[])
init('1/5e2c211e9b3833e57188466500c73260e5c24cee', ['fr', 'de', 'pt', 'es_MX'], '1/9d8bbe8e701521fb3fdcca11a15cee4aa687735e')

# populate toolkit memory cache with translations from CDS service the first time
tx.fetch_translations() 
# get a translation of your project strings, the translation is served from cache

fr_translation = tx.translate('Welcome to Transifex', 'fr')
print(fr_translation)

de_translation = tx.translate('Welcome to Transifex', 'de')
print(de_translation)

pt_translation = tx.translate('Welcome to Transifex', 'pt')
print(pt_translation)

esMX_translation = tx.translate('Welcome to Transifex', 'es_MX')
print(esMX_translation)


# get a translation with plurals and variable
translation = tx.translate(
            u'{cnt, plural, one {{cnt} {gender} duck} other {{cnt} {gender} ducks}}',
            'el',
            params={'cnt': 1, 'gender': 'ugly'}
)