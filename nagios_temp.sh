#/bin/bash 
#nagios nrpe monitor script

#Nagios rturn code
OK=0
WARNING=1
CRITICAL=2
UNKNOWN=3


CODE=""


echo $status


case $CODE in 
    OK)
        exit $OK
        ;;
    WARN)
        exit $WARNING
        ;;
    ERROR)
        exit $CRITICAL
        ;;
    *)
        exit $UNKNOWN
        ;; 
esac
