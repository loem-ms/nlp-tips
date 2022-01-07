BIN_DIR=$1
MODEL=$2
OUTPUT_PREF=$3
BEAM=$4

fairseq-generate $BIN_DIR \
--path $MODEL \
--batch-size 128 \
--remove-bpe \
--nbest $BEAM > $OUTPUT_PREF.beam.$BEAM.txt