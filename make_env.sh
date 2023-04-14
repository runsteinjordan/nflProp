#!/bin/bash
current_dir=$(pwd)
make_env_file=$current_dir/make_env.sh
# Check to see if make_env.sh exists in user's current directory
if [ -f "$make_env_file" ]; then
    echo "export PYTHONPATH=$current_dir"
    export PYTHONPATH=$current_dir
else
    echo "Please run this script from the top of the nflProp repository"
fi

