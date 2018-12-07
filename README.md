# Create opi file(s) for all motors controlled by Turbo PMAC in a beamline.
## Environment
 - EPICS
 - CS-Studio
 - Python
## Usage
1. Run pmac_motor.py on IOC servers.
2. Put all the created *-mtr-info.list files and pmac_css.py in the same folder.
3. Run pmac_css.py.
4. Copy the created *-pmac-motor-info-cntlr.opi and pmac-motor-status-1x.opi to the repository.
   These .opi files must be in the same directory.
5. Open the created *-pmac-motor-info-cntlr.opi file from CS-Studio.
## Known issues
1. The current version cannot resolve the IOC name if it's defined by macros in st.cmd.
2. Only one .opi file will be created which take controllers as collections. Device collection is to be implemented. 
