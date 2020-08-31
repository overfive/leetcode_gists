# Read from the file file.txt and output the tenth line to stdout.
c=1
while read l
do
    if [ $c -eq 10 ];then
        echo $l
        exit 0
    fi
    c=$(($c + 1))
done < file.txt
