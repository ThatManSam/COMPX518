#!/usr/bin/bash

file=""
number=""

# Function to display usage information
function display_usage {
    echo "Usage: $0 -i <input_file> -c <number>"
    echo "Options:"
    echo "  -i <input_file>    Specify the input file"
    echo "  -c <number>        Specify the byte to split the file at (must be multiple of 64)"
}

# Parse arguments
while getopts ":i:c:" opt; do
    case $opt in
        i)
            file=$OPTARG
            ;;
        c)
            number=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            display_usage
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            display_usage
            exit 1
            ;;
    esac
done

# Check if the required arguments are provided
if [[ -z $file ]]; then
    echo "Missing input file argument." >&2
    display_usage
    exit 1
fi
if [[ -z $number ]]; then
    echo "Missing number argument." >&2
    display_usage
    exit 1
fi

if ! ((number % 64 == 0)); then
    echo "Number is not a multiple of 64"
    display_usage
    exit 1
fi

number_suffix=$(($number+129))

prefix_file=split_pre_$file
suffix_file=split_suf_$file

echo "Splitting out prefix and suffix"
head -c $number $file > $prefix_file
tail -c +$number_suffix $file > $suffix_file

prefix_match_file1="$prefix_file""_match1"
prefix_match_file2="$prefix_file""_match2"

echo "Generating matching MD5 sum files"
./md5collgen -p $prefix_file -o $prefix_match_file1 $prefix_match_file2

prefix_match_file1_end="$prefix_match_file1""_end"
prefix_match_file2_end="$prefix_match_file2""_end"

echo "Pulling out last 128 bytes"
tail -c 128 $prefix_match_file1 > $prefix_match_file1_end
tail -c 128 $prefix_match_file2 > $prefix_match_file2_end

output_file1="$file"".match.1"
output_file2="$file"".match.2"

echo "Rebuilding files"
cat $prefix_file $prefix_match_file1_end $suffix_file > $output_file1
cat $prefix_file $prefix_match_file2_end $suffix_file > $output_file2

echo "Cleaning up files"
rm -f $prefix_file $suffix_file \
    $prefix_match_file1 $prefix_match_file2 \
    $prefix_match_file1_end $prefix_match_file2_end

exit 0