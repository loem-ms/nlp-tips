BIN_DIR=$1
MODEL_DIR=$2
OUTPUT_FILE=$3

fairseq-generate $BIN_DIR \
--path $MODEL_DIR \
--batch-size 128 \
--remove-bpe \
--beam 5 > $OUTPUT_FILE