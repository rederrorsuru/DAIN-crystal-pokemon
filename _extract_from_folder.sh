echo $@
for FOLDER in "$@";
do
    #echo FOLDER2=$(cygpath "$FOLDER" -u)
    FOLDER2=$(cygpath "$FOLDER" -u -a)
    #echo Cygpath folder is $FOLDER2
    FILENAME=$(basename -- "$FOLDER2")
    echo cd "$FOLDER2"
    cd "$FOLDER2"
    cd output_videos
    #pwd
    #ls
    for file in *limitPallete*.gif;
    do
        echo  cp $file ../../"$FILENAME"_dain.gif
        cp $file ../../"$FILENAME"_dain.gif
    done
done
exec $SHELL