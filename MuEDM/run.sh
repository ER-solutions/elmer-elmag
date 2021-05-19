##!/bin/bash

if [ "$#" == "0" ]
then
	echo "Run name not set for logging purposes. You can give it with: ./run.sh run_name"
	logname=""
else
	echo "Run name set to $1."
	logname="$1-"
fi

DATE=$(date +%s)
LOGFILE="$logname$DATE-run.log"
echo " "
echo "Run the coil powering: coil-energization.sif" | tee $LOGFILE
rm ./RESU/coil_* | tee -a $LOGFILE
echo "*** ElmerSolver ***"
ElmerSolver coil-energization.sif | tee -a $LOGFILE
mv $LOGFILE Log/
