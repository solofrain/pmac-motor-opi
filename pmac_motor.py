#============================================================================
#
#  This script is used to read the information of the motors controlled by 
#  PMAC controllers in a IOC server.
#      . IOC related information
#      . PMAC axis related information
#
#  Usage:
#
#      Put this script in an IOC server and run:
#
#          python pmac_motor.py
#
#  1. An IOC is considered to be a PMAC IOC if pmacStatus.substitutions 
#     exists in /epics/iocs/$(ioc_name)/db/ folder. Only the running IOCs 
#     are concerned (from command: manage-iocs status).
#
#  2. Axis information is extracted from the following files in
#     . /epics/iocs/$(ioc_name)/db/motorstatus.substitutions
#           Sys, Dev, Axis, CntlSys, CntlDev, CntlAxis
#     . /epics/iocs/$(ioc_name/iocBoot/iocmtrctl/st.cmd
#           IocName (for IOC status)
#
#     $(Sys){$(Dev)-Ax:$(Axis)} is used to identify the axes.
#
# *3. A substituion file will be created for an independent IOC to provide 
#     such information:
#         motor_info.substitutions
#         . $(Sys)
#         . $(Dev)
#         . $(Axis)
#         . $(CntlSys)
#         . $(CntlDev)
#         . $(IocSrv)
#         . $(IocName)
#     This substitions file create objects for each motor:
#         . $(Sys){$(Dev)-Ax:$(Axis)}-IocSrv
#         . $(Sys){$(Dev)-Ax:$(Axis)}-IocName
#         . $(Sys){$(Dev)-Ax:$(Axis)}-Cntlr
#         . $(Sys){$(Dev)-Ax:$(Axis)}-CntlrAxis
#
#     This has not been implemented yet.
#
#  4. Two .opi files will be created for all Axis per controller/Device
#     separately.
#     
#------------------------------------------------------------------------------
#
#  Author:
#      Ji Li <liji@bnl.gov>
#
#============================================================================
import os



iocs = [ [0 for col in range(1)] for row in range(1)]
axes = [ [0 for col in range(1)] for row in range(1)]



#========================================================
# Get the list of active PMAC IOCs
#========================================================
def get_iocs():
    global iocs
    
    os.system('manage-iocs status > ' + IOC_LIST_FILE)

    with open (IOC_LIST_FILE, 'r' ) as f:
        for line in f:
            if 'Running' in line:
                ind = line.find('\t')
                ioc = line[20:ind]
                key = IOCS_ROOT + '/' + ioc + '/db/' + PMAC_SUB_FILE
                if (os.path.exists(key)):
                    print('\n\nFind PMAC IOC %s' %(ioc))
                    iocs.append(ioc)
    f.close()
    
    #os.system('rm ' + IOC_LIST_FILE)

    iocs.pop(0)
    iocs.sort()
#========================================================




#========================================================
# Get motor information from motorstatus.substitutions
#========================================================
def get_mtr_info():
    global iocs
    global mtr

    info = [ [0 for col in range(2)] for row in range(NUM_OF_FIELDS)]
    info[0] = host

    fw = open(MTR_INFO_FILE, 'w')

    for ioc in iocs:
        info[1] = ioc
        j = 2

        # find IOC name
        # used to get PV of the IOC heartbeat
        key = IOCS_ROOT + '/' + ioc + '/iocBoot/iocmtrctl/st.cmd'
        with open (key) as f:
            for line in f:
                if '#' in line:
                    continue
                if 'iocAdminSoft' in line:
                    index = line.index('IOC')
                    line = line[index+4:len(line)-1]
                    index = line.index('"')
                    info[j] = line[0:index]
                    break
        f.close()
        
        j = 3

        # find controller information 
        # the pattern in pmacStatus.substitutions:
        # {SYS,               PMAC,    VERSION  PLC  PORT,  NAXES }
        # {"XF:28IDC-CT",     "MC:01",  "1"      5    "P0",  8     }
        key = IOCS_ROOT + '/' + ioc + '/db/' + PMAC_SUB_FILE
        print(key)
        with open (key) as f:
            for line in f:
                if '#' in line:
                    continue
                if 'MC' in line:
                    for i in range (2):
                        # remove the chars until the char next to the first "
                        leng = len(line)
                        index = line.index('"')
                        line = line[index+1:leng-1]
    
                        # get the info string
                        index = line.index('"')
                        info[j] = line[0:index]
    
                        # remove the info string and the "
                        leng = len(line)
                        line = line[index+1:leng-1]
                        j = j + 1
        f.close()
    
        key = IOCS_ROOT + '/' + ioc + '/db/' + MTR_SUB_FILE
        print(key)
        with open (key) as f:
            for line in f:
                # invalid line
                if '#' in line:
                    continue
                
                # following information is not of interest
                if 'pmac' in line:
                    f.close()
                    break
                
                j = 6
    
                if 'Ax' in line:
                    for i in range (2):
                        # remove the chars until the char next to the first "
                        leng = len(line)
                        index = line.index('"')
                        line = line[index+1:leng-1]
    
                        # get the info string
                        leng = len(line)
                        index = line.index('"')
                        info[j] = line[0:index]
    
                        # remove the info string and the "
                        line = line[index+1:leng-1]
                        j = j + 1

                    ax_index = info[j-1].index('Ax')
                    right_bracket_index = info[j-1].index('}')
                    info[j] = info[j-1][ax_index+3:right_bracket_index]
                    info[j-1] = info[j-1][1:ax_index-1]

                    # remove "P0", and following spaces
                    leng = len(line)
                    index = line.index(',')
                    line = line[index+1:leng-1]
                    leng = len(line)
                    index = line.index(',')
                    line = line[index+1:leng-1]
                    line = line.lstrip()   

                    if ' ' in line:
                        index = line.index(' ')
                        info[5] = line[0:index-1]
                    else:
                        leng = len(line)
                        info[5] = line[0:leng-1]
                    info[5] = ' ' + line[0]
                

                    for i in range(NUM_OF_FIELDS):
                        fw.writelines(info[i] + '\t')
                    fw.writelines('\n')

        f.close()
    

    fw.close()
#========================================================

#========================================================
# Main program.
#========================================================
# 1. Variable initialization
host = socket.gethostname()
IOCS_ROOT     = '/epics/iocs'
DB_DIRccc     = 'db'
ST_DIRccc     = 'iocBoot/iocmtrctl'
PMAC_SUB_FILE = 'pmacStatus.substitutions'
ST_FILE       = 'st.cmd'
MTR_SUB_FILE  = 'motorstatus.substitutions'
IOC_LIST_FILE = 'ioc.list'
MTR_INFO_FILE = host + '-mtr-info.list'

NUM_OF_FIELDS = 9

#--------------------------------------------------------
# 2. Get IOC list, and add the running ones to the list
get_iocs()

#--------------------------------------------------------
# 3. Operation
get_mtr_info()

