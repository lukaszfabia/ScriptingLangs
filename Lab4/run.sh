MYPATH="/Users/lukaszfabia/Desktop/ScriptingLangs/Lab4"
cd "$MYPATH"
filename=""
if [ "$#" -ne 1 ]; then
    read -p "file name<.txt, .csv>: " filename
else 
    filename="$1"
fi


if [ ! -d "output" ]; then 
    mkdir "output"
fi


> "output/$filename"



python "$MYPATH/main.py" >> "$MYPATH/output/$filename"
