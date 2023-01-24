#!/usr/bin/env python
#
# spack wants to install netcdf-c and netcdf-fortran seperately
# this script creates links in the netcdf-c to the netcdf-fortran
# so that they can be combined into a single module. 
#
import os
from pathlib import Path

installroot = "/project/esmf/PROGS"
moduleroot = "/fs/cgd/data0/modules/modulefiles"

compilers = ["gcc/9.3.0", "intel/20.0.1", "nag/7.0"]

netcdf_c_version="4.9.0"
netcdf_fortran_version = "4.6.0"

for comp in compilers:
    for path in Path(os.path.join(installroot, comp)).rglob('netcdf.h'):
        croot = path.parent.parent.absolute()
        for path in Path(os.path.join(installroot, comp)).rglob('netcdf.inc'):
            froot = path.parent.parent.absolute()
            if froot == croot:
                continue
            for fdir in ["bin", "include", "lib", "share", "lib/pkgconfig"]:
                file_names = os.listdir(os.path.join(froot, fdir))
                for file_name in file_names:
                    ffile = os.path.join(froot,fdir,file_name)
                    fpath = Path(ffile)
                    if not fpath.is_file():
                        continue
                    cfile = os.path.join(croot, fdir, file_name)
                    if os.path.exists(cfile):
                        os.unlink(cfile)
                    print(f"linking {ffile} to {cfile}")
                    
                    os.symlink(ffile, cfile)
            
