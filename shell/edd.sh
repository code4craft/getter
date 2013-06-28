#!/bin/sh
FILE_PATH=/usr/local/getter
PREFIX=-
[ -d "$FILE_PATH" ] || mkdir -p $FILE_PATH
if [ -z "$1" ]
then
    echo "Usage: $0 alias [command]"
else
    FILE_NAME=$FILE_PATH/$PREFIX$1
    if [ -z "$2" ]
    then
        rm -f $FILE_NAME
    else
        echo "#!/bin/sh" > $FILE_NAME
        echo "$2" >> $FILE_NAME
        chmod +x $FILE_NAME
    fi
fi