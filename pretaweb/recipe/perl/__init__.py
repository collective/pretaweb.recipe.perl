# -*- coding: utf-8 -*-
"""Recipe perl"""


from hexagonit.recipe.cmmi import Recipe as RecipeCMMI
import os.path
import subprocess

class PerlRecipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        buildoutDir = buildout["buildout"]["directory"]
        options["location"] = os.path.join (buildoutDir, name)
        options["interpreter"] = os.path.join(buildoutDir, "parts", name, "bin/perl")
        options["keep-compile-dir"] = options.get("keep-compile-dir", "false")
        options["configure-command"] = """sh Configure \
                    -Dprefix=%(buildoutDir)s/parts/%(name)s \
                    -Dlibs='-ldl -lm -lpthread -lc -lcrypt' \
                    -des """ % locals()
        options["cpan"] = options.get ("cpan", "")


    def perl_cmmi(self):
        return RecipeCMMI (self.buildout, self.name, self.options)


    def installModules(self):

        modules = self.options["cpan"]

        cpanpBin = os.path.join(self["location"], "bin/cpanp")
        cpanEnv = os.environ.copy()
        cpanEnv["HOME"] = self["location"]

        for m in modules.split ("\n"):
            cpanProc = subprocess.Popen (
                    (options["interpreter"], cpanpBin, "-i", m, "--skiptest", "--force"),
                    env=cpanEnv,
                    stdin=subprocess.PIPE )
            cpanProc.stdin.write("\n"*100)
            cpanProc.stdin.close()
            ret = cpanProc.wait()
            if ret != 0:
                raise Exception ("Was not able to install CPAM module '%s'. cpanp returned status code %s" % (m, ret))


    def install(self):
        """Installer"""

        perl_cmmi = self.perl_cmmi()

        files = perl_cmmi.install()
        self.install_modules()

        return tuple(files)


    def update(self):
        """Updater"""

        perl_cmmi = self.perl_cmmi()
        perl_cmmi.update()


Recipe = PerlRecipe
