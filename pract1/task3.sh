if [ "$#" -ne 1 ];  then
        echo "Использование: $0 \"Ваш текст\""
        exit -1
fi

text="$1"
length=${#text}

frame_length=$((length + 2))

printf '+%s+\n' "$(printf '%*s' "$frame_length" '' | tr ' ' '-')"
printf '| %s |\n' "$text"
printf '+%s+\n' "$(printf '%*s' "$frame_length" '' | tr ' ' '-')"
