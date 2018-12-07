Create opi file(s) for all motors controlled by Turbo PMAC in a beamline.

. Run pmac_motor.py on IOC servers.
. Put all the created *-mtr-info.list files and pmac_css.py in the same folder.
. Run pmac_css.py.
. Copy the created *-pmac-motor-info-cntlr.opi and pmac-motor-status-1x.opi to the repository.
  These .opi files must be in the same directory.
. Open the created *-pmac-motor-info-cntlr.opi file from CS-Studio.
