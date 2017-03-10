#"""
#   :synopsis: run file for dfnworks 
#   :version: 1.0
#   :maintainer: Jeffrey Hyman, Carl Gable, Nathaniel Knapp
#.. moduleauthor:: Jeffrey Hyman <jhyman@lanl.gov>
#"""

import os, sys
sys.path.append("/home/nknapp/dfnworks-main/pydfnworks/") 
from time import time
from pydfnworks import * 
import subprocess

def define_paths():
    # PETSC and PFLOTRAN PATHS
    os.environ['PETSC_DIR']='/home/satkarra/src/petsc-git/petsc-3.7-release'
    os.environ['PETSC_ARCH']='/Ubuntu-14.04-nodebug'
    os.environ['PFLOTRAN_DIR']='/home/satkarra/src/pflotran-dev-pt-testing'

    os.environ['DFNWORKS_PATH'] = '/home/nknapp/dfnworks-main/'
    os.environ['DFNGEN_PATH']=os.environ['DFNWORKS_PATH']+'DFNGen/'
    os.environ['DFNTRANS_PATH']= os.environ['DFNWORKS_PATH'] +'ParticleTracking/'

    # Executables	
    os.environ['python_dfn'] = '/n/swdev/packages/Ubuntu-14.04-x86_64/anaconda-python/2.4.1/bin/python'
    os.environ['lagrit_dfn'] = '/n/swdev/mesh_tools/lagrit/install-Ubuntu-14.04-x86_64/3.2.0/release/gcc-4.8.4/bin/lagrit'
    os.environ['connect_test'] = os.environ['DFNWORKS_PATH']+'DFN_Mesh_Connectivity_Test/ConnectivityTest'
    os.environ['correct_uge_PATH'] = os.environ['DFNWORKS_PATH']+'C_uge_correct/correct_uge' 
    os.environ['VTK_PATH'] = os.environ['DFNWORKS_PATH'] + 'inp_2_vtk/inp2vtk'

if __name__ == "__main__":

    define_paths()
    main_time = time()
    print 'Compiling executables'
    subprocess.call('python compile.py', shell=True)  
    DFN = create_dfn()
    if type(DFN) is ' NoneType':
        print 'ERROR: DFN object not created correctly'
        exit()
    # General Work Flow
    DFN.dfnGen()
    DFN.dfnFlow()
    DFN.dfnTrans()
    DFN.cleanup_end()

    main_elapsed = time() - main_time
    timing = 'Time Required: %0.2f Minutes'%(main_elapsed/60.0)
    print timing
    dump_time(DFN._local_jobname, DFN._jobname,main_elapsed) 
    #dfn.print_run_time()	
    print("*"*80)
    print(DFN._jobname+' complete')
    print("Thank you for using dfnWorks")
    print("*"*80)
