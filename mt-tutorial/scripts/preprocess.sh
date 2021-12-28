PARA_DIR=$1
BIN_DIR=$2

fairseq-preprocess --source-lang en --target-lang km \
--trainpref $PARA_DIR/train.alt.bpe16K \
--validpref $PARA_DIR/dev.alt.bpe16K \
--testpref $PARA_DIR/test.alt.bpe16K \
--joined-dictionary \
--destdir $BIN_DIR \