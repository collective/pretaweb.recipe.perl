# -*- coding: utf-8 -*-
"""Recipe perl"""


from hexagonit.recipe.cmmi import Recipe as RecipeCMMI
import os.path
import subprocess

class PerlRecipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        options["url"] = options.get("url", self.default_perl_url())
        buildoutDir = buildout["buildout"]["directory"]
        location = options.get("prefix", os.path.join (buildoutDir, "parts", name))
        options["location"] = location
        options["interpreter"] = os.path.join(buildoutDir, "parts", name, "bin/perl")
        options["configure-command"] = """sh Configure \
                    -Dprefix=%(location)s \
                    -Dlibs='-ldl -lm -lpthread -lc -lcrypt' \
                    -des """ % locals()
        options["cpan"] = options.get ("cpan", "")

    def default_perl_url (self):
        return "http://www.cpan.org/src/perl-5.12.3.tar.gz"


    def perl_cmmi(self):
        return RecipeCMMI (self.buildout, self.name, self.options)


    def install_modules(self):
        options = self.options

        modules = options["cpan"]

        cpanpBin = os.path.join(options["location"], "bin/cpanp")
        cpanEnv = os.environ.copy()
        cpanEnv["HOME"] = options["location"]

        for m in modules.split ("\n"):
            if len(m) > 0:
                cpanProc = subprocess.Popen (
                        (options["interpreter"], cpanpBin, 's conf prereqs 1; i ' + m, "--skiptest", "--force"),
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
