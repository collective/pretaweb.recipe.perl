# -*- coding: utf-8 -*-
"""Recipe perl"""


from hexagonit.recipe.cmmi import Recipe as RecipeCMMI
import os.path
class PerlRecipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        buildoutDir = buildout["buildout"]["directory"]
        options["location"] = os.path.join (buildoutDir, name)
        options["interpreter"] = os.path.join(buildoutDir, "parts", name, "bin/perl")
        options["keep-compile-dir"] = options.get("keep-compile-dir", "false")
        options["configure-command"] = """sh Configure \
                    -Dprefix=${buildout:directory}/parts/${:_buildout_section_name_} \
                    -Dlibs='-ldl -lm -lpthread -lc -lcrypt' \
                    -des """


    def perl_cmmi(self):
        return RecipeCMMI (self.buildout, self.name, self.options)


    def install(self):
        """Installer"""

        perl_cmmi = self.perl_cmmi()

        return tuple(cmmi.install())

    def update(self):
        """Updater"""

        perl_cmmi = self.perl_cmmi()
        perl_cmmi.update()


Recipe = PerlRecipe
