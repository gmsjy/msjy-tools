#!/bin/bash

SECS=600
UNIT_TIME=10

STEPS=$(($SECS/$UNIT_TIME))

echo Wathing CPU usage...:

for((i=0;i<$STEPS;i++))
do
  ps -eo pid,comm,pcpu |tail -n +2  >> ./cpu_usage.$$
  sleep $UNIT_TIME
done

echo 
echo CPU eaters:

cat ./cpu_usage.$$ |\
awk '
{
    flag=$1+" "+$2
    process[flag]+=$3;}
END{
    for(i in process)
    {
        printf("%-20s %s",i,process[i]);
        printf("\n");
    }
    
}' | sort -nrk 2 | head 
