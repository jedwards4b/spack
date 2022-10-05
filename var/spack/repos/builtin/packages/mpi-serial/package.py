# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mpi-serial
#
# You can edit this file again by typing:
#
#     spack edit mpi-serial
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class MpiSerial(AutotoolsPackage):
    """ A single processor implementation of the mpi library. """

    homepage = "https://github.com/MCSclimate/mpi-serial"
    url = "https://github.com/MCSclimate/mpi-serial/archive/refs/tags/MPIserial_2.3.0.tar.gz"

    # notify when the package is updated.
    maintainers = ["jedwards4b"]

    version("2.3.0", sha256="cc55e6bf0ae5e1d93aafa31ba91bfc13e896642a511c3101695ea05eccf97988")

    variant('fort-real-size', values=int, default=4,
            description='Specify the size of Fortran real variables')
    
    variant('fort-double-size', values=int, default=8,
            description='Specify the size of Fortran double precision variables')

    patch('install.patch')
    
    def configure_args(self):
        args = []
        realsize = int(self.spec.variants['fort-real-size'].value)
        if realsize != 4:
            args.extend([
                "--enable-fort-real={0}".format(realsize),
                ])
        doublesize = int(self.spec.variants['fort-double-size'].value)
        if doublesize != 8:
            args.extend([
                "--enable-fort-double={0}".format(doublesize),
                ])
        return args
