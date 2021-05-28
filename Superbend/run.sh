#!/bin/bash

if [ "$#" == "0" ]
then
	echo "Run name not set for logging purposes. You can give it with: ./run.sh run_name"
	logname=""
else
	echo "Run name set to $1."
	logname="$1-"
fi

DATE=$(date +%s)
LOGFILE="./Log/$logname$DATE-run.log"
echo " "
echo "Run the coil powering: coil-energization.sif" | tee $LOGFILE
rm ./RESU/coil_* | tee -a $LOGFILE
echo "*** ElmerSolver ***"
ElmerSolver coil-energization.sif | tee -a $LOGFILE
#python ./Python/plot_ramp.py | tee -a $LOGFILE
#eog ./Figures/ramp.png &
#echo "Run the coil extraction: coil-extraction.sif" | tee -a $LOGFILE
#ElmerSolver coil-extraction.sif | tee -a $LOGFILE
#python ./Python/plot_all.py | tee -a $LOGFILE
#eog ./Figures/all_current.png &
#eog ./Figures/all_voltage.png &
#mv $LOGFILE Log/
