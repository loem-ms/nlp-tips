PARA_DIR=$1
DICT_DIR=$2
OUTPUT_BIN_DIR=$3


fairseq-preprocess --source-lang km --target-lang en \
--srcdict $DICT_DIR/dict.km.txt \
--tgtdict $DICT_DIR/dict.en.txt \
--testpref $PARA_DIR/train.alt.bpe16K \
--destdir $OUTPUT_BIN_DIR \